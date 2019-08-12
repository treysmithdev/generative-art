

#############################################
## Landscape
#############################################


def setup():
    size(1280,720)
    background(50,50,50)
    frameRate(60)


bg = color(50,50,50)

c1 = color(185,103,255)
c2 = color(255,113,206)
c3 = color(193,12,11)
c4 = color(220,4,12)
c5 = color(255,251,150, 75)



def draw():

#############################################
## sky
#############################################

    if(frameCount == 1):
        for l in xrange(0, height, 23):
            
            stroke(c2)
            strokeWeight(1)
            
            # Straight across
            line(0,l,width,l)
            
        for l2 in xrange(0, width, 23):
            
            stroke(c2)
            strokeWeight(1)
            
            rotateX(radians(180))
            # Straight across
            line(l2,0,l2,height)
        
#############################################
## mountain ridge
#############################################
    
    if(frameCount == 1):
        landscape_anchor = (height/4)*3
        
        fill(c1)
        stroke(c1)
        rect(0,landscape_anchor,width, height/4)
        
        
        r_low = landscape_anchor
        r_high = landscape_anchor - (height/10)
        
        ridge_cnt = random(5,12)
        
        
        r_list = []
        for t in xrange(0,ridge_cnt):
                
            r_list.append(random(20,50))
            
        
        ttl = sum(r_list)
        
        r_start = 0
        
        for i in r_list:
            
            start_x = r_start
            start_y = landscape_anchor
            
            end_x = start_x + (width * (i/ttl))  
            end_y = landscape_anchor
                    
            top_x = random(start_x, end_x)
            top_y = random(r_high, r_low) 
                
            triangle(start_x,start_y,top_x,top_y,end_x,end_y)
            
            r_start = end_x
    
#############################################
## sun
#############################################
   
    rectMode(CENTER)
    
    fill(c3)
    stroke(c4)
    
    
    
    
    sun_top = height/9
    sun_bottom = (height/7) * 3.35
    
    sun_top_l = (width/7.65)*3
    sun_top_r = width - sun_top_l
    
    sun_btm_l = sun_top_l * 1.075
    sun_btm_r = width - sun_btm_l
    
    strokeWeight(5)
    noFill()
    quad(sun_top_l, sun_top, sun_top_r, sun_top, sun_btm_r, sun_bottom, sun_btm_l, sun_bottom)
    
    fill(c3)
    stroke(c4)
    
    in_fct = 15
    quad(sun_top_l + in_fct, sun_top + in_fct, sun_top_r- in_fct, sun_top + in_fct, sun_btm_r- in_fct, sun_bottom - in_fct, sun_btm_l + in_fct, sun_bottom - in_fct)
    
    fill(c3)
    stroke(c4)
    noFill() 
    
    for i in xrange(0,7):
        
        fctr = i * 25
        
        line(sun_btm_l - fctr/2, sun_bottom+fctr, sun_btm_r + fctr/2, sun_bottom+fctr)
        
        # line(sun_top_l-fctr, sun_top+fctr, sun_btm_l-fctr, sun_bottom)
        # line(sun_top_r+fctr, sun_top+fctr, sun_btm_r+fctr, sun_bottom)
        
