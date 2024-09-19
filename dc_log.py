
import discord
from discord.ext import commands
import os
import sqlite3
from datetime import datetime
now = datetime.now()

token = 'TOKEN'

intents = discord.Intents.default()

intents.message_content = True
client = discord.Client(intents=intents)

def db_stuff(dt_string,paket, autor, channel,server_name):
    dayntime= dt_string.split()
    
    time = str(dayntime[1])
    print(time)
    lists =[(str(dayntime[0]),time,server_name,channel,autor,paket)]
    print(lists)
    connection= sqlite3.connect("~/Dokumente/messages.db")
    corsor= connection.cursor() 
    corsor.execute("CREATE TABLE IF NOT EXISTS messages (date TEXT, time TEXT, server_name TEXT, channel TEXT,  user TEXT, message TEXT)")

    corsor.executemany("insert into messages values (?,?,?,?,?,?)",lists)
    
    connection.commit()
    connection.close()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    

   
        
        server_name = str(message.guild)
        
        paket= str(message.content)
        autor= str(message.author)
        channel = str(message.channel)
        channel_id = str(message.channel.id)
        dt_string = now.strftime('%d/%m/%Y %H:%M:%S')


        parent_dir = "discord\dc_logger/server/"
        add_dir = server_name+"/"
        db_stuff(dt_string,paket, autor, channel ,server_name)
      
            
        




client.run(token)
