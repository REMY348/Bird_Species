import tkinter as tk
from tkinter import filedialog,Text,Label
import tkinter.font as tkFont
from PIL import ImageTk,Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pygame



pygame.mixer.init()
new_model = tf.keras.models.load_model('saved_model/my_model')



batch_size = 32
img_height = 300
img_width = 300
class_names = ['broadbill', 'eagle', 'owl', 'parrot']
root = tk.Tk()
root.title('PROJECT BIRDS RECOGNITION!')
root.geometry("700x650")
filename ="null"
apps = []
def add_App():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
    filetypes= (("all files","*.*"),("exe","*.exe")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="white" ) 
        label.pack() 
    return filename  



def run_App():
    global filename
    img = keras.preprocessing.image.load_img(
    filename, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    Output = (
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))
    labeloutput = tk.Label(frame,text=Output,bg="white")
    labeloutput.pack()
    


canvas = tk.Canvas(root,height=650,width=650,bg="#63ad44")

canvas.pack()

frame =tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.6,relx=0.1,rely=0.1)



Fish_image =ImageTk.PhotoImage(Image.open('bird.jpg'))

fontStyle = tkFont.Font(family="Poppins",size=20)
labeltitle = Label(frame,text="PROJECT BIRD DETECTION" ,font= fontStyle,bg="white")
labeltitle.pack()

labelproject = Label(frame ,image=Fish_image)
labelproject.pack()

line = tk.Frame(frame, height=1, width=550, bg="grey80", relief='groove')
line.pack()

openFile = tk.Button(frame,text="Open File",padx=10,pady=5,fg="white",bg="#29592f",  command=add_App  )
openFile.pack(pady=10)
RunApp = tk.Button(frame,text="Run App ",padx=10,pady=5,fg="white",bg="#29592f",  command=run_App  )
RunApp.pack()


root.mainloop()