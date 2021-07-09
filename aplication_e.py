from pygame.locals import *
from juego import *
from jugador import *
from manzana import *
from computadora_e import *
from random import lognormvariate, randint
import pygame
import time

class aplication_e:
 
    windowWidth = 800
    windowHeight = 600
    jugador = 0
    manzana = 0
    computadora = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._manzana_surf = None
        self.juego = juego()
        self.jugador = jugador(3) 
        self.manzana = manzana(5,5)
        self.computadora_e = computadora_e(1)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Snake')
        self._running = True
        self._image_surf = pygame.image.load("block.jpg").convert()
        self._manzana_surf = pygame.image.load("manzana.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.jugador.update()
        self.computadora_e.update()
     
 
        # ¿la serpiente puede comer la manzana?
        for i in range(0,self.jugador.longitud):
            if self.juego.isCollision(self.manzana.x,self.manzana.y,self.jugador.x[i], self.jugador.y[i],44):
                self.manzana.x = randint(2,9) * 44
                self.manzana.y = randint(2,9) * 44
                self.jugador.longitud = self.jugador.longitud + 1

        #for i in range(0,self.computadora_e.longitud):
         #   if self.juego.isCollision(self.manzana.x,self.manzana.y,self.computadora_e.x[i], self.computadora_e.y[i],44):
          #      self.manzana.x = randint(2,9) * 44
           #     self.manzana.y = randint(2,9) * 44
            #    self.computadora_e.longitud = self.computadora_e.longitud + 1        
                
 
 
        # ¿La serpiente choca consigo misma?
        for i in range(2,self.jugador.longitud):
            if self.juego.isCollision(self.jugador.x[0],self.jugador.y[0],self.jugador.x[i], self.jugador.y[i],40):
                print("Perdiste! chocaste: ")
                print("x[0] (" + str(self.jugador.x[0]) + "," + str(self.jugador.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.jugador.x[i]) + "," + str(self.jugador.y[i]) + ")")
                exit(0)
        #for i in range(2,self.computadora_e.longitud):
        #    if self.juego.isCollision(self.computadora_e.x[0],self.computadora_e.y[0],self.computadora_e.x[i], self.computadora_e.y[i],40):
         #       print("Perdiste! chocaste: ")
          #      print("x[0] (" + str(self.computadora_e.x[0]) + "," + str(self.computadora_e.y[0]) + ")")
           #     print("x[" + str(i) + "] (" + str(self.computadora_e.x[i]) + "," + str(self.computadora_e.y[i]) + ")")
            #    exit(0)
 
        pass
        
        
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.jugador.draw(self._display_surf, self._image_surf)
        self.manzana.draw(self._display_surf, self._manzana_surf)
        self.computadora_e.draw(self._display_surf,self._image_surf)
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
                 self.computadora_e.moveRight()

            if (keys[K_KP_1]):
                self.computadora_e.moveLeft()

            if (keys[K_KP_5]):
                self.computadora_e.moveUp()
                
            if (keys[K_KP_2]):
                self.computadora_e.moveDown()

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
            
 
            time.sleep (100.0 / 500.0)
            #self.jugador.time.sleep(50.0 / 500.0)

        self.on_cleanup()
