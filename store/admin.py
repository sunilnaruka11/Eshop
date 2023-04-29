from django.contrib import admin

from .models.category import Category  # import Category Class
from .models.product import Product    # import Product Class
from .models.customer import Customer    # import Customer  Class

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
       list_display=('id','name')
	   

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
       list_display=('id','name', 'price', 'category')

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
       list_display=('id','first_name', 'last_name', 'phone','email')
       