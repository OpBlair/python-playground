import os
import sys

try:
    import yt_dlp
except ImportError:
    print("Error: 'yt-dlp' library is not installed.")
    print("Please run: pip install yt-dlp")
    sys.exit(1)

def download_youtube_video(video_url, output_path="."):
    print("Fetching video information... Please wait...")

    # Configuration options for yt-dlp
    ydl_opts = {
        # 'bestvideo+bestaudio/best' merges highest quality video and audio.
        # Note: Requires FFmpeg installed on your system for merging.
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info to print the title before downloading
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')
            
            print(f"Found: {video_title}")
            print("Downloading now...")
            
            # Start the actual download
            ydl.download([video_url])
            
        print("\nDownload completed successfully!")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("=" * 45)
    print("YouTube Video Downloader")
    print("=" * 45)
    
    url = input("Enter the YouTube video URL: ").strip()
    
    if not url:
        print("URL cannot be empty.")
    else:
        # Downloads to the current working directory by default
        download_youtube_video(url)
