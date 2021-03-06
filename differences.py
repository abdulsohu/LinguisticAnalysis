'''
Import necessary modules for speech analysis.
'''
import parselmouth
import numpy as np
import seaborn as sns
import myprosody as mysp
import matplotlib.pyplot as plt


'''
Parselmouth function to draw spectrogram of a waveform. 
'''
def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")


'''
Parselmouth function to draw intensity of a waveform.
'''
def draw_intensity(intensity):
    plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")

'''
Parselmouth function to draw pitch of a waveform.
'''
def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("fundamental frequency [Hz]")


sns.set() # Use seaborn's default style to make attractive graphs
plt.rcParams['figure.dpi'] = 100 # Show nicely large images in this notebook

'''
The word "without" analyzed.
'''

without_aave = parselmouth.Sound("audio/aave/without.wav")

intensity = without_aave.to_intensity()
spectrogram = without_aave.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([without_aave.xmin, without_aave.xmax])
plt.savefig('without_aave.png')

without_standard = parselmouth.Sound("audio/standard/without.wav")

intensity = without_standard.to_intensity()
spectrogram = without_standard.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([without_standard.xmin, without_standard.xmax])
plt.savefig('without_standard.png')

'''
The word "three" analyzed.
'''

three_aave = parselmouth.Sound("audio/aave/three.wav")

intensity = three_aave.to_intensity()
spectrogram = three_aave.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([three_aave.xmin, three_aave.xmax])
plt.savefig('three_aave.png')

three_standard = parselmouth.Sound("audio/standard/three.wav")

intensity = three_standard.to_intensity()
spectrogram = three_standard.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([three_standard.xmin, three_standard.xmax])
plt.savefig('three_standard.png')

'''
Analyzing "we gon' have no' mo' influence".
'''

shortening_aave = parselmouth.Sound("audio/aave/noMoreInfluence.wav")

intensity = shortening_aave.to_intensity()
spectrogram = shortening_aave.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([shortening_aave.xmin, shortening_aave.xmax])
plt.savefig('shortening_aave.png')

shortening_standard = parselmouth.Sound("audio/standard/noMoreInfluence.wav")

intensity = shortening_standard.to_intensity()
spectrogram = shortening_standard.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([shortening_standard.xmin, shortening_standard.xmax])
plt.savefig('shortening_standard.png')