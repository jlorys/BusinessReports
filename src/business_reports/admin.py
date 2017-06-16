from django.contrib import admin
from django.forms import PasswordInput
from django.conf import settings

from encrypted_fields import EncryptedCharField
from models import DataConnection, Parameter, DataSet, Style, Report, ReportDataSet, \
    DataSetParameter

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_datetime','updated_datetime','created_by','last_updated_by')
    def save_model(self, request, obj, form, change):
        if hasattr(obj, 'created_by') and not obj.id:
            obj.created_by = request.user
        if hasattr(obj, 'last_updated_by'):
            obj.last_updated_by = request.user
        obj.save()

class DataConnectionAdmin(BaseAdmin):
    formfield_overrides = {
        EncryptedCharField: {'widget': PasswordInput(render_value=True)},
    }

class ParameterAdmin(BaseAdmin):
    if not getattr(settings,'MR_REPORTS_ALLOW_NATIVE_PYTHON_CODE_EXEC_ON_SERVER',False):
        readonly_fields = ('python_create_default',)

class DataSetParameterInline(admin.TabularInline):
    model = DataSetParameter
    #fields = (edit_parameter_link,)
    extra = 0
    #def edit_parameter_link(self, instance):
    #    return 'test' #instance.parameter.edit_link()
    #edit_parameter_link.short_description = "Edit Parameter"

class DataSetAdmin(BaseAdmin):
    class Media:
        js = ('js/create_parameter_edit_links.js',)

    if not getattr(settings,'MR_REPORTS_ALLOW_NATIVE_PYTHON_CODE_EXEC_ON_SERVER',False):
        readonly_fields = ('python_post_processing',)
    inlines = [DataSetParameterInline]
    exclude=('parameters',)

class StyleAdmin(BaseAdmin):
    pass

class ReportDataSetInline(admin.TabularInline):
    model = ReportDataSet #Report.datasets.through
    #fields = ('dataset__name','dataset__edit_link')
    extra = 0

class ReportAdmin(BaseAdmin):
    class Media:
        js = ('js/create_dataset_edit_links.js',)
    list_display = BaseAdmin.list_display + ('view_report',)
    exclude=('datasets',)
    inlines = [ReportDataSetInline,]

    def duplicate(self, request, queryset):
        """An easy way to copy reports instead of starting from scratch."""
        #make duplicate of each object in queryset
        for obj in queryset:
            old_datasets = list(obj.reportdataset_set.all())
            obj.id = None
            obj.title += ' (copy)'
            obj.save()

            new_datasets = [
                ReportDataSet(report = obj, dataset = d.dataset, order_on_report = d.order_on_report)
                for d in old_datasets]
            ReportDataSet.objects.bulk_create(new_datasets)

    duplicate.short_description = "Duplicate Selected Reports"
    actions = [duplicate]

admin.site.register(DataConnection, DataConnectionAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Report, ReportAdmin)