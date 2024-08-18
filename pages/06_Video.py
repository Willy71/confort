import streamlit as st

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

video_url = "https://youtu.be/M4NeIIbvKZ8"
#video_url = "https://drive.google.com/file/d/1FUGzNcRRjdKT18eUaLOrVWqf0lLB_TY3/view?usp=sharing"

with st.container():
    col1, col2, col3 =st.columns([1,3,1])    
    with col2:    
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
