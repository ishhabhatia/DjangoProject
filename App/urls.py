from . import views
from django.urls import path
#app url
urlpatterns = [
    path('',views.savedemo),
    path('index',views.savedemo),
    path('show', views.displaydata),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.updatedata),
    path('delete/<int:id>', views.deletedata)
]