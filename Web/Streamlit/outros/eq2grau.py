import math

def equacao(a, b, c):
    parte1 = (abs(b*b)) 
    parte2 = 4 * a * c

    if a < 0 and c < 0:
        parte2 = -parte2
    elif (a >= 0 or c >= 0) or ():
        parte2 = abs(parte2)

    delta = parte1 + parte2

    if delta < 0:
        print('delta < 0 -> ∄ x¹,x²')
    else:
        print(f"O valor de delta é {delta}")


        if b < 0:
            b = abs(b)
        else:
            b = -b

        x1 = (b + math.sqrt(delta)) / 2*a
        x2 = (b - math.sqrt(delta)) / 2*a

        print(f"O conjunto solução é {x1, x2}")

    print("---\n")



equacao(1, -6, 8)


# import streamlit as st

# with st.form("Equação"):
#     a = st.number_input('Digite o valor de a')


#     if a == '' or b == '' or c == '':
#         st.warning('Por favor, preenche corretamente')

#     submit = st.form_submit_button('Enviar o resultado')