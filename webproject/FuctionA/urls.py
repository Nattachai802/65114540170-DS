from django.urls import path 
from .views import *

urlpatterns = [
    path('course_list/', course_list, name='course_list'),
    path('id_search/',course_idsearch,name='search_id'),
    path('name_search/',course_namesearch,name='search_name'),
    path('update/<str:Course_id>/',CourseUpdateView.as_view(),name='course_update'),
    path('delete/<str:Course_id>/', CourseDeleteView.as_view(), name='course_delete'),
]