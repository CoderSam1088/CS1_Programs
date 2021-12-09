import pygame
#from Chinsesgame import make_sprite

pygame.init()
X = 548*2
Y = 368*2

green = (0, 255, 0) 
blue = (0, 0, 128)

window = pygame.display.set_mode((X,Y))


pygame.display.set_caption("Tony's window")

def click_image(imagerect,string):
    
    x, y = pygame.mouse.get_pos()
    if imagerect.collidepoint(x,y):
        print(string)
        return(string)


def main():          
    food1sprite, food1rect = make_sprite("5858454d4f6ae202fedf27d9.png", 700,450, 250,250)

    print(food1rect)

    gameloop=True
    testing = 0

    while gameloop:
        value = click_image(food1rect, gameloop)
        if value == False:
            gameloop=False
            pygame.quit()
        pygame.display.flip()

        window.blit(food1sprite.image ,[700,450])

if __name__=="__main__":
    main()
    
    
    
            
