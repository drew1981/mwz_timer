
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

# Nomi specifici e durate manuali per ciascun timer
timer_details = [
    {'name': 'Speed Cola', 'duration': 30},
    {'name': 'Osso Di Cane', 'duration': 9},
    {'name': 'Corazza Oro', 'duration': 10},
    {'name': 'Lama Etere', 'duration': 1800},
    {'name': 'Cristallo Puro', 'duration': 1200},
    {'name': 'Timer Sei', 'duration': 600},
    {'name': 'Timer Sette', 'duration': 300},
    {'name': 'Timer Otto', 'duration': 150}
]

# Inizializzazione dei timer se non presenti in session_state
for timer in timer_details:
    if timer['name'] not in st.session_state:
        st.session_state[timer['name']] = None

# Creazione delle righe e delle colonne
for i in range(0, 8, 2):
    col1, col2 = st.columns(2)
    with col1:
        timer = timer_details[i]
        if st.image(os.path.join('images', image_files[i]), use_column_width=True) and st.button(f'Avvia {timer["name"]}'):
            start_timer(timer['name'], timer['duration'])
        if st.session_state[timer['name']]:
            now = datetime.datetime.now()
            if now < st.session_state[timer['name']]:
                st.markdown(f"{timer['name']}: {format_timedelta(st.session_state[timer['name']] - now)}")
            else:
                st.session_state[timer['name']] = None

    with col2:
        if len(image_files) > i+1:  # Verifica che l'immagine esista prima di usarla
            timer = timer_details[i+1]
            if st.image(os.path.join('images', image_files[i+1]), use_column_width=True) and st.button(f'Avvia {timer["name"]}'):
                start_timer(timer['name'], timer['duration'])
            if st.session_state[timer['name']]:
                now = datetime.datetime.now()
                if now < st.session_state[timer['name']]:
                    st.markdown(f"{timer['name']}: {format_timedelta(st.session_state[timer['name']] - now)}")
                else:
                    st.session_state[timer['name']] = None

# Forza l'aggiornamento della pagina ogni secondo
time.sleep(1)
st.experimental_rerun()
