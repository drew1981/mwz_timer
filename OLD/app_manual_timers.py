
import streamlit as st
import datetime
import time
import os

# Funzione per formattare il timedelta
def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{days}d:{hours:02d}h:{minutes:02d}m:{seconds:02d}s'

# Funzione per avviare un timer
def start_timer(timer_name, duration):
    st.session_state[timer_name] = datetime.datetime.now() + datetime.timedelta(seconds=duration)

st.title('App Conto alla Rovescia con Icone')

# Caricamento delle immagini (assicurati che le immagini siano nella cartella 'images')
image_files = [file for file in os.listdir('images') if file.endswith(('.png', '.jpg', '.jpeg'))]
image_files.sort()  # Assicurati che l'ordine delle immagini sia quello desiderato

# Verifica che ci siano almeno 8 immagini
if len(image_files) < 8:
    st.error("Sono necessarie almeno 8 immagini nella cartella 'images'")
    st.stop()

# Inizializzazione dei timer se non presenti in session_state
timer_names = [f'timer{i}_end' for i in range(1, 9)]
for timer_name in timer_names:
    if timer_name not in st.session_state:
        st.session_state[timer_name] = None

# Durate manuali per ciascun timer (in secondi)
manual_durations = [30, 10, 5, 1800, 1200, 600, 300, 150]  # Esempio di durate

# Creazione delle righe e delle colonne
for i in range(0, 8, 2):
    col1, col2 = st.columns(2)
    with col1:
        if st.image(os.path.join('images', image_files[i]), use_column_width=True) and st.button(f'Speed Cola {i+1}'):
            start_timer(timer_names[i], manual_durations[i])
        if st.session_state[timer_names[i]]:
            now = datetime.datetime.now()
            if now < st.session_state[timer_names[i]]:
                st.markdown(f"Timer {i+1}: {format_timedelta(st.session_state[timer_names[i]] - now)}")
            else:
                st.session_state[timer_names[i]] = None

    with col2:
        if len(image_files) > i+1:  # Verifica che l'immagine esista prima di usarla
            if st.image(os.path.join('images', image_files[i+1]), use_column_width=True) and st.button(f'Osso Di Cane {i+2}'):
                start_timer(timer_names[i+1], manual_durations[i+1])
            if st.session_state[timer_names[i+1]]:
                now = datetime.datetime.now()
                if now < st.session_state[timer_names[i+1]]:
                    st.markdown(f"Timer {i+2}: {format_timedelta(st.session_state[timer_names[i+1]] - now)}")
                else:
                    st.session_state[timer_names[i+1]] = None

# Forza l'aggiornamento della pagina ogni secondo
time.sleep(1)
st.experimental_rerun()
