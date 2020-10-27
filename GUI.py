from tkinter import *
from tkinter import filedialog
# import audiocrop
root = Tk() #blank window
root.title('Split On Silence - Abilisense')
def file_select():
    root.filename = filedialog.askopenfilename(initialdir="c:/Users/yuval/PycharmProjects/AudioCrop/in", title="select wav file")
    print(root.filename)
    audiocrop.file_location = root.filename
    return root.filename
title = Frame(root)
title.pack(side=TOP)
headline = Label(title, text="Split On Silence - Abilisense") #text label
headline.pack(side=TOP) #placeing the label
addfile = Button(title, text="Add file", command=file_select)
addfile.pack(side=BOTTOM)
calculateframe = Frame(root)#invisible frame
calculateframe.pack()
calculetheadline = Label(calculateframe, text="Silence frequency definition (db):") #text label
calculetheadline.pack(side=TOP) #placeing the label
userdb = Entry(calculateframe)
userdb.pack(side=TOP)
calculateb = Button(calculateframe, text="calculate")
calculateb.pack(side=TOP)
numberofevent = Label(calculateframe, text="Number of events after splitting:") #text label
numberofevent.pack(side=BOTTOM) #placeing the label
splitexitframe = Frame(root)#invisible frame
splitexitframe.pack(side=BOTTOM)
splitb = Button(splitexitframe, text="SPLIT",)
exitb = Button(splitexitframe, text="EXIT", command=quit)
splitb.pack(side=RIGHT)
exitb.pack(side=LEFT)
root.mainloop() #loop for the window to stay on screen
