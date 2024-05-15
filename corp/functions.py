from django.conf import settings
from django.utils import dateformat

def obtenerMesYAño(DateTimeFormat):
    mes_año = dateformat.format(DateTimeFormat, 'm Y')
    split = mes_año.split(" ")
    meses = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"
    }
    mes = meses[split[0]]
    año = split[1]
    concatenado = mes + ", " + año
    return concatenado