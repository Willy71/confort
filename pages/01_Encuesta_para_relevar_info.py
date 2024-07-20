import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Encuesta",
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

centrar_texto("Encuesta para Relevamiento de Información", 1, 'white')
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
st.subheader("")
texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

texto('', 4, 'white') 
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')
texto('', 5, 'lightgrey')


