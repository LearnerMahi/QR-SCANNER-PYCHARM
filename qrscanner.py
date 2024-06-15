# import qrcode
# img=qrcode.make("")
# img.save("img.png")
import qrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

def generate_qr():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        display_qr(img)

def display_qr(img):
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

app = tk.Tk()
app.title("QR Code Generator")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(pady=20)

title_label = tk.Label(frame, text="Enter URL to Generate QR Code:", font=("Helvetica", 14))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

url_entry = tk.Entry(frame, width=40, font=("Helvetica", 12))
url_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 20))

generate_button = tk.Button(frame, text="Generate QR Code", command=generate_qr, font=("Helvetica", 12))
generate_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

qr_label = tk.Label(frame)
qr_label.grid(row=3, column=0, columnspan=2)

app.mainloop()
