intro =  True

def gameloop():
    
    global intro

    def pause():

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        paused = False
            gameDisplay.fill(yellow)
            msg_to_user("PAUSED",
                        green,
                        "super_large",
                        -200)

            msg_to_user("Press c to continue, q to quit",
                        black,
                        "medium",
                        100)
            pygame.display.update()
            
            clock.tick(5) # lowers fps when paused

    def score(score):
        ScoreSurface = medium_font.render("Score: "+str(score),True,black)

        gameDisplay.blit(ScoreSurface, [0,0])

    def snake(square_side,coordinates):

        head = pygame.transform.rotate(snakeimage,rotating_degrees)

        
        gameDisplay.blit(head, (coordinates[-1][0],coordinates[-1][1]))
        
        for X_Y in coordinates[:-1]:
            pygame.draw.rect(gameDisplay,green,(X_Y[0],X_Y[1],square_side,square_side)) #when in a for loop, draws them together

    def msg_to_user(msg,color,size = "medium",extra_depth = 0):
        if size == "small":
            TextSurface = small_font.render(msg,True,color)
        elif size == "medium":
            TextSurface = medium_font.render(msg,True,color)
        elif size == "super large":
            TextSurface = super_large_font.render(msg,True,color)
        else:
            TextSurface = large_font.render(msg,True,color)
            
        TextRectangle = TextSurface.get_rect()
        TextRectangle.center = (x_pixels / 2), ((y_pixels /2 ) + extra_depth)
        gameDisplay.blit(TextSurface , TextRectangle)
        

        #the next 3 lines work and is easier
    ##        my_font = pygame.font.SysFont(None,30) 
    ##        screen_text = my_font.render(msg,True,color,black) # pygame.font.Font.render(msg, anti-alias, color, bg)
    ##        gameDisplay.blit(screen_text, [x_pixels/2 - screen_text.get_width()/2, y_pixels/2 - screen_text.get_height()/2 ]) #surface.blit( text, coordinates)


        
    import pygame,random
    from time import sleep

    x_pixels = 1200
    y_pixels = 650


    start_snake_x_position = x_pixels/2
    start_snake_y_position = y_pixels/2

    x_head = start_snake_x_position 
    y_head = start_snake_y_position


    rotating_degrees = 0


    pygame.init()

    square_side = 40

    clock = pygame.time.Clock()

    step = square_side

    #STEP SHOULD = SQUARE_SIDE TO MATCH THE FACE

    apple_eaten = 0

    coordinates = []

    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,155,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    
    fps = 15

    iconimage = pygame.image.load("icon.png") # perfect pixels for icon are 32 x 32
    snakeimage = pygame.image.load("snakehead.png")
    appleimage  = pygame.image.load("apple.png")

    pygame.display.set_icon(iconimage)
    
    pixels = [x_pixels, y_pixels]
    gameDisplay = pygame.display.set_mode(pixels) #pixels is 1st arg.
    pygame.display.set_caption("Snake") # Caption is the title

    apple_x = random.randrange(0,x_pixels - square_side)
    apple_y =  random.randrange(0,y_pixels -square_side)




    x_change = 0
    y_change = 0


    apple_side = square_side + 1


    default_size = 25


    small_font = pygame.font.SysFont(None , default_size )
    medium_font = pygame.font.SysFont(None , 2 * default_size)
    large_font = pygame.font.SysFont(None , 3 * default_size)
    super_large_font =  pygame.font.SysFont(None , 5 * default_size)

    gameExit = False
    gameOver = False
    
    gameDisplay.fill(green)
    msg_to_user("WELCOME TO SNAKE",size = "super large",
                color = blue,
                extra_depth = -200)
    
    msg_to_user("Press Q to quit, P to pause, or G to play ",
                color = black,
                extra_depth = 50)

    pygame.display.update()


    


    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # all events in CAPS
                gameExit = True
                gameOver = False
                intro = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
                    gameOver = False
                    intro = False
                elif event.key == pygame.K_g:
                    intro = False
                    gameloop()

    while  gameExit is False:





        while  gameOver is True:

            gameDisplay.fill(green)
            msg_to_user("GAME OVER ",color = red, size = "super large",extra_depth = -150)
            msg_to_user("Press Q to quit, or G to play again", color = black, extra_depth = 50)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT: # all events in CAPS
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_g:
                        gameloop()
                    

            
        for event in pygame.event.get():

            if event.type == pygame.QUIT: # all events in CAPS
                gameExit = True


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = - step
                    y_change = 0
                    rotating_degrees = 90
                    
                if event.key == pygame.K_RIGHT:
                    x_change = step
                    y_change = 0
                    rotating_degrees = 270
                    
                if event.key == pygame.K_UP:
                    y_change = - step
                    x_change = 0
                    rotating_degrees = 0
                    
                if event.key == pygame.K_DOWN:
                    y_change = step
                    x_change = 0
                    rotating_degrees = 180


                if event.key == pygame.K_p:
                    pause()
        clock.tick(fps) # FPS ... better to lower fps and raise the step size to lower processing

        


        x_head += x_change
        y_head += y_change
        
        x_y = [x_head,y_head]
        coordinates.append(x_y)


        if len(coordinates) > apple_eaten + 1:
            del coordinates[0]
            
        if x_head > x_pixels - square_side  : # 20 is a number to adjust shape at edge .. as square_side is not sufficient
            x_head = 1 
        elif x_head <= 0 :
            x_head = x_pixels - 1
            
        if y_head <= 0:
            y_head  = y_pixels - 1
            
        elif y_head >= y_pixels - square_side :
            y_head = 1

        gameDisplay.fill(blue)
        
        
        #gameDisplay.fill(black, rect = [0,0,70,70]) # Another way to draw shapes
        
        gameDisplay.blit(appleimage,[apple_x,apple_y])

        
        #THESE DONT WORK IF SNAKE IS MUCH LARGER THAN APPLE SO ENDS CAN NOT TOUCH APPLE
        
        if (x_head >= apple_x):   
            if x_head <=  (apple_x + apple_side) :
                if (y_head >= apple_y):
                    if y_head <=  (apple_y + apple_side):
                                
                        apple_eaten += 1
                        apple_x = random.randrange(0,x_pixels - apple_side)#/ step) * step   (round at first to make it multiple of 10)
                        apple_y =  random.randrange(0,y_pixels -apple_side)#/ step) * step     (round at first to make it multiple of 10)


                elif (y_head + square_side) >= apple_y :
                    if (y_head + square_side) <= ( apple_y + apple_side):
                         
                        apple_eaten += 1
                        apple_x = random.randrange(0,x_pixels - apple_side)#/ step) * step   (round at first to make it multiple of 10)
                        apple_y =  random.randrange(0,y_pixels -apple_side)#/ step) * step     (round at first to make it multiple of 10)

        elif  (x_head + square_side) >= apple_x:
            if (x_head + square_side) <= ( apple_x + apple_side):
                if (y_head + square_side) >= apple_y:
                    if (y_head + square_side) <= ( apple_y + apple_side):


                        apple_eaten += 1
                        apple_x = random.randrange(0,x_pixels - apple_side)#/ step) * step   (round at first to make it multiple of 10)
                        apple_y =  random.randrange(0,y_pixels -apple_side)#/ step) * step     (round at first to make it multiple of 10)


                elif (y_head >= apple_y):
                    if y_head <=  (apple_y + apple_side):
                        apple_eaten += 1
                        apple_x = random.randrange(0,x_pixels - apple_side)#/ step) * step   (round at first to make it multiple of 10)
                        apple_y =  random.randrange(0,y_pixels -apple_side)#/ step) * step     (round at first to make it multiple of 10)



        if [x_head,y_head] in coordinates[:-1]:
            gameOver = True

        score(apple_eaten)

                             
        snake(square_side,coordinates)

        pygame.display.update() # After all graphics are done



    pygame.quit() #Close the game
    quit()  # Close python

gameloop()
