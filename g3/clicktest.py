import pygame

def make_image(image,width,height):
    spriting = pygame.image.load(image)
    spriting = pygame.transform.scale(spriting, (width, height))
    #food1rect = food1sprite.get_rect(topleft=(x,y))
    #food1rect.move(x,y)
    return spriting

def image_clicked(image, func, event,startx,starty):
    x= event.pos[0]-startx
    y = event.pos[1]-starty

    if image.get_rect().collidepoint(x,y):
        print("clicked an image")

        
def main():
    pygame.init()
    width=548*2
    height=368*2
    screen = pygame.display.set_mode( (width, height ) )
    pygame.display.set_caption('clicked on image')

    image1=make_image("5858454d4f6ae202fedf27d9.png", 250, 250)

    image2=make_image("unnamed.png", 250, 250)
    #image3=make_image("maple-tree-transparent-background.png", 250, 250)
    #image4=make_image("pingguo.png", 250, 250)
    
    book = pygame.image.load('books_vector_287226.jpg')
    book = pygame.transform.scale(book, (width,height))

    bookrect = book.get_rect()

    x1 = 100; # x coordnate of image
    y1 = 100; # y coordinate of image
    x2=700
    y2=250
    x3=700
    y3=10
    x4=200
    y4=150
    screen.blit(book, bookrect)
    screen.blit(image1 ,  ( x1,y1)) # paint to screen
    screen.blit(image2 ,  ( x2,y2))
    #screen.blit(image3 ,  ( x3,y3))
    #screen.blit(image4 ,  ( x4,y4))
    pygame.display.flip() # paint screen one time

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                image_clicked(image1, "test", event,x1,y1)
                print("sprintrect: " +str(image1.get_rect()))
                print("position: " +str(event.pos))
            
    #loop over, quite pygame
    pygame.quit()

if __name__=="__main__":
    main()
    
