import subprocess
import os
import wave
import json
from vosk import Model, KaldiRecognizer

# Support for both Telugu and English models
MODEL_PATHS = {
    "telugu": "vosk-model-small-te-0.42",
    "english": "vosk-model-small-en-us-0.15"  # Will fallback to Telugu if not available
}

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


def transcribe(audio_file, language="telugu"):
    """Transcribe audio file. Language can be 'telugu' or 'english'"""
    clean_file = convert_audio(audio_file)

    # Try to use requested language model, fallback to Telugu if not available
    model_path = MODEL_PATHS.get(language, MODEL_PATHS["telugu"])
    if not os.path.exists(model_path):
        model_path = MODEL_PATHS["telugu"]  # Fallback

    model = Model(model_path)
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