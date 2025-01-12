from django.contrib import admin
from .models import Patient, PatientDetail,Question,QuestionOption,RndaResult
from django.utils.translation import gettext_lazy as _

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'date_of_birth', 'birth_weight', 'sex')

class PatientDetailAdmin(admin.ModelAdmin):
    list_display = ('mother_name', 'father_name', 'living_area', 'father_profession')

class MyAdminSite(admin.AdminSite):
    site_header = _("Rnda Admin")
    site_title = _("Rnda")
    index_title = _("Welcome to the Rnda Admin Dashboard")

# Instantiate your custom admin site
admin_site = MyAdminSite(name='myadmin')

# Register your models here
admin.site.register(Patient)
admin.site.register(PatientDetail)
admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(RndaResult)