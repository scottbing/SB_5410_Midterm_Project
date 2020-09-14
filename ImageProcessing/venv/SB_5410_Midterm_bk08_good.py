# BSSD Midterm Project
# Scott Bing
# Image Analysis

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk
import tkinter.font as font
from SortFunctions import selectionSort
from SortFunctions import quickSortRecursion
from SortFunctions import mergeSort
from SearchFunctions import binarySearchSub
from PixelFunctions import *
import colorsys
import os

TOGGLE_SLICE = False
TOLERENCE = False
RED = 183
GREEN = 198
BLUE = 144

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

        self.putImage(self.fileName)

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

    def putImage(self, fileName):
        # Show the user selected image
        self.image = Image.open(self.fileName)
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

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """

        # # Show a default image
        # self.image = Image.open('bakery.jpeg')
        # self.photo = ImageTk.PhotoImage(self.image)
        # self.imglbl = Label(self, image=self.photo)
        # self.imglbl.grid(row=0, column=0, columnspan=4, sticky="nsew")
        #
        # print("Current Image Size: ", self.image.size)
        #
        # # this lines UNPACKS values
        # # of variable a
        # (h, w) = self.image.size
        #
        # # create a label and text entry for the name of a person
        # Label(self,
        #       text="Current Image Size: " + str(h) + "x" + str(w)
        #       ).grid(row=1, column=0, sticky=W)

        # # create resize check button
        self.is_resize = BooleanVar()
        Checkbutton(self,
                    text="Resize",
                    variable=self.is_resize
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

        # Rotate Check button
        self.is_rotate = BooleanVar()
        Checkbutton(self,
                    text="Rotate Image",
                    variable=self.is_rotate
                    ).grid(row=3, column=0, sticky=W)
        Label(self,
              text="Angle:"
              ).grid(row=3, column=0, sticky=E)
        self.angle_ent = Entry(self, width=10)
        self.angle_ent.grid(row=3, column=1, sticky=W)

        # Flip image button
        self.is_flip = BooleanVar()
        Checkbutton(self,
                    text="Flip Image",
                    variable=self.is_flip
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

        # Reverse image button
        self.is_reverse = BooleanVar()
        Checkbutton(self,
                    text="Reverse Image",
                    variable=self.is_reverse
                    ).grid(row=5, column=0, sticky=W)

        # create color check button
        self.is_color = BooleanVar()
        Checkbutton(self,
                    text="Color",
                    variable=self.is_color
                    ).grid(row=5, column=0, sticky=E)

        # create grayscale check button
        self.is_gray = BooleanVar()
        Checkbutton(self,
                    text="GrayScale",
                    variable=self.is_gray
                    ).grid(row=5, column=1, sticky=W)

        # create a CheckBox and text entry for a Tolerance
        # Tolerance setting button
        self.is_tolerant = BooleanVar()
        Checkbutton(self,
                    text="Tolerance",
                    variable=self.is_tolerant
                    ).grid(row=6, column=0, sticky=W)
        self.tolerance_ent = Entry(self, width=8)
        self.tolerance_ent.grid(row=6, column=0, sticky=E)

        # create a CheckBox and text entry for a Brightness
        # Brightness setting button
        self.is_bright = BooleanVar()
        Checkbutton(self,
                    text="Brightness",
                    variable=self.is_bright
                    ).grid(row=7, column=0, sticky=W)
        self.tolerance_ent = Entry(self, width=8)
        self.tolerance_ent.grid(row=7, column=0, sticky=E)

        # create a CheckBox and text entry for a Sharpness
        # Sharpness setting button
        self.is_sharp = BooleanVar()
        Checkbutton(self,
                    text="Brightness",
                    variable=self.is_sharp
                    ).grid(row=8, column=0, sticky=W)
        self.tolerance_ent = Entry(self, width=8)
        self.tolerance_ent.grid(row=8, column=0, sticky=E)

        # create a filler
        Label(self,
              text=" "
              ).grid(row=9, column=0, sticky=W)

        btnFont = font.Font(weight="bold")
        btnFont = font.Font(size=20)


        # create a the generate button
        self.generate_btn = Button(self,
                                   text="Generate",
                                   command=self.processSelections,
                                   # bg='blue',
                                   # fg='#ffffff',
                                   highlightbackground='#3E4149',
                                   font = btnFont
                                   ).grid(row=9, column=1, sticky=NSEW)
    # Check for numeric and 0-255
    # https://stackoverflow.com/questions/31684083/validate-if-input-string-is-a-number-between-0-255-using-regex
    # numeric validation
    def is_number(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False
    #end def is_number(n):

    # reverse the image
    def reverse(self):
        with Image.open(self.fileName) as im:
            pixels, yiq_pixels = storePixels(im)  # store rgb pixels

            # selectionSort(yiq_pixels, comparePixels) #sort on first val
            mergeSort(yiq_pixels, comparePixels)  # sort on first val
            ## may need sorted image to see what is going on
            sorted_im = pixelsToImage(im, yiq_pixels)
            sorted_im.save('sorted_' + base[1] + '.jpg', 'JPEG')
            print("sorted pixels")

        if self.is_gray.get() == True:
            grayScale(im, pixels)  # grayscale pixels in place
        # manipulate file name for save process
        baseFile = self.fileName.split('/')
        length = len(baseFile)
        base = baseFile[len(baseFile) - 1]
        print(baseFile[len(baseFile) - 1])
        # save reversed image
        out.save('reverse-' + base)
        print("file reverse-" + base + " saved")

    # flip image on vertical axis
    def flip_vertical(self):
        # get current image
        im = Image.open(self.fileName)
        # manipulate file name for save process
        baseFile = self.fileName.split('/')
        length = len(baseFile)
        base = baseFile[len(baseFile) - 1]
        print(baseFile[len(baseFile) - 1])
        # flip image vertiical
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
        # save flipped image
        out.save('fl_vertical-' + base)
        print("file fl_vertical-" + base + " saved")

    # flip image on horizontal axis
    def flip_horizontal(self):
        # get current image
        im = Image.open(self.fileName)
        baseFile = self.fileName.split('/')
        # manipulate file name for save process
        length = len(baseFile)
        base = baseFile[len(baseFile) - 1]
        print(baseFile[len(baseFile) - 1])
        # flip image horizontal
        out = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        # save flipped image
        out.save('fl_horizontal-' + base)
        print("file fl_horizontal-" + base + " saved")

    # rotate an image
    def rotate(self):
        # get current image
        im = Image.open(self.fileName)
        baseFile = self.fileName.split('/')
        # manipulate file name for save process
        length = len(baseFile)
        base = baseFile[len(baseFile) - 1]
        print(baseFile[len(baseFile) - 1])
        # get new size
        angle = (int(self.angle_ent.get()))
        print("angle: ", angle)
        # rotate image
        out = im.rotate(angle)
        # save rotated image
        out.save('rotated-' + base)
        print("file rotated-" + base + " saved")

    # resize an image
    def resize(self):
        # get current image
        im = Image.open(self.fileName)
        baseFile = self.fileName.split('/')
        # manipulate file name for save process
        length = len(baseFile)
        base = baseFile[len(baseFile)-1]
        print(baseFile[len(baseFile)-1])
        # get new size
        size = (int(self.height_ent.get()), int(self.width_ent.get()))
        print("size: ", size)
        # resize image
        out = im.resize(size)
        # save resized image
        out.save('resized-' + base)
        print("file resized-" + base + " saved")

    # process user selections
    def processSelections(self):

        if self.is_resize.get() == True:
           self.resize()
        elif self.is_rotate.get() == True:
            self.rotate()
        elif self.is_flip.get() == True:
            if self.is_vertical.get() == True:
                self.flip_vertical()
            elif self.is_horizontal.get() == True:
                self.flip_horizontal()
        elif self.is_reverse.get() == True:
            self.reverse()

    def processImage(self):
        global TOGGLE_SLICE
        global RED
        global GREEN
        global BLUE
        global TOLERENCE

        print("filename", self.fileName)
        print(os.path.splitext(self.fileName)[0])
        file = os.path.splitext(self.fileName)[0]
        print(file.split('/'))
        base = file.split('/')
        print(base[1])


        # read each pixel into memory as the image object im
        # with Image.open(IMG_NAME + '.jpg') as im:
        with Image.open(self.fileName) as im:
            pixels, yiq_pixels = storePixels(im)  # store rgb pixels

            # selectionSort(yiq_pixels, comparePixels) #sort on first val
            mergeSort(yiq_pixels, comparePixels)  # sort on first val
            ## may need sorted image to see what is going on
            sorted_im = pixelsToImage(im, yiq_pixels)
            sorted_im.save('sorted_' + base[1] + '.jpg', 'JPEG')
            print("sorted pixels")

            grayScale(im, pixels)  # grayscale pixels in place
            # replace threshold with target color to pivot around
            target = (int(RED) / 255, int(GREEN) / 255, int(BLUE) / 255)  # /255 for conversiono
            print("RED: ", RED)
            print("GREEN: ", GREEN)
            print("BLUE: ", BLUE)
            yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])

            if TOLERENCE:
                tolerance1 = int(len(yiq_pixels) / 2)
                print("Tolerance1: ", tolerance1)
                subi = tolerance1
                # use yiq_target instead  of threshold in search
                subi = binarySearchSub([r[0][0] for r in yiq_pixels],
                                       0, len(yiq_pixels) - 1, yiq_target[0])
                im.show()
                tolerance2 = int(len(yiq_pixels) / 4)
                print("Tolerance2: ", tolerance2)
                subi = tolerance2
                # use yiq_target instead  of threshold in search
                subi = binarySearchSub([r[0][0] for r in yiq_pixels],
                                       0, len(yiq_pixels) - 1, yiq_target[0])
                im.show()
                tolerance3 = int(len(yiq_pixels) / 8)
                print("Tolerance3: ", tolerance3)
                subi = tolerance3
                # use yiq_target instead  of threshold in search
                subi = binarySearchSub([r[0][0] for r in yiq_pixels],
                                       0, len(yiq_pixels) - 1, yiq_target[0])
                im.show()

                TOLERENCE = False  # reset tolerance
            else:
                # use yiq_target instead  of threshold in search
                subi = binarySearchSub([r[0][0] for r in yiq_pixels],
                                       0, len(yiq_pixels) - 1, yiq_target[0])

            print("subi:", subi)
            # subi = binarySearchSub([r[0][0] for r in sorted_pixels],
            #                        0, len(sorted_pixels) - 1, threshold)
            if (TOGGLE_SLICE):
                pixelsToPoints(im, yiq_pixels[0:subi])  # put saved pixels on gray
            else:
                pixelsToPoints(im, yiq_pixels[subi:])
            im.show()
        # end with Image.open(IMG_NAME + '.jpg') as im:
    # end while(True):



# main
root = Tk()
root.title("BSSD 5410 Midterm Scott Bing")
app = Application(root)
root.mainloop()
