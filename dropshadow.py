from PIL import Image, ImageFilter

"""
Drop shadows with PIL.

Author: Kevin Schluff
Modifications: Matt Milliken
License: Python license
"""
from PIL import Image, ImageFilter
import math

def askopenfilename():

    return tkFileDialog.askopenfilename()

def askDirectory():
  return tkFileDialog.askdirectory()

def dropShadow( imageName, offset=(0,0), background=0xffffff, shadow=0x444444,
                border=8, iterations=3):
  """
  Add a gaussian blur drop shadow to an image.

  image       - The image to overlay on top of the shadow.
  offset      - Offset of the shadow from the image as an (x,y) tuple.  Can be
                positive or negative.
  background  - Background colour behind the image.
  shadow      - Shadow colour (darkness).
  border      - Width of the border around the image.  This must be wide
                enough to account for the blurring of the shadow.
  iterations  - Number of times to apply the filter.  More iterations
                produce a more blurred shadow, but increase processing time.
  """

  # Create the backdrop image -- a box in the background colour with a
  # shadow on it.
  imageName = askopenfilename()
  image = Image.open(imageName, 'r')

  image.thumbnail( (200,200), Image.ANTIALIAS)

  totalWidth = image.size[0] + abs(offset[0]) + 2*border
  totalHeight = image.size[1] + abs(offset[1]) + 2*border
  back = Image.new(image.mode, (410, 300), background)

  # Place the shadow, taking into account the offset from the image
  shadowLeft = border + max(offset[0], 0)
  shadowTop = border + max(offset[1], 0)
  #back.paste(shadow, [shadowLeft, shadowTop, shadowLeft + image.size[0],
    #shadowTop + image.size[1]] )

  x1 = int(math.floor((410 - image.size[0]) / 2))
  y1 = int(math.floor((300 - image.size[1]) / 2))
  back.paste(shadow, (x1, y1, x1 + image.size[0]+5, y1 + image.size[1]+5))

  # Apply the filter to blur the edges of the shadow.  Since a small kernel
  # is used, the filter must be applied repeatedly to get a decent blur.
  n = 0
  while n < iterations:
    back = back.filter(ImageFilter.BLUR)
    n += 1

  # Paste the input image onto the shadow backdrop
  imageLeft = border - min(offset[0], 0)
  imageTop = border - min(offset[1], 0)

  x1 = int(math.floor((410 - image.size[0]) / 2))
  y1 = int(math.floor((300 - image.size[1]) / 2))
  back.paste(image, (x1, y1, x1 + image.size[0], y1 + image.size[1]))


  #back.paste(image, (imageLeft, imageTop))

  #back.show()
  dest = askDirectory() + "/" + E.get() +".png"
  back.save(dest, "PNG")

  return back


import sys

# image = Image.open('one.jpg', 'r')
# image.thumbnail( (200,200), Image.ANTIALIAS)

#dropShadow('one.jpg').show()

#dropShadow(image).show()
#dropShadow(image, background=0xeeeeee, shadow=0x444444, offset=(0,5)).show()



import Tkinter
from Tkinter import Entry, Text, END, LEFT, BOTTOM, Label
import tkFileDialog

top = Tkinter.Tk()
top.wm_title("Matt's Icon Maker")
# Code to add widgets will go here...
text = Text(top, state='disabled', width=70, height=5)
text.configure(state='normal')
text.insert(END," 1) Enter name for icon file (eg \"icon\"), extension not needed\n 2) Click Generate Icon, select file to iconize in first file dialog \n 3) Select save location in second file dialog")
text.configure(state='disabled')
text.pack(side=LEFT)

E = Entry(top)
L1 = Label(top, text="File Output Name")
L1.pack( side = BOTTOM)
E = Entry(top, bd =5)

E.pack(side = BOTTOM)





B = Tkinter.Button(top, text="Generate Thumbnail", command=lambda : dropShadow('doesnt'))
B.pack(side=BOTTOM)


# text.pack(side=BOTTOM)

top.mainloop()




