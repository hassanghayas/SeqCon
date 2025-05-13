#!/usr/bin/python3.8

# Sequence manipulator


from tkinter import *
import tkinter.messagebox as messagebox

win = Tk()
win.title("SeqCon")
win.geometry("620x450")


frame = Frame(win)
frame.pack()

frame0 = Frame(win)
frame0.pack()

frame4 = Frame(win)
frame4.pack()

frame1 = Frame(win)
frame1.pack()

frame2 = Frame(win)
frame2.pack()

frame3 = Frame(win)
frame3.pack()


label1 = Label(frame, text="paste Sequence below:")
label1.pack()

# scroll bar for text box(DNA_Entry)
scrollbar1 = Scrollbar(frame0)
scrollbar1.pack(side=RIGHT, fill=Y)
# box where you can enter your sequence
DNA_Entry = Text(frame0, width=70, height=10, yscrollcommand=scrollbar1.set)
DNA_Entry.pack()
DNA_Entry.focus()
scrollbar1.config(command=DNA_Entry.yview)


# scroll bar for text box(result_Entry)
scrollbar2 = Scrollbar(frame2)
scrollbar2.pack(side=RIGHT, fill=Y)
# box where result of conversion shows
result_Entry = Text(frame2, width=70, height=10, yscrollcommand=scrollbar2.set)
result_Entry.pack()
result_Entry.insert(INSERT, ">")
scrollbar2.config(command=result_Entry.yview)


def invert():
    DNAseq = DNA_Entry.get(1.0, "end-1c")
    DNAseq = DNAseq.upper()
    inverted_seq = DNAseq.replace(" ","")[::-1]
    result_Entry.delete(1.0, END)
    result_Entry.insert(INSERT, ">inverted sequence\n" + inverted_seq)


def reverse_comp():
    DNAseq = DNA_Entry.get(1.0, END)
    DNAseq = DNAseq.upper()
    DNAseq = list(str(DNAseq))
    reverse_complement = str()
    for i in DNAseq:
        if i == "G":
            reverse_complement = "C" + reverse_complement
        if i == "A":
            reverse_complement = "T" + reverse_complement
        if i == "C":
            reverse_complement = "G" + reverse_complement
        if i == "T":
            reverse_complement = "A" + reverse_complement
        if i == "U":
            reverse_complement = "A" + reverse_complement
        if i == "N":
            reverse_complement = "N" + reverse_complement
    result_Entry.delete(1.0, END)
    result_Entry.insert(INSERT, ">reverse complementary sequence\n" + reverse_complement)


def complmentry():
    DNAseq = DNA_Entry.get(1.0, END)
    DNAseq = DNAseq.upper()
    DNAseq = list(str(DNAseq))
    complement = str()
    for i in DNAseq:
        if i == "G":
            complement = complement + "C"
        if i == "A":
            complement = complement + "T"
        if i == "C":
            complement = complement + "G"
        if i == "T":
            complement = complement + "A"
        if i == "U":
            complement = complement + "A"
        if i == "N":
            complement = complement + "N"
    result_Entry.delete(1.0, END)
    result_Entry.insert(INSERT, ">complemtary sequence\n" + complement)


def RNA():
    DNAseq = DNA_Entry.get(1.0, END)
    DNAseq = DNAseq.upper()
    DNAseq = list(str(DNAseq))
    rna = str()
    for i in DNAseq:
        if i == "G":
            rna = rna + "G"
        if i == "A":
            rna = rna + "A"
        if i == "C":
            rna = rna + "C"
        if i == "T":
            rna = rna + "U"
        if i == "U":
            rna = rna + "U"
        if i == "N":
            rna = rna + "N"
    result_Entry.delete(1.0, END)
    result_Entry.insert(INSERT, ">RNA sequence\n" + rna)


def DNA():
    DNAseq = DNA_Entry.get(1.0, END)
    DNAseq = DNAseq.upper()
    DNAseq = list(str(DNAseq))
    DNA = str()
    for i in DNAseq:
        if i == "G":
            DNA = DNA + "G"
        if i == "A":
            DNA = DNA + "A"
        if i == "C":
            DNA = DNA + "C"
        if i == "U":
            DNA = DNA + "T"
        if i == "T":
            DNA = DNA + "T"
        if i == "N":
            DNA = DNA + "N"
    result_Entry.delete(1.0, END)
    result_Entry.insert(INSERT, ">DNA sequence\n" + DNA)


def get():
    get_result = result_Entry.get(2.0, "end-1c")
    DNA_Entry.delete(1.0, END)
    DNA_Entry.insert(INSERT, get_result)


Button(frame4, text="^", command=get).pack()

label2 = Label(frame3, text="Convert to:")
label2.pack(side=LEFT)

# RNA button
Button(frame3, text="RNA", command=RNA, fg="purple", bd=3,
       bg="lightgray", font=("Arial Bold", 10)).pack(side=LEFT)

# DNA button
Button(frame3, text="DNA", command=DNA, fg="blue", bd=3,
       bg="lightgray", font=("Arial Bold", 10)).pack(side=LEFT)

# invert sequence button
Button(frame3, text="Reverse", command=invert, fg="green",
       bd=3, bg="lightgray", font=("Arial Bold", 10)).pack(side=LEFT)

# complement button
Button(frame3, text="Complement", command=complmentry,
                    fg="green", bd=3, bg="lightgray", font=("Arial Bold", 10)).pack(side=LEFT)
# reverse complement button
Button(frame3, text="Reverse Complement", command=reverse_comp,
       fg="green", bd=3, bg="lightgray", font=("Arial Bold", 10)).pack(side=LEFT)


#functions for mouse click in DNA exntry box
def copy_text():
    DNA_Entry.clipboard_clear()
    DNA_Entry.clipboard_append(DNA_Entry.selection_get())
    return


def cut():
    copy_text()
    DNA_Entry.delete("sel.first", "sel.last")
    return


def paste():
    DNA_Entry.insert(INSERT, DNA_Entry.clipboard_get())
    return


def clear():
    DNA_Entry.delete(1.0, END)
    return


def select_all():
    DNA_Entry.focus()
    DNA_Entry.tag_add(SEL, "1.0", "end-1c")
    return


mouse_menu = Menu(win, tearoff=0)
mouse_menu.add_command(label="copy", command=copy_text)
mouse_menu.add_command(label="cut", command=cut)
mouse_menu.add_command(label="paste", command=paste)
mouse_menu.add_command(label="clear", command=clear)
mouse_menu.add_command(label="select all", command=select_all)


def click(event):
    mouse_menu.tk_popup(event.x_root, event.y_root)


DNA_Entry.bind("<Button-3>", click)



# function for mouse click in result exntry box
def copy_text_result():
    result_Entry.clipboard_clear()
    result_Entry.clipboard_append(result_Entry.selection_get())
    return

def clear_result():
    result_Entry.delete(1.0, END)
    return

def select_all_result():
    result_Entry.focus()
    result_Entry.tag_add(SEL, "2.0", "end-1c")
    return

mouse_menu_result = Menu(win, tearoff=0)
mouse_menu_result.add_command(label="copy", command=copy_text_result)
mouse_menu_result.add_command(label="clear", command=clear_result)
mouse_menu_result.add_command(label="select all", command=select_all_result)


def click_result(event):
    mouse_menu_result.tk_popup(event.x_root, event.y_root)


result_Entry.bind("<Button-3>", click_result)

#message box
def msgbx():
    msg = messagebox.showinfo(
        title='About', message='SeqCon\nversion 1.3\nAuthor:\nHassan Ghayas')
    return msg


menu = Menu(win)
win.config(menu=menu)

fileMenu = Menu(win, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="copy", command=copy_text)
fileMenu.add_command(label="paste", command=paste)
fileMenu.add_command(label="Exit", command=win.destroy)

editMenu = Menu(win, tearoff=0)
menu.add_cascade(label="help", menu=editMenu)
editMenu.add_command(label="About", command=msgbx)

win.mainloop()
