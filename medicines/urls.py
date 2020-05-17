from django.urls import path,include
from medicines.views import index,signup,signin,aboutus,contactus,store,askadoctor,contactuslogin,aboutuslogin,cart,orderplace

urlpatterns = [
     path('',index),
     path('signup/',signup),
     path('signin/',signin),
     path('aboutus/',aboutus),
     path('contactus/',contactus),
     path('store/',store,),
     path('askadoctor/',askadoctor),
     # path('renderobject/',renderobject),
     path('contactuslogin/',contactuslogin),
     path('aboutuslogin/',aboutuslogin),
     path('cart/',cart),
     path('orderplace/',orderplace)
]