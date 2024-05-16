from django.http import HttpResponse
import datetime

# Home para no tener vistas con error
def home(request):
    texto = """<html>
    <body>
    <h1>Estás en la página principal</h1>
    </body>
    </html>
    """
    return HttpResponse(texto)

# Definicion de vista, primera prueba
def saludo(request):

    texto = """<html>
    <body>
    <h1>Hola mundo</h1>
    </body>
    </html>
    """
    return HttpResponse(texto)

# Definicion de una vista para contenido dinámico
def fecha(request):
    mifecha = datetime.datetime.now()

    texto2 = '''<html>
    <body>
    <h1> Fecha y hora actual: </h1>%s
    </body>
    </html>
    '''% mifecha
    return HttpResponse(texto2)

# Calculo de edad en otra vista
def calcedad(request,year,edadactual):
    periodo = year - 2024
    edadfutura = edadactual+periodo

    texto = '''<html>
    <body>
    <h2> En el año %s tendrás %s años </h2>
    </body>
    </html>
    '''% (year, edadfutura)
    
    return HttpResponse(texto)