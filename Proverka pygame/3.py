import pygame as pg
pg.init()
sc = pg.display.set_mode((800,600))
GREEN = (0,255,0)
RED = (255,0,0)
DARKGREEN = (0,100,0)
STATEBLUE=(106,90,205)
color = (75,0,130)
pg.draw.line(sc,GREEN,(0,0),(800,600),5)

pg.draw.lines(sc,RED,True,[(400,0),(800,300),(0,300)],3)
pg.draw.rect(sc,color,(10,10,50,100))
pg.draw.circle(sc,GREEN,(400,300,),40)
pg.draw.ellipse(sc,DARKGREEN,(300,300,100,50),1)
pg.draw.polygon(sc,STATEBLUE,[[150,210],[180,250],[90,290],[30,230]])





pg.display.update()
