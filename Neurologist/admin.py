from django.contrib import admin
from .models import Service, Article, DoctorInfo, Patient, MedicalRecord, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title","created_at")
    search_fields = ("title","content")

@admin.register(DoctorInfo)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name","speciality")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name","national_id","phone")

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("patient","visit_date")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient","date","status")
    list_filter = ("status",)
