from AccountApp.models import Doctor
from AppointmentApp.models import Appointement
from django.contrib import admin

# Register your models here.

@admin.action(description = "make them confirmed")
def confirmed_appointement(model,req,queryset):
    queryset.update(status = "CONFIRMED")

@admin.register(Appointement)
class AppointementAdminPers(admin.ModelAdmin):
    #inlines = [DoctorPerso]
    actions = [confirmed_appointement]
    list_display = ("appointment_date","reason","doctor","patient","status") 
    list_filter = ("status","appointment_date")
    list_editable = ("status",)
    search_fields = ("reason",)   
    list_per_page = 2
    ordering = ('-appointment_date',)
    fieldsets = (
        ('Description' , {
            'fields' : ('reason' , 'status')
        }),
        ('Date + duration' , {
            'fields' : ('appointment_date','duration_minutes')     
        }),
        ('Patient/Doctors' , {
            'fields' : ('patient','doctor')       
        }),
        ('Planification' , {
            'fields' : ('created_at' , 'updated_at')      
        }),
    ) 

    readonly_fields = ('created_at' , 'updated_at')  

"""
class AppointementAdminPers(admin.ModelAdmin):
    list_display = ("appointment_date","reason","doctor","patient","status") 
    list_filter = ("status","appointment_date")
    list_editable = ("status",)
    search_fields = ("reason",)"""
#admin.site.register(Appointement,AppointementAdminPers)