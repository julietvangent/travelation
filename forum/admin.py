from django.contrib import admin
from .models import Post, DestinationsPost, PracticalPost, OtherPost, Comment

admin.site.register(Post)
admin.site.register(DestinationsPost)
admin.site.register(PracticalPost)
admin.site.register(OtherPost)
admin.site.register(Comment)
