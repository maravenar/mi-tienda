from django.contrib import admin
from django import forms
from .models import Producto, Categoria, Slide, ConfiguracionSitio
from .widgets import ColorPickerWidget

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'activo', 'fecha_creacion']
    list_filter = ['categoria', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'stock', 'activo']
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen', 'stock', 'activo']

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'orden', 'activo']
    list_editable = ['orden', 'activo']
    ordering = ['orden']

class ConfiguracionSitioForm(forms.ModelForm):
    class Meta:
        model = ConfiguracionSitio
        fields = '__all__'
        widgets = {
            'color_primario': ColorPickerWidget(),
            'color_secundario': ColorPickerWidget(),
            'color_fondo': ColorPickerWidget(),
            'color_banner': ColorPickerWidget(),
            'color_cards': ColorPickerWidget(),
            'color_hover': ColorPickerWidget(),
        }

@admin.register(ConfiguracionSitio)
class ConfiguracionSitioAdmin(admin.ModelAdmin):
    form = ConfiguracionSitioForm
    list_display = ['mensaje_envio', 'activo']
    list_editable = ['activo']
    fieldsets = (
        ('Mensaje', {
            'fields': ('mensaje_envio', 'activo')
        }),
        ('Colores del Sitio', {
            'fields': (('color_primario', 'color_secundario'), ('color_fondo', 'color_banner'), ('color_cards', 'color_hover')),
            'description': 'Haz clic en los cuadros de color para abrir el selector de colores. Los cambios se aplicarán inmediatamente en el sitio.'
        }),
    )
    
    def has_add_permission(self, request):
        return not ConfiguracionSitio.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False