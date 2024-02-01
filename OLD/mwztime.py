import streamlit as st
import datetime
import time

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{days}d:{hours:02d}h:{minutes:02d}m:{seconds:02d}s'

def start_timer(timer_name, duration):
    st.session_state[timer_name] = datetime.datetime.now() + datetime.timedelta(seconds=duration)

st.title('App Conto alla Rovescia con Icone')

if 'timer1_end' not in st.session_state:
    st.session_state['timer1_end'] = None

if 'timer2_end' not in st.session_state:
    st.session_state['timer2_end'] = None

if st.button('Icona 1 (2 giorni)'):
    start_timer('timer1_end', 172800)  # 2 giorni in secondi

if st.button('Icona 2 (3 ore)'):
    start_timer('timer2_end', 10800)  # 3 ore in secondi

# Aggiorna i timer
now = datetime.datetime.now()
if st.session_state['timer1_end'] and now < st.session_state['timer1_end']:
    st.markdown(f"Timer 1: {format_timedelta(st.session_state['timer1_end'] - now)}")
else:
    st.session_state['timer1_end'] = None

if st.session_state['timer2_end'] and now < st.session_state['timer2_end']:
    st.markdown(f"Timer 2: {format_timedelta(st.session_state['timer2_end'] - now)}")
else:
    st.session_state['timer2_end'] = None

# Aggiungi qui altre icone e conti alla rovescia

# Forza l'aggiornamento della pagina ogni secondo
time.sleep(1)
st.experimental_rerun()

