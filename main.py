import sys, pygame
from pygame.locals import *
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("birdHit.wav")
pygame.mixer.music.load("bgMusic.mp3")

black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)

bright_blue = (0,0,255)
bright_green = (0,255,0)

birdimg = pygame.image.load('flappyBird.png')

birdUp = pygame.image.load('flappyBirdUP.png')

birdImg = pygame.image.load('flappyBirdLOGO.png')

bg = pygame.image.load('flappyBirdBackground.jpg')

pygame.display.set_icon(birdImg)

pause = False

display_width = 800
display_height = 555
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy Bird Clone')

car_height = 66

clock = pygame.time.Clock()

def button(msg, x, y, w, h, a, i, action = None):
	mouse = pygame.mouse.get_pos()
	
	click = pygame.mouse.get_pressed()
	
	
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, a, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
			
	
	else:
	
		pygame.draw.rect(gameDisplay, i, (x, y, w, h))

	
	smallText = pygame.font.SysFont('comicsansms', 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( x+(w/2), (y + (h/2)) )
	gameDisplay.blit(textSurf, textRect)
	
	


	
def quit_one():
	pygame.quit()
	quit()

def game_intro():
	
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		gameDisplay.fill(white)
		largeText = pygame.font.SysFont("comicsansms", 100)
		TextSurf, TextRect = text_objects('Flappy Bird Clone', largeText)
		TextRect.center = ((display_width / 2),(display_height / 2) )
		gameDisplay.blit(TextSurf, TextRect)
		
		button('GO!',150, 450, 100, 50, green, bright_green, game_loop)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)

def unpause():
	global pause
	pause = False
	
	pygame.mixer.music.unpause()

		
def paused():
	
	pygame.mixer.music.pause()
	
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects('Paused', largeText)
	TextRect.center = ((display_width / 2),(display_height / 2) )
	gameDisplay.blit(TextSurf, TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		
		button('Continue',150, 450, 100, 50, green, bright_green, unpause)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)


def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingh, thingw])


def bird(x,y):
	gameDisplay.blit(birdimg, (x,y))
	
def birdUP(x,y):
	gameDisplay.blit(birdUp, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width / 2),(display_height / 2) )
	gameDisplay.blit(TextSurf, TextRect)
	
	pygame.display.update()
	
	time.sleep(2)
	
	game_loop()

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: " + str(count), True, blue)
	gameDisplay.blit(text, (0,0))
	
def crash():
	
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	
	crash = True
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects('You Got Hit', largeText)
	TextRect.center = ((display_width / 2),(display_height / 2) )
	gameDisplay.blit(TextSurf, TextRect)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		
		
		button('Play Again',150, 450, 100, 50, green, bright_green, game_loop)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)



def game_loop():

	global pause
		
	pygame.mixer.music.play(-1)
	
	x = (display_width * .2)
	y = (display_height * .7)

	
	space = 100
	y_change = 0
	
	thing_startx = display_width + 5
	
	
	
	
	thing_speed = 5
	thing_width = 100
	thing_height_top = 100
	#CHANGE
	thing_height_bottom = 350
	dodged = 0
	block_space = 0
	
	
	thing_starty = 350 - thing_height_bottom
	
	thing_starty_top = 0
	

	
	gameExit = False

	things_dict = [thing_startx,thing_starty_top,thing_height_top,thing_width, green]
	things_dict_bottom = [thing_startx,thing_starty,thing_height_bottom,thing_width, green]



	things_dict[2] = random.randrange(85,350)
			#CHANGE
	things_dict_bottom[2] = 350 - things_dict[2]
				
			#Block placement
	things_dict[1] = 0 
	things_dict_bottom[1] = 450 - things_dict_bottom[2]

	while gameExit == False:
		
		for event in pygame.event.get():
		
		
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change = -5
					

				elif event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					y_change = 5
					
				
			
			
		y += y_change
		
		
		gameDisplay.blit(bg,(0,0))
		

		things(things_dict[0],things_dict[1],things_dict[2],things_dict[3],things_dict[4])
		things(things_dict_bottom[0], things_dict_bottom[1], things_dict_bottom[2],things_dict_bottom[3],things_dict_bottom[4])
		
		if y_change == -5:
			birdUP(x,y)
		else:
			bird(x,y)
		
		things_dict[0] -= thing_speed
		things_dict_bottom[0] -= thing_speed
		
		things_dodged(dodged)
		

		if y > display_height - (car_height / 2) or y < 0:
			
			crash()



		if things_dict[0] < block_space:
		
			#height of block
			things_dict[2] = random.randrange(85,350)
			#CHANGE
			things_dict_bottom[2] = 350 - things_dict[2]
			
			#Block placement
			things_dict[1] = 0 
			things_dict_bottom[1] = 450 - things_dict_bottom[2]
			
			dodged += 1
			
			things_dict[0] = display_width + 5
			things_dict_bottom[0] = display_width + 5
			
			
			block_space = int(dodged *3.5)


		if y > 390:
			crash()
		
		
		if y < things_dict[1]+things_dict[2]:


			if things_dict[0] + car_height > x > things_dict[0] or x == things_dict[0]:
				
				crash()
				
				
		if things_dict_bottom[1] < y < things_dict_bottom[1]+things_dict_bottom[2]:

			if things_dict_bottom[0] + car_height > x > things_dict_bottom[0] or x == things_dict_bottom[0]:
				
				crash()
		

        

		pygame.display.update()
		clock.tick(60)

game_intro()
pygame.quit()
quit()
