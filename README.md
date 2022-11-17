# README

# Arranque:
Luego del comando  "python manage.py runserver": 
ponemos "/App/" en la url para ir a la pagina de inicio

## Ingreso a cada seccion
Para ir a cada seccion ponemos "/" y luegos el nombre correspondiente
```python
urlpatterns = [
    path("", views.inicio,name="inicio"), 
    path("nosotros", views.nosotros,name="nosotros") ,    
    path("registro", views.registro,name="registro" ) , 
    path("persona", views.personaFormulario,name="personaFormulario" ), 
    path("listado", views.listadoTrabajadores,name="listadoTrabajadores" ),
    path("buscarPersonas", views.buscarPersonas,name="buscarPersonas" ), 
    path("buscarPersonasResultados/",views.buscar) ,
]
```

# Seccion Inicio

# Seccion Nosotros
Objetivo de la Pagina

# Puedes ingresar al panel de administracion "/admin/" para ver datos registrados:
user:fms97
clave:python1997

# Seccion Informacion
Insertar nombre, apellido ,email y nacimiento todos aquellos que quieran recibir informacion de la empresa
En en panel de administracion se vera en "registros"

# Seccion Entrevistas
Insertar nombre, apellido y profesion aquellos que quieren aplicar para una entrevista de trabajo
En en panel de administracion se vera en "integrantes"

# Seccion Registro_Integrantes
Insertar nombre,apellido, email y nacimiento aquellos que esten trabajando en la empresa  actualmente para darse de alta
En en panel de administracion se vera en "personnas"


# Seccion Integrantes
Colocar un apellido para buscar un integrante de la empresa que este trabajando actualmente y se  recibira: nombre , email y fecha de nacimiento  (busqueda en base de datos en base a los registros de la seccion "Registro_Integrantes")
En en panel de administracion se vera en "personas"

Ejemplo: poner en esta seccion el apellido "Sassi" y se veran los distintos registros

