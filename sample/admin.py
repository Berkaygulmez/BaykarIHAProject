from django.contrib import admin
from sample.models import Sample
# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    list_display= ['marka', 'model','agirlik', 'kategori']
    list_filter = ['marka', 'model','agirlik', 'kategori']
    list_display_links = ['marka']

    class Meta:

        model = Sample

admin.site.register(Sample, SampleAdmin)
