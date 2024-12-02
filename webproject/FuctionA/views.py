from django.shortcuts import render
from .models import *
from django.views.generic import UpdateView , DeleteView
from django.shortcuts import get_object_or_404, redirect 
from .forms import CourseForm
from django.urls import reverse_lazy
# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_idsearch(request):
  search = request.GET.get('code','')
  courses = Course.objects.filter(Course_id=search)
  return render(request,'course_search.html',{'courses':courses})

def course_namesearch(request):
  search = request.GET.get('code','')
  courses = Course.objects.filter(Course_name=search)
  return render(request,'course_namesearch.html',{'courses':courses})

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_update.html'
    success_url = reverse_lazy('course_list')
    
    def get_object(self, queryset=None):
        return get_object_or_404(Course, Course_id=self.kwargs['Course_id'])

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Course, Course_id=self.kwargs['Course_id'])
