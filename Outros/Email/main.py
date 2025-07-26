import smtplib
from email.message import EmailMessage


def enviar_mensagem(enviador: str, destinario: str, assunto: str, mensagem: str, senha: str):
    try:
        msg = EmailMessage()

        msg["From"] = enviador
        msg["To"] = destinario
        msg["Subject"] = assunto
        msg.set_content(mensagem)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
            email.login(enviador, senha)
            email.send_message(msg)

        return "Email Enviado com Sucesso!"
    except Exception as erro:
        return f"Erro: {erro}"


enviar_mensagem("Enviador", "Destinario", "Assunto do Email", "Mensagem do Email", "Senha do Email")
