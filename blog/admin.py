from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published', 'post_categories')       #Para mostrar las diferentes columnas de los objetos o de la base de datos}
    ordering = ('author', 'published')                   #Para ordenar primero por un campo y luego por un subcampo
    search_fields = ('title','content','author__username', 'categories__name')  #Formulario de búsquedas
    date_hierarchy = 'published'    #Permite filtrar por fechas los objetos de manera herarquica
    list_filter = ('author__username', 'categories__name') #Permite crear filtros automáticos por un campo que le definamos

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"    #Para cambiar el nombre del método mostrado como campo


admin.site.register(Category, CategoryAdmin)    #Registrar apps en el admin
admin.site.register(Post, PostAdmin)            #Registrar apps en el admin
