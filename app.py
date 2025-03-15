from flask import Flask, render_template, request
import requests

api_key = '174ea246a9bc4c4f9f9b862a356ac383'

app = Flask(__name__)

#Função para buscar receitas
def buscar_receitas(dieta,numero_de_receitas=5):
    url = f"https://api.spoonacular.com/recipes/complexSearch?diet={dieta}&number={numero_de_receitas}&apiKey={api_key}"

    response = requests.get(url)

    #Verificando o status da requesição
    if response.status_code == 200:
        return response.json() #Retorna os dados no formato JSON
    else:
        return None
    
#Página inicial
@app.route('/')
def index():
    return render_template('index.html')

#Página para buscar receitas
@app.route('/buscar',methods=['POST'])
def buscar():
    dieta = request.form['dieta']
    numero_de_receitas = int(request.form['numero_de_receitas'])
    receitas = buscar_receitas(dieta, numero_de_receitas)

    if receitas:
        receitas_list = []
        for receita in receitas['results']:
            link = ""
            if 'sourceUrl' in receita:
                link = receita['sourceUrl']
            else:
                receita_id = receita['id']
                link = f"https://spoonacular.com/recipes/{receita['title'].replace('','-')}--{receita_id}"

            receitas_list.append({'title':receita['title'],'link':link})

        return render_template('index.html',receitas=receitas_list)
    else:
        return render_template('index.html',error="Nenhuma receita encontrada.")
    
if __name__ == '__main__':
    app.run(debug=True)