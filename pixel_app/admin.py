from django.contrib import admin


from pixel_app.models import Pixel, Color, Comment, Community, Thread
# Register your models here.
admin.site.register(Pixel)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Thread)
