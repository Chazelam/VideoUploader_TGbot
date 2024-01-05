import os
from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 26262506
api_hash = "591d4da0c263183c34b6352b119188bf"
client = Client("Testy", api_id, api_hash)
downloadPath = 'D:/VSCode/TGbot/VideoFormater/downloads/'

def progress(current, total):
    print(f"{current * 100 / total:.1f}%")


def makeThumbnail(Client, message: Message, video, chat_id, Video_type = "tempVideo.mp4"):
        client.send_message(chat_id , text="Making Thumbnail ...")
        os.system(f'VideoThumbnailsMaker.exe "../downloads/{Video_type}" /silent')
        photo = client.send_photo(chat_id, f"{downloadPath}{Video_type}.jpg", caption="Video name\n\n#tegs")
        client.send_video(chat_id, video, reply_to_message_id=photo.id)

# ./VideoThumbnailsMaker.exe "../downloads/tempVideo.mp4" /silent
# ./VideoThumbnailsMaker.exe "../downloads/handpicked/{Video_name}.mp4" /silent


@client.on_message(filters=filters.video)
def download_video_TG(client: Client, message: Message):
    chat_id = message.from_user.id
    video_id = message.video.file_id
    sucsess = client.download_media(message, file_name = downloadPath + "tempVideo.mp4", progress=progress)
    if sucsess:
        client.send_message(chat_id , text="Video downloaded")
        makeThumbnail(client, message, video_id, chat_id)
    else: 
        client.send_message(chat_id , text="Download failed")


@client.on_message(filters=filters.text)
def download_video_PH(client: Client, message: Message):
    chat_id = message.from_user.id
    Video_URL = message.web_page.url
    Video_name = message.web_page.title
    Video_path = downloadPath + "handpicked/" + Video_name + ".mp4" 

    os.system(f'python phdler.py custom {Video_URL}')
    client.send_message(chat_id , text="Video downloaded")
    
    makeThumbnail(client, message, Video_path, chat_id, "handpicked/" + Video_name + ".mp4")


client.run()