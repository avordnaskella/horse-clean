// Бургер-меню
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

// Загрузка дисциплин
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

// Обновление таблицы дисциплин
function updateDisciplinesTable(data) {
    const container = document.getElementById('disciplinesContainer');
    if (!container) return;
    if (data.length === 0) {
        container.innerHTML = '<p class="text-muted">Ничего не найдено.</p>';
    } else {
        let html = '<div class="table-responsive"><table class="table table-striped table-hover">';
        html += '<thead><tr><th>Изображение</th><th>Название</th><th>Категория</th><th>Сложность</th><th>Олимпийский</th><th>Действия</th><th>Быстрый просмотр</th></tr></thead><tbody>';
        data.forEach(d => {
            html += `<tr>
                <td>${d.image ? `<img src="${d.image}" width="50" height="50" style="object-fit: cover; border-radius: 4px;">` : '—'}</td>
                <td><a href="${d.url}">${d.name}</a></td>
                <td>${d.category}</td>
                <td>${d.difficulty}</td>
                <td>${d.is_olympic ? 'Да' : 'Нет'}</td>
                <td>
                    <a href="/disciplines/${d.id}/update/" class="btn btn-sm btn-warning">Ред.</a>
                    <a href="/disciplines/${d.id}/delete/" class="btn btn-sm btn-danger">Удал.</a>
                </td>
                <td><button class="btn btn-sm btn-info quick-view-btn" data-id="${d.id}">👁️</button></td>
            </tr>`;
        });
        html += '</tbody></table></div>';
        container.innerHTML = html;
    }
    attachQuickViewHandlers();
}

// Обработчики кнопок быстрого просмотра
function attachQuickViewHandlers() {
    document.querySelectorAll('.quick-view-btn').forEach(btn => {
        btn.removeEventListener('click', quickViewHandler);
        btn.addEventListener('click', quickViewHandler);
    });
}

// Быстрый просмотр
function quickViewHandler(e) {
    const disciplineId = this.dataset.id;
    fetch(`/api/disciplines/${disciplineId}/quick/`)
        .then(response => response.json())
        .then(data => {
            const modalBody = document.getElementById('quickViewContent');
            if (modalBody) {
                modalBody.innerHTML = `
                    <p><strong>Название:</strong> ${escapeHtml(data.name)}</p>
                    <p><strong>Категория:</strong> ${escapeHtml(data.category)}</p>
                    <p><strong>Сложность:</strong> ${escapeHtml(data.difficulty)}</p>
                    <p><strong>Олимпийский:</strong> ${data.is_olympic ? '✅ Да' : '❌ Нет'}</p>
                    <p><strong>Описание:</strong> ${escapeHtml(data.description) || '—'}</p>
                    <p><strong>Дата создания:</strong> ${data.created_at}</p>
                `;
            }
            const modal = document.getElementById('quickViewModal');
            if (modal) {
                modal.style.display = 'flex';
            }
        })
        .catch(error => console.error('Ошибка загрузки деталей:', error));
}

// Закрытие модального окна
function closeModal() {
    const modal = document.getElementById('quickViewModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Закрытие по клику вне окна
window.addEventListener('click', function(e) {
    const modal = document.getElementById('quickViewModal');
    if (e.target === modal) {
        closeModal();
    }
});

// Функция для экранирования HTML
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Debounce для поиска
function debounce(func, delay) {
    let timeout;
    return function() {
        clearTimeout(timeout);
        timeout = setTimeout(func, delay);
    };
}