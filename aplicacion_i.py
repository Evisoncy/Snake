from pygame.locals import *
from juego import *
from jugador import *
from manzana import *
from computadora_i import *
from random import lognormvariate, randint
import pygame
import time

class aplicacion_i:
 
    windowWidth = 1200
    windowHeight = 650
    jugador_i = 0
    manzana = 0
    computadora_i = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._imageh_surf = None
        self._image_surf = None
        self._manzana_surf = None
        self.juego = juego()
        self.jugador_i = jugador_i(1) 
        self.manzana = manzana(13,13)
        self.computadora_i = computadora_i(1)
 
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
        self.jugador_i.update()
        self.computadora_i.update()
     
 
        # ¿la serpiente puede comer la manzana?
        for i in range(0,self.jugador_i.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.jugador_i.x[i], self.jugador_i.y[i]):
                self.manzana.x = randint(2,14) * 44
                self.manzana.y = randint(2,14) * 44
                self.jugador_i.longitud = self.jugador_i.longitud + 1

        for i in range(0,self.computadora_i.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.computadora_i.x[i], self.computadora_i.y[i]):
                self.manzana.x = randint(2,14) * 44
                self.manzana.y = randint(2,14) * 44
                self.computadora_i.longitud = self.computadora_i.longitud + 1        
                
 
 
        # ¿La serpiente choca consigo misma?
       # for i in range(2,self.jugador_i.longitud):
        #    if self.juego.isCollision(self.jugador_i.x[0],self.jugador_i.y[0],self.jugador_i.x[i], self.jugador_i.y[i],40):
         #       print("Perdiste! chocaste: ")
          #      print("x[0] (" + str(self.jugador_i.x[0]) + "," + str(self.jugador_i.y[0]) + ")")
           #     print("x[" + str(i) + "] (" + str(self.jugador_i.x[i]) + "," + str(self.jugador_i.y[i]) + ")")
            #    exit(0)
        #for i in range(2,self.computadora_i.longitud):
         #   if self.juego.isCollision(self.computadora_i.x[0],self.computadora_i.y[0],self.computadora_i.x[i], self.computadora_i.y[i],40):
          #      print("Perdiste! chocaste: ")
           #     print("x[0] (" + str(self.computadora_i.x[0]) + "," + str(self.computadora_i.y[0]) + ")")
            #    print("x[" + str(i) + "] (" + str(self.computadora_i.x[i]) + "," + str(self.computadora_i.y[i]) + ")")
             #   exit(0)
        pygame.display.set_caption(" HUMANO SCORE: " + str(self.jugador_i.longitud-1) + "     " + " COMPUTADORA SCORE: " + str(self.computadora_i.longitud-1))
        
        if self.jugador_i.longitud == 16:
            pygame.display.set_caption("\n\n\n\n GANO EL HUMANO" )
            time.sleep(10)
            pygame.quit()
        else:
            if self.computadora_i.longitud == 16:
                pygame.display.set_caption("\n\n\n\n GANO LA COMPUTADORA" )
                time.sleep(10)
                pygame.quit()
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.jugador_i.draw(self._display_surf, self._imageh_surf)
        self.manzana.draw(self._display_surf, self._manzana_surf)
        self.computadora_i.draw(self._display_surf,self._image_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 

            self.computadora_i.target(self.manzana.x, self.manzana.y)

            if (keys[K_RIGHT]):
                self.jugador_i.moveRight()
                
            if (keys[K_LEFT]):
                self.jugador_i.moveLeft()
                
            if (keys[K_UP]):
                self.jugador_i.moveUp()
                
            if (keys[K_DOWN]):
                self.jugador_i.moveDown()
                
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
            
            
            time.sleep (0.2)
        self.on_cleanup()
