from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.google.com')  # Redireciona para o Google

@app.route('/oauth/callback')
def oauth_callback():
    # Aqui você pode lidar com o código de autorização retornado pela API do Gmail
    code = request.args.get('code')
    # Faça o que for necessário com o código de autorização
    
    return code

if __name__ == '__main__':
    app.run(port=6000)
