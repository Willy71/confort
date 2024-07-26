import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Encuesta",
    page_icon="❔",
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
texto('Con lo cual se le presentó a los usuarios el siguiente cuestionario. ', 4, 'white')  
st.text("")
texto("Encuesta:", 2, 'white')
texto('Estimado usuario, nos encantaría conocer tu opinión sobre posibles nuevas funcionalidades que podríamos agregar a nuestra aplicación para mejorar tu experiencia. Por favor, tómate unos minutos para responder las siguientes preguntas. ¡Gracias por tu colaboración!', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('1. ¿Qué tan satisfecho estás con las funcionalidades actuales de nuestra app?', 4, 'white') 
texto('a. Muy satisfecho.', 5, 'lightblue')
texto('b. Satisfecho', 5, 'lightblue')
texto('c. Neutral', 5, 'lightblue')
texto('d. Insatisfecho', 5, 'lightblue')
texto('f. Muy insatisfecho', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('2. ¿Qué tipo de usuario es usted?', 4, 'white') 
texto('a. Turista', 5, 'lightblue')
texto('b. Viajero de negocios', 5, 'lightblue')
texto('c. Participante en convenciones', 5, 'lightblue')
texto('d. Otro', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('3. ¿Qué nueva funcionalidad te gustaría ver en nuestra aplicación?', 4, 'white') 
texto('a. Sistema de Recomendación Personalizado: Basado en las preferencias y comportamientos del usuario.', 5, 'lightblue')
texto('b. Chat en Tiempo Real: Entre anfitriones y huéspedes.', 5, 'lightblue')
texto('c. Integración con Servicios de Transporte: Para facilitar el traslado desde y hacia el alojamiento.', 5, 'lightblue')
texto('d. Mapas Interactivos: Que muestren puntos de interés cercanos al alojamiento.', 5, 'lightblue')
texto('f. Sistema de Revisión y Calificación Mejorado: Con más detalles y filtros.', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('4.  En cuanto a la funcionalidad "Sistema de Recomendación Personalizado", ¿qué aspectos te gustaría que se consideren para las recomendaciones? ', 4, 'white') 
texto('a. Historial de reservas', 5, 'lightblue')
texto('b. Preferencias declaradas', 5, 'lightblue')
texto('c. Recomendaciones de otros usuarios similares', 5, 'lightblue')
texto('d. Opiniones y reseñas de experiencias anteriores', 5, 'lightblue')
texto('f. Otro', 5, 'lightblue')


st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('5. Si se implementara un "Chat en Tiempo Real" entre anfitriones y huéspedes, ¿con qué frecuencia crees que lo usarías?', 4, 'white') 
texto('a. Muy frecuentemente', 5, 'lightblue')
texto('b. Frecuentemente', 5, 'lightblue')
texto('c. Ocasionalmente', 5, 'lightblue')
texto('d. Raramente', 5, 'lightblue')
texto('f. Nunca', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('6. En caso de integrar "Servicios de Transporte" en la app, ¿qué tipo de servicios te gustaría que se incluyeran?', 4, 'white') 
texto('a. Taxis', 5, 'lightblue')
texto('b. Uber, Lyft, Cabify, Google Drive, etc', 5, 'lightblue')
texto('c. Alquiler de coches', 5, 'lightblue')
texto('d. Transporte público', 5, 'lightblue')
texto('f. Otro', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('7. Si la funcionalidad de "Mapas Interactivos" se implementara, ¿qué tipo de puntos de interés te gustaría ver?', 4, 'white') 
texto('a. Restaurantes', 5, 'lightblue')
texto('b. Museos', 5, 'lightblue')
texto('c. Tiendas', 5, 'lightblue')
texto('d. Parques y atracciones naturales', 5, 'lightblue')
texto('f. Otro', 5, 'lightblue')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('8. ¿Qué características consideras más importantes en un "Sistema de Revisión y Calificación Mejorado"? ', 4, 'white') 
texto('a. Detalles específicos sobre la experiencia', 5, 'lightblue')
texto('b. Filtros para buscar reseñas por tipo de usuario', 5, 'lightblue')
texto('c. Fotos y videos adjuntos a las reseñas', 5, 'lightblue')
texto('d. Respuestas de los anfitriones a las reseñas', 5, 'lightblue')
texto('f. Otro', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('9. ¿Cómo prefieres que se te notifique sobre nuevas funcionalidades y actualizaciones en la app?', 4, 'white') 
texto('a. Notificaciones push en la app', 5, 'lightblue')
texto('b. Correo electrónico', 5, 'lightblue')
texto('c. Mensajes de texto', 5, 'lightblue')
texto('d. Whatsapp', 5, 'lightblue')
texto('f. Otro', 5, 'lightblue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('10. ¿Hay alguna otra funcionalidad que te gustaría ver en nuestra aplicación que no hayamos mencionado?', 4, 'white') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('11. ¿Te gustaría participar en pruebas beta de nuevas funcionalidades?', 4, 'white') 
texto('a. Si', 5, 'lightblue')
texto('b. No', 5, 'lightblue')


st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('12. ¿Tienes algún comentario adicional o sugerencia para mejorar nuestra app?', 4, 'white') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('¡Gracias por tu tiempo y tus valiosas opiniones! Tus respuestas nos ayudarán a mejorar nuestra app para brindarte una mejor experiencia.', 4, 'white')

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





