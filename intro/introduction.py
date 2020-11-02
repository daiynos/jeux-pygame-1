import pygame
import random
import time
import sys
from pygame import mixer



pygame.mixer.init() 
pygame.init()
##arduino= serial.Serial('/dev/cu.usbmodem641', 9600, timeout = 1)






def invadexr():
	##arduino= serial.Serial('/dev/cu.usbmodem641', 9600, timeout = 1)
	WHITE = (100 , 254 ,0)
	screen= pygame.display.set_mode((1800,1000))

	print('onp')
	pygame.display.set_caption('Premier Jeu')
	icon=pygame.image.load('test.png')
	pygame.display.set_icon(icon)
	gagner=pygame.image.load('gagner.png')
	image_fond=pygame.image.load('background.png')
	fond=pygame.font.Font('freesansbold.ttf', 100)
	page_attente=pygame.image.load('backgroun.png')

	music_liste=["intro.ogg","attente.ogg"]
	plai=False

	def musique(i):
		mixer.music.load(i)
		mixer.music.play()

	joueur=pygame.image.load('player.png')
	enemi=pygame.image.load('enn.png')
	balles=pygame.image.load("bullet.png")
	fin= False

	attaquant_x=300
	attaquant_y=600
	attaquant_x_c=0

	balle_y_c=0
	fire=False
	balle_y=600
	point=0

	ennemi_x=0
	ennemi_y=0
	ennemi_x_c=0
	ennemi_y_c=0

	page="non"
	mus=False
	load=False
	text_pa=1

	X=600
	Y=600
	def text(tex):
		while True:
			gagner= fond.render(tex,True, WHITE)
			screen.blit(gagner,(600,500))


	def ardui():
		for i in range (2):
			if i==0:
			    x = 180   
			    x = str(x)
			    x = str.encode(x)
			    arduino.write(x)
			    time.sleep(1.5)
			    print(x)
			else:
				x = 10
				x = str(x)
				x = str.encode(x)
				arduino.write(x)
				time.sleep(1.5)
				print(x)


	def attaquant(x, y):
		screen.blit(joueur,(x, y))


	def balle(x, y):
		screen.blit(balles,(x, y))
		fire=False



	def ennemi(x, y):
		if y>=500:
			return True
		screen.blit(enemi,(x, y))

	myfont = pygame.font.SysFont('Comic Sans MS', 30)


	def mort(x1, x2 ,y1,y2):
		w1=(x2-x1)**2
		w2=(y2-y1)**2
		mor=(w1+w2)**0.5
		if mor<=40:
			return True
		else:
			return False


	gagner=False
	e=0	
	score=0

	run=True

	by=True

	ennemi_vitesse=10

	balle_uti=-1
	ti_st=time.time()
	P=0
	z=2
	load=True
	att=time.time()
	while run:
		if gagner==True:
			screen.blit(gagner,(0,0))
			page="non"


		if load==True:
				tex="Chargement ..."
				screen.fill((0,0,0))
				gagner= fond.render(tex,True, WHITE)
				screen.blit(gagner,(600,500))


				if time.time()-att>5:
					load=False
					page="ok"
					plai=True
					mixer.music.stop()
					musique(music_liste[0])


		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False


			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					attaquant_x_c=-30

				if event.key==pygame.K_RIGHT:
					attaquant_x_c=30

				if event.key==pygame.K_SPACE:
					balle_uti+=1
					if balle_y<=-10:
						point=attaquant_x
						balle_y=600
						fire=True
					balle_y_c=-100


			if event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
					attaquant_x_c=0



		if ennemi_x>=1700:
				ennemi_x_c=-ennemi_vitesse
				ennemi_y+=20
		elif ennemi_x<=0:
				ennemi_y+=20
				ennemi_x_c=ennemi_vitesse

		ennemi_x+=ennemi_x_c

		balle_y+=balle_y_c

		attaquant_x+=attaquant_x_c

		if attaquant_x<=0:
			attaquant_x=0
		elif attaquant_x>=1700:
			attaquant_x=1700


		if mus==True:
			une='non'
			page="ok"
			mus=False
			musique(music_liste[2])
			att=time.time()
			load=True

		if plai==True:
			P= P % image_fond.get_rect().width+5
			screen.blit(image_fond,(P-image_fond.get_rect().width, 0))
			if P>Y-600:
				screen.blit(image_fond,(P ,0))
			attaquant(attaquant_x, attaquant_y)
			if fire==True :
				balle(point, balle_y)

			if mort (ennemi_x, point, ennemi_y, balle_y)==True:
				score+=1
				if score>=10:
					mixer.music.stop()
					if by==True:
						musique(music_liste[0])
						by=False
					gagners= fond.render("Bravo !",True, WHITE)
					plai=False
					screen.blit(gagners,(50,500))
				ennemi_x=0
				ennemi_y=0
				ennemi_vitesse+=10
			if ennemi(ennemi_x,ennemi_y)==True:
				gagners= fond.render('Les aliens nous ont envahit !',True, WHITE)
				plai=False
				screen.blit(gagners,(50,500))
				text_pa=0

			if text_pa==1:
				gagners= fond.render(str(score),True, WHITE)
				screen.blit(gagners,(30,850))
				ti=str(time.time()-ti_st)
				ti=ti[0:4]
				gagners= fond.render(str(ti),True, WHITE)
				screen.blit(gagners,(750,850))

				gagners= fond.render(str(balle_uti),True, WHITE)
				screen.blit(gagners,(1650,850))

		e+=0.1
		pygame.display.update()


def intro():
	ver = (255, 255, 255)
	roug = (200,0,0)
	screen= pygame.display.set_mode((1800,1000))

	pygame.display.set_caption('Intro')

	image_list=['bk1_v.png',]
	image_back=pygame.image.load(image_list[0])

	music_liste=["music1.ogg"]
	fond=pygame.font.Font('freesansbold.ttf', 50)
	fonds=pygame.font.Font('freesansbold.ttf', 150)

	def musique(i):
		mixer.music.load(i)
		mixer.music.play()

	musique(music_liste[0])

	X=600
	Y=600
	run=True
	P=0
	z=2
	x=5800
	y=1000
	tv=0
	t=time.time()

	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False

			if event.type==pygame.KEYUP:
				if event.key==pygame.K_a:
					run=False
					invadexr()
				elif event.key==pygame.K_b:
					...
				elif event.key==pygame.K_c:
					...



		P= P % image_back.get_rect().width
		screen.blit(image_back,(P-image_back.get_rect().width, 0))
		if P>Y-600:
			screen.blit(image_back,(P ,0))
		P-=100

		if time.time()-t>=0.5:
			col=ver
			tv+=1
			if tv>=10:
				t=time.time()
				tv=0
		else:
			col=roug

		niveau1 = pygame.draw.rect(screen,(col),(676,300,500,50))
		text1 = fond.render('Niveau 1 = a', True, (100 , 254 ,0))
		screen.blit(text1,(810,300))
		niveau2 = pygame.draw.rect(screen,(col),(676,400,500,50))
		text2=fond.render('Niveau 2 = b', True, (100 , 254 ,0))
		screen.blit(text2,(810,400))
		niveau3 = pygame.draw.rect(screen,(col),(676,500,500,50))
		text3=fond.render('Niveau 3 = c', True, (100 , 254 ,0))
		screen.blit(text3,(810,500))
		titre=fonds.render("Invasion de l'espace", True,(0, 0, 255))
		screen.blit(titre, (180,100))
		pygame.display.update()




intro()











