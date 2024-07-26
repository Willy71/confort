import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Video",
    page_icon="▶",
    layout="wide"
)

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
    
centrar_texto("Video presentación del proyecto", 1, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#1717dc;" /> """, unsafe_allow_html=True)

# URL del video de YouTube
video_url = 'https://youtu.be/uUjNcp778eU'

# URL de la miniatura de YouTube (asegúrate de que tenga las dimensiones correctas)
#thumbnail_url = ''

# HTML y CSS para ajustar la imagen
#thumbnail_html = f"""
#<div style="display: flex; justify-content: center; align-items: center; height: 720px; width: 1280px;">
#    <img src="{thumbnail_url}" style="width: 100%; height: 100%; object-fit: contain;">
#</div>
#"""

# Mostrar la miniatura como imagen
#st.markdown(thumbnail_html, unsafe_allow_html=True)

# Reproducir el video
st.video(video_url)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#1717dc;" /> """, unsafe_allow_html=True)

with st.container():
    col01, col02, col03 = st.columns(3)
    with col01:
        if st.button("Anterior", use_container_width=True):
            st.switch_page("pages/05_Diagramas_de_flujo.py")
    with col03:
        if st.button("Siguiente", use_container_width=True):
            st.switch_page("pages/07_Creditos.py")
