from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Category, Discipline
from .forms import CategoryForm, DisciplineForm

# Категории 
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('module_project:category_list')
    success_message = "Категория успешно создана."

class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('module_project:category_list')
    success_message = "Категория успешно обновлена."

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('module_project:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Категория удалена.")
        return super().delete(request, *args, **kwargs)

#  Дисциплины 
class DisciplineListView(ListView):
    model = Discipline
    template_name = 'discipline_list.html'
    context_object_name = 'disciplines'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category')
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        return context

class DisciplineDetailView(DetailView):
    model = Discipline
    template_name = 'discipline_detail.html'

class DisciplineCreateView(SuccessMessageMixin, CreateView):
    model = Discipline
    form_class = DisciplineForm
    template_name = 'discipline_form.html'
    success_url = reverse_lazy('module_project:discipline_list')
    success_message = "Дисциплина успешно добавлена."

class DisciplineUpdateView(SuccessMessageMixin, UpdateView):
    model = Discipline
    form_class = DisciplineForm
    template_name = 'discipline_form.html'
    success_url = reverse_lazy('module_project:discipline_list')
    success_message = "Дисциплина успешно обновлена."

class DisciplineDeleteView(DeleteView):
    model = Discipline
    template_name = 'discipline_confirm_delete.html'
    success_url = reverse_lazy('module_project:discipline_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Дисциплина удалена.")
        return super().delete(request, *args, **kwargs)

# AJAX для обновления данных на старнице
def filter_disciplines(request):
    category_id = request.GET.get('category')
    search = request.GET.get('search', '').strip()

    disciplines = Discipline.objects.select_related('category').all()

    if category_id:
        disciplines = disciplines.filter(category_id=category_id)

    if search:
        disciplines = disciplines.filter(name__icontains=search)

    data = [
        {
            'id': d.id,
            'name': d.name,
            'category': d.category.name,
            'difficulty': d.get_difficulty_display(),
            'is_olympic': d.


is_olympic,
            'url': d.get_absolute_url(),
        }
        for d in disciplines
    ]
    return JsonResponse(data, safe=False)

def discipline_quick_view(request, pk):
    discipline = get_object_or_404(Discipline.objects.select_related('category'), pk=pk)
    data = {
        'id': discipline.id,
        'name': discipline.name,
        'category': discipline.category.name,
        'difficulty': discipline.get_difficulty_display(),
        'is_olympic': discipline.is_olympic,
        'description': discipline.description,
        'created_at': discipline.created_at.strftime('%d.%m.%Y %H:%M'),
    }
    return JsonResponse(data)

 # для анимации
def interactive_horse(request):
    return render(request, 'interactive_horse.html')

#для кориды
def bullfight_game(request):
    return render(request, 'bullfight_game.html')

#для видео
def video_page(request):
    return render(request, 'video_page.html')


