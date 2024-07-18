import streamlit as st

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Backlog",
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

centrar_texto("Épica: Experiencias y Mapas Interactivos", 1, 'white')
centrar_texto_link('Link del backlog en Jira', 'https://tradingmcz.atlassian.net/jira/software/projects/CSLEEM/boards/2/backlog?atlOrigin=eyJpIjoiZTc1ZmQzM2FhN2RhNGJiNjk3ZTM4MWIwMjliMGIyN2MiLCJwIjoiaiJ9', 4, 'blue')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
centrar_texto("Sprint 1", 3, 'white')
centrar_texto("Fecha de inicio: 09/08/2024", 6, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 1 - Personalización de Mapas Interactivos', 4, 'yellow')
texto('Descripción: Como usuario, quiero poder personalizar los mapas interactivos con mis propios puntos de interés, para adaptar el mapa a mis necesidades. ', 5, 'white')
texto('Criterios de Aceptación:', 5, 'white')
with st.container():    
    col01, col02 = st.columns([1.4,5]) 
    with col02:
        texto('- Los usuarios deben poder añadir sus propios puntos de interés al mapa.', 5, 'white') 
        texto('- Debe haber una opción para guardar y editar estos puntos de interés.', 5, 'white')    
texto('Prioridad: 3', 5, 'white')  
texto('Fecha estimada de entrega: 23/08/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 2 - Filtro de Puntos de Interés ', 4, 'yellow')
texto('Descripción: Como usuario, quiero filtrar los puntos de interés en el mapa por categorías, para encontrar rápidamente lo que me interesa.', 5, 'white')
texto('Criterios de Aceptación:', 5, 'white')
centrar_texto('- Debe haber opciones de filtro por categorías (ej. restaurantes, museos, tiendas).', 5, 'white')
centrar_texto('- Al seleccionar una categoría, el mapa debe actualizarse para mostrar solo los puntos de interés correspondientes.', 5, 'white')
texto('Prioridad: 3 ', 5, 'white')  
texto('Fecha estimada de entrega: 23/08/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 3 - Integración con el Sistema de Reservas', 4, 'yellow')
texto('Descripción: Como usuario, quiero poder reservar experiencias únicas desde la misma plataforma donde reservé mi alojamiento. ', 5, 'white')
texto('Criterios de Aceptación:', 5, 'white')
centrar_texto('- Los usuarios deben poder seleccionar y reservar experiencias desde la página del alojamiento.', 5, 'white')
centrar_texto('- La reserva de la experiencia debe estar vinculada a la reserva del alojamiento.', 5, 'white')
centrar_texto('- Debe haber confirmación y detalles de la reserva de la experiencia.', 5, 'white')
texto('Prioridad: 5 ', 5, 'white')  
texto('Fecha estimada de entrega: 23/08/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 4 - Sección de Opiniones de Experiencias', 4, 'yellow')
texto('Descripción: Como usuario, quiero leer opiniones de otras personas sobre las experiencias disponibles, para tomar una decisión informada.', 5, 'white')
texto('Criterios de Aceptación:', 5, 'white')
centrar_texto('- Debe haber una sección de opiniones en la página de cada experiencia.', 5, 'white')
centrar_texto('- Los usuarios deben poder calificar y escribir reseñas de las experiencias.', 5, 'white')
centrar_texto('- Las opiniones deben ser visibles para todos los usuarios.', 5, 'white')
texto('Prioridad: 2 ', 5, 'white')  
texto('Fecha estimada de entrega: 23/08/2024', 5, 'white')
  
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 5 - Notificaciones de Reservas de Experiencias', 4, 'yellow')
texto('Descripción: Como usuario, quiero recibir notificaciones cuando se confirma una reserva de una experiencia, para estar informado.', 5, 'white')
texto('Criterios de Aceptación:', 5, 'white')
centrar_texto('- Los usuarios deben recibir notificaciones por email y en la app cuando una reserva de experiencia se confirme.', 5, 'white')
centrar_texto('- Las notificaciones deben incluir detalles de la reserva.', 5, 'white')
texto('Prioridad: 1', 5, 'white')  
texto('Fecha estimada de entrega: 23/08/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
centrar_texto("Sprint 1", 3, 'white')
centrar_texto("Fecha de inicio: 23/08/2024", 6, 'white')

#texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 6 - Implementación de Mapas Interactivos', 4, 'yellow')
texto('Descripción: Como usuario, quiero ver mapas interactivos que muestran puntos de interés cercanos a mi alojamiento, para planificar mejor mi viaje.', 5, 'white')
texto('Criterios de Aceptación:', 5, 'white')
centrar_texto('- El mapa interactivo debe estar disponible en la página de detalles del alojamiento.', 5, 'white')
centrar_texto('- El mapa debe mostrar puntos de interés como restaurantes, museos, tiendas, etc.', 5, 'white')
centrar_texto('- Los puntos de interés deben ser clicables y mostrar información adicional.', 5, 'white')
texto('Prioridad: 3 ', 5, 'white')  
texto('Fecha estimada de entrega: 06/09/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 7 - Experiencias Recomendadas Basadas en Preferencias ', 4, 'yellow')
texto('Descripción: Como usuario, quiero recibir recomendaciones de experiencias basadas en mis preferencias', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y comportamientos previos, para encontrar experiencias que me interesen.', 5, 'white')  
texto('Criterios de Aceptación:', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- El sistema debe recomendar experiencias basadas en el historial de reservas y', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferencias del usuario.', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Las recomendaciones deben ser visibles en la página principal de la app.', 5, 'white')
texto('Prioridad: 5', 5, 'white')  
texto('Fecha estimada de entrega: 06/09/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 8 - Integración de Calendario de Experiencias', 4, 'yellow')
texto('Descripción: Como usuario, quiero ver un calendario de todas las experiencias disponibles durante', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mi estancia, para planificar mis actividades.', 5, 'white') 
texto('Criterios de Aceptación:', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Debe haber un calendario en la página de detalles del alojamiento que muestre las experiencias', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; disponibles.', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Los usuarios deben poder filtrar las experiencias por fecha.', 5, 'white')
texto('Prioridad: 2 ', 5, 'white')  
texto('Fecha estimada de entrega: 06/09/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 9 - Evaluación de Preferencias de Usuario', 4, 'yellow')
texto('Descripción: Como administrador, quiero relevar datos sobre las preferencias de los usuarios para mejorar', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; las recomendaciones de experiencias.', 5, 'white') 
texto('Criterios de Aceptación:', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Debe haber un formulario de evaluación de preferencias que los usuarios puedan completar.', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Los datos recopilados deben ser almacenados y utilizados para mejorar las recomendaciones.', 5, 'white')
texto('Prioridad: 3', 5, 'white')  
texto('Fecha estimada de entrega: 06/09/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
texto('Historia 10 - Feedback y Participación del Cliente', 4, 'yellow')
texto('Descripción: Como administrador, quiero recibir feedback continuo del cliente durante el desarrollo', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;de la nueva funcionalidad, para asegurar que cumple con sus expectativas.', 5, 'white') 
texto('Criterios de Aceptación:', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Debe haber reuniones periódicas con el cliente para revisar el progreso y recibir feedback.', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Las sugerencias del cliente deben ser documentadas y consideradas en el desarrollo.', 5, 'white')
texto('Prioridad: 3', 5, 'white')  
texto('Fecha estimada de entrega: 06/09/2024', 5, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#3ebc32;" /> """, unsafe_allow_html=True)
