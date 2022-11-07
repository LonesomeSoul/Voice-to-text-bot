#!/usr/bin/env python
# coding: utf-8

# In[1]:


import whisper
import torch


# In[2]:


import config
import telebot
import requests,pandas as pd
import os


# In[3]:


#model=whisper.load_model("base")
model=whisper.load_model("small")


# In[6]:


torch.save(model,"small_model.pth")
del(model)
torch.cuda.empty_cache()


# In[ ]:


bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Сюда можно пересылать голосовые сообщения и аудио-файлы, чтобы получить их расшифровку")

@bot.message_handler(content_types=['audio',"voice"])
def handle_docs_audio(message):
    model=torch.load("small_model.pth")
    #bot.send_message(message.chat.id,"audio, cool")
    #print(message.document.mime_type )
    if (message.audio!=None):
        file_info = bot.get_file(message.audio.file_id)
    if (message.voice!=None):
        file_info = bot.get_file(message.voice.file_id)#.audio.file_id
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(config.token, file_info.file_path))
    with open('Audio_tmp.mp3', 'wb') as f:
        f.write(file.content)
    f.close()
    #print('https://api.telegram.org/file/bot{0}/{1}'.format(config.token, file_info.file_path))
    model_out=model.transcribe('Audio_tmp.mp3')
    del(model)
    torch.cuda.empty_cache()
    os.remove('Audio_tmp.mp3')
    bot.send_message(message.chat.id,model_out["text"])
    pass



bot.infinity_polling()

