from django.urls import path
from AtoK_app import views

urlpatterns = [
       path("",views.AtoK,name='AtoK'),
       path("home",views.home,name='hm'),
       path('aboutus/',views.aboutus,name='ab'),
       path("predict/",views.predict,name='pre'),
       path('expertsystem/',views.expertSystem,name='es'),
       path('result/',views.result, name='res')

]