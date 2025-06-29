import pygame
import random
import sys
from pygame.locals import *

# Global Variables for the game
window_width = 600
window_height = 500

# Setting up the height and width of the game window
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
gameImages = {}
framesPerSecond = 32
pipeImage = 'Flappy Bird Game/Images/pipe.png'
backgroundImage = 'Flappy Bird Game/Images/background.jpg'
birdPlayerImage = 'Flappy Bird Game/Images/bird.png'
seaLevelImage = 'Flappy Bird Game/Images/base.jfif'

def flappyBird():
    playerScore = 0
    horizontal = int(window_width/5)
    vertical = int(window_height/2)
    ground = 0
    my_temp_height = 100

    # Generates the pipes
    pipe1 = pipeCreate()
    pipe2 = pipeCreate()

    # The Lower Pipes
    pipeDown = [
        {'x': window_width+300-my_temp_height, 'y': pipe1[1]['y']},
        {'x': window_width+300-my_temp_height+(window_width), 'y': pipe2[1]['y']},
    ]

    # The Upper pipes
    pipeUp = [
        {'x': window_width+300-my_temp_height,
         'y': pipe1[0]['y']},
        {'x': window_width+200-my_temp_height+(window_width/2),
         'y': pipe2[0]['y']},
    ]

    # Pipe Velocity along X
    pipe_velocity_x = -4

    # Player Bird Velocity
    y_bird_velocity = -9
    y_bird_Max_Vel = 10
    y_bird_Min_Vel = -8
    YbirdAcc = 1

    # Velocity while flapping
    flappybird_velocity = -8

    # It's true only when the bird is flapping
    flappedbird = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    y_bird_velocity = flappybird_velocity
                    flappedbird = True

        # This function will return True if the Flappybird is crashed
        isgameOver = gameOver(horizontal, vertical, pipeUp, pipeDown)
        if isgameOver:
            return
        
        # Checks the Player Score
        playerMidPos = horizontal + gameImages['Flappy Bird'].get_width()/2
        for pipe in pipeUp:
            pipeMidPos = pipe['x'] + gameImages['Pipe Image'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                # Printing the score
                playerScore += 1
                print(f"Your score is {playerScore}")

        if y_bird_velocity < y_bird_Max_Vel and not flappedbird:
            y_bird_velocity += YbirdAcc

        if flappedbird:
            flappedbird = False
        playerHeight = gameImages['Flappy Bird'].get_height()
        vertical = vertical + min(y_bird_velocity, elevation - vertical - playerHeight)

        # Moves pipes to the left
        for pipeUpper, pipeLower in zip(pipeUp, pipeDown):
            pipeUpper['x'] += pipe_velocity_x
            pipeLower['x'] += pipe_velocity_x

        # A new pipe is added when the first is about to cross the leftmost part of the screen
        if 0 < pipeUp[0]['x'] < 5:
            pipeNew = pipeCreate()
            pipeUp.append(pipeNew[0])
            pipeDown.append(pipeNew[1])

        if pipeUp[0]['x'] <- gameImages['Pipe Image'][0].get_width():
            pipeUp.pop(0)
            pipeDown.pop(0)

        window.blit(gameImages['Background'], (0, 0))
        for pipeUpper, pipeLower in zip(pipeUp, pipeDown):
            window.blit(gameImages['Pipe Image'][0],(pipeUpper['x'], pipeUpper['y']))
            window.blit(gameImages['Pipe Image'][0],(pipeLower['x'], pipeLower['y']))

        window.blit(gameImages['Sea Level'], (ground, elevation))
        window.blit(gameImages['Flappy Bird'], (horizontal, vertical))

        # Generates the digit of scores
        numbers = [int(x) for x in list(str(playerScore))]
        width = 0

        # Finding the width of score images from numbers
        width = sum(gameImages['Score Images'][num].get_width() for num in numbers)
        offsetX = (window_width - width)/1.1

        # Blitting the images on the window
        for num in numbers:
            window.blit(gameImages['Score Images'][num], (offsetX, window_width*0.02))
            offsetX += gameImages['Score Images'][num].get_width()

        # Refreash the game to display the score
        pygame.display.update()
        framesPerSecond_Clock.tick(framesPerSecond)

def gameOver(horizontal, vertical, pipeUp, pipeDown):
    if vertical > elevation - 25 or vertical < 0:
        return True
    
    for pipe in pipeUp:
        heightPipe = gameImages['Pipe Image'][0].get_height()
        if(vertical < heightPipe + pipe['y'] and abs(horizontal - pipe['x']) < gameImages['Pipe Image'][0].get_width()):
            return True
        
    for pipe in pipeDown:
        if(vertical + gameImages['Flappy Bird'].get_height() > pipe['y'] 
        and abs(horizontal - pipe['x']) < gameImages['Pipe Image'][0].get_width()):
            return True
    return False
    
def pipeCreate():
    offset = window_height/3
    heightPipe = gameImages['Pipe Image'][0].get_height()
    y2 = offset + random.randrange(0, int(window_height - gameImages['Sea Level'].get_height() - 1.2 * offset))
    xPipe = window_width + 10
    y1 = heightPipe - y2 + offset
    pipe = [
        # Upper Pipe
        {'x': xPipe, 'y': -y1},
        # Lower Pipe
        {'x': xPipe, 'y': y2}
    ]
    return pipe

# Game Start
if __name__ == "__main__":

    pygame.init()
    framesPerSecond_Clock = pygame.time.Clock()

    # Game Title on Screen
    pygame.display.set_caption("Flappy Bird")

    # Loads all the images for the game
    # Score Images displayed
    gameImages['Score Images'] = (
        pygame.image.load('Flappy Bird Game/Images/0.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/1.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/2.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/3.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/4.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/5.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/6.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/7.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/8.png').convert_alpha(),
        pygame.image.load('Flappy Bird Game/Images/9.png').convert_alpha()
    )
    gameImages['Flappy Bird'] = pygame.image.load(birdPlayerImage).convert_alpha()
    gameImages['Sea Level'] = pygame.image.load(seaLevelImage).convert_alpha()
    gameImages['Background'] = pygame.image.load(backgroundImage).convert_alpha()
    gameImages['Pipe Image'] = (
        pygame.transform.rotate(pygame.image.load(pipeImage).convert_alpha(), 180), 
        pygame.image.load(pipeImage).convert_alpha()
    )

    print("Welcome to Flappy Bird")
    print("Press space or enter button to start")

while True:

    horizontal = int(window_width/5)
    vertical = int((window_height - gameImages['Flappy Bird'].get_height()/2))

    x_ground = 0
    while True:
        for event in pygame.event.get():

            # if the user press the cross button, closes the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()

                # Exit the game
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                flappyBird()

            # If there are no buttons pressed
            else:
                window.blit(gameImages['Background'], (0, 0))
                window.blit(gameImages['Flappy Bird'], (horizontal, vertical))
                window.blit(gameImages['Sea Level'], (x_ground, elevation))

                # Refreash the screen
                pygame.display.update()

                # Sets the rate of frames per second
                framesPerSecond_Clock.tick(framesPerSecond)