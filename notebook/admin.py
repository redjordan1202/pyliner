from django.contrib import admin
from .models import Notebook, Page, List, List_object


admin.site.register(Notebook)
admin.site.register(Page)
admin.site.register(List)
admin.site.register(List_object)
