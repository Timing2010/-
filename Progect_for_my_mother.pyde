g = 250
f = 250
img=0
def setup():
    global img
    size(1000,1000)
    background(0)
    img=loadImage("Helpy.png")
def draw():
    clear()
    img=loadImage("Helpy.png")
    image(img,f,g,400,400)
    if g<0 or f<0 or g>599 or f>599:
        textSize(50)
        text(u'Game Over!!!',50,500)
def keyPressed():
    global g,f
    if key=="a":
        f = f - 5
    if key=="s":
        g = g + 5
    if key=="d":
        f = f + 5
    if key=="w":
        g = g - 5
        
        
        
     
        
