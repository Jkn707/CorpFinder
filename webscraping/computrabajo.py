import requests
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime

def buscar_empresas(busqueda):
    url_busqueda = "https://co.computrabajo.com/empresas/buscador?q=" + urllib.parse.quote(busqueda)
    headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    res_busqueda = requests.get(url_busqueda, headers=headers)
    soup_busqueda = BeautifulSoup(res_busqueda.text, "html.parser")
    resultados = soup_busqueda.find_all("a", class_="js-o-link")
    empresas_link = {}
    for resultado in resultados:
        empresas_link[resultado.text] = resultado.attrs["href"]

    return empresas_link

def obtener_datos_empresa(link_empresa):
    base_url = "https://co.computrabajo.com"
    url = base_url + link_empresa
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f"Error: La solicitud no pudo ser completada. Código de estado: {res.status_code}")
        return None

    soup = BeautifulSoup(res.text, "html.parser")

    nombre_empresa = soup.find("h1", class_="m0 pr10").text if soup.find("h1", class_="m0 pr10") else None
    logo_empresa = None if soup.find("div", class_="logo_company").find("img")["src"] == "//cp.ct-stc.com/web/20240404.02/c/img/edVal.png" else soup.find("div", class_="logo_company").find("img")["src"] if soup.find("div", class_="logo_company") else None
    calificacion_empresa2_tag = soup.find("p", class_="ml10 fs16 mt5")
    calificacion_empresa_span = calificacion_empresa2_tag.find("span", class_="fwB mr5") if calificacion_empresa2_tag else None
    calificacion_empresa = calificacion_empresa_span.text.replace(",", ".") if calificacion_empresa_span else None
    banner_empresa = soup.find("img", class_="w_100").attrs["src"].replace(" ", "%20") if soup.find("img", class_="w_100") else None
    subtitle = soup.find("article", class_="first").find("span", class_="subtitle").text if soup.find("article", class_="first") else None
    subtitle_content = soup.find("article", class_="first").find("p").text if soup.find("article", class_="first") else None
    subtitle2 = soup.find("article", class_="second").find("span", class_="subtitle").text if soup.find("article", class_="second") else None
    subtitle2_content = soup.find("article", class_="second").find("p").text if soup.find("article", class_="second") else None
    extraido = "Computrabajo"
    seguidores = int(soup.find("span", class_="fc_aux fs14_m").text.split()[0].replace(".", "") if soup.find("span", class_="fc_aux fs14_m") else None)
    ofertas = int((soup.find("a", title="Ofertas").find("span", class_="fc_gray").text.replace(".", "") if soup.find("a", title="Ofertas") and soup.find("a", title="Ofertas").find("span", class_="fc_gray") else 0))
    evaluaciones = int((soup.find("a", title="Evaluaciones").find("span", class_="fc_gray").text.replace(".", "") if soup.find("a", title="Evaluaciones") and soup.find("a", title="Evaluaciones").find("span", class_="fc_gray") else 0))
    salarios = int((soup.find("a", title="Salarios").find("span", class_="fc_gray").text.replace(".", "") if soup.find("a", title="Salarios") and soup.find("a", title="Salarios").find("span", class_="fc_gray") else 0))
    entrevistas = int((soup.find("a", title="Entrevistas").find("span", class_="fc_gray").text.replace(".", "") if soup.find("a", title="Entrevistas") and soup.find("a", title="Entrevistas").find("span", class_="fc_gray") else 0))
    beneficios = int((soup.find("a", title="Beneficios").find("span", class_="fc_gray").text.replace(".", "") if soup.find("a", title="Beneficios") and soup.find("a", title="Beneficios").find("span", class_="fc_gray") else 0))
    fotos = int((soup.find("a", title="Fotos").find("span", class_="fc_gray").text.replace(".", "") if soup.find("a", title="Fotos") and soup.find("a", title="Fotos").find("span", class_="fc_gray") else 0))

    #Datos evaluaciones
    try:
        link_evaluaciones = soup.find("a", title="Evaluaciones")
        if link_evaluaciones:
            url2 = base_url + link_evaluaciones["href"]
            res2 = requests.get(url2, headers=headers)

            if res2.status_code != 200:
                print(f"Error: La segunda solicitud no pudo ser completada. Código de estado: {res.status_code}")
                print(url2)
                return None

            soup2 = BeautifulSoup(res2.text, "html.parser")

            ##Porcentajes
            porcentajes_evaluaciones = soup2.find_all("p", class_="fs18 fwB")
            calificaciones = [float(calificacion.text.replace(',', '.')) for calificacion in porcentajes_evaluaciones]
            calificacion_ambiente_trabajo, calificacion_salario_prestaciones, calificacion_oportunidades_carrera, calificacion_director_general = calificaciones

        else:
            calificacion_ambiente_trabajo, calificacion_salario_prestaciones, calificacion_oportunidades_carrera, calificacion_director_general = [None] * 4


    except AttributeError:
        calificacion_ambiente_trabajo, calificacion_salario_prestaciones, calificacion_oportunidades_carrera, calificacion_director_general = [None] * 4

    ##Comentarios

    datos_empresa = {
        "nombre_empresa": nombre_empresa,
        "logo_empresa": logo_empresa,
        "banner_empresa": banner_empresa,
        "subtitle": subtitle,
        "subtitle_content": subtitle_content,
        "subtitle2": subtitle2,
        "subtitle2_content": subtitle2_content,
        "seguidores": seguidores,
        "extraido_de": extraido,
        "numero_ofertas":ofertas,
        "numero_evaluaciones": evaluaciones,
        "numero_salarios": salarios,
        "numero_entrevistas": entrevistas,
        "numero_beneficios": beneficios,
        "numero_fotos": fotos,
        "calificacion_empresa": calificacion_empresa,
        "calificacion_ambiente_trabajo": calificacion_ambiente_trabajo,
        "calificacion_salario_prestaciones": calificacion_salario_prestaciones,
        "calificacion_oportunidades_carrera": calificacion_oportunidades_carrera,
        "calificacion_director_general": calificacion_director_general
    }

    return datos_empresa

