import discord
from discord.utils import get
from datetime import datetime
import time
import threading
import asyncio

CYM_TOKEN = 'OTIyNjQzMjgzNTMwODg3MTk5.YcEchA.'+'4-l7Cui77FhhDoVH2CH0PnuNWUY'

client = discord.Client()
colour_channel_id = 922191375389294632
test_channel_id = 928724975098159115
role_channel_id = 927998572174131261
rule_channel_id = 921564126130618449

weeb_emoji = '<:weeb:928834166752182353>'
kboo_emoji = '<:just_guy_with_pink_hair:928838500047007795>'
sus_emoji = '<a:sus:928840698852151317>'

Dict = {'🌴': 'he/him', '🌿': 'she/her', '🥦': 'I/me', '🌵': 'you/you',
        '🍁': 'we/us', '🍄': 'it/its', '🌲': 'they/them', '🌳': 'other/ask',
        '🎼': 'musician', weeb_emoji: 'weeb', kboo_emoji: 'K-boo', sus_emoji:
        'I aM nOt sUs', '🚁': 'heliKopter', '🐶': 'Dog', '😼': 'Cat', '': 'gamer'}

he_him_id = '927996782439432243'
she_her_id = '927996932985589851'
i_me_id = '927995985832062976'
you_you_id = '927996762596208720'
we_us_id = '927996982612598785'
it_its_id = '928737905118175332'
they_them_id = '927997044092727366'
other_ask_id = '927996964346417152'

musician_id = '928000441680269342'
weeb_id = '928000478992805969'
gamer_id = '928000377507442688'
k_boo_id = '928001159698997329'
sus_id = '928756573554241586'
helicopter_id = '928070865894141994'
dog_id = '928756417010221066'
cat_id = '928756533372813312'


@client.event
async def on_ready():
    print('Bot is online 10:40 Feb 2 2022')
    channel = client.get_channel(role_channel_id)

    # <@&{ROLE_ID}> , format for pinging a role
    # await channel.send('Now you can express yourself on our CYM Community Server! React to give yourself the roles you like. \n\n**__REACT BELOW FOR PERSONAL PRONOUNS!__**\n\n> 🥦 <@&{0}>\n> 🌵 <@&{1}>\n> 🌴 <@&{2}>\n> 🌿 <@&{3}>\n> 🍁 <@&{4}>\n> 🌲 <@&{5}>\n> 🍄 <@&{6}>\n> 🌳 <@&{7}>'.format(i_me_id, you_you_id, he_him_id, she_her_id, we_us_id, they_them_id, it_its_id, other_ask_id))

    # await channel.send('**__REACT BELOW FOR MORE ROLES__** \n\n> 🎼 <@&{0}>\n> <:weeb:928834166752182353> <@&{1}>\n> <:just_guy_with_pink_hair:928838500047007795> <@&{2}>\n> <a:sus:928840698852151317> <@&{3}>\n> 🚁 <@&{4}>\n> 🐶 <@&{5}>\n> 😼 <@&{6}>'.format('928000441680269342', '928000478992805969', '928001159698997329', '928756573554241586', '928070865894141994', '928756417010221066', '928756533372813312'))

    # open function returns a file object you use o read text from a text file
    #note = open('D:/stuff/cym.txt', 'r')
    #rules = note.read()

    #channel_rules = client.get_channel(rule_channel_id)
    # await channel_rules.send(rules)
    # note.close()  # closes file


# Event handler for reactions from user
@client.event
# MAKE SURE THE BOT HIARCHY IS ABOVE THE ROLES
async def on_reaction_add(reaction, user):
    if(reaction.message.id == 937205061057130547 or reaction.message.id == 937205069651251211):
        emoji = str(reaction.emoji)
        role = Dict.get(emoji)
        if (role != None):
            role = discord.utils.get(user.guild.roles, name=role)
            print('Role added to')
            await user.add_roles(role)
        else:
            print('Role not defined')


client.run(CYM_TOKEN)
