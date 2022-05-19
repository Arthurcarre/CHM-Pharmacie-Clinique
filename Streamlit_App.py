import streamlit as st
import pandas as pd

logo = st.sidebar.image('img/logo_chm.png')
st.sidebar.caption("Guide d'analyse pharmacothérapeutique chez le patient MUPA.")

data_frame = pd.read_csv('Analyse Pharmacotherapeutique File.csv')
data_frame.set_index('Index', inplace=True)

liste_medoc = [str(medoc) for medoc in set(data_frame.index)]
liste_medoc.sort()

col1, col2 = st.columns(2)
col1.subheader('Liste des prescriptions')
col2.subheader('Commentaires à adapter')

option = st.sidebar.selectbox(
     "Choisis un médicament. Petite astuce : Il suffit de cliquer sur la barre de recherche, pas besoin d'effacer, et de taper les première lettres du"
     " médicament (DCI ou Princeps).",
     liste_medoc)

if "liste_presc" in st.session_state:
     liste_presc = st.session_state.liste_presc

if "liste_presc" not in st.session_state:
     liste_presc = []

if st.sidebar.button("Ajouter le médicament"):
     liste_presc.append(option)
     st.session_state.liste_presc = liste_presc

if st.sidebar.button("Réinitialiser la prescritpion"):
     if 'liste_presc' in st.session_state:
            del st.session_state.liste_presc
               
if "liste_presc" in st.session_state:
     for medoc in st.session_state.liste_presc :  
          col1, col2 = st.columns(2)
          col1.write(medoc)
          with col2 :
               with st.expander("Commentaires"):                                  
                    compteur = 0
                    for i in data_frame.index: 
                        if i == medoc:
                            compteur += 1

                    for i in range(compteur):
                        txt = st.text_area(f"{data_frame.loc[{medoc}, 'Condition'][i]}", f"{data_frame.loc[{medoc}, 'Paragraphe'][i]}", max_chars=500)                   
