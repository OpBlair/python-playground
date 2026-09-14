import os
import sys
import json

try:
    import yt_dlp
except ImportError:
    print("Error: 'yt-dlp' library is not installed.")
    print("Please run: pip install yt-dlp")
    sys.exit(1)

def download_youtube_video(video_url, output_path="."):
    # Automatically create the folder if it doesn't exist
    if output_path != ".":
        os.makedirs(output_path, exist_ok=True)
        print(f"[Info] Target directory ready: ./{output_path}/")
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')
            
            print(f"[+] Found: {video_title}")
            print("Downloading now...")
            
            ydl.download([video_url])
            print("Download completed successfully!")
            
    except Exception as e:
        print(f"\n[!] An error occurred with URL {video_url}: {e}")

def batch_download_from_json(json_filepath):
    if not os.path.exists(json_filepath):
        print(f"Error: The file '{json_filepath}' was not found.")
        return

    output_folder = input("Enter output folder name for batch [default: downloads]: ").strip()
    if not output_folder:
        output_folder = "downloads"

    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if isinstance(data, list):
            urls = data
        elif isinstance(data, dict):
            urls = data.get('urls') or data.get('links')
            if not urls:
                for val in data.values():
                    if isinstance(val, list):
                        urls = val
                        break
        else:
            urls = None

        if not urls or not isinstance(urls, list):
            print("Error: Invalid JSON format. Expected a JSON list of URLs or an object containing a list.")
            return

        unique_urls = list(dict.fromkeys(urls))
        print(f"\nTotal unique videos to download: {len(unique_urls)}\n")
        
        for idx, url in enumerate(unique_urls, 1):
            print(f"--- Processing Video {idx} of {len(unique_urls)} ---")
            download_youtube_video(url, output_folder)
            
        print("\n" + "=" * 45)
        print("All batch downloads finished!")
        print("=" * 45)

    except json.JSONDecodeError:
        print(f"Error: '{json_filepath}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("=" * 45)
    print("YouTube Video Downloader")
    print("=" * 45)
    print("1. Download a single video URL")
    print("2. Batch download from a JSON file")
    
    choice = input("\nSelect an option (1 or 2): ").strip()
    
    if choice == "1":
        url = input("Enter the YouTube video URL: ").strip()
        if not url:
            print("URL cannot be empty.")
        else:
            folder = input("Enter output folder name [default: current directory]: ").strip() or "."
            download_youtube_video(url, folder)
            
    elif choice == "2":
        json_file = input("Enter the JSON file path (e.g., urls.json): ").strip()
        if not json_file:
            print("File path cannot be empty.")
        else:
            batch_download_from_json(json_file)
    else:
        print("Invalid choice. Please run the script again and select 1 or 2.")
