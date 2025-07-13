import streamlit as st
import requests
import json
from time import sleep



try:
    with open('./data/login.json', 'r') as arquivo: pass
    st.write('Boa, um passo completado! Agora, que tal explorar as funcionalidades?')

    # teste = st.pills('Tses', options=['Início', 'Pesquisar', 'Post'])
    # st.write(teste)

    # if teste == '1':
    #     st.switch_page('pages/create.py')

except Exception as erro:
    def analysis():

        requirements = True # Garante que todos os requisitos estão corretos

        ## Nome de usuário
        # Verifica se nome de usuário tem mais de 6 caracteres
        if len(username) < 6:
            st.badge('O nome de usuário deve ter ao menos 8 caracteres', color='red', icon='✖')
            requirements = False
        else:
            st.badge('O nome de usuário tem 8 caracteres', color="green", icon='✔')


        # Verifica se há vírgula ou ponto - O que influencia no csv
        forbidden = '.,'
        has_forb = [True for forb in forbidden if forb in username]

        status = True if has_forb else False
        if status:
            st.badge('O nome de usuário não deve ter ponto nem vírgula', color='red', icon='✖')
            requirements = False
        else:
            st.badge('O nome de usuário não tem ponto nem vírgula', color="green", icon='✔')



        ## Senha
        # Verifica a senha tem mais de 8 caracteres
        if len(password) < 8:
            st.badge('A senha deve ter ao menos 8 caracteres', color='red', icon='✖')
            requirements = False
        else:
            st.badge('A senha tem 8 caracteres', color="green", icon='✔')


        # Verifica se tem uma letra na senha
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        has_letter = [True for letter in letters if letter in password]

        status = True if has_letter else False
        if status:
            st.badge('A senha tem uma letra', color="green", icon='✔')
        else:
            st.badge('A senha deve ter ao mínimo 1 letra', color='red', icon='✖')
            requirements = False


        # Verifica se na senha há numeros
        numbers = '0123456789'
        has_number = [True for number in numbers if number in password]

        status = True if has_number else False
        if status == False:
            st.badge('A senha deve ter ao mínimo 1 número', color='red', icon='✖')
            requirements = False
        else:
            st.badge('A senha tem um número', color="green", icon='✔')


        # Verifica se na senha há um caractere especial
        especials = '@#!$&'
        has_especial = [True for especial in especials if especial in password]

        status = True if has_especial else False
        if status == False:
            st.badge('A senha deve ter ao menos um caractere especial - Incluindo: **@, #, !, $, &**', color='red', icon='✖')
            requirements = False
        else:
            st.badge('A senha tem um caractere especial', color="green", icon='✔')
        
        # Verifica se há vírgula ou ponto - O que influencia no csv
        forbidden = '.,'
        has_forb = [True for forb in forbidden if forb in password]

        status = True if has_forb else False
        if status:
            st.badge('A senha não deve ter ponto nem vírgula', color='red', icon='✖')
            requirements = False
        else:
            st.badge('A senha não tem ponto nem vírgula', color="green", icon='✔')



        # Verifica se os requisitos são satisfeitos
        if requirements:
            DATABASE = "https://neutrumsocial1-default-rtdb.firebaseio.com/.json"

            data = {
                username: {
                    'password': password
                }
            }

            r = requests.get(DATABASE)
            json_data = r.json()

            if json_data and username in json_data:
                st.warning('Este nome de usuário já existe. Tente outro.')
            else:
                with st.spinner('Verificando Informações...'):
                    sleep(3)
                    r = requests.patch(DATABASE, json=data)
                    if r.status_code == 200:
                        st.info("Usuário criado com sucesso!")


                        data = {
                            "user": [
                                username,
                                password
                            ]
                        }

                        with open('./data/login.json', 'w') as arquivo:
                            json.dump(data, arquivo, indent=4)


                            # acess_user = data['user'][0] # Para acessar o nome de usuário
                            # acess_pass = data['user'][1] # Para acessar a senha

                            st.divider()
                            st.info('Página prestes a recarregar')

                            sleep(2)
                            st.rerun()
                    else:
                        st.error("Erro ao criar o usuário:", r.status_code)



    with st.form('Create'):
        username = st.text_input('Crie seu nome de usuário')
        password = st.text_input('Crie sua senha')

        submit = st.form_submit_button("Enviar")
        if submit:
            analysis()
