#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
pygame.init()
cozunurluk=480,320
ekran_mod=HWSURFACE
baslik='Mangala'
fps=20
siyah=0,0,0
mavi=0,0,255
beyaz=255,255,255
kirmizi=255,0,0
ekran=pygame.display.set_mode(cozunurluk,ekran_mod)
pygame.display.set_caption(baslik)
font=pygame.font.Font(None,60)
font2=pygame.font.Font(None,35)
en=60
boy=60
def haznekutu(x,y):
	return pygame.Rect(x,y,en,boy)
hk1=[None]*6
hk2=[None]*6
for i in range(0,6):
	hk1[i]=haznekutu(en*(i+1),180)
	hk2[i]=haznekutu(en*(i+1),0)
def yenioyun():
	global s,oyuncu_birinci,oyunbitti
	s=([4]*6+[0])*2
	oyuncu_birinci=True
	oyunbitti=False
yenioyun()
def hazne(sayi,x,y,k):
	kboy=k*boy
	pygame.draw.rect(ekran,mavi,(x,y,en,kboy))
	pygame.draw.rect(ekran,beyaz,(x,y,en,kboy),1)
	yazi=font.render(str(sayi),1,siyah)
	yx,yy=yazi.get_size()
	ekran.blit(yazi,(x+en/2-yx/2,y+kboy/2-yy/2))
def olustur():
	hazne(s[6],0,boy,2)
	hazne(s[13],60*7,boy,2)
	for i in range(0,6):
		ii=5-i
		hazne(s[ii],en*(i+1),0,1)
		hazne(s[i+7],en*(i+1),180,1)
	if oyuncu_birinci:
		sirametin='1'
	else:
		sirametin='2'
	oyuncuyazi1=font2.render('1.',1,beyaz)
	oyuncuyazi2=font2.render('2.',1,beyaz)
	bilgi_yazi=font2.render('Hamle sirasi '+sirametin+'. oyuncuda',1,beyaz)
	bx,by=bilgi_yazi.get_size()
	bilgi_yazi2=font2.render('Y: Yeni Oyun ESC: Cikis',1,beyaz)
	bx2,by2=bilgi_yazi2.get_size()
	ekran.blit(oyuncuyazi1,((cozunurluk[0]-35)/2,145))
	ekran.blit(oyuncuyazi2,((cozunurluk[0]-35)/2,60))
	ekran.blit(bilgi_yazi,((cozunurluk[0]-bx)/2,boy*4+8))
	ekran.blit(bilgi_yazi2,((cozunurluk[0]-bx2)/2,boy*4+by+16))
def fonkoyunbitti():
	bittiyazi1=font2.render('Oyun Bitti',1,kirmizi)
	x1,y1=bittiyazi1.get_size()
	bittiyazi2=font2.render('1. Oyuncu: '+str(s[13])+' 2. Oyuncu: '+str(s[6]),1,mavi)
	x2,y2=bittiyazi2.get_size()
	bittiyazi3=font2.render('Y: Yeni Oyun ESC: Cikis',1,beyaz)
	x3,y3=bittiyazi3.get_size()
	ekran.blit(bittiyazi1,((cozunurluk[0]-x1)/2,(cozunurluk[1]-y2)/2-y1))
	ekran.blit(bittiyazi2,((cozunurluk[0]-x2)/2,(cozunurluk[1]-y2)/2))
	ekran.blit(bittiyazi3,((cozunurluk[0]-x3)/2,(cozunurluk[1]-y2)/2+y2))
saat=pygame.time.Clock()
bitti=False
while not bitti:
	for olay in pygame.event.get():
		if olay.type==QUIT:
			bitti=True
		elif olay.type==KEYDOWN:
			if olay.key==K_ESCAPE:
				bitti=True
			elif olay.key==K_y:
				yenioyun()
		elif olay.type==MOUSEBUTTONDOWN:
			if olay.button==1:
				if oyuncu_birinci:
					for i in range(0,6):
						if hk1[i].collidepoint(olay.pos):
							gg=s[i+7]
							if gg!=0:
								for jj in range(1,gg+1):
									s[(i+7+jj)%14]+=1
									s[i+7]=0
								son=(i+7+jj)%14
								if son==13:
									oyuncu_birinci=True
								else:
									if son in [0,5]:
										if s[son]%2==0:
											s[13]+=s[son]
											s[son]=0
									else:
										if s[son]==1:
											s[13]+=s[12-son]+1
											s[son]=0
											s[12-son]=0
									oyuncu_birinci=False
								if sum(s[7:-1])==0:
									s[13]+=sum(s[:6])
									s[:6]=[0]*6
									oyunbitti=True
				else:
					for i in range(0,6):
						if hk2[i].collidepoint(olay.pos):
							gg=s[5-i]
							if gg!=0:
								for jj in range(1,gg+1):
									s[(5-i+jj)%14]+=1
									s[5-i]=0
								son=(5-i+jj)%14
								if son==6:
									oyuncu_birinci=False
								else:
									if son in [7,12]:
										if s[son]%2==0:
											s[6]+=s[son]
											s[son]=0
									else:
										if s[son]==1:
											s[6]+=s[12-son]+1
											s[son]=0
											s[12-son]=0
									oyuncu_birinci=True
								if sum(s[:6])==0:
									s[6]+=sum(s[7:-1])
									s[7:-1]=[0]*6
									oyunbitti=True
	ekran.fill(siyah)
	if oyunbitti==False:
		olustur()
	else:
		fonkoyunbitti()
	pygame.display.flip()
	saat.tick(fps)
