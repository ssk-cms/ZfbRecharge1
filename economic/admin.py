from django.contrib import admin

# Register your models here.
from economic.models import *

admin.site.register(Gdp)
admin.site.register(Gdp_compose)
admin.site.register(Gdp_index_number)
admin.site.register(Gdp_index_year)
admin.site.register(Area_gdp)
admin.site.register(Consum_level)
