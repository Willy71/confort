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

texto('Estimado cliente', 4, 'white')
texto('Agradecemos su interés en desarrollar una nueva funcionalidad para su aplicación Confort con nuestra empresa de desarrollo. Para comprender mejor sus necesidades y expectativas, hemos creado esta encuesta para recopilar información clave. Sus respuestas serán fundamentales para definir la funcionalidad más adecuada para su aplicación y para desarrollar eficientemente nuestro trabajo.', 5, 'white') 
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('1. ¿Qué tipo de nueva funcionalidad le gustaría agregar a su aplicación?', 4, 'white')
texto('A. Opción de "Experiencias": Mapas interactivos con puntos de interés cercanos. Los usuarios pueden', 5, 'lightgrey')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reservar experiencias únicas junto con su alojamiento (tours, clases de cocina, etc.).', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Integración con plataformas de transporte: Integración con sistemas de gestión de transportes', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;locales y/o interurbano (Aereo, terrestre o tren)', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Integración con otras plataformas. Generar un entorno amigable que facilite la integración con', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;otras plataformas (APIs) para gerenciar las reservas y que no se genere overbooking.', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('2. ¿Hay alguna otra funcionalidad que no se haya mencionado y que considere importante', 4, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('3. ¿Por qué considera importante agregar esta nueva funcionalidad?', 4,'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Para mejorar la experiencia del usuario', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Para atraer nuevos clientes', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Para aumentar la fidelidad de los clientes', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D.Para diferenciarse de la competencia', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E. Otras razones (especificar)', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('4. ¿Cómo cree que esta nueva funcionalidad beneficiaría a su negocio?', 4,'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Aumentaría las reservas', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B.Mejoraría la satisfacción del cliente', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Reduciría los costos operativos', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D. Aumentaría el reconocimiento de la marca', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E. Otros beneficios (especificar)', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('5. ¿Qué tipo de información adicional considera que es necesaria para desarrollar esta nueva funcionalidad?', 4, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Datos sobre las preferencias de los usuarios', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Información sobre los alojamientos disponibles', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Documentación de los anfitriones', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D. Otras necesidades de información (especificar)', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('6. ¿Tiene algún ejemplo de otras aplicaciones que ofrecen funcionalidades similares a las que está considerando?', 4, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si. ¿Podria especificar cuales son esas aplicaciones?', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('7. ¿Cómo preferiría recibir actualizaciones sobre el progreso de desarrollo de esta funcionalidad?', 4, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Correo Electrónico', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Reuniones Semanales', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Tablero de Proyecto en Línea', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D. Otras (por favor, especifique)', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)
texto('8. ¿En qué plazo de tiempo le gustaría tener implementada esta nueva funcionalidad?', 4, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Corto plazo (menos de 3 meses)', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Mediano plazo (3-6 meses)', 5, 'white')
texto('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Largo plazo (más de 6 meses)', 5, 'white')
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#15ace6;" /> """, unsafe_allow_html=True)

