

##############################
# nikola's well
##############################


def setup():
    size(500, 500) # canvas size
    background(50,50,50) # bg color
    frameRate(60)

##############################
# globals
##############################
bg = color(50,50,50)
pink = color(255,113,206)
purple = color(185,103,255)
darkred = color(255,41,115)

ht = 500

def circleLine(d):
    
    h = width/2
    k = ht/2
    innerR = 75
    angle = radians(d)
    
    startingX = innerR*cos(radians(d))+h
    startingY = innerR*sin(radians(d))+k
    
    
    
    outerR = random(90,225)
    
    endingX = outerR*cos(radians(d))+h + (random(-1,1)*random(150))
    endingY = outerR*sin(radians(d))+k  + (random(-1,1)*random(150))
    
    line(startingX,startingY,endingX,endingY)
    
def draw():
    
    
    strokeWeight(1)
    
    triangle(5,5,5,50,50,5)
    
    ellipse(width/2, ht/2, 150, 150)
    
    noFill()
     
    
##############################
# outer ring
##############################
    
    for i in xrange(0,10):
        if(i % 2 == 0):
            stroke(255,113,206)
        else: 
            stroke(185,103,255)
        
        
        
        circleLine(random(360))
        stroke(50,50,50)
        strokeWeight(2)
        ellipse(width/2, ht/2, 150, 150)
        
        strokeWeight(3)
        ellipse(width/2, ht/2, 450, 450)
        
        
        strokeWeight(1)
        
    for c in xrange(450, ht*2):
            
        ellipse(width/2, ht/2, c, c)
    
    fill(50,50,50)   
    ellipse(width/2, ht/2, 150, 150)
      
    
##############################
# sun 
##############################   

    strokeWeight(0)
    
    sun = random(1)
    if(sun < .75):
        
    
        ray_c = color(255,251,150,25)
        fill(ray_c)
        
        triangle(60,60,485,485,380,485)
        
        sun_c = color(255,251,150)
        fill(sun_c)
        ellipse(60,60, 50,50)
        
    elif(sun >.97):

        fill(bg)
        triangle(60,60,490,490,400,490)

        
    elif(sun >.94):
        
        ray_c = color(255,41,115,200)
        fill(ray_c)
        triangle(60,60,485,485,390,485)
        
        sun_c = color(255,41,115)
        fill(sun_c)

        
                  
    elif(sun >.91):
        
        ray_c = color(255,144,31,190)
        fill(ray_c)
        triangle(60,60,485,485,390,485)
        
        sun_c = color(255,144,31)
        fill(sun_c)

    
    ellipse(60,60, 50,50)
  
    
##############################
# inner ring
##############################    
    
    if(frameCount % 1 == 0 and frameCount > 60):
        
        ring = 150-((frameCount%60) * 2.5)
    
        for r in xrange(ring, 150, 20):
        
            stroke(185,103,255, 175)
            strokeWeight(4)
            
            noFill()
            
            fillcenter = [0,1,2,59]
            filldict = {0:pink,59:purple,2:pink,1:darkred}
            
            if(frameCount%60 in fillcenter):                                
                fill(filldict[(frameCount%60)],175)
                stroke(filldict[(frameCount%60)],175)
                ellipse(width/2, ht/2, 150, 150)
            else:
                ellipse(width/2, ht/2, r, r)
    
