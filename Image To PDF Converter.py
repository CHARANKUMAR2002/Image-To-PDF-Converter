import img2pdf
from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.resizable(False, False)
root.config(bg='black')
root.iconbitmap("D:/Applications/Image To PDF/Image To PDF.ico")
root.geometry("320x190")
root.title("Image To PDF Converter")


def file():
    global img
    img = filedialog.askopenfilenames(initialdir="C:/Users/Welcome/Pictures", title='Select File',
                                     filetype=(("JPG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")))
    path.insert(0, str(img))


Label(root, text='Image To PDF Converter', font=('rosemary', 20, 'bold', 'italic', 'underline'), bg='black',
      fg='#06beb6').pack(pady=10)
path = Entry(root, width=28, bd=0, font=('times', 15, 'italic'), bg='black', fg='gray')
path.pack()
im = Button(root, text='Import', command=file, bg='black', fg='white', activebackground='black',
            activeforeground="#ee9ca7", font=("rosemary", 15, "italic"), bd=0)
im.pack()


def export():
    if len(path.get()) != 0:
        pdf = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Documents", title='Save As',
                                            defaultextension=".pdf",
                                            filetype=(("PDF", "*.pdf"), ("All Files", "*.*")))
        with open(str(pdf), 'wb') as e:
            e.write(img2pdf.convert(img))
        messagebox.showinfo('Image To PDF', 'PDF File Exported Successfully!')
        path.delete(0, END)
    else:
        messagebox.showerror('Image To PDF', 'No File Was Imported')


ex = Button(root, text='Export', command=export, bg='black', fg='white', activebackground='black',
            activeforeground="#00FF00", font=("rosemary", 15, "italic"), bd=0)
ex.pack()


def exit():
    d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
    if d =="yes":
        root.destroy()
    else:
        return None


close = Button(root, text='Exit', command=exit, bd=0, font=("rosemary", 12, "italic"), bg='black', fg='white', activebackground='black', activeforeground='#ff0000').pack()

root.mainloop()