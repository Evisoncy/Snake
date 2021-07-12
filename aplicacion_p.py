from tkinter import Label
from pygame.locals import *
from juego import *
from jugador import *
from manzana import *
from computadora_p import *
from pera import *
from random import lognormvariate, randint
import pygame
import time

class aplicacion_p:
 
    windowWidth = 1200
    windowHeight = 650
    jugador_p = 0
    manzana = 0
    carnada = 0

    computadora_p = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._imageh_surf = None
        self._image_surf = None
        self._manzana_surf = None
        self.juego = juego()
        self.jugador_p = jugador_p(1) 
        self.manzana = manzana(14,14)
        self.computadora_p = computadora_p(1)
        self.carnada = carnada(5,10)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        self._running = True
        self._imageh_surf = pygame.image.load("human.jpg").convert()
        self._image_surf = pygame.image.load("block.jpg").convert()
        self._manzana_surf = pygame.image.load("manzana.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        keys = pygame.key.get_pressed() 
        self.jugador_p.update()
        self.computadora_p.update()
        
     
 
        # ¿la serpiente puede comer la manzana?
        for i in range(0,self.jugador_p.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.jugador_p.x[i], self.jugador_p.y[i]):
                self.manzana.x = randint(2,14) * 44
                self.manzana.y = randint(2,14) * 44
                self.jugador_p.longitud = self.jugador_p.longitud + 1
                
        for i in range(0,self.computadora_p.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.computadora_p.x[i], self.computadora_p.y[i]):
                self.manzana.x = randint(2,14) * 44
                self.manzana.y = randint(2,14) * 44
                self.computadora_p.longitud = self.computadora_p.longitud + 1
        
        for i in range(0,self.computadora_p.longitud):
            if self.juego.isCollision(self.carnada.x,self.carnada.y,self.computadora_p.x[i], self.computadora_p.y[i]):
                self.carnada.x = randint(2,14) * 44
                self.carnada.y = randint(2,14) * 44

                #self.computadora_p.longitud = self.computadora_p.longitud + 1
        # for i in range(0,self.computadora_p.longitud):
        #     if self.juego.isCollision2(self.carnada.x,self.carnada.y,self.manzana.x,self.manzana.y,self.computadora_p.x[i], self.computadora_p.y[i]):
        #         self.carnada.x = randint(2,14) * 44
        #         self.carnada.y = randint(2,14) * 44
        #         self.manzana.x = randint(2,14) * 44
        #         self.manzana.y = randint(2,14) * 44

        for i in range(2,self.jugador_p.longitud):
            if self.juego.isCollision2(self.jugador_p.x[0],self.jugador_p.y[0],self.computadora_p.x[i], self.computadora_p.y[i],44):
                self.jugador_p.longitud = self.jugador_p.longitud - 1
                
        for i in range(2,self.computadora_p.longitud):
            if self.juego.isCollision2(self.computadora_p.x[0],self.computadora_p.y[0],self.jugador_p.x[i], self.jugador_p.y[i],44):
                self.computadora_p.longitud = self.computadora_p.longitud - 1                    
                
 
        pygame.display.set_caption(" HUMANO SCORE: " + str(self.jugador_p.longitud-1) + "     " + " COMPUTADORA SCORE: " + str(self.computadora_p.longitud-1))
        
        if self.jugador_p.longitud == 16:
            pygame.display.set_caption("\n\n\n\n GANO EL HUMANO" )
            time.sleep(10)
            pygame.quit()
        else:
            if self.computadora_p.longitud == 16:
                pygame.display.set_caption("\n\n\n\n GANO LA COMPUTADORA" )
                time.sleep(10)
                pygame.quit()


        # ¿La serpiente choca consigo misma?
        #for i in range(2,self.jugador.longitud):
         #   if self.juego.isCollision(self.jugador.x[0],self.jugador.y[0],self.jugador.x[i], self.jugador.y[i],44):
          #      print("Perdiste! chocaste: ")
            #    print("x[0] (" + str(self.jugador.x[0]) + "," + str(self.jugador.y[0]) + ")")
           #     print("x[" + str(i) + "] (" + str(self.jugador.x[i]) + "," + str(self.jugador.y[i]) + ")")
             #   exit(0)
        #for i in range(2,self.computadora_p.longitud):
        #    if self.juego.isCollision(self.computadora_p.x[0],self.computadora_p.y[0],self.computadora_p.x[i], self.computadora_p.y[i],40):
         #       print("Perdiste! chocaste: ")
          #      print("x[0] (" + str(self.computadora_p.x[0]) + "," + str(self.computadora_p.y[0]) + ")")
           #     print("x[" + str(i) + "] (" + str(self.computadora_p.x[i]) + "," + str(self.computadora_p.y[i]) + ")")
            #    exit(0)
 
        pass
        
        
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.jugador_p.draw(self._display_surf, self._imageh_surf)
        self.manzana.draw(self._display_surf, self._manzana_surf)
        self.computadora_p.draw(self._display_surf,self._image_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 

            self.computadora_p.target(self.carnada.x, self.carnada.y)
            #self.computadora_p.target(self.manzana.x, self.manzana.y)

            if (keys[K_RIGHT]):
                self.jugador_p.moveRight()
                
            if (keys[K_LEFT]):
                self.jugador_p.moveLeft()
                
            if (keys[K_UP]):
                self.jugador_p.moveUp()
                
            if (keys[K_DOWN]):
                self.jugador_p.moveDown()
                
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
            time.sleep(0.1)
 

        self.on_cleanup()
