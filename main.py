import expyriment
import time
import numpy as np

from pathlib import Path

all_images = []

for path in Path('datasets/OASIS/images').rglob('*.jpg'):
    all_images.append(str(path))

for path in Path('datasets/GAPED').rglob('*.bmp'):
    all_images.append(str(path))

exp = expyriment.design.Experiment(name="Text Experiment")

exp.data_variable_names = ["trial", "timestamp", "img"]

expyriment.control.initialize(exp)

block_one = expyriment.design.Block(name="A name for the first block")
trial_one = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 1, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)
trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 1, Trial 2")
trial_two.add_stimulus(stim)
block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)

block_two = expyriment.design.Block(name="A name for the second block")
trial_one = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 2, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)
trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 2, Trial 2")
trial_two.add_stimulus(stim)
block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
exp.add_block(block_two)

expyriment.control.start()

rng = np.random.default_rng()


i = 0
while True:
    try:
        rn = rng.integers(0, len(all_images))
        img = all_images[rn]
        stim = expyriment.stimuli.Picture(img)
        stim.scale_to_fullscreen()
        # stim.load()
        stim.present()
        # key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
        #                              expyriment.misc.constants.K_RIGHT])
        exp.clock.wait(5000)
        exp.data.add([i, time.time(), img])
        # To convert back ts: datetime.utcfromtimestamp(ts)
        i += 1
    except KeyboardInterrupt:
        break

expyriment.control.end()

expyriment.misc.data_preprocessing.write_concatenated_data(
    data_folder="data", file_name="main",
    output_file="results.csv")
