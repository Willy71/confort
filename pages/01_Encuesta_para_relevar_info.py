import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Encuesta",
    page_icon="❓",
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


def photo_link_left(alt_text, img_url, link_url, img_width):
    markdown_code = f'''
    <div style="text-align: left;">
        <a href="{link_url}" target="_self"; onclick="window.location.href='{link_url}'; window.history.pushState(null, null, '{link_url}'); return false;">
            <img src="{img_url}" alt="{alt_text}" width="{img_width}px">
        </a>
    </div>
    '''
    st.markdown(markdown_code, unsafe_allow_html=True)

def photo_link_right(alt_text, img_url, link_url, img_width):
    markdown_code = f'''
    <div style="text-align: right;">
        <a href="{link_url}" target="_self"; onclick="window.location.href='{link_url}'; window.history.pushState(null, null, '{link_url}'); return false;">
            <img src="{img_url}" alt="{alt_text}" width="{img_width}px">
        </a>
    </div>
    '''
    st.markdown(markdown_code, unsafe_allow_html=True)

st.write("#")

centrar_texto("Encuesta para Relevamiento de Información", 1, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
centrar_texto("Nueva funcionalidad para app Confort", 2, 'white')  
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto("Introducción:", 2, 'white')
texto('Nuestro cliente tiene una app de reservas de alojamientos temporales tipo AirBnB o Booking. ', 4, 'white') 
texto('Nos fue encomendada la misión de agregar una nueva funcionalidad según los gustos o preferencias de nuestros usuarios.', 4, 'white') 
texto('Con lo cual se le presentó a los usuarios las siguientes tres posibles nuevas funcionalidades para la app de nuestro cliente. ', 4, 'white')  
st.text("")
texto('a. Recomendaciones de eventos, atracciones y/o actividades dentro de la zona de reserva. El mismo puede incluir mapas interactivos y recomendaciones de otros usuarios.', 5, 'lightblue')
texto('b. Chat en Tiempo Real: Entre anfitriones y huéspedes.', 5, 'lightblue')
texto('c. Integración con Servicios de Transporte: Para facilitar el traslado desde y hacia el alojamiento.', 5, 'lightblue')
st.text("")
texto('La funcionalidad elegida, fue la “a”, para recomendaciones de eventos y/o actividades en la zona de la reserva de alojamiento temporario. Esta nueva funcionalidad será denominada “Experiencias” y se podrá acceder a través de mapas interactivos, por filtros de categorías, por recomendaciones de usuario y por sugerencias de un algoritmo en base a las preferencias que el usuario haya elegido previamente.', 4, 'white') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('Luego de realizar una versión beta de la nueva funcionalidad, se encuesto a algunos usuarios de la app con las siguientes preguntas: ', 4, 'white') 
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('1. Cual es el motivo principal de uso de la app?', 4, 'white') 
texto('a. Turismo', 5, 'lightblue')
texto('b. Viajes de Negocios', 5, 'lightblue')
texto('c. Convenciones', 5, 'lightblue')
texto('d. Otro (por favor, especifique)', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('2. ¿La pantalla de ingreso a esta nueva funcionalidad le resultó intuitiva y fácil de usar?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')
texto('c .Comentarios:', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('3. ¿Pudo encontrar fácilmente los puntos de interés cercanos a su alojamiento en el mapa interactivo?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')
texto('c. Comentarios:', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('4. ¿Utilizó los filtros de categorías para encontrar puntos de interés específicos?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')
texto('c. Comentarios:', 5, 'lightblue')


st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('5. ¿Le resultó útil la opción de reservar experiencias (tours, clases de cocina, etc.) directamente desde la app?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')
texto('c. Comentarios:', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('6. ¿Qué tan satisfecho está con la integración del mapa interactivo y las experiencias en la app?', 4, 'white') 
texto('a. Muy Satisfecho', 5, 'lightblue')
texto('b. Satisfecho', 5, 'lightblue')
texto('c. Neutral', 5, 'lightblue')
texto('d. Insatisfecho', 5, 'lightblue')
texto('e. Muy Insatisfecho', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('7. ¿Recibió notificaciones claras y útiles sobre las reservas de experiencias?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')
texto('c. Comentarios:', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('8. ¿Qué funcionalidades adicionales le gustaría ver en la sección de experiencias y mapas interactivos?', 4, 'white') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('9. ¿Hay algo que le haya resultado difícil o confuso al usar esta nueva funcionalidad? ', 4, 'white') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('10. ¿Recomendaría esta nueva funcionalidad a otros usuarios?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')
texto('c. Comentarios:', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('11. Edad:', 4, 'white') 
texto('a. de 18 a 25 años', 5, 'lightblue')
texto('b. de 26 a 35 años', 5, 'lightblue')
texto('c. de 36 a 45 años', 5, 'lightblue')
texto('d. de 46 a 55 años', 5, 'lightblue')
texto('e. de 56 a 65 años', 5, 'lightblue')
texto('f. Mayor de 65 años', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)


#st.markdown('<a href="https://confort.streamlit.app/Backlog" target="_self">Next page</a>', unsafe_allow_html=True)
               
with st.container():
    col01, col02, col03 = st.columns(3)
    with col01:
        if st.button("Anterior", use_container_width=True):
            st.switch_page("Home.py")
    with col03:
        if st.button("Siguiente", use_container_width=True):
            st.switch_page("pages/02_Backlog.py")





