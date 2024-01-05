import os
from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto, InputMediaVideo
from pyleaves import Leaves

api_id = 26262506
api_hash = "591d4da0c263183c34b6352b119188bf"
client = Client("Testy", api_id, api_hash)
tempVideoPath = 'D:/VSCode/TGbot/VideoFormater/downloads/tempVideo.mp4'
tempThumbnailPath = 'D:/VSCode/TGbot/VideoFormater/downloads/tempVideo.mp4.jpg'
cmd = 'VideoThumbnailsMaker.exe "../downloads/tempVideo.mp4" /silent'


def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

def makeThumbnail(Client, message: Message, video_id, chat_id):
        client.send_message(chat_id , text="Making Thumbnail ...")
        os.system(cmd)
        photo = client.send_photo(chat_id, tempThumbnailPath, caption="Video name\n\n#tegs")
        client.send_video(chat_id, video_id, reply_to_message_id=photo.id)
    
@client.on_message(filters=filters.video)
def download_video(client: Client, message: Message):
    chat_id = message.from_user.id
    video_id = message.video.file_id
    sucsess = client.download_media(message, file_name = tempVideoPath, progress=progress)
    if sucsess:
        client.send_message(chat_id , text="Video downloaded")
        makeThumbnail(client, message, video_id, chat_id)
    else: 
        client.send_message(chat_id , text="Download failed")

@client.on_message(filters=not filters.video)
def dd(client: Client, message: Message):
    chat_id = message.from_user.id
    client.send_message(chat_id=chat_id , text="Ass")



client.run()