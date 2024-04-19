from flask import Flask, request

app = Flask(__name__)

# Endpoint GET simple
@app.route('/')
def hello():
    return 'Hello, World!'

# Endpoint POST avec une vulnérabilité d'injection de shell
@app.route('/exec', methods=['POST'])
def execute():
    data = request.form.get('data')
    # eval(data) # Vulnérabilité ici : utilisation dangereuse de eval()
    return 'ok'

# Démarrage du serveur
if __name__ == '__main__':
    app.run(debug=True)
