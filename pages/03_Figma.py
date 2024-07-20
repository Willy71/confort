import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Figma",
    page_icon="🌎",
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
    texto_html = f"<h{tamanho} style='text-align: center; color: {color}'><a href='{link_url}' style='text-decoration: none;' target='_blank'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{link_texto}</a></h{tamanho}>"
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

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_imagen("https://www.figma.com/proto/MMSnWmgHF5TBpEbxJ9iR8a/Confort-for-Silvertech?node-id=2-2&t=woONfDytrchqJA9q-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1", 400)
