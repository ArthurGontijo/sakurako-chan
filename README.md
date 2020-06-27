# Sakurako-Chan
<img src='https://pm1.narvii.com/6344/30d0dacd11ff6ae7c8bca28f13f61164468a27fb_hq.jpg' width=300px height=300px> 

*Sakurako Ōmuro, mascote do bot.*

### Um Bot Para o Aplicativo de Comunicações Discord Utilizando Python

## Sobre
Sakurako-Chan é um bot contruido em Python utilizando a biblioteca discord.py. O bot possui diversas funcionalidades para serem usadas em canais de texto de servidores do aplicativo Discord. Seus comandos vão desde responder perguntas de sim ou não com base em uma lista de respostas já pré-definida até coletar dados da API da Riot Games (empresa famosa pelos jogos: League of Legends e Valorant).<br> 
  
  *Obs: Esse foi o meu primeiro projeto relativamente grande em Python após 7 meses aprendendo a linguagem.* 

## Pré-Requisitos
- Discord (Obviamente)
- Python 3.8.1 (ou superior)
- Biblioteca Discord.py <br>
Para instalar a biblioteca basta utilizar o comando:
```
pip install discord.py
```

É necessário criar uma aplicação no [*Portal do Desenvolvedor*](https://discord.com/developers/applications) do Discord. Após criada a aplicação entre na aba **Bot** e clique em **Add-Bot**, feito isso o seu bot estará criado. Clique em **Click to Reveal Token** para ter acesso ao Token do seu bot, guarde esse Token pois o utilizaremos mais tarde. Agora para adicionar o bot em seu servidor vá na aba OAuth2 e na caixa **Scopes** marque a opção **bot**, agora em **Bot Permissions** selecione as permissões que seu bot terá dentro do servidor. Para que o bot funcione corretamente marque as opções **Send Messages**, **Read Message History** e **View Channels**. Após isso, será gerado um link dentro da caixa **Scopes** acesse esse link para poder adicionar o bot em algum de seus servidores.

#### Opcional
**Esse passo é opcional, caso não deseje ter a integração com a API da Riot Games não há problema em ignora-lo visto que as outras funcionalidades não serão comprometidas.**<br> 

Primeiramente, é necessário que se tenha uma **API Key** para possibilitar o acesso à API da Riot. Essa key é obtida no [*Portal do Desenvolvedor Riot*](https://developer.riotgames.com/). Guarde o código dessa key pois o usaremos mais tarde.<br>

Além da **API Key** é necessário também a biblioteca **Requests** para instala-la utilize o comando: <br>
```
pip install requests
```

## Instalação e Utilização
- Entre no diretório que deseja baixar os arquivos e utilize o comando: <br>
```
git clone https://github.com/ArthurGontijo/sakurako-chan.git
```
- Abra o arquivo **bot.py** em um editor de texto e edite a última linha do programa: <br>
```python
client.run('Token do Bot')
```
Substitua a string **'Token do Bot'** por uma string contendo o token fornecido pelo discord para seu bot. <br>
- Caso possua uma **API Key** da Riot Games abra o arquivo **lol.py** em um editor de texto e edite a quarta linha do programa:
```python
api_key = 'Key para acessar a API da Riot Games'
```
Substitua a string **'Key para acessar a API da Riot Games'** por uma string contendo sua API Key sem os 6 primeiros caracteres: **RGAPI-**
