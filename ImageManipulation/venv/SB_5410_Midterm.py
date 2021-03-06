# BSSD Midterm Project
# Scott Bing
# Image Analysis

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk
import tkinter.font as font


class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)

        Frame.__init__(self, master)
        self.master = master

        # reverse_btn = Button(self)

        # create menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="New", command=self.donothing)
        fileMenu.add_command(label="Open", command=self.openFile)
        fileMenu.add_command(label="Save", command=self.donothing)
        fileMenu.add_command(label="Save as...", command=self.donothing)
        fileMenu.add_command(label="Close", command=self.donothing)

        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", command=root.quit)
        menu.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(menu, tearoff=0)
        editMenu.add_command(label="Undo", command=self.donothing)

        editMenu.add_separator()

        editMenu.add_command(label="Cut", command=self.donothing)
        editMenu.add_command(label="Copy", command=self.donothing)
        editMenu.add_command(label="Paste", command=self.donothing)
        editMenu.add_command(label="Delete", command=self.donothing)
        editMenu.add_command(label="Select All", command=self.donothing)

        menu.add_cascade(label="Edit", menu=editMenu)
        helpMenu = Menu(menu, tearoff=0)
        helpMenu.add_command(label="Help Index", command=self.donothing)
        helpMenu.add_command(label="About...", command=self.donothing)
        menu.add_cascade(label="Help", menu=helpMenu)

        self.grid()
        self.create_widgets()

    def openFile(self):
        self.fileName = askopenfilename(parent=self, initialdir="C:/", title='Choose an image.')
        print(self.fileName)

    def exitProgram(self):
        exit()

    def donothing(self):
        pass

    def generate(self):
        pass

    def reverse(self):

        if self.reverse_btn.config('relief')[-1] == 'sunken':
            self.reverse_btn.config(relief="raised")
        else:
            self.reverse_btn.config(relief="sunken")

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """

        # Show a default image
        self.image = Image.open('bakery.jpeg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.imglbl = Label(self, image=self.photo)
        self.imglbl.grid(row=0, column=0, columnspan=4, sticky="nsew")

        print("Current Image Size: ", self.image.size)

        # this lines UNPACKS values
        # of variable a
        (h, w) = self.image.size

        # create a label and text entry for the name of a person
        Label(self,
              text="Current Image Size: " + str(h) + "x" + str(w)
              ).grid(row=1, column=0, sticky=W)
        # self.person_ent = Entry(self)
        # self.person_ent.grid(row=1, column=1, sticky=W)

        # self.grid_columnconfigure(2, weight=1)
        # self.grid_columnconfigure(4, weight=1)

        # create a label and text entry for a plural noun
        Label(self,
              text="Resize Image:"
              ).grid(row=2, column=0, sticky=W)
        Label(self,
              text="Height:"
              ).grid(row=2, column=0, sticky=E)
        self.height_ent = Entry(self, width=10)
        self.height_ent.grid(row=2, column=1, sticky=W)
        Label(self,
              text="Width:"
              ).grid(row=2, column=1, sticky=E)
        self.width_ent = Entry(self, width=10)
        self.width_ent.grid(row=2, column=2, sticky=W)

        # create a label and text entry for a verb
        Label(self,
              text="Rotate Image:"
              ).grid(row=3, column=0, sticky=W)
        Label(self,
              text="Angle:"
              ).grid(row=3, column=0, sticky=E)
        self.angle_ent = Entry(self, width=10)
        self.angle_ent.grid(row=3, column=1, sticky=W)

        # flip image horizontal or vertical
        Label(self,
              text="Flip Image:"
              ).grid(row=4, column=0, sticky=W)

        # create vertical check button
        self.is_vertical = BooleanVar()
        Checkbutton(self,
                    text="Vertical",
                    variable=self.is_vertical
                    ).grid(row=4, column=0, sticky=E)

        # create horizontal check button
        self.is_horizontal = BooleanVar()
        Checkbutton(self,
                    text="Horizontal",
                    variable=self.is_horizontal
                    ).grid(row=4, column=1, sticky=W)

        # create a label and text entry for a Tolerance
        Label(self,
              text="Tolerance:"
              ).grid(row=5, column=0, sticky=W)
        self.tolerance_ent = Entry(self, width=8)
        self.tolerance_ent.grid(row=5, column=0, sticky=E)

        # create a label and text entry for a Brightness
        Label(self,
              text="Brightness:"
              ).grid(row=6, column=0, sticky=W)
        self.brightness_ent = Entry(self, width=8)
        self.brightness_ent.grid(row=6, column=0, sticky=E)

        # create a label and text entry for a Sharpness
        Label(self,
              text="Sharpness:"
              ).grid(row=7, column=0, sticky=W)
        self.sharpness_ent = Entry(self, width=8)
        self.sharpness_ent.grid(row=7, column=0, sticky=E)

        self.reverse_btn = Button(self,
                                  text="Reverse",
                                  relief="sunken",
                                  command=self.reverse
                                  ).grid(row=8, column=0, sticky=W)

        # create a filler
        Label(self,
              text=" "
              ).grid(row=9, column=0, sticky=W)

        btnFont = font.Font(weight="bold")
        btnFont = font.Font(size=20)


        # create a the generate button
        self.generate_btn = Button(self,
                                   text="Generate",
                                   command=self.generate,
                                   # bg='blue',
                                   # fg='#ffffff',
                                   highlightbackground='#3E4149',
                                   font = btnFont
                                   ).grid(row=9, column=1, sticky=NSEW)


# main
root = Tk()
root.title("BSSD 5410 Midterm Scott Bing")
app = Application(root)
root.mainloop()
