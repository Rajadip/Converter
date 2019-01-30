import moviepy.editor as mp
import tkinter.filedialog as fd
import tkinter as tk
from tkinter import messagebox
import timeConversion as tm


def videoToAudio(mainframe=None, videoPath=None, outputfile=None, sec1=None, sec2=None):
    try:
        if videoPath:
            clip = mp.VideoFileClip(videoPath)
            if sec1 == "" or sec2 == "":
                print("No Sec")
                pass
            else:

                sec1 = tm.toSec(sec1)
                sec2 = tm.toSec(sec2)
                dur = clip.duration
                print("Sec")
                if sec1 > dur or sec2 > dur:
                    messagebox.showinfo("Duration Error", "Start or End is greation than original Video.")
                elif sec1 >= sec2:
                    messagebox.showinfo("Duration Error", "Start can't greater than end.")
                else:
                    clip = clip.subclip(sec1, sec2)

            clip.audio.write_audiofile(r"output/" + outputfile)
            messagebox.showinfo("Success", "Video Converted...!!!")
    except Exception as e:
        messagebox.showinfo("Fail", "Error Occured\n" + str(e))

def videoToVideo(mainframe=None, videoPath=None, outputfile=None, sec1=None, sec2=None):
    try:
        if videoPath:
            clip = mp.VideoFileClip(videoPath)
            if sec1 == "" or sec2 == "":
                messagebox.showinfo("Error", "Failed...!!!\nYou should try after filling 'Start' and 'End'....")
                pass
            else:

                sec1 = tm.toSec(sec1)
                sec2 = tm.toSec(sec2)
                dur = clip.duration
                print("Sec")
                if sec1 > dur or sec2 > dur:
                    messagebox.showinfo("Duration Error", "Start or End is greation than original Video.")
                elif sec1 >= sec2:
                    messagebox.showinfo("Duration Error", "Start can't greater than end.")
                else:
                    clip = clip.subclip(sec1, sec2)
                    clip.write_videofile(r"output/" + outputfile)
                    messagebox.showinfo("Success", "Video Converted...!!!")
    except Exception as e:
        messagebox.showinfo("Fail", "Error Occured\n" + str(e))

def appendAudio(mainframe=None, videoPath=None, outputfile=None, maxTime=None ):
    try:
        clip = mp.AudioFileClip(videoPath)
        duration = clip.duration

        maxTime = tm.toSec(maxTime)

        if duration > maxTime:
            messagebox.showinfo('Failure', 'Max Time should greater than duration')

        clips = []
        for i in range(0, round(maxTime), round(duration)):
            clips.append(clip)
        concat_clip = mp.concatenate_audioclips(clips)
        concat_clip.write_audiofile('output/'+outputfile)
        messagebox.showinfo('Success', 'Success')
    except Exception as e:
        messagebox.showinfo('Failure','You have done somthing wrong...!!!' + str(e))

def appendVideo(mainframe=None, videoPath=None, outputfile=None, maxTime=None ):
    try:
        clip = mp.VideoFileClip(videoPath)
        duration = clip.duration
        clips = []
        for i in range(0, maxTime, round(duration)):
            clips.append(clip)
        concat_clip = mp.concatenate_videoclips(clips)
        concat_clip.write_videofile('output/'+outputfile)
    except Exception as e:
        messagebox.showinfo('Failure','You have done somthing wrong...!!!' + str(e))
    print(mainframe)
