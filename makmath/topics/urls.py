from django.urls import path

from .views import *

urlpatterns = [
    path('', MakMathHome.as_view(), name="home"),
    path('section/<slug:section_slug>/', SectionShower.as_view(), name="section"),
    path('about/', about, name="about"),
    path('topics/<slug:topic_slug>/', show_topic, name='topic'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('user_cabinet/', show_user_info, name='user_profil')


]
