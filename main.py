import yt_dlp
import os

# Function to download a YouTube video or playlist
def download_youtube_video(video_url, download_path='.', quality='best', audio_only=False):
    try:
        # Ensure the download path exists
        os.makedirs(download_path, exist_ok=True)

        # Options for download
        ydl_opts = {
            'format': quality,  # Specify quality
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save path and filename template
            'noplaylist': False if 'list=' in video_url else True,  # Handle playlists appropriately
            'ignoreerrors': True,  # Skip errors in playlist
            'quiet': False,  # Show info (but not too verbose)
            'no_warnings': False,  # Show warnings
        }

        # If audio_only is True, download only the video's audio
        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        # Use yt-dlp to download the video or playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)  # Extract info first to check if it's a playlist
            if 'entries' in info:  # It's a playlist
                print(f"Downloading playlist: {info['title']} ({len(info['entries'])} videos)")
                ydl.download([video_url])
            else:  # It's a single video
                print(f"Downloading video: {info['title']}")
                ydl.download([video_url])
            print("Download completed (skipped any errors).")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=uI69hppld40&list=PLPp3tv5LbPLFgeYZ4yCfivwmiI6U80dqD'  # Playlist URL
download_path = 'F:/fcai/others/Youtube-Downloader-Sayed-Sharrat/playlist_classic'  # Change this to your desired download path
quality = 'bestvideo+bestaudio'  # Adjust quality, e.g., 'best', 'worst', '720p', etc.
audio_only = True  # Set to True for audio-only download
download_youtube_video(video_url, download_path, quality, audio_only)