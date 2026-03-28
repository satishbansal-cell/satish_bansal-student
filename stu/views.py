from django.urls import reverse_lazy
from .models import Student
# Create your views here.
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
class StuList(ListView):
	model=Student
	template_name="list.html"
	context_object_name="stu"

class StuCreate(CreateView):
	model=Student
	fields=[ 'name','course','fee']
	template_name="stu_create.html"
	success_url=reverse_lazy("list")

class StuUpdate(UpdateView):
	model = Student
	fields=[ 'name','course','fee']
	template_name = 'stu_create.html'
	success_url = reverse_lazy('list')

class StuDelete(DeleteView):
	model = Student
	template_name = 'stu_delete.html'
	success_url = reverse_lazy('list')
