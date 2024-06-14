# utils.py
import os

def list_audio_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.wav')]

def list_textgrid_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.TextGrid')]
