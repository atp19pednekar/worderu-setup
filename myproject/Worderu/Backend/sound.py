import pyaudio
import wave

def sound_record():
    audio=pyaudio.PyAudio()

    stream=audio.open(format=pyaudio.paInt16, channels=1,rate=16000, input=True, frames_per_buffer=1024)

    frames=[]

    try:
        while True:
            data=stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file=wave.open("Recording.wav","wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(16000)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

#This is Working Now