import yt_dlp
import requests
import os

# Token و Chat ID
BOT_TOKEN = "7939936881:AAHbAcdWbr0Bo7n-bPndIIvxLusPgmp6cSU"
CHAT_ID = "1009363022"

def download_video(url):
    # ڤیدیۆیەک دابەزێنە ب navê "video.mp4"
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "video.mp4"

def send_video_to_telegram(video_path):
    with open(video_path, 'rb') as video_file:
        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo",
            data={'chat_id': CHAT_ID},
            files={'video': video_file}
        )
    return response.json()

if __name__ == "__main__":
    url = input("لینکی ڤیدیۆ بدە (Instagram/TikTok): ")
    print("...ڤیدیۆ دابەزێت")
    video_path = download_video(url)
    print("...ڤیدیۆ نێردرا بۆ Telegram")
    result = send_video_to_telegram(video_path)
    print("ئامادە! ئەمە هەڵسەنگاندنە:")
    print(result)

    # سڕینەوەی ڤیدیۆیەک لە هاردی ڕوونکاری
    if os.path.exists(video_path):
        os.remove(video_path)