from django.contrib import admin
from biblioteca.models import Autor
from biblioteca.models import Libro
from biblioteca.models import Usuario
from biblioteca.models import Ejemplar

# Register your models here.

admin.site.register(Autor, )
admin.site.register(Libro, )
admin.site.register(Usuario, )
admin.site.register(Ejemplar, )