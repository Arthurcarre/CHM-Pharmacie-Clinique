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
col2.subheader('Commentaires à adapter selon le contexte')

option = st.sidebar.selectbox(
     "Choisis un médicament. Petite astuce : Il suffit de cliquer sur la barre de recherche, pas besoin d'effacer, et de taper les première lettres du"
     " médicament (DCI ou Princeps).",
     liste_medoc)

if st.sidebar.button("Ajouter le médicament"):
     st.session_state.medoc = option
     
if "medoc" in st.session_state :     
     col1.write(st.session_state.medoc)
     with col2 :
          with st.expander("Commentaires"):                                  
               compteur = 0
               for i in data_frame.index: 
                   if i == st.session_state.medoc:
                       compteur += 1

               for i in range(compteur):
                   txt = st.text_area(f"{data_frame.loc[{st.session_state.medoc}, 'Condition'][i]}", f"{data_frame.loc[{st.session_state.medoc}, 'Paragraphe'][i]}", max_chars=500)
