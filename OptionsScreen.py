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
                    
                    
                    
                    
                    
        if selection > 2:
            selection = 1
        if selection < 1:
            selection = 2
        
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
        

        # Setup "RULES NAME TITLE"
        rulesTitleText = font.render("RULES", 1, (255,255,255), (0,0,0))
        rulesTitleTextPos = rulesTitleText.get_rect()
        rulesTitleTextPos.centerx = (background.get_rect().centerx)
        rulesTitleTextPos.centery = (background.get_rect().centery + 100)
        

        # Setup "RULES BOX" Menu button
        color = (0,0,0)
        rules = displayRules()

        rulesText1 = font.render(rules[0], 1, (255,255,255), color)
        rulesText1Pos = rulesText1.get_rect()
        rulesText1Pos.centerx = (background.get_rect().centerx - 20)
        rulesText1Pos.centery = (background.get_rect().centery + 130)

        rulesText2 = font.render(rules[1], 1, (255,255,255), color)
        rulesText2Pos = rulesText2.get_rect()
        rulesText2Pos.centerx = (background.get_rect().centerx + 7)
        rulesText2Pos.centery = (background.get_rect().centery + 160)

        rulesText3 = font.render(rules[2], 1, (255,255,255), color)
        rulesText3Pos = rulesText3.get_rect()
        rulesText3Pos.centerx = (background.get_rect().centerx + 2)
        rulesText3Pos.centery = (background.get_rect().centery + 190)

        rulesText4 = font.render(rules[3], 1, (255,255,255), color)
        rulesText4Pos = rulesText4.get_rect()
        rulesText4Pos.centerx = (background.get_rect().centerx + 23)
        rulesText4Pos.centery = (background.get_rect().centery + 220)

        rulesText5 = font.render(rules[4], 1, (255,255,255), color)
        rulesText5Pos = rulesText5.get_rect()
        rulesText5Pos.centerx = (background.get_rect().centerx + 15)
        rulesText5Pos.centery = (background.get_rect().centery + 250)

        rulesText6 = font.render(rules[5], 1, (255,255,255), color)
        rulesText6Pos = rulesText6.get_rect()
        rulesText6Pos.centerx = (background.get_rect().centerx - 68)
        rulesText6Pos.centery = (background.get_rect().centery + 280)

        rulesText7 = font.render(rules[6], 1, (255,255,255), color)
        rulesText7Pos = rulesText7.get_rect()
        rulesText7Pos.centerx = (background.get_rect().centerx + 35)
        rulesText7Pos.centery = (background.get_rect().centery + 310)

        rulesText8 = font.render(rules[7], 1, (255,255,255), color)
        rulesText8Pos = rulesText8.get_rect()
        rulesText8Pos.centerx = (background.get_rect().centerx - 65)
        rulesText8Pos.centery = (background.get_rect().centery + 340)


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

        screen.blit(rulesTitleText, rulesTitleTextPos)
        screen.blit(rulesText1, rulesText1Pos)
        screen.blit(rulesText2, rulesText2Pos)
        screen.blit(rulesText3, rulesText3Pos)
        screen.blit(rulesText4, rulesText4Pos)
        screen.blit(rulesText5, rulesText5Pos)
        screen.blit(rulesText6, rulesText6Pos)
        screen.blit(rulesText7, rulesText7Pos)
        screen.blit(rulesText8, rulesText8Pos)


        screen.blit(backText, backTextPos)
        pygame.display.flip()
    
    #raw_input("Press Enter to continue")
    return screen


def displayRules():
    rules = []
    rules1 = "PLAYER BEGINS GAME WITH 3 LIVES"
    rules.append(rules1)
    rules2 = "SHOOT ASTEROIDS TO INCREASE SCORE"
    rules.append(rules2)
    rules3 = "EACH ASTEROID IS WORTH 100 POINTS "
    rules.append(rules3)
    rules4 = "CLEAR SCREEN TO MOVE TO HIGHER LEVEL"
    rules.append(rules4)
    rules5 = "EVERY 1000 POINTS EARN NEW POWER UP"
    rules.append(rules5)
    rules6 = "USE UP ARROW FOR THRUST"
    rules.append(rules6)
    rules7 = "USE LEFT AND RIGHT ARROWS TO TURN SHIP"
    rules.append(rules7)
    rules8 = "PRESS SPACE BAR TO SHOOT"
    rules.append(rules8)
    return rules