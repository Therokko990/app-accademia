import streamlit as st
import pandas as pd
import os

# --- SETTINGS ---
DATA_FILE = "app_academy.xlsx"

# --- Load data ---
@st.cache_data
def load_data():
    xl = pd.ExcelFile(DATA_FILE)
    materie = xl.parse("Materie")
    alunni = xl.parse("Alunni")
    esami = xl.parse("Anno accedemico")
    return materie, alunni, esami

materie_df, alunni_df, esami_df = load_data()

st.title("🎓 Gestione Accademia")

menu = st.sidebar.radio("Scegli sezione:", ["Materie", "Alunni", "Esami"])

# --- Materie ---
if menu == "Materie":
    st.header("📘 Materie")
    st.dataframe(materie_df)

    if st.checkbox("Aggiungi nuova materia"):
        with st.form("form_materia"):
            nome = st.text_input("Nome materia")
            anno = st.selectbox("Anno di insegnamento", [1, 2, 3])
            attiva = st.checkbox("Attiva", value=True)
            materiale = st.selectbox("Tipo materiale", ["Libro", "Dispensa"])
            lingue = st.text_input("Lingue del materiale")
            link = st.text_input("Link al materiale")
            submitted = st.form_submit_button("Aggiungi")
            if submitted:
                new_row = {
                    "Nome materia": nome,
                    "anno di insegamento \n [1/2/3]": anno,
                    "Attiva \n [true/false]": attiva,
                    "materiale \n [Libro/dispensa]": materiale,
                    "Lingue in cui e tradotto il materiale": lingue,
                    "Link al materiale": link
                }
                materie_df = pd.concat([materie_df, pd.DataFrame([new_row])], ignore_index=True)
                st.success("Materia aggiunta!")

# --- Alunni ---
elif menu == "Alunni":
    st.header("🧑‍🎓 Alunni")
    st.dataframe(alunni_df)

    if st.checkbox("Aggiungi nuovo alunno"):
        with st.form("form_alunno"):
            nome = st.text_input("Nome")
            cognome = st.text_input("Cognome")
            email = st.text_input("Email")
            telefono = st.text_input("Telefono")
            chiesa = st.text_input("Chiesa")
            submitted = st.form_submit_button("Aggiungi")
            if submitted:
                new_row = {
                    "nome": nome,
                    "cognome": cognome,
                    "email ": email,
                    "numero di telefono": telefono,
                    "chiesa": chiesa
                }
                alunni_df = pd.concat([alunni_df, pd.DataFrame([new_row])], ignore_index=True)
                st.success("Alunno aggiunto!")

# --- Esami ---
elif menu == "Esami":
    st.header("📅 Esami")
    st.dataframe(esami_df)

    if st.checkbox("Aggiungi nuovo esame"):
        with st.form("form_esame"):
            alunno = st.text_input("Nome alunno")
            materia = st.text_input("Materia")
            tipo_freq = st.selectbox("Tipologia frequenza", ["Presenza", "Online"])
            chiesa = st.text_input("Chiesa dove si è svolto l'esame")
            voto = st.text_input("Voto")
            docente = st.text_input("Docente")
            submitted = st.form_submit_button("Aggiungi")
            if submitted:
                new_row = {
                    "Alunno \n [Link alla tabella ]": alunno,
                    "Materia\n [Link alla tabella ]": materia,
                    "Tipologia di frequenza\n [Presenza/Online]": tipo_freq,
                    "Chiesa dove si è svolto l'esame": chiesa,
                    "Voto": voto,
                    "Docente che ha fatto l'esame": docente
                }
                esami_df = pd.concat([esami_df, pd.DataFrame([new_row])], ignore_index=True)
                st.success("Esame aggiunto!")

# --- Salvataggio ---
if st.button("💾 Salva modifiche su Excel"):
    with pd.ExcelWriter(DATA_FILE, engine="openpyxl", mode="w") as writer:
        materie_df.to_excel(writer, sheet_name="Materie", index=False)
        alunni_df.to_excel(writer, sheet_name="Alunni", index=False)
        esami_df.to_excel(writer, sheet_name="Anno accedemico", index=False)
    st.success("File aggiornato!")
