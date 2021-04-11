import discord
import asyncio
import random
import re

def apply_regex(inputstr: str, replacements: list) -> str:

    result = inputstr

    for (prev, new) in replacements:
        result = re.sub(prev, new, result)

    return result


def format_response(sentence: str) -> str:

    basic_replacements = [('^porque ', '')]

    # apply basic transformations to the input string
    simplified = apply_regex(sentence, basic_replacements)

    verb_replacements = [('soy', 'eres'),
                         ('tengo', 'tienes'),
                         ('se', 'sabes'),
                         ('estoy', 'estas'),
                         ('hablo', 'hablas'),
                         ('busco', 'buscas'),
                         ('hago', 'haces'),
                         ('me', 'te'),
                         ('llamo', 'llamas')]

    # check for some special cases
    if simplified == 'si':
        return 'piensas que \"si\". Yo creo que es \"no\"'

    if simplified == 'no':
        return 'piensas que \"no\". Yo creo que es \"si\"'

    # repalce verb tense
    verb_replaced = apply_regex(simplified, verb_replacements)

    # No verb has been found, return quoted response
    if verb_replaced == simplified:
        return 'dices \"' + simplified + '\"'

    # otherwise return version with replaced verb
    return 'crees que ' + verb_replaced


def doctor(problem: str):

    print(problem)

    responses = ['Hmm, interesante. Porque',
                 'Entiendo. Pero entonces como es que',
                 'Obvio. Porque exactamente',
                 'Otro paciente mio tuvo un problema similar. Porque exactamente',
                 'Uff, un problema duro. Porque',
                 'No se que decir... Porque',
                 'Me estoy cansando, tienes que responder mi pregunta! Porque',
                 'Okey... pero _porque_']

    eastereggs = [('.*(romeu|cer0|jorge)', 'Conozes a Romeu? Ese tio es legendario! Me enseño todo lo que sé. Volviendo al tema...'),
                  ('hola mundo', 'Ha! mis primeras mis primeras palabras eran: "Hello World" que casualidad. Volviendo al tema...'),
                  ('.*(gonzalo|gon|gogord|gorgonzola|barrero)', 'Conozes a Gonzalo? Era un paciente mio... Tenia un problema muy serio, estaba enamorado de una francesa... Volviendo al tema... '),
                  ('.*(molt|torque|javier)', 'Conozes a Javier? Era un paciente mio... Tenia muchos problemas... Se pensaba que era torquemada... Volviendo al tema... '),
                  ('.*municio', '𝅘𝅥𝅮 Muni Muni Muni 𝅘𝅥𝅮 Perdón, me estoy distrayendo...'),
                  ('.*(miguel|wasos|quij)', 'Ah hola Miguel. Te apetece una partida de ajedrez? https://www.chess.com/play/computer'),
                  ('.*(nacho|royo)', '_play The Weekend'),
                  ('comunista', 'Comunista tu! Volviendo al tema...'),
                  ('.*(robot|bot|maquina|máquina)', 'Robot? Que robot? Volviendo al tema...'),
                  ('ajedrez', 'Seguro? tengo un ranking muy bueno. Volviendo al tema...'),
                  ('.*jaj', 'JAJAJAJAJ volviendo al tema...'),
                  ('.*(vienna|budapest)', 'Que dize este tio? Volviendo al tema...'),
                  ('.*(tonto|idiota|bobo|muere|inutil|inútil|:middle_finger)', 'Nos calmamos? Volviendo al tema...')]

    if (re.match('.*jaj', problem)):
        return 'JAJAJAJAJ'

    if (re.match('.*guapo', problem)):
        return 'No hay nadie mas guapo que mi creador'


    prefix = ''

    for (pattern, easteregg) in eastereggs:
        if re.match(pattern, problem):
            prefix = easteregg;

    return prefix + ' ' + random.choice(responses) + ' ' + format_response(problem) + '?'


# link: https://discord.com/api/oauth2/authorize?client_id=825967247637610497&scope=bot&permissions=8

# ids of everybody
u_romeu = 586145916671492096
u_wasos = 687757195441471500
u_gonzl = 356404830429773824
u_molto = 688069027217801323
u_muni = 687274895020785697
u_japele = 688844653214433350
u_nacho = 688069409180221515
u_sacris = 753701487858811041

c_music = 696094910453121024
c_mc = 693830686595088435
c_general = 687754202683932694
c_doctor = 827802982271680583
c_private = 825970215841038396
c_say = 827927829462253620

bot = discord.Client()

@bot.event
async def on_message(msg):

    # Bot doenst respond to itself
    if msg.author == bot.user:
        return
    if msg.author.bot: return

    if msg.channel.id == c_say:
        await bot.get_channel(c_doctor).send(msg.content)

    # psycologist channel we are in chann
    if msg.channel.id == c_doctor or msg.channel.id == c_private:
        await msg.channel.send(doctor(msg.content.lower()))


bot.run('ODI1OTY3MjQ3NjM3NjEwNDk3.YGFn8Q.Hri-L7lwWQjZCgOBx0y-M0p5wI4')
