from flask import Flask, render_template, request
from pytube import YouTube
import re
import os

app = Flask(__name__)

def download_video(video_link, download_path):
    yt = YouTube(video_link)
    ys = yt.streams.get_highest_resolution()
    valid_title = re.sub(r'[<>:"/\\|?*]', '_', yt.title)
    video_path = os.path.join(download_path, f'{valid_title}.mp4')
    ys.download(video_path)
    return valid_title

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form['video_link']
        download_path = request.form['download_path']

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        title = download_video(video_link, download_path)
        return f'Download concluído: {title}.mp4'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
