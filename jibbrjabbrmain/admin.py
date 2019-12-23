from django.contrib import admin
from .models import JJStory, JJItem, storyReloadConditional

# Register your models here.
admin.site.register(JJStory)
admin.site.register(JJItem)
admin.site.register(storyReloadConditional)