#!/bin/python3
# -*- coding: utf-8 -*-

# files
import glob
from pathlib import Path
# data
import pandas as pd
# audio and textgrid
import tgt
from praatio import textgrid
from praatio.utilities.constants import Interval
from pydub import AudioSegment

##### FUNCTIONS #####
def update_textgrid_with_annotations(path_to_tg, annotations):
    tg = textgrid.openTextgrid(path_to_tg, includeEmptyIntervals=False)
    new_tg = tg.new() # copy
    tier = new_tg.getTier("MAUS")
    new_tier = tier.new() # copy
    emptied_tier = tier.new(name="schwa_annotations", entries=annotations) # copy

    return new_tg

def annotate_schwa(tg):
    phones_tier = tg.get_tier_by_name("MAU")

    annotations = []
    for i in range(len(phones_tier)-1):
        intr = phones_tier[i]
        if intr.text == "@": # schwa
            start_time = intr.start_time
            end_time = intr.end_time
            next_interval_start = phones_tier[i+1].start_time if i+1 < len(phones_tier) else sound.end_time
            next_interval_label = phones_tier[i+1].text if i+1 < len(phones_tier) else ""

            is_prepausal = (next_interval_label == "" or next_interval_label == "<p:>")

            annotations.append((start_time, end_time, "pre-pausal") if is_prepausal else "non-prepausal")
    return annotations

##### MAIN #####
def main():
    wav_folder = "data/processed_audio"
    tg_folder = "data/audio"

    wav_files = glob.glob(wav_folder + "/*.wav")
    tg_files = glob.glob(tg_folder + "/*/*.TextGrid")
    n_files = len(wav_files)

    for i in range(n_files):
        grid = tg_files[i]
        filename = Path(grid).stem
        tg = tgt.io.read_textgrid(grid)
        new_entries = annotate_schwa(tg)

        new_intr = textgrid.IntervalTier(name="schwa_annotations", entries=new_entries)
        tg.add_tier(new_intr)

        # save annotated tg
        tg_praat = tgt.io.export_to_long_textgrid(tg)
        with open("data/annotations/" + "annotated_" + filename + ".TextGrid", "w") as f:
            f.write(tg_praat)


if __name__ == "__main__":
    main()
