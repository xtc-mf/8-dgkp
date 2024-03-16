from django.contrib import admin
from .models import Breaking, Material, Staff, BreakingMaterial

admin.site.register(Staff)
admin.site.register(Material)
admin.site.register(Breaking)
admin.site.register(BreakingMaterial)
# dgkpADMIN