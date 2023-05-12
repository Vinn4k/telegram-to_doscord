from file_service import ler_arquivo_json, criar_arquivo_json
from send_message import sendMessage
from telethon import TelegramClient, events, sync

cliientId = 0
clientKey = "0"

if __name__ == '__main__':
    with sync.TelegramClient('projectGeremias', cliientId, clientKey) as client:
        dialogs = client.get_dialogs()

        config = {}
        if ler_arquivo_json() == False:
            print("Digite o numero correspondente ao grupo")
            for i, elem in enumerate(dialogs):
                print(i, elem.title, elem.id)
            grupo = input("Digite o numero do Correspondente do grupo: ")
            print("Grupo selecionado, " + dialogs[int(grupo)].title + " " + str(dialogs[int(grupo)].id)),
            groupLink = input("Cole o link do webhook do discord: ")
            print("Grupo informado: " + groupLink)
            botName = input("Digite o nome que seu bot vai chamar discord: ")
            botTitle = input("Digite Titulo das menssagem: ")

            config = criar_arquivo_json(
                {"groupNameTelegram": dialogs[int(grupo)].title, "groupIdTelegram": dialogs[int(grupo)].id,
                 "discordGoup": str(groupLink), "botName": botName, "botTitle": botTitle})
        else:
            print("Configuração encontrada")
            config = ler_arquivo_json()

        print("Aguardando menssagens")


        @client.on(sync.events.NewMessage(chats=[config["groupIdTelegram"]], pattern='.*'))
        async def handler(event):
            print("nova mensagem")
            sendMessage(nomeBot=config["botName"], titulo=config["botTitle"], message=event.message.message,
                        botUrl=config["discordGoup"])
            print("Aguardando menssagens")


        client.run_until_disconnected()
