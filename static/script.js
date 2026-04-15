document.addEventListener('DOMContentLoaded', function() {
    const toggler = document.querySelector('.navbar-toggler');
    const nav = document.querySelector('.navbar-nav');
    if (toggler && nav) {
        toggler.addEventListener('click', function() {
            nav.classList.toggle('show');
        });
    }

    const categoryFilter = document.getElementById('categoryFilter');
    const searchInput = document.getElementById('searchInput');
    if (categoryFilter && searchInput) {
        categoryFilter.addEventListener('change', loadDisciplines);
        searchInput.addEventListener('input', debounce(loadDisciplines, 300));
        attachQuickViewHandlers();
    }
});

function loadDisciplines() {
    const categoryId = document.getElementById('categoryFilter').value;
    const search = document.getElementById('searchInput').value;
    const url = new URL('/api/disciplines/filter/', window.location.origin);
    if (categoryId) url.searchParams.set('category', categoryId);
    if (search) url.searchParams.set('search', search);

    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.classList.remove('d-none');

    fetch(url)
        .then(response => response.json())
        .then(data => {
            updateDisciplinesTable(data);
        })
        .catch(error => console.error('Ошибка:', error))
        .finally(() => {
            if (spinner) spinner.classList.add('d-none');
        });
}

function updateDisciplinesTable(data) {
    const container = document.getElementById('disciplinesContainer');
    if (!container) return;
    if (data.length === 0) {
        container.innerHTML = '<p class="text-muted">Ничего не найдено.</p>';
    } else {
        let html = '<table class="table table-striped table-hover">';
        html += '<thead><tr><th>Название</th><th>Категория</th><th>Сложность</th><th>Олимпийский</th><th>Действия</th><th>Быстрый просмотр</th></tr></thead><tbody>';
        data.forEach(d => {
            html += `<tr>
                <td><a href="${d.url}">${d.name}</a></td>
                <td>${d.category}</td>
                <td>${d.difficulty}</td>
                <td>${d.is_olympic ? 'Да' : 'Нет'}</td>
                <td>
                    <a href="/disciplines/${d.id}/update/" class="btn btn-sm btn-warning">Ред.</a>
                    <a href="/disciplines/${d.id}/delete/" class="btn btn-sm btn-danger">Удал.</a>
                </td>
                <td>
                    <button class="btn btn-sm btn-info quick-view-btn" data-id="${d.id}">👁️</button>
                </td>
            </tr>`;
        });
        html += '</tbody></table>';
        container.innerHTML = html;
    }
    attachQuickViewHandlers();
}

function attachQuickViewHandlers() {
    document.querySelectorAll('.quick-view-btn').forEach(btn => {
        btn.removeEventListener('click', quickViewHandler);
        btn.addEventListener('click', quickViewHandler);
    });
}

function quickViewHandler(e) {
    const disciplineId = this.dataset.id;
    fetch(`/api/disciplines/${disciplineId}/quick/`)
        .then(response => response.json())
        .then(data => {
            const modalBody = document.getElementById('quickViewContent');
            if (modalBody) {
                modalBody.innerHTML = `
                    <p><strong>Название:</strong> ${data.name}</p>
                    <p><strong>Категория:</strong> ${data.category}</p>
                    <p><strong>Сложность:</strong> ${data.difficulty}</p>
                    <p><strong>Олимпийский:</strong> ${data.is_olympic ? 'Да' : 'Нет'}</p>
                    <p><strong>Описание:</strong> ${data.description}</p>
                    <p><strong>Дата создания:</strong> ${data.created_at}</p>
                `;
            }
            const modal = document.getElementById('quickViewModal');
            if (modal) modal.style.display = 'flex';
        })
        .catch(error => console.


error('Ошибка загрузки деталей:', error));
}

function closeModal() {
    const modal = document.getElementById('quickViewModal');
    if (modal) modal.style.display = 'none';
}

function debounce(func, delay) {
    let timeout;
    return function() {
        clearTimeout(timeout);
        timeout = setTimeout(func, delay);
    };
}