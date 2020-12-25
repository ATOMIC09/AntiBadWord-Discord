import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', description="พูดมากว่ะ", intents=intents)
bot.remove_command('help')
		

@bot.listen()
async def on_message(message):
	if "fuck" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "fk" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	if "fuk" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "bitch" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "motherfucker" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "asshole" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "shit" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "cunt" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "ass" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "bastard" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "arsehole" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "crap" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "pussy" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "dickhead" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "kuy" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "kuay" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "sas" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "ควย" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "สัส" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "ฟัก" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "ฟัค" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "พ่อง" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "ไอ้" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	elif "แม่ง" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()

	if "ห่า" in message.content.lower():
		w = discord.Embed(title = "⚠️**ตรวจพบคำหยาบ**⚠️", color = 0xFF0000)
		w.add_field(name="⛔ ไม่ใช้คำหยาบนะ",value="🚫 Don't use rude words")
		if message.author.id == bot.user.id:
			return
		else:
			await message.channel.send(embed = w)
			await message.delete()


# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Anti-Badword Activated"))
	print('Activated')

Token = os.environ["AntiBadWordToken"]
bot.run(Token)
