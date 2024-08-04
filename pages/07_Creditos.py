import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Creditos",
    page_icon="📪",
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

def left_texto_link(link_texto, link_url, tamanho, color):
    texto_html = f"<h{tamanho} style='text-align: left; color: {color}'><a href='{link_url}' style='text-decoration: none;' target='_blank'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{link_texto}</a></h{tamanho}>"
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

st.write("#")

centrar_texto("Trabajo realizado", 1, 'white')
centrar_texto("por", 1, 'white')
centrar_texto("Guillermo Cerato", 1, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)
centrar_texto("Curso realizado por Silvertech", 2, 'white')
photo_link("Silvertech", "https://github.com/Willy71/confort/blob/main/pictures/Silvertech.png?raw=true", "https://www.soysilvertech.org/comunidad", 200)

st.subheader("")
               
centrar_texto("Socios estratégicos", 4, 'lightblue') 
with st.container():
    col10, col11, col12, col13, col14  = st.columns([4,2,0.1,2,4])
    with col11:
        photo_link("Diagonal", "https://github.com/Willy71/confort/blob/main/pictures/diagonal.png?raw=true", "https://diagonal.org.ar/", 100)
    with col13:
        photo_link("Bolster", "https://github.com/Willy71/confort/blob/main/pictures/Bolster.png?raw=true", "https://www.hibolster.com/index.html", 100)        
st.subheader("")
centrar_texto("Impulsan", 4, 'lightblue')
with st.container():
    col01, col02, col03, col04, col05 = st.columns([4,2,0.1,2,4])
    with col02:
        photo_link("Eidos", "https://github.com/Willy71/confort/blob/main/pictures/Eidos.png?raw=true", "https://www.eidosglobal.org/", 100)
    with col04:
        photo_link("Bid Lab", "https://github.com/Willy71/confort/blob/main/pictures/bid%20lab.png?raw=true", "https://bidlab.org/es", 130)
               
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)
centrar_texto("Mis redes sociales", 2, 'white')
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
centrar_texto_link("Mi portfolio", "https://guillermocerato.streamlit.app", 2, "blue")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)
centrar_texto_link("Link del repositorio de Github de esta presentación", "https://github.com/Willy71/confort/tree/main", 2, 'blue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)

centrar_texto("Herramientas utilizadas.", 1, 'white' )

with st.container():
    col60, col61, col62, col63, col64 = st.columns([3,4,1,4,1.5])
    with col61:
        left_texto_link("Google Docs", "https://docs.google.com/document/u/0/",  3, "white")
        left_texto_link("Jira", "https://www.atlassian.com/software/jira",  3, "white")
        left_texto_link("Figma", "https://www.figma.com/es-la/",  3, "white")
        left_texto_link("Miro", "https://miro.com/app/dashboard/", 3, "white")
        left_texto_link("Visual Sudio Code", "https://code.visualstudio.com/", 3, "white")
    with col63:
        left_texto_link("Github", "https://github.com/", 3, "white")
        left_texto_link("Streamlit", "https://docs.streamlit.io/", 3, "white")   
        left_texto_link("Canva", "https://www.canva.com/", 3, "white")
        left_texto_link("OBS", "https://obsproject.com/", 3, "white")
        left_texto_link("Cap Cut", "https://obsproject.com/", 3, "white") 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#e1e615;" /> """, unsafe_allow_html=True)
centrar_texto('Send an email 💌', 1, 'white')

with st.container():
    co01, co02, co03 = st.columns([2, 4, 2])
    with co02:
        # Taking inputs
        email_sender = 'gcerato@gmail.com'
        email_receiver = 'gcerato@gmail.com'
        email = st.text_input("Email")
        subject = st.text_input('Subject')
        body = st.text_area('Body')
        total = ("Trabajo final de Analista Funcional  \n" + body + "\n" + email)

        if st.button("Send Email"):
            try:
                msg = MIMEText(total)
                msg['From'] = email_sender
                msg['To'] = email_receiver
                msg['Subject'] = subject

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(st.secrets["email"]["gmail"], st.secrets["email"]["password"])
                server.sendmail(email_sender, email_receiver, msg.as_string())
                server.quit()
        
                st.success('Email sent successfully! 🚀')
            except Exception as e:
                st.error(f"Failed to send email: {e}")
               
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

with st.container():
    col01, col02, col03 = st.columns(3)
    with col01:
        if st.button("Anterior", use_container_width=True):
            st.switch_page("pages/06_Video.py")
