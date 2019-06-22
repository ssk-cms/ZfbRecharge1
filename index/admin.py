from django.contrib import admin
from .models import *
# Register your models here.

# 地区相关的模型注册
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Area)

# 店铺相关的模型注册
admin.site.register(Shop)
admin.site.register(Position)
admin.site.register(Employee)

# 商品相关的模型注册
admin.site.register(GoodType)
admin.site.register(Good)

# 库存相关的模型注册
admin.site.register(BasicRecord)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Paytype)
admin.site.register(InRecord)
admin.site.register(OutRecord)
admin.site.register(BackRecord)


