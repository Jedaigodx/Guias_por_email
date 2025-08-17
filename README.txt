
1. Crie um projeto no Google Cloud e ative a Google Sheets API.
2. Baixe o arquivo de credenciais JSON e salve como 'credentials.json' na raiz do projeto.
3. Crie uma planilha chamada 'GuiaFuSEx' no Google Sheets com os seguintes cabeçalhos:
   ID, Nome, Nascimento, Idade, FuSEx, E-mail, Telefone, Local, Especialidade, Arquivo URL
4. Crie uma conta gratuita no https://cloudinary.com e obtenha:
   - cloud_name
   - api_key
   - api_secret
5. Substitua essas informações no app.py no bloco cloudinary.config(...)
6. Execute com: python app.py
7. Acesse o formulário em http://localhost:5000
