import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Calculadora de IMC",
    page_icon = "💪🏻"
)


with st.form("IMC"):
    col1, col2 = st.columns([1, 1])

    with col1:
        peso = st.text_input("Peso em quilogramas (kg)", value="", placeholder="Ex: 75.5")

    with col2:
        altura = st.text_input("Altura em metros (m)", value="", placeholder="Ex: 1.75 (Utilize ponto/vírgula)")

    submit = st.form_submit_button("Calcular")

    if submit:
        try:
            peso = float(peso.replace(",", "."))
            altura = float(altura.replace(",", "."))

            if altura > 0:
                IMC = peso / (altura ** 2)

                if IMC <= 10 or IMC >= 60:
                    st.error("Por favor, insira valores numéricos válidos para peso e altura.")

                else:

                    if IMC < 18.5:
                        st.write("Abaixo do peso")
                    elif IMC >= 18.5 and IMC <= 24.9:
                        st.write("Peso normal")
                    elif IMC >= 25 and IMC <= 29.9:
                        st.write("Sobrepeso")
                    elif IMC >= 30 and IMC <= 34.9:
                        st.write("Obesidade grau I")
                    elif IMC >= 35 and IMC <= 39.9:
                        st.write("Obesidade grau II (Severa)")
                    elif IMC >= 40:
                        st.write("Obesidade grau III (Mórbida)")

                    st.info(f"Seu IMC é: **{IMC:.2f}**")


            else:
                st.error("A altura deve ser maior que zero.")

        except ValueError:
            st.error("Por favor, insira valores numéricos válidos para peso e altura.")

    with st.expander("Informações Adicionais"):
        st.markdown("### Como funciona o cálculo do IMC?")

        st.caption("O cálculo do IMC é baseada numa fórmula que calcula o peso e a altura, sendo: ")
        st.latex(r"IMC = \frac{peso}{altura^2}")

        st.badge("Níveis de IMC", color="orange", icon="🎇")
        df = pd.DataFrame({
            "Valor": ["Abaixo do peso", "Peso normal", "Sobrepeso", "Obesidade grau I", "Obesidade grau II (Severa)", "Obesidade grau III (Mórbida)"],
            "IMC": ["Abaixo de 18.5", "Entre 18.5 e 24.9", "Entre 25 e 29.9", "Entre 30 e 34.9", "Entre 35 e 39.9", "Mais de 40"]}
        )

        st.write(df)
