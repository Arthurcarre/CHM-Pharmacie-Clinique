import streamlit as st
import pandas as pd
import numpy as np
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():

    data_frame = pd.read_csv('Analyse Pharmacotherapeutique File.csv')
    data_frame.set_index('Index', inplace=True)

    liste_medoc = [str(medoc) for medoc in set(data_frame.index)]
    liste_medoc.sort()

    option = st.sidebar.selectbox(
          "Choose a medicine. Tip: Just click on the search bar (no need to delete) and type the first letters of the drug (INN or Princeps).",
          liste_medoc)

    if "liste_presc" in st.session_state:
          liste_presc = st.session_state.liste_presc

    if "liste_presc" not in st.session_state:
          liste_presc = []

    if st.sidebar.button("Add the medicine"):
          if option not in liste_presc:
               liste_presc.append(option)
               st.session_state.liste_presc = liste_presc
          else :
               st.error("ERROR : You cannot add the same drug twice to the prescription list !")

    if st.sidebar.button("Remove the medicine"):
          try : 
               liste_presc.remove(option)
               st.session_state.liste_presc = liste_presc
          except ValueError :
               st.error("ERROR : You cannot remove a drug from the prescriptions that is not already in the prescriptions !")

    if st.sidebar.button("Reset the list of prescriptions"):
          if 'liste_presc' in st.session_state:
                 del st.session_state.liste_presc

    st.header('Pharmaco-therapeutic analysis')
    st.subheader('List of prescriptions')

    if "liste_presc" in st.session_state:
         for medoc in st.session_state.liste_presc :  
              col1, col2 = st.columns([1, 3])
              col1.write(medoc)
              with col2 :
                   with st.expander("Analysis of the prescription"):                                  
                        compteur = 0
                        for i in data_frame.index: 
                            if i == medoc:
                                compteur += 1

                        compteur2 = 0
                        for i in range(compteur):
                             if data_frame.loc[{medoc}, 'Category'][i] == 'Contr??le des indications :' :
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
                                            st.text_area("?? adatper selon le contexte", 
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
                                            st.error("ERROR : La base de donn??es interne contient un duplicat (Nom de m??dicament + Condition). ?? corriger")
                                       if txt :                
                                            st.text_area("?? adatper selon le contexte", 
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
              Nous recommandons de v??rifier la pr??sence d'int??raction m??dicamenteuse entre chaque m??dicament et l'inducteur enzymatique 
              ?? l'aide du d??tecteur d'int??raction m??dicamenteuse du Vidal ou de la derni??re version r??cente du Th??saurus de l'ANSM (en s'assurant de v??rifier
              ?? la fois dans la partie "Anticonvulsivant inducteur enzymatique" mais aussi dans la partie propre du m??dicamennt inducteur enzymatique concern??).
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
              if data_frame.loc[{medoc}, 'Torsadog??ne'][0] == 1 :
                   torsadogene_num.append(int(data_frame.loc[{medoc}, 'Torsadog??ne'][0]))
                   torsadogene_name.append(medoc)
              if data_frame.loc[{medoc}, 'Hypok'][0] == 1 :
                   hypok_num.append(int(data_frame.loc[{medoc}, 'Hypok'][0]))
                   hypok_name.append(medoc)
              if data_frame.loc[{medoc}, 'HyperK'][0] == 1 :
                   hyperk_num.append(int(data_frame.loc[{medoc}, 'HyperK'][0]))
                   hyperk_name.append(medoc)
              if data_frame.loc[{medoc}, 'D??presseur_SNC'][0] == 1 :
                   depresseur_SNC_num.append(int(data_frame.loc[{medoc}, 'D??presseur_SNC'][0]))
                   depresseur_SNC_name.append(medoc)
              if data_frame.loc[{medoc}, 'M??dicam inapprop'][0] == 1 :
                   medoc_inaprop_num.append(int(data_frame.loc[{medoc}, 'M??dicam inapprop'][0]))
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
              col1.write(f"Nombre de m??dicament **potentiellement inappropri?? chez la personne ??g??e** dans ce bilan m??dicamenteux : {np.sum(medoc_inaprop_num)}")
              with col2 :
                   with st.expander("M??dicament(s) potentiellement inappropri??(s) chez la personne ??g??e du bilan m??dicamenteux"):
                        for name in medoc_inaprop_name : 
                             st.write(f"\n {name}")
         if np.sum(hypoT_ortho_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **?? l'origine d'hypotension** (hors antihypertenseur), notamment orthostatique, dans ce bilan m??dicamenteux : {np.sum(hypoT_ortho_num)}")
              with col2 :
                   with st.expander("M??dicament(s) ?? l'origine d'hypotension (hors antihypertenseur), notamment orthostatique, du bilan m??dicamenteux"):
                        for name in hypoT_ortho_name : 
                             st.write(f"\n {name}")                         
         if np.sum(depresseur_SNC_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **d??presseur du syst??me nerveux central** dans ce bilan m??dicamenteux : {np.sum(depresseur_SNC_num)}")
              with col2 :
                   with st.expander("M??dicament(s) d??presseur(s) du syst??me nerveux central du bilan m??dicamenteux"):
                        for name in depresseur_SNC_name : 
                             st.write(f"\n {name}")     
         if np.sum(anticholinergics_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **anticholinergique** de ce bilan m??dicamenteux : {np.sum(anticholinergics_num)}")
              with col2 :
                   with st.expander("M??dicament(s) anticholinergique(s) du bilan m??dicamenteux"):
                        for name in anticholinergics_name : 
                             st.write(f"\n {name}")
         if np.sum(torsadogene_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **torsadog??ne** dans ce bilan m??dicamenteux : {np.sum(torsadogene_num)}")
              with col2 :
                   with st.expander("M??dicament(s) torsadog??ne(s) du bilan m??dicamenteux"):
                        for name in torsadogene_name : 
                             st.write(f"\n {name}")
         if np.sum(bradycardi_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **bradycardisant** dans ce bilan m??dicamenteux : {np.sum(bradycardi_num)}")
              with col2 :
                   with st.expander("M??dicament(s) bradycardisant(s)"):
                        for name in bradycardi_name : 
                             st.write(f"\n {name}")
         if np.sum(hypok_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **hypokali??miant** dans ce bilan m??dicamenteux : {np.sum(hypok_num)}")
              with col2 :
                   with st.expander("M??dicament(s) hypokali??miant(s) du bilan m??dicamenteux"):
                        for name in hypok_name : 
                             st.write(f"\n {name}")
         if np.sum(hyperk_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **hyperkali??miant** dans ce bilan m??dicamenteux : {np.sum(hyperk_num)}")
              with col2 :
                   with st.expander("M??dicament(s) hyperkali??miant(s) du bilan m??dicamenteux"):
                        for name in hyperk_name : 
                             st.write(f"\n {name}")                
         if np.sum(pro_convuls_num) > 0 :
              col1, col2 = st.columns(2)
              col1.write(f"Nombre de m??dicament **proconvulsivant** dans ce bilan m??dicamenteux : {np.sum(pro_convuls_num)}")
              with col2 :
                   with st.expander("M??dicament(s) proconvulsivant(s) du bilan m??dicamenteux"):
                        for name in pro_convuls_name : 
                             st.write(f"\n {name}")

    st.sidebar.write(" ----------------------------- ")    
    
    Listes_medocs = pd.read_csv('Listes_medicaments.csv')
    Listes_medocs.set_index('Index_L', inplace=True)
    
    option2 = st.sidebar.selectbox(
         "Choisis une liste pour la consulter.",
         Listes_medocs.index)

    if option2 != "# Choisir une liste de m??dicaments"  :
         st.text_area(option2, 
                      f"{Listes_medocs.loc[{str(option2)}, 'Listes'][0]}",
                      key = option2)
