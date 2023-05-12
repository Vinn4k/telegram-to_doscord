
from discord_webhook import DiscordWebhook, DiscordEmbed



def sendMessage(nomeBot,titulo,message,botUrl):
    # INICIANDO MONTAGEM DA MENSAGEM PARA ENVIAR PARA O DISCORD
    webhook = DiscordWebhook(
        url=botUrl)
    embed = DiscordEmbed(title=titulo, color='03b2f8')
    # Nome Do bot
    embed.set_author(name=nomeBot,
                     icon_url='https://coffops.com/wp-content/uploads/2020/09/cropped-logo-coffops-transparente-1.png')
    embed.add_embed_field(name='Sinal', value='%s' % (message))

    webhook.add_embed(embed)
    response = webhook.execute(embed)




