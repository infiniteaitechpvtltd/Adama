from django.contrib import admin
from .models import User_Data, Shift, Tank, Chemical, SOP, Batch_Card,CreateTask,Tasks_list, ManPower_Detail, Plant_Detail, Maintenance_Detail, Sample, PackageCard,notifications_db,Plant_List

admin.site.register(User_Data)
admin.site.register(Shift)
admin.site.register(Tank)
admin.site.register(Chemical)
class SOPAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(SOP, SOPAdmin)
admin.site.register(Batch_Card)


class TaskAdmin(admin.ModelAdmin):
    readonly_fields=('id',)


admin.site.register(CreateTask, TaskAdmin)
admin.site.register(Tasks_list)
admin.site.register(ManPower_Detail)
admin.site.register(Plant_Detail)
admin.site.register(Plant_List)


class MaintenanceAdmin(admin.ModelAdmin):
    readonly_fields=('id',)


admin.site.register(Maintenance_Detail, MaintenanceAdmin)
admin.site.register(Sample)
admin.site.register(PackageCard)
admin.site.register(notifications_db)