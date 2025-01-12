from django.urls import path

from .import views

urlpatterns = [
    path("",views.index, name="rnda"),
    path("",views.index, name=""),
    path("demographic",views.demographic_information, name="demographic"),
    path('patient-step-1/', views.patient_step_1, name='patient_step_1'),
    path('patient-step-2/', views.patient_step_2, name='patient_step_2'),
    path("result",views.rnda_results, name="result"),
    path("/success",views.index, name="success"),


] 