import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Diagrama de flujo",
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
    texto_html = f"<h{tamanho} style='text-align: center; color: {color}'><a href='{link_url}' target='_blank'>{link_texto}</a></h{tamanho}>"
    st.markdown(texto_html, unsafe_allow_html=True)
    
centrar_texto("Diagramas de flujo", 1, 'white')
centrar_texto_link("Link Diagrama de flujo de la App","https://miro.com/app/board/uXjVKyXysYo=/", 4, 'blue')
centrar_texto_link("Link Diagrama de flujo del proyecto","https://miro.com/app/board/uXjVKyVTNOI=/", 4, 'blue') 
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#a2129f;" /> """, unsafe_allow_html=True)

centrar_texto("Diagrama de flujo de la App - Funcionamiento general", 2, 'white')
st.subheader("")
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/018.png?raw=true", 1200)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#a2129f;" /> """, unsafe_allow_html=True)

centrar_texto("Diagrama de flujo del proyecto - Funcionamiento general", 2, 'white')
st.subheader("")
centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/012.png?raw=true", 1200)


