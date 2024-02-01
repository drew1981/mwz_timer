
import streamlit as st
import datetime
import time
import random

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

# Inizializzazione dei timer se non presenti in session_state
timer_names = [f'timer{i}_end' for i in range(1, 9)]
for timer_name in timer_names:
    if timer_name not in st.session_state:
        st.session_state[timer_name] = None

# Creazione di tempi random (esempio: tra 1 minuto e 1 giorno)
random_durations = [random.randint(60, 86400) for _ in range(8)]

# Creazione delle righe e delle colonne
for i in range(0, 8, 2):
    col1, col2 = st.columns(2)
    with col1:
        icon_label = f'Icona {i+1}'
        if st.button(icon_label):
            start_timer(timer_names[i], random_durations[i])
        if st.session_state[timer_names[i]]:
            now = datetime.datetime.now()
            if now < st.session_state[timer_names[i]]:
                st.markdown(f"{icon_label}: {format_timedelta(st.session_state[timer_names[i]] - now)}")
            else:
                st.session_state[timer_names[i]] = None

    with col2:
        icon_label = f'Icona {i+2}'
        if st.button(icon_label):
            start_timer(timer_names[i+1], random_durations[i+1])
        if st.session_state[timer_names[i+1]]:
            now = datetime.datetime.now()
            if now < st.session_state[timer_names[i+1]]:
                st.markdown(f"{icon_label}: {format_timedelta(st.session_state[timer_names[i+1]] - now)}")
            else:
                st.session_state[timer_names[i+1]] = None

# Forza l'aggiornamento della pagina ogni secondo
time.sleep(1)
st.experimental_rerun()
