import streamlit as st

def afficher_json(data_json):
    st.write("# Fiche Médicale")

    # Informations du Médecin
    st.write("## Informations du Médecin")
    st.text_input("Nom du médecin", value=data_json.get("doctor_name", ""))

    # Informations du Patient
    st.write("## Informations du Patient")
    st.text_input("Nom du patient", value=data_json.get("patient_name", ""))
    st.number_input("Âge du patient", value=data_json.get("patient_age", 0))

    # Détails de la Consultation
    st.write("## Détails de la Consultation")
    options_symptomes = ["toux persistante", "fièvre", "fatigue", "maux de tête", "essoufflement"]
    default_symptomes = [s for s in data_json.get("symptoms", []) if s in options_symptomes]
    st.multiselect("Symptômes", options=options_symptomes, default=default_symptomes)

    options_examens = ["rougeur de la gorge", "augmentation des ganglions lymphatiques", "congestion nasale"]
    default_examens = [e for e in data_json.get("physical_examination_findings", []) if e in options_examens]
    st.multiselect("Constatations de l'examen physique", options=options_examens, default=default_examens)

    options_diagnostic = ["infection virale", "pharyngite", "grippe", "rhume"]
    default_diagnostic = [d for d in data_json.get("diagnostic_hypotheses", []) if d in options_diagnostic]
    st.multiselect("Hypothèses diagnostiques", options=options_diagnostic, default=default_diagnostic)

    # Tests et Traitements Supplémentaires
    st.write("## Tests et Traitements Supplémentaires")
    options_tests = ["analyse sanguine", "radiographie pulmonaire", "ECG"]
    default_tests = [t for t in data_json.get("additional_tests", []) if t in options_tests]
    st.multiselect("Tests supplémentaires", options=options_tests, default=default_tests)

    options_traitement = ["repos au lit", "hydratation", "antibiotiques (si nécessaire)", "anti-inflammatoires"]
    default_traitement = [t for t in data_json.get("treatment_plan", []) if t in options_traitement]
    st.multiselect("Plan de traitement", options=options_traitement, default=default_traitement)

    # Recommandations de Suivi
    st.write("## Recommandations de Suivi")
    options_suivi = ["contrôle dans 5 jours", "ajustement du traitement selon les résultats des tests", "consultation de suivi"]
    default_suivi = [s for s in data_json.get("follow_up_recommendations", []) if s in options_suivi]
    st.multiselect("Recommandations de suivi", options=options_suivi, default=default_suivi)

    # Conclusion
    st.write("## Conclusion")
    st.text_area("Conclusion", value=data_json.get("conclusion", ""))

    if st.button('Enregistrer'):
        st.success('Données enregistrées (fonctionnalité à implémenter)')
