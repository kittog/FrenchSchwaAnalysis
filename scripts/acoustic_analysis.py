# analyze_acoustics.py
import parselmouth
from parselmouth.praat import call
from praatio import tgio
import csv
import os
import glob

##### CONSTANTS #####
WAV_DIR = "data/processed_audio"
TG_DIR = "data/audio"

##### FUNCTIONS #####
def analyze_schwa_intervals(wav_path, annotations):
    sound = parselmouth.Sound(wav_path)
    results = []

    for start_time, end_time, label in annotations:
        segment = sound.extract_part(from_time=start_time, to_time=end_time)
        duration = end_time - start_time

        formant = call(segment, "To Formant (burg)", 0.0, 5.0, 5500, 0.025, 50.0)
        f1 = call(formant, "Get value at time", 1, (start_time + end_time) / 2, "Hertz", "Linear")
        f2 = call(formant, "Get value at time", 2, (start_time + end_time) / 2, "Hertz", "Linear")

        pitch = call(segment, "To Pitch", 0.0, 75, 600)
        f0 = call(pitch, "Get mean", 0, 0, "Hertz")

        intensity = call(segment, "Get intensity (dB)")

        results.append((start_time, end_time, duration, f1, f2, f0, intensity, label))

    return results

def save_results_to_csv(results, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['start_time', 'end_time', 'duration', 'f1', 'f2', 'f0', 'intensity', 'label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow({
                'start_time': result[0],
                'end_time': result[1],
                'duration': result[2],
                'f1': result[3],
                'f2': result[4],
                'f0': result[5],
                'intensity': result[6],
                'label': result[7]
            })

##### MAIN #####
def main():


if __name__ == "__main__":
    wav_path = 'data/processed_audio/your_audio_file.wav'
    textgrid_path = 'data/transcriptions/your_textgrid_file_annotated.TextGrid'
    annotations = extract_schwa.annotate_schwa(wav_path, textgrid_path)
    results = analyze_schwa_intervals(wav_path, annotations)
    save_results_to_csv(results, 'data/results/schwa_analysis_results.csv')
