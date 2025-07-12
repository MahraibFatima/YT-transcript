## YouTube Transcript Downloader

A Python script that downloads transcripts from YouTube videos with timestamps and saves them to a text file.

## Features

- Downloads both manually created transcripts and auto-generated captions
- Formats transcripts with timestamps in [MM:SS] format
- Saves output to `transcript.txt`
- Handles various YouTube URL formats
- Provides clear feedback when transcripts are unavailable

## Requirements

- Python 3.6 or higher
- youtube-transcript-api package

## Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/yourusername/youtube-transcript-downloader.git
   cd youtube-transcript-downloader
   ```

2. Create and activate a virtual environment (recommended):

### Create Python Virtual Environment

1. Open your terminal or command prompt and navigate to the project directory.

2. Run the following command to create a new virtual environment:
   ```bash
   python3 -m venv myenv
   ```
   This will create a new virtual environment named `myenv` in the current directory.

3. Activate the virtual environment:

   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. To deactivate the virtual environment when you're done:
   ```bash
   deactivate
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. When prompted:
   ```
   Enter YouTube video URL:
   ```
3. Enter the YouTube video URL (for testing):
   ```
   https://youtu.be/kPa7bsKwL-c
   ```
or your desired link.


5. The script will:
   - Attempt to download the transcript
   - Format it with timestamps
   - Save it to `transcript.txt`
   - Display status messages in the console

## Output Example

The `transcript.txt` file will contain formatted text like:
```
[00:00] Welcome to this tutorial on Python programming.

[00:04] Today we'll be learning about web scraping.

[00:08] First, let's install the required packages.
```


## Troubleshooting

- If you get "Transcript unavailable", the video may not have captions.
- Some videos have disabled transcripts.
- Try different language codes if English isn't available.
- Make sure the URL is correct and the video is publicly available.
