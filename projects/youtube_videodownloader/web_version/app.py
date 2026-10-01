import os
import sys

try:
    import yt_dlp
except ImportError:
    print("Error: 'yt-dlp' library is not installed")
    print("Please run pip install yt-dlp flask")
    sys.exit(1)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download_route():
    data = request.json
    video_url = data.get("url")
    output_path = data.get("output_path", "downloads").strip()

    if not output_path:
        output_path = "downloads"

    success, message = download_youtube_video(video_url, output_path)

    if success:
        return jsonify({"status": "success", "message": message})
    else:
        return jsonify({"status": "error", "message": message}), 500

def download_youtube_video(video_url, output_path="."):
    if output_path != ".":
        os.makedirs(output_path, exist_ok=True)
        print(f"Target directory ready: ./{output_path}")

    yt_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')

            print(f"Found: {video_title}")
            print("Downloading now...")

            ydl.download([video_url])
            return True, f"Successfully downloaded: {video_title}"

    except Exception as e:
        error_msg = str(e)
        print(f"\nAn error occurred with URL {video_url}: {error_msg}")
        return False, error_msg

if __name__ == "__main__":
    print("Starting Web Server at http://127.0.0.1:5000 ...")
    app.run(debug=True, port=5000)