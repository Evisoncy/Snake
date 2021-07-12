from pygame.locals import *
from juego import *
from jugador import *
from manzana import *
from jugador_2 import *
from random import lognormvariate, randint
import pygame
import time

class aplicacion:
 
    windowWidth = 1200
    windowHeight = 650
    jugador = 0
    manzana = 0
    jugador_2 = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._imageh_surf = None
        self._image_surf = None
        self._manzana_surf = None
        self.juego = juego()
        self.jugador = jugador(1) 
        self.manzana = manzana(13,13)
        self.jugador_2 = jugador_2(1)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Snake')
        self._running = True
        self._imageh_surf = pygame.image.load("human.jpg").convert()
        self._image_surf = pygame.image.load("block.jpg").convert()
        self._manzana_surf = pygame.image.load("manzana.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.jugador.update()
        self.jugador_2.update()
     
 
        # ¿la serpiente puede comer la manzana?
        for i in range(0,self.jugador.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.jugador.x[i], self.jugador.y[i]):
                self.manzana.x = randint(2,14) * 44
                self.manzana.y = randint(2,14) * 44
                self.jugador.longitud = self.jugador.longitud + 1

        for i in range(0,self.jugador_2.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.jugador_2.x[i], self.jugador_2.y[i]):
                self.manzana.x = randint(2,14) * 44
                self.manzana.y = randint(2,14) * 44
                self.jugador_2.longitud = self.jugador_2.longitud + 1        
                
 
 
        # ¿La serpiente choca consigo misma?
        #for i in range(2,self.jugador.longitud):
         #   if self.juego.isCollision(self.jugador.x[0],self.jugador.y[0],self.jugador.x[i], self.jugador.y[i],40):
          #      print("Perdiste! chocaste: ")
           #     print("x[0] (" + str(self.jugador.x[0]) + "," + str(self.jugador.y[0]) + ")")
            #    print("x[" + str(i) + "] (" + str(self.jugador.x[i]) + "," + str(self.jugador.y[i]) + ")")
             #   exit(0)
        #for i in range(2,self.jugador_2.longitud):
         #   if self.juego.isCollision(self.jugador_2.x[0],self.jugador_2.y[0],self.jugador_2.x[i], self.jugador_2.y[i],40):
          #      print("Perdiste! chocaste: ")
           #     print("x[0] (" + str(self.jugador_2.x[0]) + "," + str(self.jugador_2.y[0]) + ")")
            #    print("x[" + str(i) + "] (" + str(self.jugador_2.x[i]) + "," + str(self.jugador_2.y[i]) + ")")
             #   exit(0)
        for i in range(2,self.jugador.longitud):
            if self.juego.isCollision2(self.jugador.x[0],self.jugador.y[0],self.jugador_2.x[i], self.jugador_2.y[i],44):
                self.jugador.longitud = self.jugador.longitud - 1
                
        for i in range(2,self.jugador_2.longitud):
            if self.juego.isCollision2(self.jugador_2.x[0],self.jugador_2.y[0],self.jugador.x[i], self.jugador.y[i],44):
                self.jugador_2.longitud = self.jugador_2.longitud - 1  
 
        pygame.display.set_caption(" JUGADOR 1 SCORE: " + str(self.jugador.longitud-1) + "     " + " JUGADOR 2 SCORE: " + str(self.jugador_2.longitud-1))
        
        if self.jugador.longitud == 16:
            pygame.display.set_caption("\n\n\n\n GANO EL JUGADOR 1" )
            time.sleep(10)
            pygame.quit()
        else:
            if self.jugador_2.longitud == 16:
                pygame.display.set_caption("\n\n\n\n GANO EL JUGADOR 2" )
                time.sleep(10)
                pygame.quit()

        pass
        
        
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.jugador.draw(self._display_surf, self._imageh_surf)
        self.manzana.draw(self._display_surf, self._manzana_surf)
        self.jugador_2.draw(self._display_surf,self._image_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 

            if (keys[K_KP_3]):
                self.jugador_2.moveRight()
                
            if (keys[K_KP_1]):
                self.jugador_2.moveLeft()
                
            if (keys[K_KP_5]):
                self.jugador_2.moveUp()
                
            if (keys[K_KP_2]):
                self.jugador_2.moveDown()

            if (keys[K_RIGHT]):
                self.jugador.moveRight()
                
            if (keys[K_LEFT]):
                self.jugador.moveLeft()
                
            if (keys[K_UP]):
                self.jugador.moveUp()
                
            if (keys[K_DOWN]):
                self.jugador.moveDown()
                
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
            
 
            time.sleep (0.1)
        self.on_cleanup()
