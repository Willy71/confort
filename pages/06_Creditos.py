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
    texto_html = f"<h{tamanho} style='text-align: center; color: {color}'><a href='{link_url}' style="text_decoration: none;" target='_blank'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{link_texto}</a></h{tamanho}>"
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
    markdown_code = f'<a href="{link_url}" target="_blank"><img src="{img_url}" alt="{alt_text}" width="{img_width}px"></a>'
    st.markdown(markdown_code, unsafe_allow_html=True)

centrar_texto("Creditos - Guillermo Cerato", 1, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_texto("Curso realizado por Silvertech, en colaboración con", 2, 'white')
centrar_texto("Eidos Global y Diagonal Asociación Civil", 2, 'white')
st.subheader("")
with st.container():
    col01, col02, col03, col04, col05 = st.columns([1.7,2,2,2,0.5])
    with col02:
        photo_link("Silvertech", "https://github.com/Willy71/confort/blob/main/pictures/Silvertech.png?raw=true", "https://www.soysilvertech.org/comunidad", 110)
    with col03:
        photo_link("Eidos", "https://github.com/Willy71/confort/blob/main/pictures/Eidos.png?raw=true", "https://www.eidosglobal.org/", 110)
    with col04:
        photo_link("Diagonal", "https://github.com/Willy71/confort/blob/main/pictures/diagonal.png?raw=true", "https://diagonal.org.ar/", 110)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

with st.container():    
    col41, col42, col43 = st.columns(3)
    with col41:
        centrar_imagen("https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png", 80)
        centrar_texto_link("Kaggle", "https://www.kaggle.com/willycerato", 6, 'white')
    with col42:
        centrar_imagen("https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png", 80)
        centrar_texto_link("Github", "https://github.com/Willy71", 6, 'white')
    with col43:
        centrar_imagen("https://img.freepik.com/vetores-premium/logotipo-quadrado-do-linkedin-isolado-no-fundo-branco_469489-892.jpg", 80)
        centrar_texto_link("Linkedin", "https://www.linkedin.com/in/willycerato",  6, 'white')
    st.caption("")
    col44, col45, col46 = st.columns(3)
    with col44:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2023_Facebook_icon.svg/50px-2023_Facebook_icon.svg.png", 80)
        centrar_texto_link("Facebook", "https://www.facebook.com/guillermo.cerato", 6, 'white')
    with col45:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/150px-Instagram_logo_2022.svg.png", 80)
        centrar_texto_link("Instagram", "https://www.instagram.com/willycerato", 6 ,'white')
    with col46:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/120px-WhatsApp.svg.png", 80)
        centrar_texto_link("Whatsapp", "https://wa.me/5542991657847", 6, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

with st.container():
    col51, col52 = st.columns(2)
    with col51:
        st.markdown("<h2 style='text-align: center; color: white'>Website made with Streamlit</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: blue;'>Programmed with Python</h2>", unsafe_allow_html=True)
    with col52:
        co53, col54, col55, col56, col57 = st.columns(5)
        with col54:            
            st.text(" ")
            st.text(" ")
            photo_link('', "https://i.postimg.cc/cJhYJnqx/streamlit-logo.jpg", 'https://streamlit.io/', 200)
        with col56:
            photo_link('', "https://i.postimg.cc/9Q3yg2th/python.png", 'https://www.python.org', 200)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_texto_link("Link del repositorio de Github de esta presentación", "https://github.com/Willy71/confort/tree/main", 4, 'blue')
            
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)
