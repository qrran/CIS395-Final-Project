
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('dashboard', views.dashboard, name="dashboard"),

    path('createRecord', views.createRecord, name="createRecord"),

    path('updateRecord/<int:pk>', views.updateRecord, name='updateRecord'),
    # making it dynamic url /< >and passing int(datatype)

    path('viewRecord/<int:pk>', views.viewRecord, name="viewRecord"),

    path('deleteRecord/<int:pk>', views.deleteRecord, name="deleteRecord"),

]









