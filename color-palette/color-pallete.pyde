
## ///////////////////////////////////////////////////////////////////////////
## // color-palette
## ///////////////////////////////////////////////////////////////////////////

# This is an program to be used to generate random palettes based off of the 
# GitHub project: https://github.com/Jam3/nice-color-palettes
#
# This script can be used in any project and this is more so the base of it. 

def setup():
    size(520,210)
    noLoop()
    background(255,255,255)
     
cPalette = ''

def createColorPalette(input_file, num):
    
    global c0
    global c1
    global c2
    global c3
    global c4
    global palette
    global cPalette

    
    raw = input_file[0]
    
    
    colorPalettes = []
     
    # Parse json file dicts
    for left in raw.split('['):
    
        for right in left.split(']'):
        
            colorPalette = []
            if(right != ',' and len(right) > 0):
                
                for i in right.split(','):
                    
                    colorPalette.append('FF'+i.replace('"','').replace('#',''))
                
                
                colorPalettes.append(colorPalette)
            
    
    # Assign color palette to variables                
    palette = colorPalettes[num]
    
    bg = color(255,255,255)
    c0 = unhex(palette[0])
    c1 = unhex(palette[1])
    c2 = unhex(palette[2])
    c3 = unhex(palette[3])
    c4 = unhex(palette[4])
    
    cPalette = [c0,c1,c2,c3,c4]

    
# color def file 
color_file = loadStrings("/Users/treysmith/art/processing/color_pallete/data/1000.json")

  
paletteNumber = int(round(random(0,999)))

createColorPalette(color_file, paletteNumber)

pHeader = 'Palette #'+ str(paletteNumber)
pDetail = palette

def draw():


    for x in xrange(0,5):

        fill(cPalette[x])
        rect(100*x + 10,10,100,100)
        
        textSize(32)
        textAlign(CENTER)
        fill(color(15,15,15))
        text(pHeader, width/2, 155)
        textSize(14)
        text(str(pDetail).replace('u\'','\'').replace('\'',''), width/2, 185)
        
