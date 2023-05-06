from django.contrib import admin
from producto_app.models import Marca, Producto

class MarcaAdmin(admin.ModelAdmin):
    model = Marca
    list_display = ("id","nombre")
    search_fields = ("nombre",)

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ("id","nombre","precio","marca")
    search_fields = ("nombre","marca__nombre")
    list_filter = ("marca__nombre",)



admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca, MarcaAdmin)