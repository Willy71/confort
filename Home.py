import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Silvertech - Trabajo final",
    page_icon="🌎",
    layout="wide"
)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/Willy71/confort/blob/main/pictures/background2.png?raw=true");
background-size: 180%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

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

def photo_link_right(alt_text, img_url, link_url, img_width):
    markdown_code = f'''
    <div style="text-align: right;">
        <a href="{link_url}" target="_self">
            <img src="{img_url}" alt="{alt_text}" width="{img_width}px">
        </a>
    </div>
    '''
    st.markdown(markdown_code, unsafe_allow_html=True)

def photo_link_center(alt_text, img_url, link_url, img_width):
    markdown_code = f'''
    <div style="text-align: center;">
        <a href="{link_url}" target="_self">
            <img src="{img_url}" alt="{alt_text}" width="{img_width}px">
        </a>
    </div>
    '''
    st.markdown(markdown_code, unsafe_allow_html=True)

centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/titular3.png?raw=true", 600)
    
#centrar_texto("Nueva funcionalidad para app Confort", 1, "white")

if 'rerun' not in st.session_state:
    st.session_state.rerun = False

if st.button("Reiniciar"):
    st.session_state.rerun = True

if st.session_state.rerun:
    st.experimental_rerun()

with st.container():
    col01, col02, col03 = st.columns(3)
    with col02:
        centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/confort_remove.png?raw=true", 300)
    with col03:
        st.header("")
        st.header("")
        photo_link_right("", "https://github.com/Willy71/confort/blob/main/pictures/Button%20-%20Siguiente.png?raw=true","https://confort.streamlit.app/Encuesta_para_relevar_info", 80)

