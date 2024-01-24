import discord
import random
import aiohttp
import asyncio
import urllib




ytapi = 'AIzaSyBmlyQwMglTm4vWsYagFxFlc3nJyuf3M_8'
TOKEN = 'NjI0OTU4NTgzOTA1MTg5ODk5.XYYkNw.aLy-wDkI9qdQgZx3tc2Uxnu6GKA'

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
#-----------------------------------------------------------calculator--------------------------------------------------------#
    id = client.get_guild(562763598930247701)
        

    if message.content.find('o$users') > -1:
        await message.channel.send('*{0}'.format(str(id.member_count)))


    



    if message.content.find("o$calculate") > -1:
        boi = message.content.split(" ")
        if len(boi) == 4:

            
            if boi[1].isnumeric():
                
                if boi[3].isnumeric():

                    calculate1 = int(boi[1])
                    calculate2 = int(boi[3])

 
                            
                    
                    if boi[2] == '+':

                        if calculate1 == 1:
                            if calculate2 == 1:
                                calculationresult = "window"
                                
                                emb = discord.Embed(title = ("here is the calculation"), description = (calculationresult), color = 0xF1D420)
                                await message.channel.send(content=None, embed=emb)


                        else:
                            calculationresult = calculate1 + calculate2


                            emb = discord.Embed(title = ("here is the calculation"), description = str(calculationresult), color = 0xF1D420)
                            await message.channel.send(content=None, embed=emb)
                    
                    elif boi[2] == '*':

                        calculationresult = calculate1 * calculate2

                        emb = discord.Embed(title = ("here is the calculation"), description = str(calculationresult), color = 0xF1D420)
                        await message.channel.send(content=None, embed=emb)

                    elif boi[2] == '/':

                        calculationresult = calculate1 / calculate2

                        emb = discord.Embed(title = ("here is the calculation"), description = str(calculationresult), color = 0xF1D420)
                        await message.channel.send(content=None, embed=emb)

                    elif boi[2] == '-':

                        calculationresult = calculate1 - calculate2

                        emb = discord.Embed(title = ("here is the calculation"), description = str(calculationresult), color = 0xF1D420)
                        await message.channel.send(content=None, embed=emb)


    if message.content.startswith('w!'):
        await message.channel.send(wikipedia.summary(message.content[2:]))


    if message.content.startswith('u!'):
        defs = ud.define(message.content[2:])

    #if message.content.startswith('U!'):
    for d in defs:
        await message.channel.send(d.definition)


#-------------------------------gamble---------------------------------------------#
    rewards = [10000,1000,500,250,150,100,50,10,1,0,0,-1,-10,-50,-100,-150,-250,-500,-1000,-10000]
        
    
    user_url = message.author.nick.replace(" ", "%20")
    
    account = 100
    url = 'https://www.hattonparkevents.co.uk/butt3rs.co.uk/gamble/api/get_balance.php?u={0}&d={1}'.format(user_url, account)
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        account = int(response)
    
    
    
    if message.content.find("o$gamble") > -1:
        # Take 10 from the current balance
        account = account - 10
        emb = discord.Embed(title = ("💸here is your account balance"), description = ("💸so it looks like you have " + str(account) + " in your account!"), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        
        # Pick a random prize
        prize = (random.choice(rewards))
        account = account + prize

        if prize == 0:
            msg = "💸{0.author.mention} Looks like you didn't win anything! That means you now have {1}".format(message, account)
        
        if prize > 0:           
            msg = "💸🤑{0.author.mention} Woah, you've won {1}! That means you now have {2}".format(message, prize, account)
        
        if prize < 0:
            msg = "💸{0.author.mention} Awww maaan, you've lost {1}! That means you now have {2}".format(message, prize, account)
        
        emb = discord.Embed(title = ("ayy boi you just gambled"), description = (msg), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)


    if message.content.find("o$account") > -1:
        emb = discord.Embed(title = ("your balance"), description = str(account), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)

    pin123 = [3567,5839,8079,3646,9895,4723,9788,5632,5689,5467,3920,7684]
    pin123ran = random.choice(pin123)
    
    ages = [15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110]
    age = random.choice(ages)

    if message.content.find("o$bank") > -1:
        embed = discord.Embed(title="welcome to the cronus bank", description="here are your details", color=0xF1D420)
        embed.add_field(name="name", value="{0.author.mention}".format(message) )
        embed.add_field(name="pin number" , value=(pin123ran))
        embed.add_field(name="age" , value=(age))
        embed.add_field(name="balance" , value=(account))
        await message.channel.send(embed = embed)     
        
    #---------------------------------------------the cronus coin thing------------------#


#-----------------------------------------chest----------------------------------------------#
#----------------------------------------weapons---------------------------------------------#

    
    if  message.content.find("o$shoot ") > -1:
        parts = message.content.split(" ")
        
        if len(parts) > 0:
            target = parts[1]
            msg = "!tempmute {0} 15 s".format(target)
            await message.channel.send(msg)

        if len(parts) > 4:
            if parts[2] == "with" or parts[2] == "using":
                msg = "😎 lol you just killed {0} using a {1} , lol a {1}, you could have picked any weapon in the world to kill {0} like a {2}, but you picked a {1} dam bro thats harsh🆒".format(target, parts[4], "machine gun")
                await message.channel.send(msg)

    if message.content.find("o$weapons") > -1:
        url = 'https://www.hattonparkevents.co.uk/butt3rs.co.uk/gamble/api/get_weapons_for_user.php?u={0.author.nick}'.format(message)
        async with aiohttp.ClientSession() as session:  
            raw_response = await session.get(url)
            response = await raw_response.text()
                
        await message.channel.send(response)



    if message.content.find("o$exchangeRate") > -1:
        embed = discord.Embed(title="The official CC to £ exchange rate", description="these are the exchange prices from CC to pounds", color=0xF1D420)
        embed.add_field(name="1CC = £0.50", value="0" )
        embed.add_field(name="100CC = £50.00" , value="0")
        embed.add_field(name="1000CC = £500.00", value="0")
        embed.add_field(name="10,000CC = £5000.00", value="0")
        embed.add_field(name="100,000CC = £50000.00", value="0")
        embed.set_footer(text="Please note that I am 15 and not in the financial position to exchange, and that CC is not a real currency")
        await message.channel.send(embed = embed)

    if message.content.find("o$help") > -1:
        embed = discord.Embed(title="Hello I am BlueOsiris a gambling and investment bot for servers like these", description="these are the commands you can use", color=0xF1D420)
        embed.add_field(name="😎shit you need to know", value="First of all, the money you earn and spend is CC (CronusCoins) which is the fake currency of the cronus server (the bots home). To keep this money we store it in a account in a database so get gambling   " )
        embed.add_field(name="😎the commands" , value="these commands all use the prefix o$")
        embed.add_field(name="😎gambling commands", value="these are all the gambling commands you can do just type o$ghelp for them.")
        embed.add_field(name="😎investment commands", value="these are all the investment commands you can do just type o!$help for them.")
        embed.add_field(name="😎general", value="these are all the general commands you can do just type o$general for them.")
        embed.add_field(name="😎profile", value="profile stuff. try o$profile")
        embed.add_field(name="😎support", value="to find out the python behind this bot or a problem go use o$support")
        await message.channel.send(embed = embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    if message.content.find("o$profile") > -1:
        embed = discord.Embed(title="welcome to your PROFILE WOW!", description="0", color=0xF1D420)
        embed.add_field(name="😎o$bank", value="find out your bank details")
        embed.add_field(name="😎o$account", value="find out how much money you have")

        await message.channel.send(embed = embed)
    
    if message.content.find("o$support") > -1:
        embed = discord.Embed(title="this bot was made by a incompetent 15 year old who wants to become a software developer when he is older so there will be problems", description="if there is a problem go to the discord server", color=0xF1D420)
        embed.add_field(name="😎discord", value="https://discord.gg/Vw58GeA")
        

        await message.channel.send(embed = embed)
    
    
    
    
    
    
    
    if message.content.find("o$ghelp") > -1:
        embed = discord.Embed(title="welcome to the Cronus Casino", description="these are the commands you can use", color=0xF1D420)
        embed.add_field(name="🤑o$gamble", value="quick money gambling")
        embed.add_field(name="🤑o$donate", value="if im generous you can have some coins")
        embed.add_field(name="🤑o$account", value="gives you your account")
        embed.add_field(name="🤑o$slots", value="slot machines")
        embed.add_field(name="🤑o$dice", value="a quick dice game")
        await message.channel.send(embed = embed)
    
    if message.content.find("o$ihelp") > -1:
        embed = discord.Embed(title="welcome to the Cronus investment app", description="these are the commands you can use to invest your money", color=0xF1D420)
        embed.add_field(name="😎o$inv_ezcoin", value="this is a crypto currency well known for its simplicity to use")
        embed.add_field(name="😎o$inv_business", value="this will open the business command which will give you help when investing in businesses")
        embed.add_field(name="😎o$inv_youtube", value="use this to promote your business on youtube")
        embed.add_field(name="😎o$inv_instagram", value="use this to promote your business with influencers")
        await message.channel.send(embed = embed)

    if message.content.find("o$general") > -1:
        embed = discord.Embed(title="general stuff if you really want it (i didnt make half of these lol)", description="here are the general commands", color=0xF1D420)
        embed.add_field(name="😎o$hello", value="0")
        embed.add_field(name="😎o$stfuboomer", value="0")
        embed.add_field(name="😎o$oohtellem", value="0")
        embed.add_field(name="😎o$hug", value="0")
        embed.add_field(name="😎o$fuck", value="0")
        embed.add_field(name="😎o$gday", value="0")
        
        await message.channel.send(embed = embed)


    





        await message.channel.send(embed = embed)

    if message.content.find("o$attack") > -1:
        parts = message.content.split(" ")


        if len(parts) > 0:
            target = parts[1]
            msg = "{0} you are being attacked".format(target)
            await message.channel.send(msg)
                
            if len(parts) > 4:

                if parts[2] == "with" or parts[2] == "using":

                    weapon = parts[4]
                    

                    if len(weapon) > 0:
                        url = 'https://www.hattonparkevents.co.uk/butt3rs.co.uk/gamble/api/get_weapons_for_user.php?u={0.author.nick}&w=weapon_name'.format(message)
                        async with aiohttp.ClientSession() as session:  
                            raw_response = await session.get(url)
                            response = await raw_response.text()
                        
                        if response == ("You currently have no weapons in your arsenal"):
                            await message.channel.send("{0.author.mention} you dont have a {1} to attack {2}".format(message, weapon, target))
                        else:
                            await message.channel.send("{0.author.mention} you have something in your arsenal")
                            

                            response_parts = response.split(",")
                            if len(response_parts) == 3:

                                if response_parts[2] == weapon:
                                    await message.channel.send("{0.author.mention} you have a {1} so you can kick {2} ass with that {1}".format(message, weapon, target))
                                else:
                                    await message.channel.send("{0.author.mention} you seem to not have a {1} so you can't attack {2} shame they are such a cuck smh".format(message, weapon, target))
                                    
#----------------------------------------------------------------------------------------------------general--------------------------------------------------------------------------------------------------------#
    if message.content.find("o$hello") > -1:
        emb = discord.Embed(title = ("hello "), description = ("its nice to meet you😎"), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)

    if message.content.find("o$stfuboomer") > -1:
        emb = discord.Embed(title = ("😎what the fuck did you just say to me you little bitch"), description = (" I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands.😎"), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)  

    if message.content.find("o$oohtellem") > -1:
        emb = discord.Embed(title = ("😎oi mate😎"), description = (" 😎your irrelevent, stupid, dumb ,fucked up , shit looking ass better run the fuck away before you get a try of {0.author.mention} fuckin fist you little wet dumb ass😎".format(message)), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb) 

    if message.content.find("o$hug") > -1:
        msg = ("😎OH MY GOD {0.author.mention} IS TRYING TO RAPE MEEE!!!!! SOMEONE FUCKING HELP! 😎").format(message)
        await message.channel.send (msg)

    if message.content.find("o$fuck") > -1:
        msg = ("{0.author.mention} NO JUST FUCKING NO DON'T EVEN THINK ABOUT IT").format(message)
        await message.channel.send (msg)

    if message.content.find("o$hello") > -1:
        msg = ("😎{0.author.mention} HELLO! if you want to gamble do o!gamble😎").format(message)
        await message.channel.send (msg)

    if message.content.find("o$gday") > -1:
        msg = ("😎{0.author.mention} Gday mate if you want to gamble do o!gamble😎").format(message)
        await message.channel.send (msg)  
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#        
        
    ezcoinoutput = [100,250,1000,1550,2000,5000,10000,50000,100,250,1000,1000,250]
    ezcoinran = random.choice(ezcoinoutput)

    
    
    if message.content.find("o$inv_ezcoin") > -1:
        emb = discord.Embed(title = ("you have invested 1000cc into ez coin💲"), description = ("you have now transferred it back💲"), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        account = account -1000
        emb = discord.Embed(title = ("ez coin to cc"), description = ("you have now got back 💲{0}".format(ezcoinran)), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        account = account + ezcoinran

    outputyoutube1 = ("uh oh you picked pewdiepie and now the media thinks your a nazi - 10,000 in sales")
    outputyoutube2 = ("you sponsored logan pauls japan forest video im sure that will go down with the press - 100,000 in fines")
    outputyoutube3 = ("you sponsored a mental health video and have been noticed by the community + 10,000 well done")
    outputyoutube4 = ("you put some money in mr Beasts video fund dam people really like you now  + 10,000 in sales")
    outputyoutube5 = ("you sponsored the logan paul vs ksi fight dam that made millions + 10,000 boi")
    outputyoutube6 = ("you sponsored its every day bro by jake paul here take the views + 1000")

    youtube123 = [outputyoutube1,outputyoutube2,outputyoutube3,outputyoutube4,outputyoutube5,outputyoutube6]
    youtubechoice = random.choice(youtube123)
    
    
    if message.content.find("o$inv_youtube") > -1:
        emb = discord.Embed(title = ("💲you have paid a youtuber to do a promotion💲"), description = (youtubechoice), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        if youtubechoice == outputyoutube1:
            account = account - 10000
        elif youtubechoice == outputyoutube2:
            account = account - 100000
        elif youtubechoice == outputyoutube3:
            account = account + 10000
        elif youtubechoice == outputyoutube4:
            account = account + 10000
        elif youtubechoice == outputyoutube5:
            account = account + 10000
        elif youtubechoice == outputyoutube6:
            account = account - 100000

    business12 = ["A+J games","razor","peelseries","quinoa & co","Fl1 digital","hipsley green","Nskidia","AM🅱️","microloft","pear","lamborgene","astra","space x_69_x",".turtle development","we🅱️🅱️ois" ]
    businesspoopoo = random.choice(business12)
    monybus = [1000,5000,10000,1000,3000,4000,5000,6000,100000,1000,1000,1000,0,0,0,0,]
    monybusran = random.choice(monybus)
    msg234 = ("you have invested 5000 in {0}".format(businesspoopoo))
    msg567 = ("hello {0.author.mention} due to your investment in {1} you have made {2} in profit".format(message, businesspoopoo , monybusran))
    
    if message.content.find("o$inv_business") > -1:
        account = account - 5000
        emb = discord.Embed(title = ("💲the cronus investment app💲"), description = (msg234), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        emb = discord.Embed(title = ("💲the cronus investment app💲"), description = (msg567), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        account = account + monybusran

    smallnumbers = [10,20,30,40,50,60,70,80,90,0,0,0,0,0,0,0,0]
    smallnumbersran =  random.choice(smallnumbers)

    if message.content.find("o$inv_instagram") > -1:
        emb = discord.Embed(title = ("💷you promted yourself in a influencers comment section you saddo💷"), description = ("💷you got {0} outta it💷".format(smallnumbersran)), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        account = account + smallnumbers
         


                
                        








        
        


            
#----------------------------------------other shit----------------------------------------#

    
    
    
    a = ["pineapple","pear","apple","strawberry"]
    aa = random.choice(a)
    b = ["pineapple","pear","apple","strawberry"]
    bb = random.choice(b)
    c = ["pineapple","pear","apple","strawberry"]
    cc = random.choice(c)
    
    output1f = ("💸the results are in {0.author.mention} {1} , {2} , {3} 💸".format(message, aa , bb , cc))
    output2f = ("{0.author.mention} jack pot".format(message))
    output3f = ("{0.author.mention} you got two the same".format(message))
    output4f = ("{0.author.mention} you lost everything".format(message))
    
    if message.content.find("o$slots") > -1:
        emb = discord.Embed(title = ("here are the slot machines"), description = ("💸o$fruity finances , o$gold rush, o$Senpai Slots  💸"), color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
                
    if message.content.find("o$fruity finances") > -1:
        emb = discord.Embed(title = "💸your gamble💸", description = output1f, color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)
        

        if aa == bb and bb == cc: 
            emb = discord.Embed(title = "💸your gamble💸", description = output2f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account * 2 

        elif aa == bb and bb != cc:
            emb = discord.Embed(title = "💸your gamble💸", description = output3f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account + 1000

        elif aa != bb and bb == cc:
            emb = discord.Embed(title = "💸your gamble💸", description = output3f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account + 1000    
        else:
            emb = discord.Embed(title = "💸your gamble💸", description = output4f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account / 2
                
                
                

    


    r1 = ["hat","gun","machete","boots","gold"]
    r1r = random.choice(r1)
    r2r = random.choice(r1)
    r3r = random.choice(r1)

    output1r = ("💸the results are in {0.author.mention} {1} , {2} , {3} 💸".format(message, r1r , r2r , r3r))
                
    if message.content.find("o$gold rush") > -1:
        emb = discord.Embed(title = "💸your gamble💸", description = output1r, color = 0xF1D420)
        await message.channel.send(content=None, embed=emb)

        if r1r == r2r and r2r == r3r:
            emb = discord.Embed(title = "💸your gamble💸", description = output2f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account + 10000 

        elif r1r == r2r and r2r != r3r:
            emb = discord.Embed(title = "💸your gamble💸", description = output3f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account + 100

        elif r1r != r2r and r2r == r3r:
            emb = discord.Embed(title = "💸your gamble💸", description = output3f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account + 100    
        else:
            emb = discord.Embed(title = "💸your gamble💸", description = output4f, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
            account = account - 1000


    w1 = ["waifu","senpai","hentai","OwO","Hatsune Miku"]
    w1w = random.choice(w1)
    w2 = ["waifu","senpai","hentai","OwO","Hatsune Miku"]
    w2w = random.choice(w2)
    w3 = ["waifu","senpai","hentai","OwO","Hatsune Miku"]
    w3w = random.choice(w3)

    output1r = ("💸the results are in {0.author.mention} {1} , {2} , {3} 💸".format(message, w1w , w2w , w3w))
                
    if message.content.find("o$Senpai Slots") > -1:
        if account > 100000:
            emb = discord.Embed(title = "💸your gamble💸", description = output1r, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)

            if w1w == w2w and w2w == w3w:
                emb = discord.Embed(title = "💸your gamble💸", description = output2f, color = 0xF1D420)
                await message.channel.send(content=None, embed=emb)
                await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
                account = account + 100000 

            elif w1w == w2w and w2w != w3w:
                emb = discord.Embed(title = "💸your gamble💸", description = output3f, color = 0xF1D420)
                await message.channel.send(content=None, embed=emb)
                await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
                account = account - 100000

            elif w1w != w2w and w2w == w3w:
                emb = discord.Embed(title = "💸your gamble💸", description = output3f, color = 0xF1D420)
                await message.channel.send(content=None, embed=emb)
                await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
                account = account + 10000    
            else:
                emb = discord.Embed(title = "💸your gamble💸", description = output4f, color = 0xF1D420)
                await message.channel.send(content=None, embed=emb)
                await message.channel.send("https://tenor.com/view/fatman-jackpot-slot-machine-gif-9591567")
                account = account - 10000      
        else:   
            emb = discord.Embed(title = "😎woah there buddy😎", description = "😎you dont have vip so you cant use this slot😎", color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            
    

    





    numbers = [1,2,3,4,5,6]
    
    dicep = random.choice(numbers) 
    diceb = random.choice(numbers)    
    
    scoredice1 = ("💸{0.author.mention} you rolled {1} and blue osiris rolled {2}💸".format(message, dicep, diceb))
    
    
    if message.content.find("o$dice") > -1:
        if diceb == dicep:
            emb = discord.Embed(title = "💸the scores💸", description = scoredice1, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            emb2 = discord.Embed(title = "💸what has gone through", description = "you have won nothing💸", color = 0xF1D420)
            await message.channel.send(content=None, embed=emb2)
            emb3 = discord.Embed(title = "💸your account now💸", description = account, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb3)
        
        elif diceb < dicep:
            account = account + 10000
            emb = discord.Embed(title = "💸the scores💸", description = scoredice1, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            emb2 = discord.Embed(title = "💸what has gone through💸", description = "💸you have won 10,000 Cronus Coins💸", color = 0xF1D420)
            await message.channel.send(content=None, embed=emb2)
            emb3 = discord.Embed(title = "💸your account now💸", description = account, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb3)

        elif diceb > dicep:
            account = account - 1000
            emb = discord.Embed(title = "💸the scores💸", description = scoredice1, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb)
            emb2 = discord.Embed(title = "💸what has gone through💸", description = "💸you have lost 1000 Cronus Coins💸", color = 0xF1D420)
            await message.channel.send(content=None, embed=emb2)
            emb3 = discord.Embed(title = "💸your account now💸", description = account, color = 0xF1D420)
            await message.channel.send(content=None, embed=emb3)

#---------------------------------------------------------------------------------------------------------------------------------#













    condition = True
    
    while condition == True:

        if message.content.find("o$spamboof") > -1:
            
            await message.channel.send("a.work")


                                 

    
    

    if message.content.find("shutup") > -1:
        await message.channel.send("No u")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    url = 'https://www.hattonparkevents.co.uk/butt3rs.co.uk/gamble/api/set_balance.php?u={0.author.nick}&b={1}'.format(message, account)
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
    


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("😎Looking out for o$ 👀"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)





