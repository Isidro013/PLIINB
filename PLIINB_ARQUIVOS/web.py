import json
import requests
from googletrans import Translator

def lin():
    print('-'*30)

def web():
    translator = Translator()
    r = requests.get('https://r4u.herokuapp.com/getFilme/4')
    if r.status_code == 200:
        reddit_data = json.loads(r.content)
        u = reddit_data['filme']
        o = requests.get('http://www.omdbapi.com/?t={}&apikey=ed2baf'.format(u))
        reddit2_data = json.loads(o.content)
        lin()
        print("Titulo:")
        print(reddit2_data['Title'])
        print('')
        lin()
        print('Lançamento:')
        
        print(reddit2_data['Released'])
        print('')
        lin()
        print('Genero: ')
        traduGenre = translator.translate(reddit2_data['Genre'], dest='pt')
        print(traduGenre.text)
        print('')
        lin()
        print('Duração: ')
        
        print(reddit2_data['Runtime'])
        print('')
        lin()
        print('Sinopse: ')
        
        traduPLot = translator.translate(reddit2_data['Plot'], dest='pt')
        print(traduPLot.text)
        print('')
        lin()
    else:
        print('Erro')
    return web