import subprocess
import os
import wave
import json
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-te-0.42"

def convert_audio(input_file, output_file="clean.wav"):
    subprocess.run([
        "ffmpeg", "-y",
        "-i", input_file,
        "-ar", "16000",
        "-ac", "1",
        "-sample_fmt", "s16",
        output_file
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_file


def transcribe(audio_file):

    clean_file = convert_audio(audio_file)

    model = Model(MODEL_PATH)
    wf = wave.open(clean_file, "rb")

    rec = KaldiRecognizer(model, 16000)
    rec.SetWords(True)

    full_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            full_text += " " + res.get("text", "")

    final = json.loads(rec.FinalResult())
    full_text += " " + final.get("text", "")

    return full_text.strip()