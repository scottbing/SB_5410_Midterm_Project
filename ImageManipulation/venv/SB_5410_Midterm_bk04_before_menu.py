# BSSD Midterm Project
# Scott Bing
# Image Analysis

from tkinter import *
from PIL import Image, ImageDraw, ImageTk


class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label

        # Show an image
        self.image = Image.open('bakery.jpeg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.imglbl = Label(self, image=self.photo)
        self.imglbl.grid(row=0, column=0, columnspan=4, sticky="nsew")

        print("Image Size: ", self.image.size)

        # this lines UNPACKS values
        # of variable a
        (h, w) = self.image.size

        # create a label and text entry for the name of a person
        Label(self,
              text="Image Size: " + str(h) + "x" + str(w)
              ).grid(row=1, column=0, sticky=W)
        # self.person_ent = Entry(self)
        # self.person_ent.grid(row=1, column=1, sticky=W)

        #self.grid_columnconfigure(2, weight=1)
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

        # create a filler
        Label(self,
              text=" "
              ).grid(row=8, column=0, sticky=W)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, "
        if self.is_joyous.get():
            adjectives += "joyous, "
        if self.is_electric.get():
            adjectives += "electric, "
        body_part = self.body_part.get()

        # create the story
        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."

        # display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


# main
root = Tk()
root.title("BSSD 5410 Midterm Scott Bing")
app = Application(root)
root.mainloop()
