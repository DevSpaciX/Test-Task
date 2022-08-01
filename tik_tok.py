from moviepy.editor import VideoFileClip
import requests
import os
video_url = 'https://samplelib.com/lib/preview/mp4/sample-5s.mp4'
#Your video url unfourchantly don`t working
# https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55

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

clip = VideoFileClip('TikTok-example-1.mp4')
clip.write_gif('TikTok-example-1.gif')
print(os.path.abspath('TikTok-example-1.gif'))

#probably we need to remove mp4 file