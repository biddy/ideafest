from django.contrib import admin

from nodes.models import Node,Title


class NodeAdmin(admin.ModelAdmin):
    list_display = ["title","user","id","inherit","content","status"]
    list_editable = ["inherit"]


admin.site.register(Node, NodeAdmin)
admin.site.register(Title)
