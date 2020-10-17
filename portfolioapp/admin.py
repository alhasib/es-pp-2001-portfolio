from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Award)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Profile)

