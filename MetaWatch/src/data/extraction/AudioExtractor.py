import moviepy.editor as mp
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioAnalysis
from pyAudioAnalysis import ShortTermFeatures
from pyAudioAnalysis import MidTermFeatures
import numpy as np
import matplotlib.pyplot as plt
import csv

def analysisAudio(vid_uuid, analysis_uuid):
    with open("../../../data/processed/"+str(vid_uuid)+"-"+str(analysis_uuid)+"_extracted.interest.csv") as interestfile:
        interest_reader = csv.reader(interestfile, delimiter=',')
        interest_header = next(interest_reader, None)
        minFrame = int(list(next(interest_reader, None))[0])
        test = reversed(list(interest_reader))
        maxFrame = int(list(next(test, None))[0])
    startTime = minFrame/60
    endTime = maxFrame/60
    
    clip = mp.VideoFileClip("../../../data/raw/"+ str(vid_uuid) + "/replay.mp4").subclip(startTime, endTime)
    clip.audio.write_audiofile("../../../data/raw/"+ str(vid_uuid) + "/"+ str(analysis_uuid) +"-audio.wav")
  
    VIDEOFILE = "../../../data/raw/"+ str(vid_uuid) + "/replay.mp4"
    AUDIOFILE = "../../../data/raw/"+ str(vid_uuid) + "/" + str(analysis_uuid) + "-audio.wav"
    FEATUREFILE = "../../../data/processed/"+ str(vid_uuid) + "-" + str(analysis_uuid) +"_extracted.ft"
    [Fs, x] = audioBasicIO.read_audio_file(AUDIOFILE)
    x = audioBasicIO.stereo_to_mono(x)

    midF, shortF, midFNames = MidTermFeatures.mid_feature_extraction(x,Fs, (1/30)*Fs,(1/60)*Fs,(1/60)*Fs,(1/120)*Fs)

    np.save(FEATUREFILE, midF)
    np.savetxt(FEATUREFILE + ".csv", midF.T, delimiter=",", header=",".join(midFNames))
    #%%
    audioAnalysis.thumbnailWrapper(AUDIOFILE,50)
    #explore the audio
    #audioAnalysis.fileSpectrogramWrapper(AUDIOFILE)
    #audioAnalysis.fileChromagramWrapper(AUDIOFILE)

analysisAudio(35,97)
