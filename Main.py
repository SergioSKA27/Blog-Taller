from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from streamlit_lottie import st_lottie
from st_xatadb_connection import XataConnection
import asyncio
import requests
import base64
import random


#Configuraciones de la pagina
st.set_page_config(layout="wide",page_title='Mi portafolio',
page_icon='https://www.alexgrey.com/img/containers/art_images/Psychedelic-Healing---2020-Alex-Grey-smaller-watermarked.jpg/173f3855733a06912abc4e11ecd04c48.jpg')

xata = st.connection('xata',type=XataConnection)


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

#------------------------------------------------------------------------------------------------
#Funciones
async def get_random_image(query='random'):
    try:
        result = await asyncio.to_thread(requests.get, f'https://source.unsplash.com/random/600x400?{query}',timeout=.5)
        return base64.b64encode(result.content).decode('utf-8')
    except Exception as e:
        return f"https://source.unsplash.com/random/600x400?{query}"

def insert_message(name,motive,email,message):
    try:
        xata.insert("Mensaje", {
    "emisor": name,
    "correo": email,
    "motivo": motive,
    "contenido": message
    })
        st.success('Mensaje enviado con éxito!')
        st.toast('Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.',icon='🤗')
    except Exception as e:
        st.error('Ocurrió un error al enviar el mensaje. Por favor, inténtalo de nuevo más tarde.')
        st.exception(e)


def update_articles():
    st.session_state.articles = xata.query('Articulo')

def set_article(article):
    st.session_state.article = article

def render_article_prev(article):
    with st.container(border=True,height=500):
        if 'banner' in article and 'url' in article['banner']:
            da1 = f'<img src="{article["banner"]["url"]}" alt="article" width="300" height="200">'
        else:
            with st.spinner('Cargando...'):
                img1 = asyncio.run(get_random_image('data-science'))
            if 'https' in img1:
                da1 = f'<img src="{img1}" alt="article" width="300" height="200">'
            else:
                da1 = f'<img src="data:image/png;base64,{img1}" alt="article" width="300" height="200">'


        st.markdown(f'''
        <div class="aboutc">
        {da1}
        </div>
        ''', unsafe_allow_html=True)
        ctags = list(map(lambda x: f':blue[{x}]' if random.choice([True,False]) else f':rainbow[{x}]',article['tags']))
        st.write(f'## {article["titulo"]}')
        st.write(', '.join(ctags))
        st.button('Leer',key=article['id'],use_container_width=True,on_click=set_article,args=(article,))


def read_article(article):
    if st.button('Regresar',use_container_width=True):
        st.session_state.article = None
        st.rerun()
    st.markdown(f'# {article["titulo"]}')
    st.caption(f'Publicado el {article["xata"]["createdAt"][:10]}')
    ctags = list(map(lambda x: f':blue[{x}]' if random.choice([True,False]) else f':rainbow[{x}]',article['tags']))
    st.write(', '.join(ctags))
    st.divider()
    st.write(article['contenido'],unsafe_allow_html=True)


def main():
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
    en diversos sectores.En mi tiempo libre, disfruto sumergirme en una variedad de actividades que alimentan mi curiosidad y mi deseo de aprender.
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div class="about">
    <h1>Sobre Mi</h1>
    <hr>
    </div>
    ''', unsafe_allow_html=True)


    ab1, ab2, ab3 = st.columns([0.3, 0.3, 0.3])

    with ab1.container(border=True,height=600):
        plh1 = st.empty()
        with st.spinner('Cargando...'):
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


    with ab2.container(border=True,height=600):
        plh2 = st.empty()
        with st.spinner('Cargando...'):
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


    with ab3.container(border=True,height=600):
        plh3 = st.empty()
        with st.spinner('Cargando...'):
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

    st_lottie('https://lottie.host/bed34c9d-f065-42bd-8747-4b37cc12b007/PifHQomLzh.json',loop=False,height=200)

def contact():
    st.markdown('''
    <h1 style="text-align: center";>Contactame
    </h1>
    ''', unsafe_allow_html=True)

    _,fcol,_ = st.columns([0.2, 0.6, 0.2])
    with fcol.form(key='contact_form'):
        name = st.text_input('Tu nombre*')
        motive = st.text_input('Motivo de contacto*')
        email = st.text_input('Email*')
        message = st.text_area('Mensaje')
        if st.form_submit_button('Enviar',use_container_width=True):
            if name == '' or motive == '' or email == '':
                st.warning('Por favor, llena todos los campos marcados con *',icon='⚠️')
            else:
                if message == '':
                    message = 'Sin mensaje'
                insert_message(name,motive,email,message)


def render_project(project):
    with st.container(border=True):
        c1,c2 = st.columns([0.7, 0.3])

        with c1:
            if project['embed']:
                with st.expander('Descripción'):
                    st.write(project['descripcion'],unsafe_allow_html=True)

        st.markdown(f'''
        <iframe src="{project['url']}" width="100%" height="400" frameborder="0" scrolling="yes"></iframe>
        ''',unsafe_allow_html=True)

        with c2:
            st.subheader(project['titulo'])
            st.link_button('Ver proyecto',project['url'],use_container_width=True)

def projects():
    pc1, pc2 = st.columns([0.6, 0.4])
    with pc1:
        st.markdown('''
        <div class="projects">
        <h1>Mis Proyectos</h1>
        <p> En esta sección, puedes encontrar algunos de mis proyectos más recientes. Estos proyectos abarcan una
        variedad de temas, incluyendo la ciencia de datos, el desarrollo de software, y el análisis de negocios.
        Espero que encuentres estos proyectos interesantes y útiles.
        </p>
        ''', unsafe_allow_html=True)

    with pc2:
        st_lottie('https://lottie.host/bb7b964f-b151-48d4-902c-f8ff5e1ea037/H2O7NOxRVS.json',loop=True,height=400)

    st.divider()

    #st.write(st.session_state.projects)

    for i in st.session_state.projects['records']:
        render_project(i)

def blog():
    bcol1 , bcol2 = st.columns([0.6, 0.4])

    with bcol1:
        st.markdown('''
        <div class="blog">
            <h1>
            Mi Blog Personal
            </h1>
            <p>
            En mi blog personal, comparto mis pensamientos y experiencias sobre una variedad de temas, incluyendo la
            ciencia de datos, el desarrollo de software, y el análisis de negocios. Me encanta compartir lo que he
            aprendido y las lecciones que he aprendido en el camino, y espero que encuentres mi blog interesante y útil.
            </p>
        </div>
        ''', unsafe_allow_html=True)


    with bcol2:
        st_lottie('https://lottie.host/cb5f87f1-36d5-467e-8de7-fcaa27a79c58/Klr9IfoJsE.json',loop=True,height=400)

    st.markdown('''
    ---

    <div class="blog">
    <h2>Publicaciones Recientes</h2>
    <p> Aquí hay algunas de mis publicaciones más recientes en mi blog personal:</p>
    </div>
    ''', unsafe_allow_html=True)

    _,ref = st.columns([0.9, 0.1])
    ref.button('Actualizar',on_click=update_articles,use_container_width=True)

    cols = st.columns(3)
    k = 0
    for i in st.session_state.articles['records']:
        with cols[k]:
            render_article_prev(i)
        k += 1
        if k == 3:
            k = 0


if 'articles' not in st.session_state:
    st.session_state.articles = xata.query('Articulo')

if 'marticles' not in st.session_state:
    st.session_state.marticles = []

if 'projects' not in st.session_state:
    st.session_state.projects = xata.query('Proyecto')


if 'article' not in st.session_state:
    st.session_state.article = None


#------------------------------------------------------------------------------------------------
#Titulo de la pagina
#st.title('Mi primer portafolio con Streamlit')
#st.divider()

#------------------------------------------------------------------------------------------------
#Estilos de la barra lateral
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Inicio', 'Blog','Proyectos', 'Contacto'],
                        iconName=['dashboard', 'newspaper','verified', 'contact_page'],
                        styles = {'navtab': {'background-color':'#1d3557',
                                              'color': '#457b9d',
                                              'font-size': '18px',
                                              'transition': '.3s',
                                              'white-space': 'nowrap',
                                              'text-transform': 'capitalize'},
                                   'tabOptionsStyle': {':hover :hover': {'color': '#F63366',
                                                                  'cursor': 'pointer'}},
                                   'iconStyle':{'position':'fixed',
                                                'left':'7.5px',
                                                'text-align': 'left'},
                                   'tabStyle' : {'list-style-type': 'none',
                                                 'margin-bottom': '30px',
                                                 'padding-left': '30px'}},
                        key="1",default_choice=0)

#------------------------------------------------------------------------------------------------
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
.blog {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 2.5rem;
    align-items: center;
    text-align: justify;
}
.blog h1 {
    text-align: center;
    font-size: 10vh;
    font-weight: bold;
    color: #1d3557;
    font-family: 'Lobster', cursive;
    }
.blog h2 {
    font-size: 30px;
    font-weight: bold;
    color: #1d3557;
    font-family: 'Lobster', cursive;
    margin-top: 0rem; !important;
    }
.blog p {
    font-family: 'Lobster', cursive;
    font-size: 20px;
    font-weight: bold;
    }
.projects {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 2.5rem;
    align-items: center;
    text-align: justify;
}
.projects h1 {
    font-size: 13vh;
    font-weight: bold;
    color: #1d3557;
    }
.projects p {
    font-family: 'Lobster', cursive;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    }
</style>
''', unsafe_allow_html=True)


#------------------------------------------------------------------------------------------------
#Main
if tabs == 'Inicio':
    main()



if tabs == 'Contacto':
    contact()


if tabs == 'Blog':
    if st.session_state.article is not None:
        read_article(st.session_state.article)
    else:
        blog()
        _,rini , nxt = st.columns([0.7,0.2,0.1])
        if rini.button('Regresar al inicio',use_container_width=True):
            update_articles()
            st.rerun()
        if nxt.button('Mostrar más'):
            st.session_state.articles = xata.next_page('Articulo',st.session_state.articles)
            st.rerun()


if tabs == 'Proyectos':
    projects()

