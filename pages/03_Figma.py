import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Figma",
    page_icon="🌎",
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
    
def centrar_imagen_link(imagen, link, nombre, ancho):
    st.markdown(
        f"""
        <style>
            .imagen-enlace {{
                cursor: pointer;
                transition: transform 0.3s;
            }}
        </style>
        <div style="display: flex; justify-content: center;">
            <a href="{imagen}" target="_blank">
                <img class="imagen-enlace" src="{imagen}" width="{ancho}" alt="{nombre}">
            </a>
        </div>
        <h5 style='text-align: center;'><a href='{link}' target="_blank">{nombre}</a></h5>
        """,
        unsafe_allow_html=True
    )
    
def photo_link(alt_text, img_url, link_url, img_width):
    markdown_code = f'''
    <div style="text-align: center;">
        <a href="{link_url}" target="_blank">
            <img src="{img_url}" alt="{alt_text}" width="{img_width}px">
        </a>
    </div>
    '''
    st.markdown(markdown_code, unsafe_allow_html=True)

centrar_texto("Images de figma", 1, 'white')
centrar_texto_link("Link a Figma", "https://www.figma.com/files/team/1396528640782472952/recents-and-sharing/recently-viewed?fuid=1396528638461514079", 5, "blue")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la Historia 1", 3, 'white')
centrar_texto("Personalización de Mapas Interactivos", 3, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20001.png?raw=true", 400)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la Historia 2", 3, 'white')
centrar_texto("Filtro de Puntos de Interés", 3, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20002.png?raw=true", 400)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la Historia 3", 3, 'white')
centrar_texto("Integración con el Sistema de Reservas", 3, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20003.png?raw=true", 500)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la Historia 4", 3, 'white')
centrar_texto("Sección de Opiniones de Experiencias", 3, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20004.png?raw=true", 500)
               
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la Historia 5", 3, 'white')
centrar_texto("Notificaciones de Reservas de Experiencias", 3, 'white')
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20005.png?raw=true", 400)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la historia 6", 3, "white")
centrar_texto("Implementación de Mapas Interactivos", 3, "white")  
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20006.png?raw=true", 500)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la historia 7", 3, "white")
centrar_texto("Experiencias Recomendadas Basadas en Preferencias", 3, "white")  
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20007.png?raw=true", 500)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la historia 8", 3, "white")
centrar_texto("Integración de Calendario de Experienciass", 3, "white")  
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20008.png?raw=true", 500)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)
centrar_texto("Imagen para la historia 10", 3, "white")
centrar_texto("Sistema de Recompensas por Reservas", 3, "white")  
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/Historia%20010.png?raw=true", 450)


st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#ffb754;" /> """, unsafe_allow_html=True)

with st.container():
    col01, col02, col03 = st.columns(3)
    with col01:
        if st.button("Anterior", use_container_width=True):
            st.switch_page("pages/02_Backlog.py")
    with col03:
        if st.button("Siguiente", use_container_width=True):
            st.switch_page("pages/04_Jira_instructivo.py")
