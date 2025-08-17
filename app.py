
from flask import Flask, request, render_template, redirect
import datetime
import uuid
import cloudinary
import cloudinary.uploader
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configurações do Cloudinary
cloudinary.config(
    cloud_name='YOUR_CLOUD_NAME',
    api_key='YOUR_API_KEY',
    api_secret='YOUR_API_SECRET'
)

# Autenticação com Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("GuiaFuSEx").sheet1

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        nascimento = request.form["nascimento"]
        fus_ex = request.form["fusex"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        local = request.form["local"]
        especialidade = request.form["especialidade"]
        arquivo = request.files["arquivo"]
        
        # Cálculo da idade
        nasc_date = datetime.datetime.strptime(nascimento, "%Y-%m-%d")
        hoje = datetime.datetime.now()
        idade = hoje.year - nasc_date.year - ((hoje.month, hoje.day) < (nasc_date.month, nasc_date.day))

        # Upload no Cloudinary
        upload_result = cloudinary.uploader.upload(arquivo)
        arquivo_url = upload_result.get("secure_url", "")

        # ID único
        registro_id = str(uuid.uuid4())

        # Salvar no Google Sheets
        sheet.append_row([registro_id, nome, nascimento, idade, fus_ex, email, telefone, local, especialidade, arquivo_url])

        return redirect("/sucesso")

    return render_template("form.html")

@app.route("/sucesso")
def sucesso():
    return "Dados enviados com sucesso! Aguarde nosso contato por e-mail."

if __name__ == "__main__":
    app.run(debug=True)
