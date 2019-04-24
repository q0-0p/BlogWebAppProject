from django.urls import path

from . import views
app_name = 'post'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('create', views.create, name='create'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('addAuthor/', views.addAuthor, name='addAuthor'),

]
