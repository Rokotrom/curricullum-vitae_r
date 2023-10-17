from pathlib import Path 

import streamlit as st 
from PIL import Image 
import time
import html
import glob
# import scipy.motion as motion

from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from streamlit_javascript import st_javascript
from streamlit.components.v1 import html

# @st.cache_data

# ---Path Settings ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ---General Settings ---

PAGE_TITLE = "Digital CV | Ronny Fernández Rodriguez"
PAGE_ICON = "random"
NAME = "Ronny Fernández Rodriguez"
DESCRIPTION = """
O sorriso é meu, mas o motivo é ter minha família saudável e juntos o que quer que aconteça
"""
EMAIL = "ronny850214@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Resumen Digital | CV")

# --- LOAD CSS, PDF & PROFIL PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---- SIDE BAR ---- # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
                     # https://icons.getbootstrap.com/

with st.sidebar:

    #    with st.echo():
        st.header("***Perfil***", divider='rainbow')
    #    st.write("---")
        st.write(
                """
                :label: Otimismo diante das dificuldades

                :label: Ansiosa para aprender

                :label: Curiosa
                
                :label: Receptiva 
                """)

        st.write("---")
        st.header("***Contato***")

        col1, col2 = st.columns((1, 3), gap="small")
        with col1:
            st.button(":phone:", disabled=True)
            st.button(":world_map:", disabled=True)
            st.button(":mailbox:", disabled=True)

        with col2:
            st.write("", "(11) 951965540")
            st.write("Rua Pedro Alexandre, 58 - Jovaia, Guarulhos.")
            st.write("", EMAIL)

        st.write("---")
        st.header("***EDUCAÇÃO***")
        st.write(
                """
                :mortar_board: Técnico de Beleza | Autodidata 2020 - 2023

                :mortar_board: Arquivo de gerenciamento | SERVIGEN 2011 - 2019

                :mortar_board: Instituto Politécnico de Alimentos | "Exército Rebelde" 2000 - 2004
                """)


        st.write("---")
        st.header("***IDIOMAS***")
        st.slider("Espanhol", value=100, disabled=True)
        st.slider("Português", value=29, disabled=True)
        st.slider("Inglês", value=15, disabled=True)

# --- HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
    )
    st.write("", EMAIL)

# --- SOCIAL LINKS ---
#
# st.write("#")
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")
#
# --- NAVIGATION MENU ---

st.write("#")

selected = option_menu(
    menu_title=None,
    options=["Português", "Espanhol", "Gallery"],
    icons=["yin-yang", "fingerprint", "play-btn"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)


# --- Experience & Qualifications ---
if selected == "Português":
    st.write("#")
    st.header("***EXPERIÊNCIA DE TRABALHO***")
    st.write("#")
    st.subheader("Salões de Beleza | Manicure")
    st.write(
            """
            ***2020 - Presente*** 
    
            Beauty Technique, especializada em manicure e pedicure, depilação de sobrancelhas
            """)
    
    st.write("#")
    st.subheader("Empresa de Serviços Gerais | BIOCUBAFARMA")
    st.write(
            """
            ***2011 - 2020***
    
            Assistente de Direção
    
            Secretária de Gravação
    
            Secretário dos Conselhos de Administração e Órgãos Auxiliares
    
            Planos de Trabalho Executivos
            """)
    
    st.write("#")
    st.subheader("CNCA | AZCUBA")
    st.write(
            """
            ***2008 - 2011***
    
            Protocolo Gastronomia
            """)
    
    

if selected == "Espanhol":
    st.write("#")
    st.header("***EXPERIENCIA DE TRABAJO***")
    st.write("#")
    st.subheader("Salones de Belleza | Manicure")
    st.write(
            """
            ***2020 - Presente***
    
            Técnica de Belleza, especializada en manicure y pedicure, depilación de cejas con cera
            """)
    
    st.write("#")
    st.subheader("Empresa de Servicios Generales | BIOCUBAFARMA")
    st.write(
            """
            ***2011 - 2020***
    
            Assistente de Dirección 
    
            Secretária de Actas
    
            Secretaria de Consejos de dirección y Organos Auxiliares
    
            Planes de Trabajo de directivos
            """)
    
    st.write("#")
    st.subheader("CNCA | AZCUBA")
    st.write(
            """
            ***2008 - 2011***
    
            Protocolo Gastronomia
            """)
    
if selected == "Gallery":

    st.caption("Ejemplos de Trabajos")
    st.write("#")
    st.video("./assets/001.mp4")

























#   video = motion.VideoReader("./assets/001.mp4")
#   st.image(video.read())

    #    # Define your javascript
    #   my_js = """
    #   alert("Hola mundo");
    #   """
    #   
    #   # Wrapt the javascript as html code
    #   my_html = f"<script>{my_js}</script>"
    #   
    #   # Execute your app
    #   st.title("Galeria de Imágenes")
    #   st.caption("Galeria de Imágenes")
    #   html(my_html)
    #
    #   def load_images():
    #       image_files = glob.glob("images/*/*.jpg")
    #       n_cols = int(st.number_input("Number of Columns", 1, 5, 3))
    #
    #       st.write(f"We are using {n_cols} columns")

#       manuscripts = []
#       for image_file in image_files:
#           image_file = image_file.replace("\\", "/")
#           parts = image_file.split("/")
#           if parts[1] not in manuscripts:
#               manuscripts.append(parts[1])
#       manuscripts.sort()
#       return image_files, manuscripts
#   
#   images, manuscripts = load_images()
#   
#   manuscripts = st.multiselect("Select Manuscript", manuscripts)
#   
#   view_images = []
#   for image in images:
#       if any(manuscript in image for manuscript in manuscripts):
#           view_images.append(image)
#   
#   n = st.number_input("Grid Width", 1, 5, 2)
#   
#   groups = []
#   for i in range(0, len(view_images), n):
#       groups.append(view_images[i:i+n])
#   
#   
#   for group in groups:
#       cols = st.columns(n)
#       for i, image in enumerate(group):
#           cols[i].image(image)
   

# --- Hard Skills ---

# --- Work History ---


# ---Job 1
 

# ---Job 2
 
# st.write("#")
# st.write("***Empresa de Servicios Generales | BIOCUBAFARMA***")
# st.write("2011 - 2023")
# st.write(
#        """
#        - Asistente de Dirección. 
#        - Secretaria de Actas.
#        - Secretaria de Consejos de Dirección y Organos Auxiliares.
#        - Planes de Trabajo de Directivos.
#        """)

# ---Job 3
 
