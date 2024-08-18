import streamlit as st
from urllib.parse import urlparse, parse_qs

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Video",
    page_icon="▶",
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
    
centrar_texto("Video presentación del proyecto", 1, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#1717dc;" /> """, unsafe_allow_html=True)

def video(url):
    # Parsear la URL para extraer el video_id
    parsed_url = urlparse(url)
    video_id = ""
    
    if parsed_url.hostname == "youtu.be":
        # Formato corto de YouTube: https://youtu.be/video_id
        video_id = parsed_url.path[1:]
    elif parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        if parsed_url.path == "/watch":
            # URL normal: https://www.youtube.com/watch?v=video_id
            video_id = parse_qs(parsed_url.query).get("v", [None])[0]
        elif parsed_url.path.startswith("/embed/"):
            # URL embed: https://www.youtube.com/embed/video_id
            video_id = parsed_url.path.split("/")[2]
        elif parsed_url.path.startswith("/v/"):
            # URL tipo /v/: https://www.youtube.com/v/video_id
            video_id = parsed_url.path.split("/")[2]
    
    # Generar la URL de embed si se encontró el video_id
    if video_id:
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        st.markdown(f"""
                    <div style="display: flex; justify-content: center;">
                        <iframe width="1280" height="300"
                        src="{embed_url}" 
                        frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
                        </iframe>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.error("No se pudo extraer el ID del video. Asegúrate de que el enlace sea válido.")


video_url = "https://youtu.be/M4NeIIbvKZ8"
#video_url = "https://drive.google.com/file/d/1FUGzNcRRjdKT18eUaLOrVWqf0lLB_TY3/view?usp=sharing"

with st.container():
    col1, col2, col3 =st.columns([1,3,1])    
    with col2:    
        video(video_url)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#1717dc;" /> """, unsafe_allow_html=True)

with st.container():
    col01, col02, col03 = st.columns(3)
    with col01:
        if st.button("Anterior", use_container_width=True):
            st.switch_page("pages/05_Diagramas_de_flujo.py")
    with col03:
        if st.button("Siguiente", use_container_width=True):
            st.switch_page("pages/07_Creditos.py")
