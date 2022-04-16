#imports
import random
import lightbulb
#from ast import Pass just imported idk wtf this is
import hikari as h

#getting token of bot and assigning shit to bot
bot = lightbulb.BotApp(
    token='OTMzNjc3NDQ3NDI4MzI5NDky.YelA4g.PbSVzi0w-mIdHLFfTBiCgCsnD5s',
    default_enabled_guilds=(895148548587393045, 820892867199369236, 892624305471516693,867283568522035210))

#events
@bot.listen(event_type=h.GuildMessageCreateEvent) #event type is a parameter
async def hello(event):
    if event.content == 'Hello':
        pass

#sends msg in cmd when the bot starts
@bot.listen(h.StartedEvent)
async def startup(event):
    print('Bot has started')


#slash commands

@bot.command()
#@thing.command(name, description (other things too but not needed here))
@lightbulb.command('ping','Says Pong')
@lightbulb.implements(lightbulb.SlashCommand)#slash commands :o an upgrade
async def ping(ctx):
    await ctx.respond(f'pong')

@bot.command()
@lightbulb.command('description','Gives the Bot\'s description')
@lightbulb.implements(lightbulb.SlashCommand)
async def desc(ctx):
    await ctx.respond(f'I am Judge\'sBotv2.0. I am a bit of an improvement from Judge\'sBot cuz i have slash commands :cool:. Many more commands will be added to me in the future. P.S. its all slash commands no prefixes')

@bot.command()
@lightbulb.option('text','What you wanna say' )
@lightbulb.command('say','Get the bot to say something')
@lightbulb.implements(lightbulb.SlashCommand)
async def say(ctx):
    await ctx.respond(f'{ctx.options.text}')

@bot.command()
@lightbulb.option('question','A yes/no question' )
@lightbulb.command('8ball', 'Ask a yes/no question')
@lightbulb.implements(lightbulb.SlashCommand)
async def eightball(ctx):
    replies=["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.",
             "Most likely.","Outlook good.","Yes.","Signs point to yes.","Don't count on it.","My reply is no.","My sources say no.",
             "Outlook not so good.","Very doubtful.","Absolutely no"]   
    for_shingeki=[True, False]
    
    
    #if ctx.user.users==878545660897525790:
        #if random.choice(for_shingeki)==True:
            #if ctx.questions.endswith('?'):
                #await ctx.reply(f'Question: {ctx.questions}\nAnswer: {random.choice(replies)}')
            #else:
                    #await ctx.reply(f'Question: {ctx.questions}?\nAnswer: {random.choice(replies)}')
        #else:
            #await ctx.reply(f'i am fed up with ur bs stfu pls')
    #elif ctx.author.id == 768425819751055381:
        #await ctx.respond('Why are you here? Timilai no answer.')
    #else:
    if ctx.options.question.endswith('?'):
        await ctx.respond(f'Question: {ctx.options.question}\nAnswer: {random.choice(replies)}')
    else:
        await ctx.respond(f'Question: {ctx.options.question}?\nAnswer: {random.choice(replies)}')


@bot.command
@lightbulb.command('test', 'test for a command')
@lightbulb.implements(lightbulb.SlashCommand)
async def test(ctx):
    await ctx.respond('I think the test worked')

@bot.command
@lightbulb.command('laugh', 'Sends a random laughing gif', aliases=['laugh', 'lol','lmao'])
@lightbulb.implements(lightbulb.SlashCommand)
async def laugh(ctx):
    gifs = ['https://media.discordapp.net/attachments/892624305911898113/909658889115549786/HAHAHAHAHA_LMAO.jpg','https://tenor.com/view/lol-laughing-hysterically-laughing-out-loud-funny-steve-carell-gif-22904325','https://tenor.com/view/ravil27-gif-20704161','https://tenor.com/view/john-jonah-jameson-lol-laughing-hysterically-laughing-out-loud-funny-gif-17710543','https://tenor.com/view/laugh-jerry-tom-and-jerry-mouse-lol-gif-17060825']
    await ctx.respond(f'{random.choice(gifs)}')

@bot.command
@lightbulb.command('cry', 'Sends a random crying gif', aliases=['cry','sad','sed'])
@lightbulb.implements(lightbulb.SlashCommand)
async def cry(ctx):
    gifs = ['https://tenor.com/view/dramatic-cry-will-ferrell-gif-13298637','https://tenor.com/view/sad-cry-crying-tears-broken-gif-15062040','https://tenor.com/view/tom-y-jerry-tom-and-jerry-meme-sad-cry-gif-18054267','https://tenor.com/view/the-office-crying-michael-scott-sad-upset-gif-9816214']
    await ctx.respond(f'{random.choice(gifs)}')
#group comman
#@bot.command()
#@lightbulb.command()

@bot.command
@lightbulb.option('text', 'Text to be made sarcastic')
@lightbulb.command('sarcastic', 'Sends the same message in a sarcastic way')
@lightbulb.implements(lightbulb.SlashCommand)
async def sarcasm(ctx):
    text = str(ctx.options.text)
    yn = [True, False]
    msg = ''
    for letter in text:
        if random.choice(yn) == True:
            
            msg =  msg + letter.upper()
        
        else: 
            msg = msg + letter.lower()
        
    await ctx.respond(msg)
#help

#@bot.command
#@lightbulb.command('help','Shows the list of available commands')
#@lightbulb.implements(lightbulb.SlashCommand)
#async def _help(ctx):
#    await ctx.respond(
#'''`These are the available commands
#1. ping - sends pong
#2. description - description of the bot
#3. 8ball - answers to a yes or no question
#4. laugh - sends a random laughing gif
#5. cry - sends a random crying gif
#6. help - this`''')

#poke2
@bot.command
@lightbulb.option('text','Text we will use')
@lightbulb.command('poke2','Play poke2 for this')
@lightbulb.implements(lightbulb.SlashCommand)
async def poke2(ctx):
    await ctx.respond(f'p!{ctx.options.text}')


#running the bot
bot.run()
