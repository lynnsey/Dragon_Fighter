"""
Name of File: FinalProject_LynnseyOng.py
Name: Lynnsey Ong
Version : 1.0
Last edited: December 20, 2017
You collect as many coins as you can.
Biblio = https://www.allwallpaper.in/fr/very-cool-blue-sky-wallpaper-13659.html
         http://www.pngmart.com/image/32887
         http://object-survival-island.wikia.com/wiki/File:NUKEY.png
         https://www.youtube.com/watch?v=2C4lFUpI_4U
         https://www.youtube.com/watch?v=rPSx_cSPw_0
"""
import pygame
import random

pygame.mixer.init(44100, -16, 2, 2048)

#Constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
THISTLE = (255, 225, 255)
SKYBLUE = (135, 206, 255)
PINK = (255, 192, 203)
PALEGREEN = (144, 238, 144)
ORANGERED = (255, 69, 0)
NAVY = (0 ,0, 128)
GOLD = (255, 215, 0)
CRIMSON = (220, 20, 60)

main_character_image = pygame.image.load("dragon_copy2.png")
background_image = pygame.image.load("sky.png")
bomb_image = pygame.image.load("bomb.png")
end_game = pygame.image.load("gameover1.png")
dead_mus = pygame.mixer.Sound("dragon_roar.ogg")


SCREEN_WIDTH = 750
SCREEN_HEIGHT = 425

size = (750, 425)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Dragon_Fighter")


PLAYER_VELOCITY = 3

x_vel = 0
y_vel = 0

dead = 0
score = 0

DRAGON_SPEED = 5

dragon_xcoord = 320
dragon_ycoord = 390
dragon_xvel = 0
dragon_yvel = 0

coins_cord = []
bombs_cord = []

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()

        # Visual representation of Coin
        self.image = pygame.Surface([10, 10])
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, GOLD, [5, 5], 5, 0)


        # Rectangle to represent position
        self.rect = self.image.get_rect()
    def reset(self):
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = random.randrange(-1000, -10)

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb, self).__init__()

        self.image = bomb_image

        self.rect = self.image.get_rect()

    def reset(self):
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = random.randrange(-1000, -10)



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = main_character_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.xvel = 0
        self.yvel = 0

    def changevelocity(self, x, y):
        """ Changes velocity of the player """
        self.xvel += x
        self.yvel += y

    def update(self):
        """ Updates the position of the Player according to velocity """
        self.rect.x += self.xvel
        self.rect.y += self.yvel

pygame.init()

word_font = pygame.font.SysFont("Bungee", 25)
word_font2 = pygame.font.SysFont("Bungee", 40)
word_font3 = pygame.font.SysFont("Bungee", 25)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# TODO: Create bad_block_list
# TODO: Create good_block_list
coin_list = pygame.sprite.Group()
bomb_list = pygame.sprite.Group()

# All sprites in app
all_sprites_list = pygame.sprite.Group()

for i in range(200):
    coin = Coin()

    # Random location for Coin
    coin.rect.x = random.randrange(0, SCREEN_WIDTH)
    coin.rect.y = random.randrange(-1000, -10)

    # Add the block to the list of objects
    coin_list.add(coin)
    all_sprites_list.add(coin)
    coins_cord.append([coin.rect.x, coin.rect.y])

for i in range(15):
    bomb = Bomb()

    bomb.rect.x = random.randrange(SCREEN_WIDTH)
    bomb.rect.y = random.randrange(-1000, -10)

    bomb_list.add(bomb)
    all_sprites_list.add(bomb)

# TODO: Create instance of player class
player = Player(dragon_xcoord, dragon_ycoord)
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()

score = 0

pygame.mixer.music.load("Adeventuresong.mp3")
pygame.mixer.music.play(1, 0.0)

# -------- Main Program Loop -----------
while not done:
    # TODO: Control character with keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_xvel -= DRAGON_SPEED
            elif event.key == pygame.K_RIGHT:
                dragon_xvel += DRAGON_SPEED
            elif event.key == pygame.K_DOWN:
                dragon_yvel += DRAGON_SPEED
            elif event.key == pygame.K_UP:
                dragon_yvel -= DRAGON_SPEED
            if event.key == pygame.K_SPACE and dead >= 1:
                dead = 0
                score = 0
                dead_mus.stop()
                coin_list = pygame.sprite.Group()
                all_sprites_list = pygame.sprite.Group()
                bomb_list = pygame.sprite.Group()
                for i in range(200):
                    coin = Coin()

                    # Random location for Coin
                    coin.rect.x = random.randrange(0, SCREEN_WIDTH)
                    coin.rect.y = random.randrange(-1000, -10)

                    # Add the block to the list of objects
                    coin_list.add(coin)
                    all_sprites_list.add(coin)
                    coins_cord.append([coin.rect.x, coin.rect.y])

                for i in range(15):
                    bomb = Bomb()

                    bomb.rect.x = random.randrange(SCREEN_WIDTH)
                    bomb.rect.y = random.randrange(-1000, -10)

                    bomb_list.add(bomb)
                    all_sprites_list.add(bomb)
                pygame.mixer.music.load("Adeventuresong.mp3")
                pygame.mixer.music.play(1, 0.0)
                player.rect.x = 320
                player.rect.y = 390
                all_sprites_list.add(player)


            if event.key == pygame.K_ESCAPE:
                done = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dragon_xvel = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dragon_yvel = 0

    #pos = pygame.mouse.get_pos()

    dragon_xcoord += dragon_xvel
    dragon_ycoord += dragon_yvel

    #animation of the falling object:
    for coin in coin_list:
        coin.rect.y += 1
        if coin.rect.y >= SCREEN_HEIGHT:
            coin.rect.y = 0
            coin.rect.x = random.randrange(SCREEN_WIDTH)

    for bomb in bomb_list:
        bomb.rect.y += 1
        if bomb.rect.y >= SCREEN_HEIGHT:
            bomb.rect.y = random.randrange(SCREEN_WIDTH)


    # Clear the screen
    screen.blit(background_image, (0,0))

    #Sound at the background_image
    Instruction = word_font.render("Collect as many coins as you can. Dodge the bombs to survive.", 3, BLACK)
    screen.blit(Instruction, (5,5))

    Instruction1 = word_font3.render("Bombs may appear out of no where. Good luck!", 3, BLACK)
    screen.blit(Instruction1, (5, 20))

    Score = word_font2.render("Score: " + str(score), 50, BLACK)
    screen.blit(Score, (550,400))


    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    #pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = dragon_xcoord
    player.rect.y = dragon_ycoord

    # TODO: Check for good and bad collisions
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
    dead_hit_list = pygame.sprite.spritecollide(player, bomb_list, True)

    # TODO: Update score - good collisions = score + 1
    # TODO: Update score - bad collisions = score - 1
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        if not dead >= 1:
            print(score)


    # Draw all the spites
    all_sprites_list.draw(screen)

    #for the dead screen to appear:
    for bomb in dead_hit_list:
        dead += 1

    if dead >= 1:
        pygame.mixer.music.stop()
        screen.blit(end_game, (0,0))
        dead_mus.play()


    #So the dragon doesn't escape the screen:
    if dragon_xcoord <= 5:
        dragon_xcoord += 2
        dragon_xvel = 0

    elif dragon_xcoord >= 650:
        dragon_xcoord -= 2
        dragon_xvel = 0

    elif dragon_ycoord <= 10:
        dragon_ycoord += 2
        dragon_yvel = 0

    elif dragon_ycoord >= 370:
        dragon_ycoord -= 2
        dragon_yvel = 0


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
