from django.contrib import admin
from .models import Size,Color,GeneralCategory,Category,Campaign,Product,ProductImage
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model=ProductImage
    readonly_fields=['image_tag']
    extra=1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline]


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ProductImage)