#import whisper
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from faster_whisper import WhisperModel

def transcription():
    model_size = "small"

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments,info = model.transcribe("avatar.m4a", beam_size=5, language="en", condition_on_previous_text=False)

    transcript=" "
    for segment in segments:
        transcript=transcript+segment.text

    return transcript

#This Module is Working