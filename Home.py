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

centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/titular3.png?raw=true", 600)
    
#centrar_texto("Nueva funcionalidad para app Confort", 1, "white")

centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/confort_remove.png?raw=true", 300)
