import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Creditos",
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

centrar_texto("- Creditos -", 1, 'white')
centrar_texto("Trabajo realizado", 1, 'white')
centrar_texto("por", 1, 'white')
centrar_texto("Guillermo Cerato", 1, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_texto("Curso realizado por Silvertech", 2, 'white')
photo_link("Silvertech", "https://github.com/Willy71/confort/blob/main/pictures/Silvertech.png?raw=true", "https://www.soysilvertech.org/comunidad", 200)

st.subheader("")
               
with st.container():
    col10, col11 = st.columns(2)
    with col10:
        centrar_texto("Socios estratégicos", 4, 'white')
    with col11:
        centrar_texto("Impulsan", 4, 'white')
        
with st.container():
    col01, col02, col03, col04 = st.columns(4)
    with col01:
        st.text("")
        photo_link("Diagonal", "https://github.com/Willy71/confort/blob/main/pictures/diagonal.png?raw=true", "https://diagonal.org.ar/", 100)
    with col02:
        st.text("")
        photo_link("Bolster", "https://github.com/Willy71/confort/blob/main/pictures/Bolster.png?raw=true", "https://www.hibolster.com/index.html", 100)
    with col03:
        st.text("")
        photo_link("Eidos", "https://github.com/Willy71/confort/blob/main/pictures/Eidos.png?raw=true", "https://www.eidosglobal.org/", 100)
    with col04:
        st.text("")
        photo_link("Bid Lab", "https://github.com/Willy71/confort/blob/main/pictures/bid%20lab.png?raw=true", "https://bidlab.org/es", 130)
       
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_texto("Redes sociales", 1, 'white')
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
    col51, col52, col53, col54 = st.columns([4,0.5,1,0.5])
    with col51:
        centrar_texto("Website made with Streamlit framework", 2, 'white')   
    with col53:            
        photo_link('', "https://i.postimg.cc/cJhYJnqx/streamlit-logo.jpg", 'https://streamlit.io/', 120)
        
        
with st.container():
    col55, col56, col57, col58 = st.columns([4,0.5,1,0.5])
    with col55:
        st.text("")
        centrar_texto("Programmed with Python for Guillermo Cerato", 2, 'blue')
    with col57:
        photo_link('', "https://i.postimg.cc/9Q3yg2th/python.png", 'https://www.python.org', 120)
        
        

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_texto_link("Link del repositorio de Github de esta presentación", "https://github.com/Willy71/confort/tree/main", 4, 'blue')
            
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)
