# nikola's well

### Description

This is my first go at creating generative art. I've been super into vaporwave art and more so their color schemes. So with that in mind, I wanted to make something like that.

### Challenges

The biggest challenge of this project was figuring out how to randomly generate lines around a circle's circumference. It's a simple task to do it from a single point, but I wanted to leave the middle empty. After brushing up on my trigonometry I was able to implement the algorithm pretty easily.

[Parametric Form](https://en.wikipedia.org/wiki/Circle#Equations)


```
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
```
----

![nikolas-well](./nikolas-well.gif)