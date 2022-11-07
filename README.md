# Voice-to-text-bot
Telegram bot for transcribing audio messages to text  @voice_handler_bot

Setting up the environment:
1) pip install git+https://github.com/openai/whisper.git 
2) pip install -r requirements.txt
3) install PyTorch with CUDA available: https://pytorch.org/
4) Open config.py and paste your bot token in brackets
5) Also i had an issue with openAI's code and in order to fix it you have to put executable file from ffmpeg library in the folder. (download https://drive.google.com/file/d/1yIDW3u6O7HdjDPq7Z_q62_pZMgC8jdeI/view?usp=sharing and put it in the folder)
6) Run voice_bot.py
