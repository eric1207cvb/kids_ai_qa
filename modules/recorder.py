import sounddevice as sd
import soundfile as sf

def record_audio(filename='input.wav', duration=5, samplerate=16000):
    print("🎙️ 開始錄音，請說話...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, recording, samplerate)
    print(f"✅ 錄音完成！音訊已儲存為：{filename}")
