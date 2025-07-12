from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_youtube_video_id(url):
    """Extract video ID from various YouTube URL formats"""
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    elif 'youtube.com' in url:
        if 'v=' in url:
            return url.split('v=')[1].split('&')[0]
    return None

def format_transcript(transcript):
    """Format transcript with timestamps and newlines for readability"""
    formatted_text = ""
    for entry in transcript:
        # Convert seconds to MM:SS format
        minutes = int(entry.start // 60)
        seconds = int(entry.start % 60)
        timestamp = f"[{minutes:02d}:{seconds:02d}]"
        formatted_text += f"{timestamp} {entry.text}\n\n"
    return formatted_text.strip()

def download_transcript():
    """Main function to handle transcript downloading"""
    video_url = input("Enter YouTube video URL: ")
    video_id = get_youtube_video_id(video_url)
    
    if not video_id:
        print("Invalid YouTube URL")
        return
    
    try:
        # Try to get manually created transcripts first
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try English transcript first, then any available language
        try:
            transcript = transcript_list.find_transcript(['en'])
        except:
            transcript = transcript_list.find_transcript(transcript_list._manually_created_transcripts)
        
        # Fetch the actual transcript data
        transcript_data = transcript.fetch()
        
        # Format and save the transcript
        formatted_text = format_transcript(transcript_data)
        
        with open('transcript.txt', 'w', encoding='utf-8') as f:
            f.write(formatted_text)
        print("Transcript successfully saved to transcript.txt")
        
    except (TranscriptsDisabled, NoTranscriptFound):
        # If no manual transcript, try generated captions
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            formatted_text = format_transcript(transcript)
            
            with open('transcript.txt', 'w', encoding='utf-8') as f:
                f.write(formatted_text)
            print("Auto-generated captions saved to transcript.txt")
            
        except Exception as e:
            print("Transcript unavailable - no manual transcript or auto-captions found")
            # Ensure no file is created if no content available
            open('transcript.txt', 'w').close()  # Creates/clears file but doesn't store content

if __name__ == "__main__":
    download_transcript()