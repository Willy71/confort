import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Jira",
    page_icon="🧢",
    layout="wide"
)

# We reduced the empty space at the beginning of the streamlit
reduce_space ="""
            <style type="text/css">
            /* Remueve el espacio en el encabezado por defecto de las apps de Streamlit */
            div[data-testid="stAppViewBlockContainer"]{
                padding-top:30px;
            }
            </style>
            """
# We load reduce_space
st.html(reduce_space)

def centrar_imagen(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{imagen}" width="{ancho}">'
        f'</div>',
        unsafe_allow_html=True
    )
    
def centrar_texto(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: center; color: {color}'>{texto}</h{tamanho}>",
            unsafe_allow_html=True)
    
def texto(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: left; color: {color}'>{texto}</h{tamanho}>",
            unsafe_allow_html=True)
    
def centrar_texto_link(link_texto, link_url, tamanho, color):
    texto_html = f"<h{tamanho} style='text-align: center; color: {color}'><a href='{link_url}' target='_blank'>{link_texto}</a></h{tamanho}>"
    st.markdown(texto_html, unsafe_allow_html=True)

st.write("#")

centrar_texto("Jira - Instructivo", 1, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ef5626;" /> """, unsafe_allow_html=True)

texto("1er Paso - Luego de crear una cuenta y de confirmar via email, loguearse en la cuenta.", 5, 'white')
texto("2do Paso - En la pagina principal de la cuenta, hacer click en el 'PROYECTO', y luego en 'CREAR PROYECTO' en el menu desplegable, como se muestra en la figura.", 5, 'white') 
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_001.png?raw=true", 700)

st.subheader("")
texto("3er Paso - Hacer click en la opción 'DESARROLLO DE SOFTWARE'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_002.png?raw=true", 700)

st.subheader("")
texto("4to Paso - Hacer click en la metodologia 'SCRUM'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_003.png?raw=true", 700)

st.subheader("")
texto("5to Paso - Hacer click en 'USAR PLANTILLA'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_004.png?raw=true", 700)

st.subheader("")
texto("6to Paso - Hacer click en 'PROYECTO GESTIONADO POR EL EQUIPO'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_005.png?raw=true", 700)

st.subheader("")
texto("7mo Paso - Colocar el nombre del proyecto, luego seleccionar el tipo de acceso, en mi caso coloque abierto para que cualquiera que tenga el link de mi proyecto pueda acceder a verlo. A continuación hacer click en 'SIGUIENTE'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_006.png?raw=true", 700)

st.subheader("")
texto("8vo Paso - El proyecto ha sido creado. Para continuar haga click en 'BACKLOG'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_007.png?raw=true", 700)

st.subheader("")
texto("Ya estariamos listos para comenzar a adicionar historias, solo que antes es conveniente agregar algunos 'TIPOS DE INCIDENCIA', como por ejemplo 'CRITERIO DE ACEPTACIÓN', 'PRIORIDAD' Y 'FECHA ESTIMADA DE ENTREGA'", 5, 'white')

st.subheader("")
texto("9no Paso - Hacer click en 'CONFIGURACIONES DEL PROYECTO' en el costado izquierdo de la pagina (1) luego hacer click en 'TIPOS DE INCIDENCIA (2), y luego hacer click en 'STORY' (3)", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_008.png?raw=true", 700)

st.subheader("")
texto("10mo Paso - Para agregar el item 'CRITERIOS DE ACEPTACIÓN', haga click en 'PARRAFO' del lado derecho de la pantalla. Luego coloque el nombre 'CRITERIO DE ACEPTACIÓN', luego una breve descripción, y para finalizar esta etapa haga click en 'GUARDAR CAMBIOS'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_009.png?raw=true", 700)

st.subheader("")
texto("11er Paso - Agarre con el mouse 'CRITERIOS DE ACEPTACIÓN', arraste hacia abajo y luego suelte para ordenar", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_010.png?raw=true", 700)

st.subheader("")
texto("Para agregar 'PRIORIDAD' siga las mismas instrucciones que los pasos 10 y 11, solo que en vez de 'PARRAFO' seleccione 'NÚMERO'", 5, 'white')
texto("Para agregar 'FECHA ESTIMADA DE ENTREGA' siga las mismas instrucciones que los pasos 10 y 11, solo que en vez de 'PARRAFO' seleccione 'MARCA DE TIEMPO'", 5, 'white')

st.subheader("")
texto("12do Paso - Al finalizar guarde los cambios para continuar y vuelva al proyecto a traves de las flechas en la parte superior izquierda de la pagina (dos veces)", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_011.png?raw=true", 700)

st.subheader("")
texto("13er Paso - Realice los siguientes pasos para comenzar a crear la 'Epica'. Coloque el nombre y aprete 'ENTER'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_012.png?raw=true", 700)

st.subheader("")
texto("14to Paso - Haga click en crear incidencia", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_013.png?raw=true", 700)

st.subheader("")
texto("15to Paso - Haga click la flecha de la lista desplegable. Luego seleccione 'HISTORIA'", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_014.png?raw=true", 700)

st.subheader("")
texto("16to Paso - Coloque el nombre de la historia y aprete 'ENTER'. Ahora ya esta listo para agregar todos los campos del lado derecho de la pantalla", 5, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/jira_015.png?raw=true", 700)

st.subheader("")
centrar_texto("Buena suerte y buen trabajo!!!!", 3, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ef5626;" /> """, unsafe_allow_html=True)

with st.container():
    col01, col02, col03 = st.columns(3)
    with col01:
        if st.button("Anterior", use_container_width=True):
            st.switch_page("pages/03_Figma.py")
    with col03:
        if st.button("Siguiente", use_container_width=True):
            st.switch_page("pages/05_Diagramas_de_flujo.py")
