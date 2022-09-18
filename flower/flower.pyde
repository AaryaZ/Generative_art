Degrees= 360
r=255
g=255
b=255
radius=0

def setup():
    global displayWidth,displayHeight,radius
    size(displayWidth / 2,displayHeight)
    radius=height/2
    noFill()
    background(0)
    
    
    
def draw():
    
    #
    center_x=width/2
    center_y=height /2
    
    global Degrees,r,g,b,radius
    stroke (r,g,b,25)
    # fourth paramerter is for opacity
    

    
    beginShape()
    for i in range(Degrees):
        n=noise(i*0.02,float(frameCount)/100)
        x=center_x + radius* cos(radians(i)) *n
        y=center_y + radius* sin(radians(i)) *n
        curveVertex(x,y)
        r=random(255)
        g=random(100)
        b=random(255)
    
    endShape(CLOSE)
    radius -=1
    
    
    if radius ==0 :
        noLoop()
        #To stop once radius is equal to zero otherwise radius is -ve and it grows outward
    save("Aarya.png")
