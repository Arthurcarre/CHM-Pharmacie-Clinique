import streamlit as st
import pandas as pd
import numpy as np

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
     "Choisis un médicament. Petite astuce : Il suffit de cliquer sur la barre de recherche (pas besoin d'effacer) et de taper les première lettres du"
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

st.write(" ----------------------------- ")                
                    
torsadogene_num = []
torsadogene_name = []
hypok_num = []
hypok_name = []
hyperk_num = []
hyperk_name = []
                    
if "liste_presc" in st.session_state:
     for medoc in st.session_state.liste_presc :
          if data_frame.loc[{medoc}, 'Torsadogène'][0] == 1 :
               torsadogene_num.append(int(data_frame.loc[{medoc}, 'Torsadogène'][0]))
               torsadogene_name.append(medoc)
          if data_frame.loc[{medoc}, 'Hypok'][0] == 1 :
               hypok_num.append(int(data_frame.loc[{medoc}, 'Hypok'][0]))
               hypok_name.append(medoc)
          if data_frame.loc[{medoc}, 'HyperK'][0] == 1 :
               hyperk_num.append(int(data_frame.loc[{medoc}, 'HyperK'][0]))
               hyperk_name.append(medoc)
     col1, col2 = st.columns(2)
     col1.write(f"Nombre de médicament torsadogène dans cette prescription : {np.sum(torsadogene_num)}")
     with col2 :
          with st.expander("Médicament(s) torsadogène(s) de la prescription"):
               for name in torsadogene_name : 
                    st.write(f"\n {name}")
     col1, col2 = st.columns(2)
     col1.write(f"Nombre de médicament hypokaliémiant dans cette prescription : {np.sum(hypok_num)}")
     with col2 :
          with st.expander("Médicament(s) hypokaliémiant(s) de la prescription"):
               for name in hypok_name : 
                    st.write(f"\n {name}")
     col1, col2 = st.columns(2)
     col1.write(f"Nombre de médicament hyperkaliémiant dans cette prescription : {np.sum(hyperk_num)}")
     with col2 :
          with st.expander("Médicament(s) hyperkaliémiant(s) de la prescription"):
               for name in hyperk_name : 
                    st.write(f"\n {name}")
     
