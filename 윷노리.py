#import pygame engine
import pygame

#import random
import random

#import time
import time

#Initialize pygame engine
pygame.init()


#Define global variable
    #define function
def turn():
    random_list = [random.randint(0, 1) for x in range(4)]


    s = sum(random_list)

    if s == 1:
        if random_list == [1,0,0,0]:
            result = "빽도"
        else:
            result = "도"
    elif s == 2:
        result = "개"
    elif s == 3:
        result = "걸"
    elif s == 4:
        result = "윷"
    else:
        result = "모"

    print ('굴리는중.')
    time.sleep(0.4)
    print('굴리는중..')
    time.sleep(0.4)
    print('굴리는중...')
    time.sleep(0.4)


    print('결과는',result,'!')


    #define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
    #set the hight and width the screen
size = [1024,768]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("윷놀이")
    #loop until the user clicks the close button
done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(60) ##leave this out we use all cpu as we can
    
    #call images




#Main event loop

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYUP: #main turn event  ###Not Finished Yet!!
            turn()
            time.sleep(2)
            ###Draw new text code here
            
            
               
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    screen.fill(white) 
    

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    