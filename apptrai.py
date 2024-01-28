import streamlit as st
import whisper
import json
from schema import get_schema
import tempfile
from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI
import os
import dotenv

# Importation des modules depuis les fichiers
from schema import get_schema
from fiche import afficher_json

# Initialisation
dotenv.load_dotenv()
model = whisper.load_model("base")

# Streamlit Interface
st.title("Application de Transcription Médicale")

# Upload Audio File
audio_file = st.file_uploader("Téléchargez un fichier audio", type=['mp3', 'wav'])

if audio_file is not None:
    # Sauvegarde temporaire du fichier audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tmp_file.write(audio_file.getvalue())
        audio_file_path = tmp_file.name

    # Simplification de l'extraction de texte avec Whisper
    result = model.transcribe(audio_file_path)
    extracted_text = result["text"]
    st.text_area("Texte extrait", extracted_text, height=150)

    if st.button('Traiter le Texte Extrait'):
        # Traitement du texte extrait
        schema = get_schema # Récupération du schéma depuis schema.py

        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        chain = create_extraction_chain(schema, llm)
        extraction_result = chain.run(extracted_text)
        
        st.text_area("Resultat d'extraction", extraction_result, height=150)
 
        # Affichage des données extraites
        afficher_json(extraction_result)  # Utilisation de la fonction depuis fiche.py
