import pygame
import time
import random
from clickimage import click_image
#from filename import functionname
#import clicktest

def make_sprite(image, x,y,width,height):
    food1sprite = pygame.sprite.Sprite()
    food1sprite.image = pygame.image.load(image)
    food1sprite.image = pygame.transform.scale(food1sprite.image, (width, height))
    food1rect = food1sprite.image.get_rect(topleft=(x,y))
    #food1rect.move(x,y)
    return food1sprite, food1rect

def dothis():
    global correct
    correctlist = [0, 2]
    correct = random.choice(correctlist)
    print("correct: " +str(correct))
    listofsymbols = ['treechinese.jpg', 'blank', 'spaghetti.png']
    heightlist = [250, 0, 75.9]
    
    food4sprite, food4rect = make_sprite(listofsymbols[correct], 200, 150, 250, int(heightlist[correct]))

    
food4sprite = ""
food4rect = ""
correct = 1


food1sprite, food1rect = make_sprite("5858454d4f6ae202fedf27d9.png", 700,450,250,250)
food2sprite, food2rect = make_sprite("unnamed.png", 700, 250, 250,250)
food3sprite, food3rect = make_sprite("maple-tree-transparent-background.png", 700, 10, 250,250)
food4sprite, food4rect = make_sprite("pingguo.png", 200, 150, 200,400)

def main():
    global correct

    pygame.init()
    X = 548*2
    Y = 368*2

    green = (0, 255, 0) 
    blue = (0, 0, 128)

    window = pygame.display.set_mode((X,Y))


    pygame.display.set_caption("Tony's window")



    



    food1value = "Wrong!"
    food2value = "Wrong!"
    food3value = "Wrong!"
    gameloop = True
    if correct==0:
        food1value = "Correct"
    elif correct==1:
        food2value = "Correct"
    elif correct==2:
        food3value = "Correct"

    while gameloop:
        
        #value = click_image(food2rect, gameloop, "Correct", dothis)
        #value2 = click_image(food1rect, gameloop, "Wrong!", dothis)
        #value3 = click_image(food3rect, gameloop, "Wrong!", dothis)
        #print(value)
        pygame.time.delay(-20)
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                gameloop=False
                pygame.quit()
            if (event.type==pygame.MOUSEBUTTONDOWN):
                
                
                value = click_image(food2rect, food2value)
                
                if food2value=="Correct":
                    dothis()
                value = click_image(food1rect, food1value)
                print(value)
                if food1value=="Correct":
                    dothis()
                value = click_image(food3rect, food3value)
                if food3value=="Correct":
                    dothis()

                
                
        
        book = pygame.image.load('books_vector_287226.jpg')

        book = pygame.transform.scale(book, (X,Y))

        bookrect = book.get_rect()
        

        pygame.display.flip()
        
        window.blit(book, bookrect)

        #food1rect =[700,450] #y is 450
        

        window.blit(food1sprite.image, food1rect)
        
        

        window.blit(food2sprite.image ,food2rect)

        window.blit(food3sprite.image ,food3rect)

        window.blit(food4sprite.image ,food4rect)

        
    pygame.quit()


main()

