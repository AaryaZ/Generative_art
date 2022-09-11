Degrees= 360
r=255
g=255
b=255

def setup():
    global displayWidth,displayHeight
    size(displayWidth / 2,displayHeight)

    noFill()
    # strokeWeight(10)
    # background(0)
    
    
def draw():
    background(0)
    radius = height/3
    center_x=width/2
    center_y=height /2
    
    global Degrees,r,g,b
    stroke (r,g,b)
    
    # stroke (255)
    # strokeWeight(10)
    
    beginShape()
    for i in range(Degrees):
        # fill(r,g,b)
        x=center_x + radius* cos(radians(i)) + random(100)
        y=center_y + radius* sin(radians(i)) + random(100)
        curveVertex(x,y)
        r=random(255)
        g=random(255)
        b=random(255)
    
    endShape(CLOSE)
    
