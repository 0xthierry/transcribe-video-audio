import moviepy.editor as mp
import os
import whisper

BASE_DIR = os.getcwd()
AUDIO_DIR = os.path.join(BASE_DIR, 'audio')
VIDEO_DIR = os.path.join(BASE_DIR, 'video')
TRANSCRIPTION_DIR = os.path.join(BASE_DIR, 'transcription')

def extract_audio(source: str, destination: str):
  video = mp.VideoFileClip(source)
  video.audio.write_audiofile(destination, codec='pcm_s16le')

def transcribe_audio(source: str):
  model = whisper.load_model("medium")
  transcription = model.transcribe(source)
  return transcription["text"]

if __name__ == '__main__':
  video_filename = 'video.mp4'
  video = os.path.join(VIDEO_DIR, video_filename)
  audio_filename = 'audio.wav'
  audio = os.path.join(AUDIO_DIR, audio_filename)
  
  extract_audio(video, audio)

  transcription = transcribe_audio(audio)

  with open(os.path.join(TRANSCRIPTION_DIR, 'transcription.txt'), 'w') as f:
    f.write(transcription)

  print("Transcription complete!")