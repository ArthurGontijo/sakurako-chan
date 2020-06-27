import requests
import datetime

api_key = 'Key para acessar a API da Riot Games'

def jogos_com_champion(nick, champion):
    pedido_invocador = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + nick.lower().strip() + '?api_key=RGAPI-' + api_key)
    status_code = pedido_invocador.status_code
    champion = champion.title()

    if status_code == 404:
        return 'Não achei o invocador que você estava procurando. Vê se escreve direito na próxima'

    elif status_code == 401 or status_code == 403:
        return f'Avisa pro animal do Arthur trocar a API Key porque tá dando o erro {status_code}'

    elif status_code != 200:
        return 'Ocorreu um erro inesperado. Tente novamente'
    
    else:
        pedido_champion = requests.get('https://ddragon.leagueoflegends.com/cdn/10.9.1/data/pt_BR/champion.json')
        if pedido_champion.status_code != 200:
            return 'Ocorreu um erro inesperado.'

        else:
            champion_id = pedido_champion.json()['data'][champion]['key']
            account_id = pedido_invocador.json()['accountId']
            pedido_hist = requests.get('https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + account_id + '?champion='+ champion_id +'&api_key=RGAPI-' + api_key)
            if pedido_hist.status_code == 404:
                return 'Não encontrei partidas com esse champion'
            elif pedido_hist.status_code != 200:
                return 'Ocorreu um  erro inesperado. Tente novamente'
            
            else:
                jogos = pedido_hist.json()['totalGames']
                mais_antigo = pedido_hist.json()['endIndex'] - 1
                unix = pedido_hist.json()['matches'][mais_antigo]['timestamp']
                unix = round(unix/1000)
                date = datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y')

                return f'De acordo com a base de dados da Riot, {nick} já jogou {jogos} jogos de {champion}. O jogo mais antigo que encontrei é do dia: {date}'