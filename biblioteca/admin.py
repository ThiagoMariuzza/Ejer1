from django.contrib import admin
from biblioteca.models import Autor
from biblioteca.models import Libro
from biblioteca.models import Usuario
from biblioteca.models import Ejemplar


class LibroAdmin(admin.ModelAdmin):
    list_display = ['Titulo', 'Editorial']
    #fields = ['Titulo', 'Editorial']

class LibroInline(admin.TabularInline):
    model = Libro

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Direccion']
    list_display_links = ['Nombre', ]
    fieldsets = ( 
        ('Datos', {
            'fields': ('Nombre',)
        }),
        ('Contacto',{
            'fields': ('Telefono','Direccion')
        }),
    )

class AutorAdmin(admin.ModelAdmin):
    list_display = ['Nombre',]
    inlines = [LibroInline,]
    search_fields = ['Nombre']

class EjemplarAutor(admin.ModelAdmin):
    list_display = ['Libro', 'Usuario']
    list_filter = ('Libro',)


# Register your models here.

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Ejemplar, EjemplarAutor)