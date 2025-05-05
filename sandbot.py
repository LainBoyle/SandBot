import discord
from discord.ext import commands
from session import Session
from chance import Chance


DISCORD_TOKEN = ""

bot = commands.Bot(command_prefix="!",case_insensitive=True, intents = discord.Intents.all())

mySessions = []


'''
Check if discord.member member has an active session in List<Session> mySessions
@PARAM discord.member member
@RETURN Session i, the active Session of discord.member member
'''
def checkSessions(member):
    for i in mySessions:
        if i.getUser() == member:
            return i
    return None


'''Print "Ready." to terminal on ready'''
@bot.event
async def on_ready():
    print("Ready.")
    

'''On command !hello, send message "Hello!"'''
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
    
'''On command !add x y z, send the sum of the integers'''
@bot.command()
async def add(ctx, *arr):
    result = int(arr[0])
    prefix = str(arr[0])
    arr = arr[1:]
    for i in arr:
        result += int(i)
        prefix = prefix + " + " + str(i) 
    output = prefix + " = " + str(result)
    await ctx.send(output)
    
    
'''On command !investigate, initiate an investigation Session'''
@bot.command()
async def investigate(ctx):
    i = checkSessions(ctx.author)
    if i is not None:
        i.close()
        mySessions.remove(i)
    mySession = Session(ctx.author, ctx.channel, 'Bot Test.txt')
    mySessions.append(mySession)
    curInvestigation = mySession.investigate()
    if curInvestigation is not None:
        await ctx.send(curInvestigation)
    
    
'''On command getSessionInfo, send info about any Session from the message author'''
@bot.command()
async def getSessionInfo(ctx):
    await ctx.send("Fetching session info...")
    i = checkSessions(ctx.author)
    if i is None:
        await ctx.send("No existing session from this user.")
    else:
        await ctx.send("ID: " + str(i.getID()))
        await ctx.send("User: " + str(i.getUser()))
        await ctx.send("Path: " + i.getPath())
        await ctx.send("User Vars: " + str(i.userVars))
        
    
'''On command !close, manually close the message author's investigative session'''  
@bot.command()
async def close(ctx):
    i = checkSessions(ctx.author)
    if i is not None:
        mySessions.remove(i)
        i.close()
        await ctx.send("Done.")
    else:
        await ctx.send("No open sessions from " + str(ctx.author))
        

'''On command !flip, flip a coin'''
@bot.command()
async def flip(ctx):
    await ctx.send(str(ctx.author) + ", You got " + Chance.flip())
    

'''On command !roll xdy[+/-]z'''
@bot.command()
async def roll(ctx):
    await ctx.send(Chance.parseRollCommand(ctx.content))
        
   
'''On message, check if this is a response to an active investigation, parse response and continue investigation'''     
@bot.listen()
async def on_message(message):
    
    i = checkSessions(message.author)
    
    if i is None:
        
        return
    
    elif i.awaitingInput and message.content.isnumeric():
        
            num = int(message.content)
            if len(i.options) >= num:
                
                i.addPath(i.options[num - 1])
                await message.channel.send("You chose: " + i.options[num - 1])
                i.awaitingInput = False
                investigation = i.investigate()
                
                if investigation is None:
                    
                    mySessions.remove(i)
                    i.close()
                    
                elif not i.isAwaitingInput():
                    
                    mySessions.remove(i)
                    i.close()
                    await message.channel.send(investigation)
                    
                else:
                    await message.channel.send(investigation)

            return
    

bot.run(DISCORD_TOKEN)