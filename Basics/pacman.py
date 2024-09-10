import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


class Ellipse(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ellipse
        pygame.draw.ellipse(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        
class Slime(pygame.sprite.Sprite):
    def __init__(self,x,y,change_x,change_y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the direction of the slime
        self.change_x = change_x
        self.change_y = change_y
        # Load image
        self.image = pygame.image.load("slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
 

    def update(self,horizontal_blocks,vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left","right","up","down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2
                

    def get_intersection_position(self):
        items = []
        for i,row in enumerate(enviroment()):
            for j,item in enumerate(row):
                if item == 3:
                    items.append((j*32,i*32))

        return items
    
        
def enviroment():
    grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    return grid

def draw_enviroment(screen):
    for i,row in enumerate(enviroment()):
        for j,item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+32,i*32], 3)
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+32,i*32+32], 3)
            elif item == 2:
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 3)
                pygame.draw.line(screen, BLUE , [j*32+32, i*32], [j*32+32,i*32+32], 3)
The code given is the python file enemies which shows the different colors of ghost enemies that you want to avoid.


The Code Given Below Is For The Python File Game
import pygame
from player import Player
from enemies import *
import tkinter
from tkinter import messagebox
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None,40)
        self.about = False
        self.game_over = True
        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)
        # Create the menu of the game
        self.menu = Menu(("Start","About","Exit"),font_color = WHITE,font_size=60)
        # Create the player
        self.player = Player(32,128,"player.png")
        # Create the blocks that will set the paths where the player can go
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dots_group = pygame.sprite.Group()
        # Set the enviroment:
        for i,row in enumerate(enviroment()):
            for j,item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                elif item == 2:
                    self.vertical_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
        # Create the enemies
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288,96,0,2))
        self.enemies.add(Slime(288,320,0,-2))
        self.enemies.add(Slime(544,128,0,2))
        self.enemies.add(Slime(32,224,0,2))
        self.enemies.add(Slime(160,64,2,0))
        self.enemies.add(Slime(448,64,-2,0))
        self.enemies.add(Slime(640,448,2,0))
        self.enemies.add(Slime(448,320,2,0))
        # Add the dots inside the game
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Ellipse(j*32+12,i*32+12,WHITE,8,8))

        # Load the sound effects
        self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")


    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            # ---- START ------
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            # --- ABOUT ------
                            self.about = True
                        elif self.menu.state == 2:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True
                    
        return False

    def run_logic(self):
        if not self.game_over:
            self.player.update(self.horizontal_blocks,self.vertical_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player,self.dots_group,True)
            # When the block_hit_list contains one sprite that means that player hit a dot
            if len(block_hit_list) > 0:
                # Here will be the sound effect
                self.pacman_sound.play()
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player,self.enemies,True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.game_over_sound.play()
            self.game_over = self.player.game_over
            self.enemies.update(self.horizontal_blocks,self.vertical_blocks)
           # tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))    

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.about:
                self.display_message(screen,"It is an arcade Game")
                #"a maze containing various dots,\n"
                #known as Pac-Dots, and four ghosts.\n"
                #"The four ghosts roam the maze, trying to kill Pac-Man.\n"
                #"If any of the ghosts hit Pac-Man, he loses a life;\n"
                #"the game is over.\n")
            else:
                self.menu.display_frame(screen)
        else:
            # --- Draw the game here ---
            self.horizontal_blocks.draw(screen)
            self.vertical_blocks.draw(screen)
            draw_enviroment(screen)
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image,self.player.rect)
            #text=self.font.render("Score: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Render the text for the score
            text = self.font.render("Score: " + str(self.score),True,GREEN)
            # Put the text on the screen
            screen.blit(text,[120,20])
            
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def display_message(self,screen,message,color=(255,0,0)):
        label = self.font.render(message,True,color)
        # Get the width and height of the label
        width = label.get_width()
        height = label.get_height()
        # Determine the position of the label
        posX = (SCREEN_WIDTH /2) - (width /2)
        posY = (SCREEN_HEIGHT /2) - (height /2)
        # Draw the label onto the screen
        screen.blit(label,(posX,posY))


class Menu(object):
    state = 0
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


class Ellipse(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ellipse
        pygame.draw.ellipse(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        
class Slime(pygame.sprite.Sprite):
    def __init__(self,x,y,change_x,change_y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the direction of the slime
        self.change_x = change_x
        self.change_y = change_y
        # Load image
        self.image = pygame.image.load("slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
 

    def update(self,horizontal_blocks,vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left","right","up","down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2
                

    def get_intersection_position(self):
        items = []
        for i,row in enumerate(enviroment()):
            for j,item in enumerate(row):
                if item == 3:
                    items.append((j*32,i*32))

        return items
    
        
def enviroment():
    grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    return grid

def draw_enviroment(screen):
    for i,row in enumerate(enviroment()):
        for j,item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32+32,i*32], 3)
                pygame.draw.line(screen, BLUE , [j*32, i*32+32], [j*32+32,i*32+32], 3)
            elif item == 2:
                pygame.draw.line(screen, BLUE , [j*32, i*32], [j*32,i*32+32], 3)
                pygame.draw.line(screen, BLUE , [j*32+32, i*32], [j*32+32,i*32+32], 3)
The code given is the python file enemies which shows the different colors of ghost enemies that you want to avoid.


The Code Given Below Is For The Python File Game
import pygame
from player import Player
from enemies import *
import tkinter
from tkinter import messagebox
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None,40)
        self.about = False
        self.game_over = True
        # Create the variable for the score
        self.score = 0
        # Create the font for displaying the score on the screen
        self.font = pygame.font.Font(None,35)
        # Create the menu of the game
        self.menu = Menu(("Start","About","Exit"),font_color = WHITE,font_size=60)
        # Create the player
        self.player = Player(32,128,"player.png")
        # Create the blocks that will set the paths where the player can go
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        # Create a group for the dots on the screen
        self.dots_group = pygame.sprite.Group()
        # Set the enviroment:
        for i,row in enumerate(enviroment()):
            for j,item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                elif item == 2:
                    self.vertical_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
        # Create the enemies
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288,96,0,2))
        self.enemies.add(Slime(288,320,0,-2))
        self.enemies.add(Slime(544,128,0,2))
        self.enemies.add(Slime(32,224,0,2))
        self.enemies.add(Slime(160,64,2,0))
        self.enemies.add(Slime(448,64,-2,0))
        self.enemies.add(Slime(640,448,2,0))
        self.enemies.add(Slime(448,320,2,0))
        # Add the dots inside the game
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Ellipse(j*32+12,i*32+12,WHITE,8,8))

        # Load the sound effects
        self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")


    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            # ---- START ------
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            # --- ABOUT ------
                            self.about = True
                        elif self.menu.state == 2:
                            # --- EXIT -------
                            # User clicked exit
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True
                    
        return False

    def run_logic(self):
        if not self.game_over:
            self.player.update(self.horizontal_blocks,self.vertical_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player,self.dots_group,True)
            # When the block_hit_list contains one sprite that means that player hit a dot
            if len(block_hit_list) > 0:
                # Here will be the sound effect
                self.pacman_sound.play()
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player,self.enemies,True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.game_over_sound.play()
            self.game_over = self.player.game_over
            self.enemies.update(self.horizontal_blocks,self.vertical_blocks)
           # tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))    

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(BLACK)
        # --- Drawing code should go here
        if self.game_over:
            if self.about:
                self.display_message(screen,"It is an arcade Game")
                #"a maze containing various dots,\n"
                #known as Pac-Dots, and four ghosts.\n"
                #"The four ghosts roam the maze, trying to kill Pac-Man.\n"
                #"If any of the ghosts hit Pac-Man, he loses a life;\n"
                #"the game is over.\n")
            else:
                self.menu.display_frame(screen)
        else:
            # --- Draw the game here ---
            self.horizontal_blocks.draw(screen)
            self.vertical_blocks.draw(screen)
            draw_enviroment(screen)
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image,self.player.rect)
            #text=self.font.render("Score: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Render the text for the score
            text = self.font.render("Score: " + str(self.score),True,GREEN)
            # Put the text on the screen
            screen.blit(text,[120,20])
            
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def display_message(self,screen,message,color=(255,0,0)):
        label = self.font.render(message,True,color)
        # Get the width and height of the label
        width = label.get_width()
        height = label.get_height()
        # Determine the position of the label
        posX = (SCREEN_WIDTH /2) - (width /2)
        posY = (SCREEN_HEIGHT /2) - (height /2)
        # Draw the label onto the screen
        screen.blit(label,(posX,posY))


class Menu(object):
    state = 0
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1