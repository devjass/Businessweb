from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    read_only = ('created', 'updated')
    
    def get_readonly_fields(self, request, obj=None):#Sobrescribimos este método para controlar que se muestra a los usuarios en el panel admin
        if(request.user.groups.filter(name="Personal").exists()):
            return ('key','name')
        else:
            return ('created','updated' )

admin.site.register(Link, LinkAdmin)