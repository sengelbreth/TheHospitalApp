from django.contrib import admin


from .models import Patient, Doctor, Records

admin.site.register(Doctor)
admin.site.register(Patient)

admin.site.register(Records)
