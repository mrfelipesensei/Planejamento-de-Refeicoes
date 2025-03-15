import requests

api_key = '174ea246a9bc4c4f9f9b862a356ac383'

#Função para buscar receitas
def buscar_receitas(dieta,numero_de_receitas=5):
    url = f"https://api.spoonacular.com/recipes/complexSearch?diet={dieta}&number={numero_de_receitas}&apiKey={api_key}"

    response = requests.get(url)

    #Verificando o status da requesição
    if response.status_code == 200:
        return response.json() #Retorna os dados no formato JSON
    else:
        print(f"Erro: {response.status_code}")
        return None
    
#Exemplo de uso
dieta = 'vegan'
receitas = buscar_receitas(dieta)

if receitas:
    for i, receita in enumerate(receitas['results'],start=1):
        print(f"{i}. {receita['title']}")
        
        if 'sourceUrl' in receita:
            print(f"Link: {receita['sourceUrl']}")
        else:
            receita_id = receita['id']
            print(f"Link alternativo: https://spoonacular.com/recipes/{receita['title'].replace(' ', '-')}-{receita_id}")

        print("-" * 50)
