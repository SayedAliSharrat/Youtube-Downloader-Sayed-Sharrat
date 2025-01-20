# Youtube Downloader - Sayed Sharrat

## Overview
This script allows you to download videos or playlists from YouTube with customizable options for quality and format. Before you can use the script, ensure you have the required tools and libraries installed.

---

## Prerequisites

### 1. Install Python
Ensure you have Python installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/).

### 2. Install Required Libraries
After installing Python, install the required libraries by running the following command in the project directory:
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg Binary
FFmpeg is needed for processing video and audio. Follow these steps to install FFmpeg:

1. Visit the official FFmpeg download page: [https://ffmpeg.org/download.html#build-windows](https://ffmpeg.org/download.html#build-windows).
2. Download the build suitable for your operating system.
3. Extract the archive to a folder (e.g., `C:\ffmpeg`).
4. Add the `bin` directory (e.g., `C:\ffmpeg\bin`) to your system's PATH environment variable.

---

## Usage

### 1. Open the Script
Open the `main.py` file in your preferred code editor (e.g., Visual Studio Code, PyCharm, or any other).

### 2. Configure Variables
Edit the following variables in the script as needed:

- **`video_url`**: Put the URL of the video or playlist you want to download.
  ```python
  video_url = "YOUR_VIDEO_OR_PLAYLIST_URL"
  ```

- **`download_path`**: Specify the directory where you want the videos to be saved.
  ```python
  download_path = "YOUR_DOWNLOAD_DIRECTORY"
  ```

- **`quality`**: Adjust the preferred quality of the download (e.g., `high`, `medium`, `low`).
  ```python
  quality = "preferred_quality"
  ```

- **`audio_only`**: Set to `True` to download only the audio, or `False` to download the video.
  ```python
  audio_only = True  # For audio-only downloads
  audio_only = False # For video downloads
  ```

### 3. Run the Script
Run the script in your terminal or code editor to download the desired videos.

---

## Enjoy!
Feel free to customize the script as needed and enjoy downloading your favorite videos or playlists!

---

### Notes
- Ensure the FFmpeg binary is properly installed and accessible through the system PATH for seamless operation.
- If you encounter any issues, double-check the configuration steps above or consult the script's documentation.

