# Sakurako-Chan
<img src='https://pm1.narvii.com/6344/30d0dacd11ff6ae7c8bca28f13f61164468a27fb_hq.jpg' width=300px height=300px> 

*Sakurako Ōmuro, mascote do bot.*

### Um Bot Para o Aplicativo de Comunicações Discord Utilizando Python

## Sobre
Sakurako-Chan é um bot contruido em Python utilizando a biblioteca discord.py. O bot possui diversas funcionalidades para serem usadas em canais de texto de servidores do aplicativo Discord. Seus comandos vão desde responder perguntas de sim ou não com base em uma lista de respostas já pré-definida até coletar dados da API da Riot Games (empresa famosa pelos jogos: League of Legends e Valorant).<br> 
  
  *Obs: Esse foi o meu primeiro projeto relativamente grande em Python após 7 meses aprendendo a linguagem.* 

## Pré-Requisitos
- Python 3.8.1 (ou superior)
- Biblioteca Discord.py
- Biblioteca Requests
Para instalar as bibliotecas necessárias basta utilizar os comandos:
<br>```pip install discord.py```
<br>```pip install requests```

É necessário criar uma aplicação no [*Portal do Desenvolvedor*](https://discord.com/developers/applications) do Discord. Após criada a aplicação entre na aba **Bot** e clique em **Add-Bot**, feito isso o seu bot estará criado. Clique em **Click to Reveal Token** para ter acesso ao Token do seu bot, guarde esse Token pois o utilizaremos mais tarde. Agora para adicionar o bot em seu servidor vá na aba OAuth2 e na caixa **Scopes** marque a opção **bot**, agora em **Bot Permissions** selecione as permissões que seu bot terá dentro do servidor. Para que o bot funcione corretamente marque as opções **Send Messages**, **Read Message History** e **View Channels**. Após isso, será gerado um link dentro da caixa **Scopes** acesse esse link para poder adicionar o bot em algum de seus servidores.
