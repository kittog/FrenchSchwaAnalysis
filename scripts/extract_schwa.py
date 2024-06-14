# extract_schwa.py
import parselmouth
from parselmouth.praat import call
from praatio import textgrid
import pandas as pd
import glob

##### FUNCTIONS #####
def annotate_schwa(wav_path, textgrid_path):
    sound = parselmouth.Sound(wav_path)
    tg = parselmouth.read(textgrid_path)
    interval_tier = tg.get_tier_by_name("MAU")

    schwa_intervals = [interval for interval in interval_tier if interval.text == '@']
    annotations = []

    for i, interval in enumerate(schwa_intervals):
        start_time = interval.start_time
        end_time = interval.end_time
        next_interval_start = interval_tier[i+1].start_time if i+1 < len(interval_tier) else sound.end_time
        next_interval_label = interval_tier[i+1].text if i+1 < len(interval_tier) else ""

        # Determine if next interval is a pause (empty or labeled as "pause", adjust label as per your convention)
        is_prepausal = (next_interval_label == "" or next_interval_label == "pause")

        annotations.append((start_time, end_time, 'pre-pausal' if is_prepausal else 'non-prepausal'))

    return annotations

def update_textgrid_with_annotations(textgrid_path, annotations):
    tg = textgrid.openTextgrid(textgrid_path)
    annotation_tier = textgrid.IntervalTier('schwa_annotations', [])

    for start_time, end_time, label in annotations:
        annotation_tier.insertEntry(start_time, end_time, label, warnFlag=False)

    tg.addTier(annotation_tier)
    tg.save(textgrid_path.replace('.TextGrid', '_annotated.TextGrid'), format='short_textgrid', includeBlankSpaces=True)

##### MAIN #####
def main():
    # paths
    wav_path = "data/processed_audio"
    textgrid_path = "data/audio"
    # get files lists
    wav_files = glob.glob(wav_path + "/*.wav")
    tg_files = glob.glob(textgrid_path + "/*/*.TextGrid")
    n_files = len(wav_files)
    # loop through files to run annotation
    for i in range(n_files):
        annotations = annotate_schwa(wav_files[i], tg_files[i])
        update_textgrid_with_annotations(tg_files[i], annotations)

if __name__ == "__main__":
    main()
