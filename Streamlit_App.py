import streamlit as st
import pandas as pd
import numpy as np
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

logo = st.sidebar.image('img/logo_chm.png')
st.sidebar.caption("Guide d'analyse pharmacothérapeutique chez le patient MUPA.")

data_frame = pd.read_csv('Analyse Pharmacotherapeutique File.csv')
data_frame.set_index('Index', inplace=True)

liste_medoc = [str(medoc) for medoc in set(data_frame.index)]
liste_medoc.sort()

option = st.sidebar.selectbox(
     "Choisis un médicament. Petite astuce : Il suffit de cliquer sur la barre de recherche (pas besoin d'effacer) et de taper les première lettres du"
     " médicament (DCI ou Princeps).",
     liste_medoc)

if "liste_presc" in st.session_state:
     liste_presc = st.session_state.liste_presc

if "liste_presc" not in st.session_state:
     liste_presc = []

if st.sidebar.button("**Ajouter** le médicament"):
     if option not in liste_presc:
          liste_presc.append(option)
          st.session_state.liste_presc = liste_presc
     else :
          st.error("ERROR : Tu ne peux pas ajouter deux fois le même médicament dans la liste des prescriptions !")

if st.sidebar.button("**Retirer** le médicament"):
     try : 
          liste_presc.remove(option)
          st.session_state.liste_presc = liste_presc
     except ValueError :
          st.error("ERROR : Tu ne peux pas retirer des prescritpions un médicament qui n'est pas déjà dans les prescriptions !")

if st.sidebar.button("Réinitialiser la liste des prescriptions"):
     if 'liste_presc' in st.session_state:
            del st.session_state.liste_presc

st.header('Analyse pharmaco-thérapeutique')
st.subheader('Liste des prescriptions')

if "liste_presc" in st.session_state:
     for medoc in st.session_state.liste_presc :  
          col1, col2 = st.columns([1, 3])
          col1.write(medoc)
          with col2 :
               with st.expander("Analyse de la prescription"):                                  
                    compteur = 0
                    for i in data_frame.index: 
                        if i == medoc:
                            compteur += 1

                    compteur2 = 0
                    for i in range(compteur):
                         if data_frame.loc[{medoc}, 'Category'][i] == 'Contrôle des indications :' :
                              compteur2 += 1
                    for i in range(compteur):
                         if i == 0 :
                              if compteur2 == 1 :
                                  st.write(f"**{data_frame.loc[{medoc}, 'Category'][i]}**")
                                  st.text_area(f"{data_frame.loc[{medoc}, 'Condition'][i]}",
                                           f"{data_frame.loc[{medoc}, 'Paragraphe'][i]}",
                                           key = medoc)
                                  text_to_be_copied = data_frame.loc[{medoc}, 'Paragraphe'][i]
                                  copy_dict = {"content": text_to_be_copied}

                                  copy_button = Button(label="Copier le texte")
                                  copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
                                       navigator.clipboard.writeText(content);
                                       """))
                                   
                                  no_event = streamlit_bokeh_events(
                                       copy_button,
                                       events="GET_TEXT",
                                       key=int(np.random.randint(0, 100000, size=(1, 1))),
                                       refresh_on_update=True,
                                       override_height=40,
                                       debounce_time=0)
                                   
                              elif data_frame.loc[{medoc}, 'Category'][i] == '0' :
                                   st.text_area(f"{data_frame.loc[{medoc}, 'Condition'][i]}",
                                           f"{data_frame.loc[{medoc}, 'Paragraphe'][i]}",
                                           key = medoc)
                                   text_to_be_copied = data_frame.loc[{medoc}, 'Paragraphe'][i]
                                   copy_dict = {"content": text_to_be_copied}

                                   copy_button = Button(label="Copier le texte")
                                   copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
                                       navigator.clipboard.writeText(content);
                                       """))

                                   no_event = streamlit_bokeh_events(
                                       copy_button,
                                       events="GET_TEXT",
                                       key=int(np.random.randint(0, 100000, size=(1, 1))),
                                       refresh_on_update=True,
                                       override_height=40,
                                       debounce_time=0)
                              else :
                                   st.write(f"**{data_frame.loc[{medoc}, 'Category'][i]}**")
                                   txt = st.checkbox(f"{data_frame.loc[{medoc}, 'Condition'][i]}",
                                                  key = medoc)
                                   if txt :                
                                        st.text_area("À adatper selon le contexte", 
                                                  f"{data_frame.loc[{medoc}, 'Paragraphe'][i]}",
                                                  key = medoc)
                                        text_to_be_copied = data_frame.loc[{medoc}, 'Paragraphe'][i]
                                        copy_dict = {"content": text_to_be_copied}

                                        copy_button = Button(label="Copier le texte")
                                        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
                                            navigator.clipboard.writeText(content);
                                            """))

                                        no_event = streamlit_bokeh_events(
                                            copy_button,
                                            events="GET_TEXT",
                                            key=int(np.random.randint(0, 100000, size=(1, 1))),
                                            refresh_on_update=True,
                                            override_height=40,
                                            debounce_time=0)
                         else :
                              if data_frame.loc[{medoc}, 'Category'][i] == '0' :
                                   st.text_area(f"{data_frame.loc[{medoc}, 'Condition'][i]}",
                                           f"{data_frame.loc[{medoc}, 'Paragraphe'][i]}",
                                           key = medoc)
                                   text_to_be_copied = data_frame.loc[{medoc}, 'Paragraphe'][i]
                                   copy_dict = {"content": text_to_be_copied}

                                   copy_button = Button(label="Copier le texte")
                                   copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
                                       navigator.clipboard.writeText(content);
                                       """))

                                   no_event = streamlit_bokeh_events(
                                       copy_button,
                                       events="GET_TEXT",
                                       key=int(np.random.randint(0, 100000, size=(1, 1))),
                                       refresh_on_update=True,
                                       override_height=40,
                                       debounce_time=0)
                              else :
                                   try :
                                        if data_frame.loc[{medoc}, 'Category'][i] != data_frame.loc[{medoc}, 'Category'][i-1] :
                                             st.write(" ----------------------------- ") 
                                             st.write(f"**{data_frame.loc[{medoc}, 'Category'][i]}**")
                                        txt = st.checkbox(f"{data_frame.loc[{medoc}, 'Condition'][i]}",
                                                         key = medoc)
                                   except :
                                        st.error("ERROR : La base de données interne contient un duplicat (Nom de médicament + Condition). À corriger")
                                   if txt :                
                                        st.text_area("À adatper selon le contexte", 
                                                    f"{data_frame.loc[{medoc}, 'Paragraphe'][i]}",
                                                    key = medoc, max_chars=500)
                                        text_to_be_copied = data_frame.loc[{medoc}, 'Paragraphe'][i]
                                        copy_dict = {"content": text_to_be_copied}

                                        copy_button = Button(label="Copier le texte")
                                        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
                                            navigator.clipboard.writeText(content);
                                            """))

                                        no_event = streamlit_bokeh_events(
                                            copy_button,
                                            events="GET_TEXT",
                                            key=int(np.random.randint(0, 100000, size=(1, 1))),
                                            refresh_on_update=True,
                                            override_height=40,
                                            debounce_time=0)  
                                        
          if data_frame.loc[{medoc}, 'Inducteur_enz'][0] == 1 :
               col1.warning("Inducteur enzymatique puissant")
               with col2 :
                    with st.expander("Recommandation"):
                         st.write("""
         Nous recommandons de vérifier la présence d'intéraction médicamenteuse entre chaque médicament et l'inducteur enzymatique 
         à l'aide du détecteur d'intéraction médicamenteuse du Vidal ou de la dernière version récente du Thésaurus de l'ANSM (en s'assurant de vérifier
         à la fois dans la partie "Anticonvulsivant inducteur enzymatique" mais aussi dans la partie propre du médicamennt inducteur enzymatique concerné).
     """)
                    
anticholinergics_num = []
anticholinergics_name = []
torsadogene_num = []
torsadogene_name = []
hypok_num = []
hypok_name = []
hyperk_num = []
hyperk_name = []
depresseur_SNC_num = []
depresseur_SNC_name = []
medoc_inaprop_num = []
medoc_inaprop_name = []
bradycardi_num = []
bradycardi_name = []
hypoT_ortho_num = []
hypoT_ortho_name = []
pro_convuls_num = []
pro_convuls_name = []
                    
if "liste_presc" in st.session_state:
     for medoc in st.session_state.liste_presc :
          if data_frame.loc[{medoc}, 'Anticholinergics'][0] > 0 :
               anticholinergics_num.append(int(data_frame.loc[{medoc}, 'Anticholinergics'][0]))
               anticholinergics_name.append(medoc)
          if data_frame.loc[{medoc}, 'Torsadogène'][0] == 1 :
               torsadogene_num.append(int(data_frame.loc[{medoc}, 'Torsadogène'][0]))
               torsadogene_name.append(medoc)
          if data_frame.loc[{medoc}, 'Hypok'][0] == 1 :
               hypok_num.append(int(data_frame.loc[{medoc}, 'Hypok'][0]))
               hypok_name.append(medoc)
          if data_frame.loc[{medoc}, 'HyperK'][0] == 1 :
               hyperk_num.append(int(data_frame.loc[{medoc}, 'HyperK'][0]))
               hyperk_name.append(medoc)
          if data_frame.loc[{medoc}, 'Dépresseur_SNC'][0] == 1 :
               depresseur_SNC_num.append(int(data_frame.loc[{medoc}, 'Dépresseur_SNC'][0]))
               depresseur_SNC_name.append(medoc)
          if data_frame.loc[{medoc}, 'Médicam inapprop'][0] == 1 :
               medoc_inaprop_num.append(int(data_frame.loc[{medoc}, 'Médicam inapprop'][0]))
               medoc_inaprop_name.append(medoc)
          if data_frame.loc[{medoc}, 'Bradycardisant'][0] == 1 :
               bradycardi_num.append(int(data_frame.loc[{medoc}, 'Bradycardisant'][0]))
               bradycardi_name.append(medoc)
          if data_frame.loc[{medoc}, 'HypoT_Ortho'][0] == 1 :
               hypoT_ortho_num.append(int(data_frame.loc[{medoc}, 'HypoT_Ortho'][0]))
               hypoT_ortho_name.append(medoc)
          if data_frame.loc[{medoc}, 'Pro_convul'][0] == 1 :
               pro_convuls_num.append(int(data_frame.loc[{medoc}, 'Pro_convul'][0]))
               pro_convuls_name.append(medoc)
               
     st.write(" ----------------------------- ")   
     
     if np.sum(medoc_inaprop_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **potentiellement inapproprié chez la personne âgée** dans cette prescription : {np.sum(medoc_inaprop_num)}")
          with col2 :
               with st.expander("Médicament(s) potentiellement inapproprié(s) chez la personne âgée de la prescription"):
                    for name in medoc_inaprop_name : 
                         st.write(f"\n {name}")
     if np.sum(hypoT_ortho_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **à l'origine d'hypotension** (hors antihypertenseur), notamment orthostatique, dans cette prescription : {np.sum(hypoT_ortho_num)}")
          with col2 :
               with st.expander("Médicament(s) à l'origine d'hypotension (hors antihypertenseur), notamment orthostatique, de la prescription"):
                    for name in hypoT_ortho_name : 
                         st.write(f"\n {name}")                         
     if np.sum(depresseur_SNC_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **dépresseur du système nerveux central** dans cette prescription : {np.sum(depresseur_SNC_num)}")
          with col2 :
               with st.expander("Médicament(s) dépresseur(s) du système nerveux central de la prescription"):
                    for name in depresseur_SNC_name : 
                         st.write(f"\n {name}")     
     if np.sum(anticholinergics_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **anticholinergique** de cette prescription : {np.sum(anticholinergics_num)}")
          with col2 :
               with st.expander("Médicament(s) anticholinergique(s) de la prescription"):
                    for name in anticholinergics_name : 
                         st.write(f"\n {name}")
     if np.sum(torsadogene_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **torsadogène** dans cette prescription : {np.sum(torsadogene_num)}")
          with col2 :
               with st.expander("Médicament(s) torsadogène(s) de la prescription"):
                    for name in torsadogene_name : 
                         st.write(f"\n {name}")
     if np.sum(bradycardi_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **bradycardisant** dans cette prescription : {np.sum(bradycardi_num)}")
          with col2 :
               with st.expander("Médicament(s) bradycardisant(s)"):
                    for name in bradycardi_name : 
                         st.write(f"\n {name}")
     if np.sum(hypok_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **hypokaliémiant** dans cette prescription : {np.sum(hypok_num)}")
          with col2 :
               with st.expander("Médicament(s) hypokaliémiant(s) de la prescription"):
                    for name in hypok_name : 
                         st.write(f"\n {name}")
     if np.sum(hyperk_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **hyperkaliémiant** dans cette prescription : {np.sum(hyperk_num)}")
          with col2 :
               with st.expander("Médicament(s) hyperkaliémiant(s) de la prescription"):
                    for name in hyperk_name : 
                         st.write(f"\n {name}")                
     if np.sum(pro_convuls_num) > 0 :
          col1, col2 = st.columns(2)
          col1.write(f"Nombre de médicament **proconvulsivant** dans cette prescription : {np.sum(pro_convuls_num)}")
          with col2 :
               with st.expander("Médicament(s) proconvulsivant(s) de la prescription"):
                    for name in pro_convuls_name : 
                         st.write(f"\n {name}")
    
st.sidebar.write(" ----------------------------- ")    

Listes_medocs = pd.read_csv('Listes_medicaments.csv')
Listes_medocs.set_index('Index_L', inplace=True)

option2 = st.sidebar.selectbox(
     "Choisis une liste pour la consulter.",
     Listes_medocs.index)

if option2 != "# Choisir une liste de médicaments"  :
     st.text_area(option2, 
                  f"{Listes_medocs.loc[{str(option2)}, 'Listes'][0]}",
                  key = option2)
