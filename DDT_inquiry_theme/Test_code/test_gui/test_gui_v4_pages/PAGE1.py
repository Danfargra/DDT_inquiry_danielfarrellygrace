from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg'] = '#5d8a82'

f = ("Times bold", 14)



def nextPage():
    ws.destroy()
    import v1_skeleton.test_gui.test_gui_v4_pages.PAGE2 as PAGE2


def prevPage():
    ws.destroy()
    import PAGE3


Label(
    ws,
    text="This is First page",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Previous Page",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()



PAGES

from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import PAGE3


def prevPage():
    ws.destroy()
    import v1_skeleton.test_gui.test_gui_v4_pages.PAGE1 as PAGE1


Label(
    ws,
    text="This is Second page",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Previous Page",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()



PAGES

from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import v1_skeleton.test_gui.test_gui_v4_pages.PAGE1 as PAGE1


def prevPage():
    ws.destroy()
    import v1_skeleton.test_gui.test_gui_v4_pages.PAGE2 as PAGE2


Label(
    ws,
    text="This is Third page",
    font=f,
    padx=20,
    pady=20,
    bg='#bfff00'
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Previous Page",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()