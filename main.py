import mechanicalsoup
import requests
from bs4 import BeautifulSoup

# crear la lista de convocatorias
scholarchipCalls=[]
# añadir la cabecera
headerList=["País","Programa","Area","Oferente","Tipo","Título"]
scholarchipCalls.append(headerList)

# URL de la página del ICETEX a consultar las becas
url = "https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true"
browser = mechanicalsoup.StatefulBrowser()  # se define el browser
browser.open(url)  # se abre la URL

# Esta página muestra las becas solo cuando se da click en la opción "Todas"
browser.select_form("#form1")  # seleccionamos el formulario
browser["RBLOpcionBuscar"] = "Todas"  # seleccionamos que busque con la opción "Todas"
response = browser.submit_selected()  # enviamos el fomulario y capturamos las respuestas
# en este punto ya tenemos la tabla #GVConvocatorias con la lista de becas
# hay que proceder a realizar la extracción de datos teniendo en cuenta la paginación

# Entrar a cada una de las convocatorias
#for i in (0,9):
browser2 = browser
browser2.select_form("#form1")
# añadir los parámetros escondidos, usar force=True
# opción de consulta de convocatoria
browser2.get_current_form().set("__EVENTTARGET", "GVConvocatorias",  True)
# identificador de la convocatoria
browser2.get_current_form().set("__EVENTARGUMENT", "$0",  True) # activar el for y reemplazar el 0 con i
# enviar el formulario que consulta la convocatoria específica
response2 = browser2.submit_selected()

# obtener el soup a partir de la respuesta a la acción anterior
soup = BeautifulSoup(response2.text, "html.parser")
# obtener cada fila de la tabla
rows = soup.findAll("span", { "class" : "label1" })


# para cada fila
for row in rows:
    tupla = ();
    print(row)
    if row.has_attr("id"):
        id = row["id"]
        value = row[0]
        print(id, value)


# print(response2.text)

