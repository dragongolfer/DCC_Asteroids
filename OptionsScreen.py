import pygame
from display_functions import *
pygame.init()



def displayOptionsScreen(options):
    # Set Screen parameters
    size = setScreenSize(800, 800)
    screen = createScreen(size)

    NameEditFlag = True # True while editing the nameText
    
    pygame.display.set_caption('Asteroids For The Win!')
    selection = 1    
    while True:
        # Process Menu Selection Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass
                if event.key == pygame.K_DOWN:# and not NameEditFlag:
                    selection += 1
                if event.key == pygame.K_UP:# and not NameEditFlag:
                    selection -= 1
                # if (event.key == pygame.K_RETURN) and (selection == 1):
                    # NameEditFlag = not NameEditFlag
                if (event.key == pygame.K_RETURN) and (selection == 2):
                    return options                    
                if event.key == pygame.K_ESCAPE:
                    return options
                    
                # Alphabet while editing the field
                if event.key == pygame.K_BACKSPACE and NameEditFlag:
                    options[0] = options[0][:-1]        
                if event.key == pygame.K_a and NameEditFlag:
                    options[0] += "A"
                if event.key == pygame.K_b and NameEditFlag:
                    options[0] += "B"   
                if event.key == pygame.K_c and NameEditFlag:
                    options[0] += "C"   
                if event.key == pygame.K_d and NameEditFlag:
                    options[0] += "D"   
                if event.key == pygame.K_e and NameEditFlag:
                    options[0] += "E"   
                if event.key == pygame.K_f and NameEditFlag:
                    options[0] += "F"   
                if event.key == pygame.K_g and NameEditFlag:
                    options[0] += "G"   
                if event.key == pygame.K_h and NameEditFlag:
                    options[0] += "H"       
                if event.key == pygame.K_i and NameEditFlag:
                    options[0] += "I"   
                if event.key == pygame.K_j and NameEditFlag:
                    options[0] += "J"
                if event.key == pygame.K_k and NameEditFlag:
                    options[0] += "K"   
                if event.key == pygame.K_l and NameEditFlag:
                    options[0] += "L"   
                if event.key == pygame.K_m and NameEditFlag:
                    options[0] += "M"   
                if event.key == pygame.K_n and NameEditFlag:
                    options[0] += "N"   
                if event.key == pygame.K_o and NameEditFlag:
                    options[0] += "O"   
                if event.key == pygame.K_p and NameEditFlag:
                    options[0] += "P"   
                if event.key == pygame.K_q and NameEditFlag:
                    options[0] += "Q"       
                if event.key == pygame.K_r and NameEditFlag:
                    options[0] += "R"   
                if event.key == pygame.K_s and NameEditFlag:
                    options[0] += "S"   
                if event.key == pygame.K_t and NameEditFlag:
                    options[0] += "T"   
                if event.key == pygame.K_u and NameEditFlag:
                    options[0] += "U"   
                if event.key == pygame.K_v and NameEditFlag:
                    options[0] += "V"   
                if event.key == pygame.K_w and NameEditFlag:
                    options[0] += "W"   
                if event.key == pygame.K_x and NameEditFlag:
                    options[0] += "X"   
                if event.key == pygame.K_y and NameEditFlag:
                    options[0] += "Y"       
                if event.key == pygame.K_z and NameEditFlag:
                    options[0] += "Z"                         
                    
        while len(options[0]) > 3:
            options[0]=options[0][:3]        
                    
                    
                    
                    
                    
            # if selection > 2:
                # selection = 1
            # if selection < 1:
                # selection = 2
        
        # Setup Background
        backgroundimage = pygame.image.load("StarField_2.png")
        background = pygame.transform.scale(backgroundimage,(size))
        
        # Setup "OPTIONS" Title
        font = pygame.font.Font(None, 100)
        optionText = font.render("Options", 1, (255,255,255), (0,0,0))
        optionTextPos = optionText.get_rect()
        optionTextPos.centerx = (background.get_rect().centerx)
        optionTextPos.centery = (background.get_rect().centery - 50)

        #Set font for remaining items
        font = pygame.font.Font(None, 36)
        
        # Setup "PLAYER NAME TITLE"
        nameTitleText = font.render("INITIALS", 1, (255,255,255), (0,0,0))
        nameTitleTextPos = nameTitleText.get_rect()
        nameTitleTextPos.centerx = (background.get_rect().centerx - 50)
        nameTitleTextPos.centery = (background.get_rect().centery + 20)
        
        # Setup "PLAYER NAME BOX" Menu button
        if selection == 1: 
            color = (100,100,100)
        else:
            color = (0,0,0)
        nameText = font.render(str(options[0]), 1, (255,255,255), color)
        nameTextPos = nameText.get_rect()
        nameTextPos.centerx = (background.get_rect().centerx + 50)
        nameTextPos.centery = (background.get_rect().centery + 20)
            
        # Setup "BACK BUTTON" Menu button
        if selection == 2: 
            color = (100,100,100)
        else:
            color = (0,0,0)
        backText = font.render("BACK", 1, (255,255,255), color)
        backTextPos = backText.get_rect()
        backTextPos.centerx = background.get_rect().centerx
        backTextPos.centery = (background.get_rect().centery + 50) 
        
        # Blit Screen
        screen.blit(background, (0,0))
        screen.blit(optionText, optionTextPos)
        screen.blit(nameTitleText, nameTitleTextPos)
        screen.blit(nameText, nameTextPos)
        screen.blit(backText, backTextPos)
        pygame.display.flip()
    
    #raw_input("Press Enter to continue")
    return screen
