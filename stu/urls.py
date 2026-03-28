from django.urls import path
from .views import StuList, StuCreate, StuDelete, StuUpdate

urlpatterns=[
path('',StuList.as_view(), name="list"),
path('create/',StuCreate.as_view(), name="stu_create"),
path('<int:pk>/update/',StuUpdate.as_view(), name="stu_update"),
path('<int:pk>/delete/',StuDelete.as_view(), name="stu_delete")
]