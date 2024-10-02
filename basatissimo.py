import discord
from discord.ext import commands
#credentials
token = 'OTI4NDAwMTE5Mjg2NjI4NDEz.YdYN_Q.LMKXiDIkX8pMfc83MK0qfhEq1JY'
#create bot
client = commands.Bot( command_prefix = ".")
#startup information
@client.event
async def on_ready():
    print("connected to bot: {}".format(client.user.name))
    print("bot ID: {}".format(client.user.id))
#chiamare una funzione da discord
@client.command()
async def ei(ctx):
    await ctx.send("HELLO :)")

@client.command()
async def basato(ctx):
    await ctx.send('''Basato? basato su cosa? sul tuo cazzo? per favore chiudi quella cazzo di bocca e usa parole propriamente dette, troglodita; pensi che Dio ci abbia dato la libertà di parola per sputare parole che non hanno significato e non correlate all'argomento della conversazione? Cioè, per favore, ti lamenti sempre che nessuno ti parli o esprima le sue opinioni su di te perché stai sempre a sputare stronzate come "basato", "cringe", "poggers" e quando qualcuno prova a chiederti cosa significhi rispondi che fa semplicemente ridere? che cazzo. Cosa cazzo ci trovi di divertente? Pensi che diventerai uno stand-up comedian ed otterrai una standing ovation solo perché hai detto "sborra" sul palco? CAZZO NO FOTTUTO IDIOTA, fammi il piacere e chiudi quella cazzo di bocca, usa parole reali.''')

@client.command()
async def taiwan(ctx):
    await ctx.send('''ATTENTION CITIZEN! 市民请注意!

⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿
⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻
⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄

ATTENTION CITIZEN! 市民请注意!

This is the Ministry of State Security. 您的浏览记录和活动引起了我们的注意 YOUR INTERNET ACTIVITY HAS ATTRACTED OUR ATTENTION. 同志們注意了 you have been found protesting in the subreddit!!!!! 這是通知你，你必須認同我們將接管台灣 serious crime 以及世界其他地方 100 social credits have been deducted from your account 這對我們未來的所有下屬來說都是重要的機會 stop the protest immediately 立即加入我們的宣傳活動，提前獲得救贖 do not do this again! 不要再这样做! if you do not hesitate, more social credits ( -11115 social credits )will be subtracted from your profile, resulting in the subtraction of ration supplies. (由人民供应部重新分配 ccp) you'll also be sent into a re-education camp in the xinjiang uyghur autonomous zone.

为党争光! Glory to the CCP!




    ''')



#run the bot
client.run(token)