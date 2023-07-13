from django.urls import path
from .views import result_create, result_detail, result_update, result_delete,result_list

app_name = 'results'

urlpatterns = [
    path('create/', result_create, name='result_create'),
    path('<int:pk>/', result_detail, name='result_detail'),
    path('<int:pk>/update/', result_update, name='result_update'),
    path('<int:pk>/delete/', result_delete, name='result_delete'),
    path("list/",result_list,name="result_list")
]