import requests
from bs4 import BeautifulSoup
import time
from IPython.display import display, Markdown

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
base_url = "https://co.computrabajo.com"
headers = {"user-agent": userAgent}

def obtener_comentarios(url, limite_paginas=10):
    page = 1
    comentarios_totales = []

    while page <= limite_paginas:
        if page != 1:
            url_pagina = f"{url}?p={page}"
        else:
            url_pagina = url

        res_busqueda = requests.get(url_pagina, headers=headers)
        soup = BeautifulSoup(res_busqueda.text, "html.parser")

        comentarios = soup.find_all("div", class_="pt10 pb10 mbB")

        for comentario in comentarios:
            cargo = comentario.select_one('span.fwB').text.strip()
            info = comentario.select_one('p.list_dot.fc_aux.mb10').text.strip().replace("\n","").replace("\r","")
            contenido_tags = comentario.find_all('p', class_='mb10')[-1].contents

            contenido = ""
            for tag in contenido_tags:
                if tag.name == "strong":
                    contenido += f"<strong>{tag.get_text(strip=True)}</strong> "
                elif tag.name == "span":
                    contenido += f"{tag.get_text(strip=True)} "
                else:
                    contenido += f"{tag.get_text(strip=True)}"

            # Buscar la ubicación en la segunda parte de la cadena 'info'
            partes = info.split()
            fecha = partes[-2] + " " + partes[-1]
            if len(partes) == 5:
                ubicacion = partes[2]
            elif len(partes) == 6:
                ubicacion = partes[2] + " " + partes[3]
            elif len(partes) == 7:
                ubicacion = partes[2] + " " + partes[3] + " " + partes[4]

            # Almacenar los datos del comentario en una estructura de datos adecuada
            datos_comentario = {
                'cargo': cargo,
                'ubicacion': ubicacion,
                'fecha': fecha,
                'contenido': contenido.strip()
            }
            comentarios_totales.append(datos_comentario)

        # Busca el enlace a la siguiente página de comentarios
        next_page_link = soup.find("a", id="nextPage")

        if next_page_link:
            # Si se encuentra el enlace a la siguiente página, actualiza la página
            page += 1
        else:
            # Si no se encuentra el enlace, termina el bucle
            break

    return comentarios_totales

# URL base de la página de comentarios
url = "https://co.computrabajo.com/activos/evaluaciones"

# Obtener comentarios limitados a 10 páginas
comentarios = obtener_comentarios(url, limite_paginas=10)

# Imprimir los comentarios
numero = 0
for comentario in comentarios:
    numero = numero + 1
    print(f'{numero} - Cargo: {comentario["cargo"]}, Ubicación: {comentario["ubicacion"]}, Fecha: {comentario["fecha"]}, contenido: {comentario["contenido"]}')
