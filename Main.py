import tkinter as tk
from Conversion import *


def forgot_slaves(frame=None):
    slaves = frame.pack_slaves()
    for each_item in slaves:
        each_item.forget()


def pack_slaveframe(m_frame=None, frame_to_pack=None):
    forgot_slaves(m_frame)
    frame_to_pack.pack()
    m_frame.pack()


videoPath = None


def browse(parent=None):
    global videoPath
    videoPath = tk.filedialog.askopenfilename(parent=parent, initialdir=r'/', title='Choose a file')
    # print(videoPath)

    # for video in videoPath:
    #     video = video.split("/")
    #     print(video[-1])


def fill_vtov(frametofill=None):
    global videoPath

    tk.Label(frametofill, text="Video To Video", font=("Times New Roman Bold", 20), pady=5).grid(row=0, column=1,
                                                                                                 padx=100)

    tk.Button(frametofill, text="Browse Video", font=15, command=lambda: browse(frametofill)).grid(row=1, column=1,
                                                                                                   pady=10)
    tk.Label(frametofill, text="Output file Name").grid(row=2, column=0)

    textbox = tk.Text(frametofill, height=1, width=25)
    textbox.grid(row=2, column=1)

    tk.Label(frametofill, text="Start ( HH:MM:SS )").grid(row=3, column=0)

    Tb_startTime = tk.Text(frametofill, height=1, width=25)
    Tb_startTime.grid(row=3, column=1)

    tk.Label(frametofill, text="End  ( HH:MM:SS )").grid(row=4, column=0)

    Tb_EndTime = tk.Text(frametofill, height=1, width=25)
    Tb_EndTime.grid(row=4, column=1)

    tk.Button(frametofill, text="Submit", font=15,
              command=lambda: videoToVideo(frametofill, videoPath, textbox.get("1.0", 'end-1c'),
                                           Tb_startTime.get("1.0", 'end-1c'), Tb_EndTime.get("1.0", 'end-1c'))).grid(
        row=5, column=1, pady=10)

    return frametofill

def fill_vtoA(frametofill=None):
    global videoPath

    tk.Label(frametofill, text="Video To Audio", font=("Times New Roman Bold", 20), pady=5).grid(row=0, column=1,
                                                                                                 padx=100)

    tk.Button(frametofill, text="Browse Video", font=15, command=lambda: browse(frametofill)).grid(row=1, column=1,
                                                                                                   pady=10)
    tk.Label(frametofill, text="Output file Name").grid(row=2, column=0)

    textbox = tk.Text(frametofill, height=1, width=25)
    textbox.grid(row=2, column=1)

    tk.Label(frametofill, text="Start ( HH:MM:SS )").grid(row=3, column=0)

    Tb_startTime = tk.Text(frametofill, height=1, width=25)
    Tb_startTime.grid(row=3, column=1)

    tk.Label(frametofill, text="End  ( HH:MM:SS )").grid(row=4, column=0)

    Tb_EndTime = tk.Text(frametofill, height=1, width=25)
    Tb_EndTime.grid(row=4, column=1)

    tk.Button(frametofill, text="Submit", font=15,
              command=lambda: videoToAudio(frametofill, videoPath, textbox.get("1.0", 'end-1c'),
                                           Tb_startTime.get("1.0", 'end-1c'), Tb_EndTime.get("1.0", 'end-1c'))).grid(
        row=5, column=1, pady=10)
    return frametofill


def fill_audioloop(frametofill=None):
    tk.Label(frametofill, text="Audio Loop", font=("Times New Roman Bold", 20)).grid(row=0, column=0)

    tk.Button(frametofill, text="Browse", font=("Times New Roman Bold", 15), command=lambda: browse(frametofill)).grid(
        row=1, column=0)

    tk.Label(frametofill, text="Output file Name").grid(row=2, column=0)

    textbox = tk.Text(frametofill, height=1, width=25)
    textbox.grid(row=2, column=1)

    tk.Label(frametofill, text="End  ( HH:MM:SS )").grid(row=4, column=0)

    Tb_maxTime = tk.Text(frametofill, height=1, width=25)
    Tb_maxTime.grid(row=4, column=1)

    tk.Button(frametofill, text="Submit", font=15,
              command=lambda: appendAudio(frametofill, videoPath, textbox.get("1.0", 'end-1c'),
                                           Tb_maxTime.get("1.0", 'end-1c'))).grid(
        row=5, column=1, pady=10)

    return frametofill


def __main__():
    root = tk.Tk()
    root.title('Convertor')

    tk.Label(master=root, text="Convert Audio-Video", font=("Times New Roman Bold", 20), pady=10).pack()
    menubar = tk.Menu(root)

    subMenu_convert = tk.Menu(menubar)

    subMenu_convert.add_command(label="Video to Audio",
                                command=lambda: pack_slaveframe(mainframe, frame_videoToAudio))

    subMenu_convert.add_command(label="Video To Video",
                                command=lambda: pack_slaveframe(mainframe, frame_videoToVideo))

    menubar.add_cascade(label="Convert", menu=subMenu_convert)

    subMenu_loop = tk.Menu(menubar)
    subMenu_loop.add_command(label="Video Loop",)
    subMenu_loop.add_command(label="Audio Loop", command=lambda: pack_slaveframe(mainframe, frame_audioloop))
    subMenu_loop.add_command(label="Video to Audio Loop")
    menubar.add_cascade(label="Loop", menu=subMenu_loop)
    menubar.add_command(label="Quit", command=root.quit)
    root.config(menu=menubar)

    mainframe = tk.Frame(root, bg="Black", height=650, width=1000)

    frame_videoToAudio = tk.Frame(mainframe, pady=5)
    frame_videoToAudio = fill_vtoA(frametofill=frame_videoToAudio)


    frame_videoToVideo = tk.Frame(mainframe, pady=5)
    frame_videoToVideo = fill_vtov(frametofill=frame_videoToVideo)

    frame_audioloop = tk.Frame(mainframe, pady=5, padx=5)
    frame_audioloop = fill_audioloop(frame_audioloop)

    mainframe.pack()
    mainframe.pack_propagate(0)
    root.pack_propagate(0)

    root.config(height=800, width=1080)
    root.mainloop()


if __name__ == "__main__":
    __main__()
