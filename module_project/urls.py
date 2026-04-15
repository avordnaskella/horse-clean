from django.urls import path
from . import views

app_name = 'module_project'

urlpatterns = [
    # категории
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # дисциплины
    path('', views.DisciplineListView.as_view(), name='discipline_list'),
    path('disciplines/create/', views.DisciplineCreateView.as_view(), name='discipline_create'),
    path('disciplines/<int:pk>/', views.DisciplineDetailView.as_view(), name='discipline_detail'),
    path('disciplines/<int:pk>/update/', views.DisciplineUpdateView.as_view(), name='discipline_update'),
    path('disciplines/<int:pk>/delete/', views.DisciplineDeleteView.as_view(), name='discipline_delete'),

    # API
    path('api/disciplines/filter/', views.filter_disciplines, name='filter_disciplines'),
    path('api/disciplines/<int:pk>/quick/', views.discipline_quick_view, name='discipline_quick_view'),
    
    # для анимации
    path('interactive-horse/', views.interactive_horse, name='interactive_horse'),

    #для игры
    path('bullfight-game/', views.bullfight_game, name='bullfight_game'),

    #для видео
    path('video/', views.video_page, name='video_page'),
]