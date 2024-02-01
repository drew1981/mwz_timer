
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

# Funzione per far lampeggiare un messaggio
def flashing_message(message, color='green'):
    st.markdown(f"<span style='color: {color};'>{message}</span>", unsafe_allow_html=True)

st.title('MWZ PERKS TIMER')

# Dettagli di ciascun timer con nome, durata e immagine
timer_details = [
    {'name': 'Speed Cola', 'duration': 10800, 'image': 'image1.png'},
    {'name': 'Juggernog', 'duration': 10800, 'image': 'image2.png'},
    {'name': 'Energia +', 'duration': 10800, 'image': 'image3.png'},
    {'name': 'Lama Etere', 'duration': 172800, 'image': 'image4.png'},
    {'name': 'Corazza Oro', 'duration': 172800, 'image': 'image5.png'},
    {'name': 'Osso Di Un Cane', 'duration': 172800, 'image': 'image6.png'},
    {'name': 'Cristallo Etere Puro', 'duration': 259200, 'image': 'image7.png'},
    {'name': 'Cristallo Etere Raffinato', 'duration': 57600, 'image': 'image8.png'}
]

# Inizializzazione dei timer se non presenti in session_state
for timer in timer_details:
    if timer['name'] not in st.session_state:
        st.session_state[timer['name']] = None

# Creazione delle righe e delle colonne per ciascun timer
for timer in timer_details:
    col1, col2 = st.columns(2)
    with col1:
        if st.image(os.path.join('images', timer['image']), width=100) and st.button(f'Avvia {timer["name"]}'):
            start_timer(timer['name'], timer['duration'])
    with col2:
        if st.session_state[timer['name']]:
            now = datetime.datetime.now()
            if now < st.session_state[timer['name']]:
                st.markdown(f"<h2 style='font-size: 30px;'>{timer['name']}: {format_timedelta(st.session_state[timer['name']] - now)}</h2>", unsafe_allow_html=True)
            else:
                flashing_message("Ora puoi ricrearlo")

# Forza l'aggiornamento della pagina ogni secondo
time.sleep(1)
st.experimental_rerun()
