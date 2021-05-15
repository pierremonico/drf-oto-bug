from django.contrib import admin

from wines.models import Bottle, Cork


admin.site.register(Bottle)
admin.site.register(Cork)