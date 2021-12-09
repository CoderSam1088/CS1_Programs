import pygame
import time
import random
#from clickimage import click_image
#from filename import functionname
#from clicktest import image_clicked

def make_image(image,xpos,ypos,width,height):
    spriting = pygame.image.load(image)
    spriting = pygame.transform.scale(spriting, (width, height))
    #spriting.rect.x = xpos
    #spriting.rect.y = ypos
    #spriting.get_rect.move((x,y))
    #recting.move(x,y)
    return spriting


def image_clicked(image,event,startx,starty, param):
    """Tell which image to use, event, xcoord, ycoord, and True or False for correct"""
    x=event.pos[0]-startx
    y=event.pos[1]-starty
    if image.get_rect().collidepoint(x,y):
        if param:
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False

def whatround(rounds):
    listofy = [10, 250, 450]
    rand1 = random.randint(0,2)
    rand2 = random.randint(0,1)
    yy1 = listofy.pop(rand1)
    yy2 = listofy.pop(rand2)
    yy3 = listofy[0]
    if rounds==2:
        image1 = "images/Apple.png"
        image2 = "images/Burger.png"
        image3 = "images/Cat.png"
        image4 = "images/Dog.png"
    else:
        image1 = "images/Dog.png"
        image2 = "images/Pizza.png"
        image3 = "images/Tiger.png"
        image4 = "images/Apple.png"
    return image1, image2, image3, image4,yy1,yy2,yy3

    
    
    
        

"""
food1sprite = make_image("5858454d4f6ae202fedf27d9.png", 700,450,250,250)
food2sprite = make_image("unnamed.png", 700, 250, 250,250)
food3sprite = make_image("maple-tree-transparent-background.png", 700, 10, 250,250)
food4sprite = make_image("pingguo.png", 200, 150, 200,400)
"""

def main():

    pygame.init()
    X = 548*2
    Y = 368*2

    #green = (0, 255, 0) 
    #blue = (0, 0, 128)

    window = pygame.display.set_mode((X,Y))


    pygame.display.set_caption("Tony's window")

    food1sprite = make_image("5858454d4f6ae202fedf27d9.png", 700,450,200,200)
    food2sprite = make_image("unnamed.png", 700, 250, 200,200)
    food3sprite = make_image("maple-tree-transparent-background.png", 700, 10, 200,200)
    food4sprite = make_image("pingguo.png", 200, 150, 200,400)

    


    """
    food1value = "Wrong!"
    food2value = "Wrong!"
    food3value = "Wrong!"
    """
    

    """
    if correct==0:
        food1value = "Correct"
    elif correct==1:
        food2value = "Correct"
    elif correct==2:
        food3value = "Correct"
    """
    book = pygame.image.load('books_vector_287226.jpg')

    book = pygame.transform.scale(book, (X,Y))

    bookrect = book.get_rect()
        
    x1, y1 = 700,450
    x2, y2 = 700, 250
    x4, y4 = 200, 150
    x3=700
    y3=10
        

    gameloop = True
    whichround=1
    while gameloop:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                gameloop=False
            if (event.type==pygame.MOUSEBUTTONDOWN):
                if (image_clicked(food3sprite, event,x3,y3, True)):
                    whichround+=1
                    i1,i2,i3,i4,y1,y2,y3 = whatround(whichround)
                    food1sprite = make_image(i1, x1,y1,200,200)
                    food2sprite = make_image(i2, x2,y2, 200,200)
                    food3sprite = make_image(i3, x3,y3, 200,200)
                    food4sprite = make_image(i4, x4,y4, 200,200)  
                image_clicked(food2sprite, event,x2,y2, False)
                image_clicked(food1sprite, event,x1,y1, False)
                
        window.blit(book, bookrect)
        window.blit(food1sprite,  (x1,y1))
        window.blit(food2sprite , (x2,y2))
        window.blit(food3sprite , (x3,y3))
        window.blit(food4sprite , (x4,y4))
        pygame.display.flip()
        
    pygame.quit()


main()

