from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk




MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def morse(message):
    cipher = ''
    cipher_array = []
    for letter in message.upper():
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    for char in cipher:
        if char == '.':
            cipher_array.append('0000')
        elif char == '-':
            cipher_array.append('1111')
        else:
            cipher_array.append('0101')
    return cipher_array

def encode(img,pixels_h,pixels_v,message):
    img = img.reshape((3,pixels_h*pixels_v))
    message = morse(message)
    img[0][0] = len(message)
    for i in range(1,len(message)+1):
        bits = format(img[0][i],'08b')
        bits = bits[:4] + message[i-1]
        img[0][i] = int(bits,2)
    img =  img.reshape((pixels_h,pixels_v,3))
    return img

def decode(img,pixels_h,pixels_v):
    img = img.reshape((3,pixels_h*pixels_v))
    message_len = img[0][0]
    message_arr = []
    for i in range(message_len):
        bits = format(img[0][i],'08b')[-4:]
        if bits == '0000':
            message_arr.append('.')
        elif bits == '1111':
            message_arr.append('-')
        elif bits == '0101':
            message_arr.append(' ')
    message = reduce(lambda a, b : a+str(b), message_arr)
    message = anti_morse(message)
    return message

def anti_morse(message):
    print(message)
    message += ' '
    decipher = ''
    citext = ''
    i=1
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
 
    return decipher


# new_img = encode(img,img.shape[0],img.shape[1],"Hail Hitler")
# print(decode(new_img,new_img.shape[0],new_img.shape[1]))


# cv2.imshow("Cat", new_img)
# cv2.waitKey(0)

IMG = np.zeros((3,3,3))
file_name= ''
text = ''

def save_new_img():
    global text,IMG,file_name
    new_img = encode(IMG,IMG.shape[0],IMG.shape[1],text)
    print(decode(new_img,new_img.shape[0],new_img.shape[1]))
    print("HEY")
    new_name = file_name.split('.')[0] + str('_stego') + '.png'
    cv2.imwrite(new_name,new_img)
    x = np.array(cv2.imread(new_name))
    print(decode(x,x.shape[0],x.shape[1]))
    IMG = new_img

def browse_image():
    global IMG, file_name
    filename = filedialog.askopenfilename()
    if filename:
        file_name = filename
        IMG = np.array(cv2.imread(filename))
        display_image(filename)

def display_image(filename):
    img = Image.open(filename)
    img.thumbnail((400, 400)) 
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo  
    show_message("Image loaded!", "green")

def process_image():
    global IMG
    message = decode(IMG,IMG.shape[0],IMG.shape[1])
    show_message(message, "green")

def show_message(message, color):
    message_label.config(text=message, fg=color)

root = tk.Tk()
root.title("Stegonizer")
root.geometry("600x500")
root.configure(bg="#F0F0F0")

main_frame = tk.Frame(root, bg="#F0F0F0")
main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

title_label = tk.Label(main_frame, text="Stegonizer", font=("Arial", 24, "bold"), bg="#F0F0F0")
title_label.pack(pady=(0, 20))

button_frame = tk.Frame(main_frame, bg="#F0F0F0")
button_frame.pack()

browse_button = tk.Button(button_frame, text="Browse Image", command=browse_image, width=20, height=2, bg="#3498DB", fg="white", font=("Arial", 12, "bold"))
browse_button.pack(side=tk.LEFT, padx=10, pady=10)

process_button = tk.Button(button_frame, text="Decode Image", command=process_image, width=20, height=2, bg="#27AE60", fg="white", font=("Arial", 12, "bold"))
process_button.pack(side=tk.RIGHT, padx=10, pady=10)

image_label = tk.Label(main_frame, bg="#D5DBDB")
image_label.pack(expand=True, fill=tk.BOTH, padx=20, pady=(10, 0))

message_label = tk.Label(root, font=("Arial", 14), fg="black", bg="#F0F0F0")
message_label.pack(pady=10, fill=tk.X)

entry_label = tk.Label(main_frame, text="Enter something:", bg="#F0F0F0")
entry_label.pack()

entry_text = tk.StringVar()
entry = tk.Entry(main_frame, width=30,textvariable=entry_text)
entry.pack()

def print_entry_text():
    global text
    text = entry.get()
    save_new_img()


extra_button = tk.Button(main_frame, text="Encode Image", command=print_entry_text,width=20, height=2, bg="#FF6347", fg="white", font=("Arial", 12, "bold"))
extra_button.pack(pady=10)

root.mainloop()
