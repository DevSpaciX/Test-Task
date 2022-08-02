from moviepy.editor import VideoFileClip
import requests
import os
video_url = 'https://v16m-webapp.tiktokcdn-us.com/a6e3b7e6a064bc43da3a39ab93460ef8/62e921d5/video/tos/useast5/tos-useast5-ve-0068c003-tx/41b44c2a3cc840929f658665d57979d1/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1150&bt=575&cs=0&ds=3&ft=ebtHKH-qMyq8ZwkJKwe2NoTcfl7Gb&mime_type=video_mp4&qs=0&rc=aTozOTNmZmg5MzpnOzo1ZUBpM3g6OmQ6ZmhvZTMzZzczNEAwLjRiMDZhNmMxLmJfMTYzYSNqczAycjRnYmZgLS1kMS9zcw%3D%3D&l=20220802070706CBA8CD072C869B2562D9'

def download_video(url):
    try:
        response = requests.get(url=url)
        with open('TikTok-example-1.mp4','wb') as file:
            file.write(response.content)
        return 'Video downloaded successfully , converting ...'

    except Exception as ex:
        return 'oops ... Wrong Url'

def main():
    print(download_video(url=video_url))
if __name__ == '__main__':
    main()
def convert():
    clip = VideoFileClip('TikTok-example-1.mp4')
    clip.write_gif('TikTok-example-1.gif')

convert()
print(os.path.abspath('TikTok-example-1.gif'))

def delete():
    try:
        os.remove('TikTok-example-1.mp4')
    except Exception as ex:
        return
delete()
    #probably we need to remove mp4 file