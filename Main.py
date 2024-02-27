from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import asyncio
import requests
import base64
st.set_page_config(layout="wide")



#Funciones
async def get_random_image(query='random'):
    try:
        result = await asyncio.to_thread(requests.get, f'https://source.unsplash.com/random/600x400?{query}',timeout=1)
        return base64.b64encode(result.content).decode('utf-8')
    except Exception as e:
        return f"https://source.unsplash.com/random/600x400?{query}"




#Cuerpo de la pagina principal
st.title('Mi primer portafolio con Streamlit')
st.divider()
st.markdown('''
<style>
#MainMenu, header {visibility: hidden;}
.appview-container .main .block-container
{
    padding-top: 0px;
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 5rem;
}
</style>
''', unsafe_allow_html=True)
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
        tabs = on_hover_tabs(tabName=['Inicio', 'Blog', 'Economy'],
                             iconName=['dashboard', 'article', 'economy'],
                             styles = {'navtab': {'background-color':'#1d3557',
                                                  'color': '#457b9d',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'capitalize'},
                                       'tabOptionsStyle': {':hover :hover': {'color': '#e63946',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")


#Estilos de la pagina principal
st.markdown('''
<style>
.fotop {
    display: block;
    margin-left: 2.5rem;
    margin-right: auto;
}
.fotop img {
    border-radius: 50%;
    width: 300px;
    height: 300px;
}
.presentation {
    display: flex;
    font-family: 'Lobster', cursive;
    font-size: 20px;
    font-weight: bold;
    justify-content: center;
    margin: 2.5rem;
    align-items: center;
    text-align: justify;

}
.about {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 2.5rem;
    align-items: center;
    text-align: justify;
}
.about h1 {
    font-size: 30px;
    font-weight: bold;
    color: #1d3557;
}
.about hr {
    width: 100%;
    border: 1px solid #1d3557;
    margin-top: 0px;
    margin-bottom: 0px;
}
.aboutc {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 1rem;
    align-items: center;
    text-align: justify;
}
.aboutc img {
    border-radius: 10px;
    margin-top: 0rem;
    margin-bottom: 1rem;
}
.aboutc p {
    font-size: 15px;
    font-weight: bold;
    }
.aboutc h3 {
    font-size: 25px;
    font-weight: bold;
    text-align: center;
    }
</style>
''', unsafe_allow_html=True)

mc1, mc2 = st.columns([0.3, 0.7])
mc1.markdown('''
<div class="fotop">
<img src="https://scontent.fmex1-5.fna.fbcdn.net/v/t39.30808-6/274720958_4910776422332711_3703056979704527277_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=9c7eae&_nc_eui2=AeFe0fRN05jNzGFbOAxsEo8IvL_oD5rnjDW8v-gPmueMNZreUO9dCIFS2o1pQcy7HvE-Zjy2u3YxZYwK_jX6Jd_n&_nc_ohc=ux-LkuNDkfcAX_Ams12&_nc_ht=scontent.fmex1-5.fna&oh=00_AfC4IKIyrIF9uhGPca_5MdkQ2zNDCV9udrSA769QA4Tw-g&oe=65E33710">
</div>
''', unsafe_allow_html=True)

mc2.markdown('''
<div class="presentation">
¡Hola!
Soy Sergio, estudiante apasionado de Matemáticas Aplicadas y Computación, con un enfoque en Machine Learning y Ciencia de Datos. Mi objetivo es transformar datos en soluciones innovadoras con impacto real
en diversos sectores.
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="about">
<h1>Sobre Mi</h1>
<hr>
</div>
''', unsafe_allow_html=True)


ab1, ab2, ab3 = st.columns([0.3, 0.3, 0.3])

with ab1.container(border=True,height=550):
    plh1 = st.empty()
    img1 = asyncio.run(get_random_image('data-science'))
    if 'https' in img1:
        da1 = f'<img src="{img1}" alt="data-science" width="300" height="200">'
    else:
        da1 = f'<img src="data:image/png;base64,{img1}" alt="data-science" width="300" height="200">'
    plh1.markdown(f'''
    <div class="aboutc">
        <h3>Enfoque en la Ciencia de Datos y Machine Learning</h3>
        {da1}
        <p>
        Soy un apasionado de la Ciencia de Datos y el Machine Learning, y mi carrera se ha centrado en explorar las
        posibilidades que estos campos ofrecen. Mi objetivo es aprovechar el poder de los datos para generar soluciones
        creativas y prácticas que tengan un impacto significativo en diversos sectores.
        </p>
    </div>
    ''', unsafe_allow_html=True)


with ab2.container(border=True,height=550):
    plh2 = st.empty()
    img2 = asyncio.run(get_random_image('web-development'))
    if 'https' in img2:
        da2 = f'<img src="{img2}" alt="web-development" width="300" height="200">'
    else:
        da2 = f'<img src="data:image/png;base64,{img2}" alt="web-development" width="300" height="200">'
    plh2.markdown(f'''
    <div class="aboutc">
        <h3>Experiencia en Desarrollo de Software</h3>
        {da2}
        <p>
        Tengo experiencia en el desarrollo de software, y he trabajado en proyectos de desarrollo web y móvil. Me encanta
        aprender nuevas tecnologías y explorar las posibilidades que ofrecen para crear soluciones innovadoras.
        </p>
    </div>
    ''', unsafe_allow_html=True)


with ab3.container(border=True,height=550):
    plh3 = st.empty()
    img3 = asyncio.run(get_random_image('business'))
    if 'https' in img3:
        da3 = f'<img src="{img3}" alt="business" width="300" height="200">'
    else:
        da3 = f'<img src="data:image/png;base64,{img3}" alt="business" width="300" height="200">'
    plh3.markdown(f'''
    <div class="aboutc">
        <h3>Interés en el Análisis de Negocios</h3>
        {da3}
        <p>
        Me interesa el análisis de negocios y la toma de decisiones basada en datos. Creo que el análisis de datos puede
        proporcionar información valiosa que puede ayudar a las empresas a tomar decisiones más informadas y eficaces.
        </p>
    </div>
    ''', unsafe_allow_html=True)