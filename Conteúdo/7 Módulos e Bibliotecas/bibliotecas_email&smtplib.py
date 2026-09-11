# Import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

# Parâmetros
senha = "05122005G"
msg['From'] = "gabrielcamoesdasilva10@gmail.com"
msg['To'] = "weirdgab@disroot.org"
msg['Subject'] = "Testando."

# Criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# Criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login na conta para envio
server.login(msg['From'], senha)

# Envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Encerramento do servidor
server.quit()