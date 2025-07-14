import streamlit as st
import requests
import json
from time import sleep

st.title('Bem vindo!')

try:
    with open('data/welcome-data.txt', 'r', encoding='utf-8') as file: pass
except:
    with open('data/welcome-data.txt', 'w', encoding='utf-8') as file: pass

    try:
        DATABASE = "https://neutrumsocial1-default-rtdb.firebaseio.com/.json"


        r = requests.get(DATABASE)
        json_data = r.json()

        if json_data == None:
            data = {
                "users": 1
            }

            r = requests.patch(DATABASE, json=data)
        else:
            old_users = json_data["users"]

            data = {
                "users": old_users + 1
            }

            r = requests.patch(DATABASE, json=data)
    except: pass

    st.balloons()

    st.toast("+1 Membro!", icon="🤗")
    sleep(2)

    st.toast("Faça login para receber todas as funcionalidades!", icon="⛄")


try:
    with open('./data/login.json', 'r') as arquivo: pass

except Exception as erro:
    st.subheader('O que é o :rainbow[NeutrumSocial]?')
    st.caption('NeutrumSocial é um projeto grande de uma simulação de Rede Social. Aqui você pode ser livre para criar contas, testar, fazer postagens e tudo mais! **Lembrete: Isso é uma simulação!**')

    st.subheader('Por que isso foi criado?')
    st.caption('Isso é uma simulação de um sistema completo, o que não é nada fácil de fazer, além de que fortalece a criatividade e o aprendizado. Isso é um desafio para Iniciantes, e com este sistema qualquer desenvolvedor será capaz de aprender algo. O objetivo desse projeto é apenas simular uma rede social, como anteriormente dito, e brincar com suas funcionalidades. Espero que você, usuário goste, e boa jornada.')

    st.subheader('🪐 Recursos do NeutrumSocial')
    st.caption("""Com o NeutrumSocial, você pode:
- 📝 Criar postagens com textos, imagens e links
- 💬 Enviar mensagens privadas
- 🧑‍🤝‍🧑 Seguir outros usuários
- 🔔 Receber notificações de interações
- 📊 Ver estatísticas básicas do seu perfil
- 🔐 Simulação de login/cadastro""")

    st.subheader('Como começar?')
    st.caption('O primeiro passo para entrar no NeutrumSocial é criar um nome de usuário e uma senha. Você pode fazer isso preenchendo seus dados. Caso não tenha uma conta, você pode criar uma no primeiro contâiner - Cadastrar. Porém, se já possui uma, você pode fazer login no segundo contâiner - Entrar.')

    def analysis_register():
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
            st.badge('Deve ser incluso **@/#/!/$/&** na senha', color='red', icon='✖')
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
                        st.toast("Usuário criado com sucesso!", icon="✔")


                        data = {
                            "user": [
                                username,
                                password
                            ]
                        }

                        with open('./data/login.json', 'w') as arquivo:
                            json.dump(data, arquivo, indent=4)

                            st.info('Página prestes a recarregar')
                            st.toast("Página prestes a recarregar!", icon="🔁")

                            sleep(3)
                            st.rerun()
                    else:
                        st.error("Erro ao criar o usuário:", r.status_code)

    def analysis_login():
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
            st.badge('Deve ser incluso **@/#/!/$/&** na senha', color='red', icon='✖')
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

            r = requests.get(DATABASE)
            json_data = r.json()

            if username in json_data:
                if json_data[username]["password"] == password:
                    if r.status_code == 200:
                        with st.spinner('Verificando Informações...'):
                            sleep(3)
                            st.info("Informações Corretas!")
                            st.toast("Informações Corretas!", icon="✔")




                            data = {
                                "user": [
                                    username,
                                    password
                                ]
                            }

                            with open('./data/login.json', 'w') as arquivo:
                                json.dump(data, arquivo, indent=4)

                                st.info('Página prestes a recarregar')
                                st.toast("Página prestes a recarregar🔁")

                                sleep(2)
                                st.rerun()


                        st.write('Login realizado!')
                    else:
                        st.warning(f'Erro: {r.status_code}')
                else:
                    st.warning('Senha incorreta')
            else:
                st.warning('Nome de usuário não encontrado')

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.expander('**Cadastrar - Criar uma conta**', expanded=True):
            st.markdown('<style>h2 {text-align: center;}</style><h2>Cadastrar</h2>', unsafe_allow_html=True)

            username = st.text_input('Crie seu nome de usuário')
            password = st.text_input('Crie sua senha')

            submit = st.button("Cadastrar", use_container_width=True)
            if submit:
                analysis_register()

    with col2:
        with st.expander('**Entrar - Já tem uma conta**', expanded=True):
            st.markdown('<style>h2 {text-align: center;}</style><h2>Entrar</h2>', unsafe_allow_html=True)

            username = st.text_input('Digite seu nome de usuário')
            password = st.text_input('Digite sua senha')

            submit = st.button("Entrar", use_container_width=True)
            if submit:
                analysis_login()
