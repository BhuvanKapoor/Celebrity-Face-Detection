import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Upload")

# function to open file dialog and display image
def upload_image():
    global img, panel
    f_types = [('Image files', '*.jpg *.jpeg *.png')]
    path = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(path)
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    panel.config(image=img_tk)
    panel.image = img_tk

# create a button to open file dialog
btn = tk.Button(window, text="Upload Image", command=upload_image)
btn.pack(side="top", fill="x")

# create a panel to display the image
panel = tk.Label(window, image=None)
panel.pack(side="top", fill="x", pady=10)

# create a canvas to display the image
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack(side="top", fill="x", pady=10)

# display the uploaded image on the canvas
def show_image():
    global img, canvas
    img = Image.open(filedialog.askopenfilename())
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    canvas.delete("image")
    canvas.create_image(0, 0, image=img_tk, anchor=tk.NW, tag="image")
    canvas.image = img_tk

# create a button to show the image
btn_show = tk.Button(window, text="Show Image", command=show_image)
btn_show.pack(side="top", fill="x", pady=10)

window.mainloop()