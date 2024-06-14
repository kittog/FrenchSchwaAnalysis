# preprocess_audio.py
import os
import glob
from pathlib import Path
from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np
import noisereduce as nr

##### CONSTANTS #####
AUDIO_DIR = "data/audio"
PROC_AUDIO_DIR = "data/processed_audio"

##### FUNCTIONS #####
def normalize_audio(audio_segment):
    # Normalize audio to -20dBFS
    return audio_segment.apply_gain(-20.0 - audio_segment.dBFS)

def reduce_noise(audio_path, output_path):
    rate, data = wavfile.read(audio_path)
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(output_path, rate, reduced_noise)

def preprocess_audio(wav_file:str, wav_dir:str):
    audio = AudioSegment.from_wav(wav_file)
    filename = Path(wav_file).stem
    # normalization
    normalized_audio = normalize_audio(audio)
    normalized_audio_path = PROC_AUDIO_DIR + "/" + "normalized_" + filename + ".wav"
    normalized_audio.export(normalized_audio_path, format="wav")

    # noise reduction
    #noise_reduced_path = PROC_AUDIO_DIR + "/" + "nreduced_" + filename + ".wav"
    #reduce_noise(normalized_audio_path, noise_reduced_path)

    # remove intermediate files
    #os.remove(normalized_audio_path)

##### MAIN #####
def main():
    wav_files = glob.glob(AUDIO_DIR + "/*/*.wav") # all wav files from all speakers
    # loop through wav_files
    for wav in wav_files:
        preprocess_audio(wav, PROC_AUDIO_DIR)

if __name__ == "__main__":
    main()
