from django.urls import path
from App import views

urlpatterns = [
    path("", views.inicio,name="inicio"), 
    path("nosotros", views.nosotros,name="nosotros") ,    
    path("registro", views.registro,name="registro" ) , 
    path("persona", views.personaFormulario,name="personaFormulario" ), 
    path("listado", views.listadoTrabajadores,name="listadoTrabajadores" ),
    path("buscarPersonas", views.buscarPersonas,name="buscarPersonas" ), 
    path("buscarPersonasResultados/",views.buscar) ,
]