
from django.urls import path
from .views import *

urlpatterns = [
    path('<name>/', about_me),
    path('<name>/about-me', about_me, name='about-me'),
    path('<name>/skill', skill, name='skill'),
    path('<name>/interest', interest, name='interest'),
    path('<name>/award', award, name='award'),
    path('<name>/education', education, name='education'),
    path('<name>/experience', experience, name='experience'),
    path('custom/admin/', c_admin, name='custom-admin'),
    path('custom/skills', admin_skills, name='admin_skill'),
    path('custom/add-skills', add_skill, name='add_skill')

]
