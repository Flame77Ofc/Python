import streamlit as st
import datetime
import random
from time import sleep

st.set_page_config(
    page_title = "Calculadora de Idade",
    page_icon = "🎂",
    layout = "centered"
)

with st.sidebar:
    st.title("Calculadora de Idade")

    st.divider()

    st.badge("Guia", color="red", icon="🍁")
    st.caption('Este programa realiza o cálculo de dias, meses e anos que o usuário tem. No campo de "Data de Nascimento" o usuário precisa colocar sua data de nascimento - ou uma data qualquer que seja menor que a atual, clicar no botão de Enviar e o programa automaticamente retorna ao usuário quantos dias, meses e anos o usuário tem.')

    st.divider()

    st.badge("Sobre", color="orange", icon="🥏")
    st.caption("A fórmula que o programa utiliza é a seguinte:")
    st.latex(r"data - choice")
    st.caption("Onde **data é data atual** e **choice é a data que o usuário escolheu.** Uma data é composta por dia, mês e ano, e o programa faz a subtração do dia atual e do dia que o usuário escolheu e a mesma coisa com o mês e o ano.")

st.markdown("<style>input, .stFormSubmitButton, .st-fq {text-align: center;}</style>", unsafe_allow_html=True)


with st.form("Nascimento"):
    limit = datetime.datetime.now().year - 80 # Definindo o limite anual
    st.caption('<p style="text-align: center;">A data de nascimento deve ser no formato inglês: YYYY/MM/DD (ANO/MÊS/DIA) <br> Exemplo: 2005/12/25</p>', unsafe_allow_html = True)
    date = str(st.date_input("Data de Nascimento", min_value=datetime.date(limit, 1, 1))) # Input de data para o usuário digitar

    # Data de hoje
    today = datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day
    today_year, today_month, today_day = today

    # Data que o usuário escolheu
    choice = int(date[:4]), int(date[5:7]), int(date[8:])
    user_year, user_month, user_day = choice


    # Calculando a data: Ano de hoje - Ano que o usuário escolheu, ...
    year = today_year - user_year
    month = today_month - user_month
    day = today_day - user_day


    if st.form_submit_button("Enviar"):
        if choice > today or user_month > 12 or user_day > 30:
            st.warning('Por favor, digite uma data válida')
        else:
            with st.spinner('Carregando', show_time=True):
                sleep(1)

                with st.expander('Informações'):
                    days = (month * 30) + (year * 365) + day
                    st.caption(f"Você tem aproximadamente {days} dias de vida.")

                    months = (days // 30)
                    st.caption(f"Você tem aproximadamente {months} meses de vida.")

                    st.caption(f"Dias: {abs(day)}")
                    st.caption(f"Meses: {abs(month)}")
                    st.caption(f"Anos: {year}")

                    icones = random.choice(['🎈', '🎆', '✨', '🧨', '👴🏻', '👵🏻', '🎊', '🪁', '🎯', '💫', '🎇', '🔆', '🚀', '🌻', '🌹'])

                    st.toast(f"Você tem aproximadamente {days} dias de vida, ou {months} meses de vida.", icon=icones)
