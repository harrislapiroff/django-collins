from models import *
from django.contrib import admin
from django.contrib.contenttypes import generic

class PostShellInline(generic.GenericStackedInline):
	model = PostShell
	ct_field = 'post_content_type'
	ct_fk_field = 'post_content_id'
	extra = 1
	max_num = 1
	can_delete = False
	template = 'collins/admin/shell_inline.html'

class PostAdmin(admin.ModelAdmin):
	inlines = [PostShellInline]
	
admin.site.register(Blog)
admin.site.register(TextPost, PostAdmin)
admin.site.register(ImagePost, PostAdmin)
admin.site.register(LinkPost, PostAdmin)
admin.site.register(ChatPost, PostAdmin)
admin.site.register(VideoFilePost, PostAdmin)
admin.site.register(VideoExternalPost, PostAdmin)
admin.site.register(AudioPost, PostAdmin)
admin.site.register(CodePost, PostAdmin)
admin.site.register(PostShell)