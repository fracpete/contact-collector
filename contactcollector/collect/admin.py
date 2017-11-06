from django.contrib import admin

from .models import Survey, Employer, Employee, Job

admin.site.register(Survey)
admin.site.register(Employer)
admin.site.register(Employee)
admin.site.register(Job)

