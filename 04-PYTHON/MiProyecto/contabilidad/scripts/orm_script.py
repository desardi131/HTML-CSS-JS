from contabilidad.models import Cliente, Factura
import datetime

def run():
    pass


'''

    pedro = Cliente(id=1)
    factura = Factura(
        cliente = pedro, 
        importe = 5690.12, 
        pagada = False
        )
    factura.save()

Es lo mismo que esto:

    factura = Factura()
    factura.cliente = pedro
    factura.importe = 5690.12
    factura.pagada = False
    factura.save

'''