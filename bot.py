from lol import jogos_com_champion
import discord
from discord.ext import commands
import random
from velha import jogada, resetar
from forca import sortear_e_limpar, checar_letra


client = commands.Bot(command_prefix='*')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('*comandos'))
    print('Tudo ok!')



@client.command()
async def jogos(ctx, nick, champion):
    await ctx.send(jogos_com_champion(nick, champion))



@client.command()
async def pergunta(ctx, *, question):
    respostas =  [  'Na minha opnião, sim.',
                    'Acho melhor não falar sobre isso agora',
                    'Não sei dizer',
                    'Não conte com isso',
                    'Certamente',
                    'Provavelmente',
                    'Não',
                    'Segundo minhas fontes, não',
                    'As chances não são grandes',
                    'As chances são bem altas',
                    'Tudo indica que sim',
                    'Bem difícil',
                    'Sem dúvida',
                    'Sim',
                    'Sim - Definitivamente',
                    'Melhor não contar com isso']

    await ctx.send(random.choice(respostas))



@client.command()
async def velha(ctx):
    await ctx.send(resetar())



@client.command()
async def velhajogada(ctx, pos):
    await ctx.send(jogada(pos))



@client.command()
async def informações(ctx):
    await ctx.send('Eu fui criada na linguagem Python utilizando as bibliotecas discord.py e requests.')



@client.command()
async def forcanovo(ctx):
    await ctx.send(sortear_e_limpar())



@client.command()
async def forca(ctx, letra):
    await ctx.send(checar_letra(letra))



@client.command()
async def comandos(ctx):
    embed = discord.Embed(
    color = discord.Color.orange()

    )

    embed.set_author(name='Comandos')
    embed.add_field(name='*pergunta (sua pergunta)', value='Recebe uma pergunta de sim ou não e retorna uma resposta', inline=False)
    embed.add_field(name='*informações', value='Auto-explicativo', inline=False)
    embed.add_field(name='*jogos (seu nick) (champion)', value='Retorna o número de partidas que um invocador já jogou com certo champion', inline=False)
    embed.add_field(name='*velha', value='Limpa o tabuleiro e inicia um novo jogo de jogo da velha', inline=False)
    embed.add_field(name='*velhajogada (casa)', value='Coloca sua jogada no tabuleiro do jogo da velha de acordo com a casa informada', inline=False)
    embed.add_field(name='*forcanovo', value='Sorteia uma palavras e incia um novo jogo de forca', inline=False)
    embed.add_field(name='*forca (letra)', value='Recebe uma letra do usuário e verifica se esta letra está ou não na palavra sorteada', inline=False)

    await ctx.send(embed=embed)



client.run('Token do Bot')