import streamlit as st
from streamlit_gtag import st_gtag
#import streamlit.components.v1 as components

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Silvertech - Trabajo final",
    page_icon="🍀",
    layout="wide"
)

###########################################################################################################

st_gtag(
    key="gtag_send_event_a",
    id="G-ZY2745B9DJ",
    event_name="app_main_page",
    params={
        "event_category": "test_category_a",
        "event_label": "test_label_a",
        "value": 97,
    },
)

if st.button("Send Event A"):
    st_gtag(
        key="gtag_send_event_b",
        id="G-ZY2745B9DJ",
        event_name="send_event_button",
        params={
            "event_category": "test_category_b",
            "event_label": "test_label_b",
            "value": 97,
        },
    )


#st.markdown(
#    """
#        <!-- Global site tag (gtag.js) - Google Analytics -->
#        <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZY2745B9DJ"></script>
#        <script>
#            window.dataLayer = window.dataLayer || [];
#            function gtag(){dataLayer.push(arguments);}
#            gtag('js', new Date());
#            gtag('config', 'G-ZY2745B9DJ');
#        </script>
#    """, unsafe_allow_html=True)

# Include Google Analytics tracking code
#with open("google_analytics.html", "r") as f:
#    html_code = f.read()
#    components.html(html_code, height=0)
###########################################################################################################

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

st.write("#")

centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/titular3.png?raw=true", 450)

centrar_imagen("https://github.com/Willy71/confort/blob/main/pictures/001.png?raw=true", 300)
#https://github.com/Willy71/confort/blob/main/pictures/confort_remove.png?raw=true

with st.container():
    col01, col02, col03 = st.columns(3)
    with col03:
        if st.button("Siguiente", use_container_width=True):
            st.switch_page("pages/01_Encuesta_para_relevar_info.py")



