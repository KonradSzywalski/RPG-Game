import pygame
import sys
import time
import pygame
import sys
import os
import random
from math import pi, sin, cos, atan2
from pygame.locals import *


## STAŁE
## kolory


WHITE = pygame.color.THECOLORS['white']
BLACK = pygame.color.THECOLORS['black']
DARKRED = pygame.color.THECOLORS['darkred']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
BLUE = pygame.color.THECOLORS['blue']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']


stand_R = pygame.image.load(os.path.join('png', 'player_standR_new.png'))
walk_R1 = pygame.image.load(os.path.join('png', 'player_walkR1_new.png'))
walk_R2 = pygame.image.load(os.path.join('png', 'player_walkR2_new.png'))

stand_up = pygame.image.load(os.path.join('png', 'player_standUP_new.png'))
up_R1 = pygame.image.load(os.path.join('png', 'player_upR1_new.png'))
up_R2 = pygame.image.load(os.path.join('png', 'player_upR2_new.png'))

stand_down = pygame.image.load(os.path.join('png', 'player_standDOWN_new.png'))
down_L1 = pygame.image.load(os.path.join('png', 'player_downL1_new.png'))
down_L2 = pygame.image.load(os.path.join('png', 'player_downL2_new.png'))

stand_L = pygame.image.load(os.path.join('png', 'player_standL_new.png'))
walk_L1 = pygame.image.load(os.path.join('png', 'player_walkL1_new.png'))
walk_L2 = pygame.image.load(os.path.join('png', 'player_walkL2_new.png'))

image_right = [walk_R1, walk_R2]
image_left = [walk_L1, walk_L2]
image_up = [up_R1, stand_up]
image_down = [down_L1,down_L2]

fight_L1 = pygame.image.load(os.path.join('png', 'player_fight_L1.png'))
fight_R1 = pygame.image.load(os.path.join('png', 'player_fight_R1.png'))
fight_up1 = pygame.image.load(os.path.join('png', 'player_fight_up.png'))
fight_down1 = pygame.image.load(os.path.join('png', 'player_fight_down.png'))


fight_left = [fight_L1, stand_L]
fight_right = [fight_R1, stand_R]
fight_up = [fight_up1, stand_up]
fight_down = [fight_down1, stand_down]


ZOMBIE_STAND_R = pygame.image.load(os.path.join('png', 'snake_stand.png'))

ZOMBIE_WALK_R1 = pygame.image.load(os.path.join('png', 'snake_walkR1.png'))
ZOMBIE_WALK_R2 = pygame.image.load(os.path.join('png', 'snake_walkR2.png'))

ZOMBIE_WALK_L1 = pygame.image.load(os.path.join('png', 'snake_walkL1.png'))
ZOMBIE_WALK_L2 = pygame.image.load(os.path.join('png', 'snake_walkL2.png'))

ZOMBIE_DEAD_R = pygame.image.load(os.path.join('png', 'snake_walkR1.png'))
ZOMBIE_DEAD_L = pygame.image.load(os.path.join('png', 'snake_walkL1.png'))

ZOMBIE_WALK_R = [ZOMBIE_WALK_R1, ZOMBIE_WALK_R2]
ZOMBIE_WALK_L = [ZOMBIE_WALK_L1, ZOMBIE_WALK_L2]
ZOMBIE_DEAD_R = [ZOMBIE_DEAD_R, ZOMBIE_DEAD_R]
ZOMBIE_DEAD_L = [ZOMBIE_DEAD_L, ZOMBIE_DEAD_L]


GUARDIAN_STAND_R = pygame.image.load(os.path.join('png', 'guardian_stand.png'))

GUARDIAN_WALK_R1 = pygame.image.load(os.path.join('png', 'guardian_walkR1.png'))
GUARDIAN_WALK_R2 = pygame.image.load(os.path.join('png', 'guardian_walkR2.png'))

GUARDIAN_WALK_L1 = pygame.image.load(os.path.join('png', 'guardian_walkL1.png'))
GUARDIAN_WALK_L2 = pygame.image.load(os.path.join('png', 'guardian_walkL2.png'))

GUARDIAN_DEAD_R = pygame.image.load(os.path.join('png', 'guardian_walkR1.png'))
GUARDIAN_DEAD_L = pygame.image.load(os.path.join('png', 'guardian_walkL1.png'))

GUARDIAN_WALK_R = [GUARDIAN_WALK_R1, GUARDIAN_WALK_R2]
GUARDIAN_WALK_L = [GUARDIAN_WALK_L1, GUARDIAN_WALK_L2]
GUARDIAN_DEAD_R = [GUARDIAN_DEAD_R, GUARDIAN_DEAD_R]
GUARDIAN_DEAD_L = [GUARDIAN_DEAD_L, GUARDIAN_DEAD_L]



BOSS_STAND_R = pygame.image.load(os.path.join('png', 'boss_stand.png'))

BOSS_WALK_R1 = pygame.image.load(os.path.join('png', 'boss_walkR1.png'))
BOSS_WALK_R2 = pygame.image.load(os.path.join('png', 'boss_walkR2.png'))

BOSS_WALK_L1 = pygame.image.load(os.path.join('png', 'boss_walkL1.png'))
BOSS_WALK_L2 = pygame.image.load(os.path.join('png', 'boss_walkL2.png'))

BOSS_DEAD_R = pygame.image.load(os.path.join('png', 'boss_walkR1.png'))
BOSS_DEAD_L = pygame.image.load(os.path.join('png', 'boss_walkL1.png'))

BOSS_WALK_R = [BOSS_WALK_R1, BOSS_WALK_R2]
BOSS_WALK_L = [BOSS_WALK_L1, BOSS_WALK_L2]
BOSS_DEAD_R = [BOSS_DEAD_R, BOSS_DEAD_R]
BOSS_DEAD_L = [BOSS_DEAD_L, BOSS_DEAD_L]



NPC_FIRST_STAND_R = pygame.image.load(os.path.join('png', 'npc_first_stand.png'))

NPC_FIRST_WALK_R1 = pygame.image.load(os.path.join('png', 'npc_first_walkR1.png'))
NPC_FIRST_WALK_R2 = pygame.image.load(os.path.join('png', 'npc_first_walkR2.png'))

NPC_FIRST_WALK_L1 = pygame.image.load(os.path.join('png', 'npc_first_walkL1.png'))
NPC_FIRST_WALK_L2 = pygame.image.load(os.path.join('png', 'npc_first_walkL2.png'))

NPC_FIRST_DEAD_R = pygame.image.load(os.path.join('png', 'npc_first_walkR1.png'))
NPC_FIRST_DEAD_L = pygame.image.load(os.path.join('png', 'npc_first_walkL1.png'))


NPC_FIRST_WALK_R = [NPC_FIRST_WALK_R1, NPC_FIRST_WALK_R2]
NPC_FIRST_WALK_L = [NPC_FIRST_WALK_L1, NPC_FIRST_WALK_L2]
NPC_FIRST_DEAD_R = [NPC_FIRST_DEAD_R, NPC_FIRST_DEAD_R]
NPC_FIRST_DEAD_L = [NPC_FIRST_DEAD_L, NPC_FIRST_DEAD_L]


NPC_SECOND_STAND_R = pygame.image.load(os.path.join('png', 'npc_second_stand.png'))

NPC_SECOND_WALK_R1 = pygame.image.load(os.path.join('png', 'npc_second_walkR1.png'))
NPC_SECOND_WALK_R2 = pygame.image.load(os.path.join('png', 'npc_second_walkR2.png'))

NPC_SECOND_WALK_L1 = pygame.image.load(os.path.join('png', 'npc_second_walkL1.png'))
NPC_SECOND_WALK_L2 = pygame.image.load(os.path.join('png', 'npc_second_walkL2.png'))

NPC_SECOND_DEAD_R = pygame.image.load(os.path.join('png', 'npc_second_walkR1.png'))
NPC_SECOND_DEAD_L = pygame.image.load(os.path.join('png', 'npc_second_walkL1.png'))


NPC_SECOND_WALK_R = [NPC_SECOND_WALK_R1, NPC_SECOND_WALK_R2]
NPC_SECOND_WALK_L = [NPC_SECOND_WALK_L1, NPC_SECOND_WALK_L2]
NPC_SECOND_DEAD_R = [NPC_SECOND_DEAD_R, NPC_SECOND_DEAD_R]
NPC_SECOND_DEAD_L = [NPC_SECOND_DEAD_L, NPC_SECOND_DEAD_L]



NPC_THIRD_STAND_R = pygame.image.load(os.path.join('png', 'npc_third_stand.png'))

NPC_THIRD_WALK_R1 = pygame.image.load(os.path.join('png', 'npc_third_walkR1.png'))
NPC_THIRD_WALK_R2 = pygame.image.load(os.path.join('png', 'npc_third_walkR2.png'))

NPC_THIRD_WALK_L1 = pygame.image.load(os.path.join('png', 'npc_third_walkL1.png'))
NPC_THIRD_WALK_L2 = pygame.image.load(os.path.join('png', 'npc_third_walkL2.png'))

NPC_THIRD_DEAD_R = pygame.image.load(os.path.join('png', 'npc_third_walkR1.png'))
NPC_THIRD_DEAD_L = pygame.image.load(os.path.join('png', 'npc_third_walkL1.png'))


NPC_THIRD_WALK_R = [NPC_THIRD_WALK_R1, NPC_THIRD_WALK_R2]
NPC_THIRD_WALK_L = [NPC_THIRD_WALK_L1, NPC_THIRD_WALK_L2]
NPC_THIRD_DEAD_R = [NPC_THIRD_DEAD_R, NPC_THIRD_DEAD_R]
NPC_THIRD_DEAD_L = [NPC_THIRD_DEAD_L, NPC_THIRD_DEAD_L]


NPC_FOURTH_STAND_R = pygame.image.load(os.path.join('png', 'npc_fourth_stand.png'))

NPC_FOURTH_WALK_R1 = pygame.image.load(os.path.join('png', 'npc_fourth_walkR1.png'))
NPC_FOURTH_WALK_R2 = pygame.image.load(os.path.join('png', 'npc_fourth_walkR2.png'))

NPC_FOURTH_WALK_L1 = pygame.image.load(os.path.join('png', 'npc_fourth_walkL1.png'))
NPC_FOURTH_WALK_L2 = pygame.image.load(os.path.join('png', 'npc_fourth_walkL2.png'))

NPC_FOURTH_DEAD_R = pygame.image.load(os.path.join('png', 'npc_fourth_walkR1.png'))
NPC_FOURTH_DEAD_L = pygame.image.load(os.path.join('png', 'npc_fourth_walkL1.png'))


NPC_FOURTH_WALK_R = [NPC_FOURTH_WALK_R1, NPC_FOURTH_WALK_R2]
NPC_FOURTH_WALK_L = [NPC_FOURTH_WALK_L1, NPC_FOURTH_WALK_L2]
NPC_FOURTH_DEAD_R = [NPC_FOURTH_DEAD_R, NPC_FOURTH_DEAD_R]
NPC_FOURTH_DEAD_L = [NPC_FOURTH_DEAD_L, NPC_FOURTH_DEAD_L]

NPC_FIFTH_STAND_R = pygame.image.load(os.path.join('png', 'npc_fifth_stand.png'))

NPC_FIFTH_WALK_R1 = pygame.image.load(os.path.join('png', 'npc_fifth_walkR1.png'))
NPC_FIFTH_WALK_R2 = pygame.image.load(os.path.join('png', 'npc_fifth_walkR1.png'))

NPC_FIFTH_WALK_L1 = pygame.image.load(os.path.join('png', 'npc_fifth_walkL1.png'))
NPC_FIFTH_WALK_L2 = pygame.image.load(os.path.join('png', 'npc_fifth_walkL1.png'))

NPC_FIFTH_DEAD_R = pygame.image.load(os.path.join('png', 'npc_fifth_walkR1.png'))
NPC_FIFTH_DEAD_L = pygame.image.load(os.path.join('png', 'npc_fifth_walkL1.png'))


NPC_FIFTH_WALK_R = [NPC_FIFTH_WALK_R1, NPC_FIFTH_WALK_R2]
NPC_FIFTH_WALK_L = [NPC_FIFTH_WALK_L1, NPC_FIFTH_WALK_L2]
NPC_FIFTH_DEAD_R = [NPC_FIFTH_DEAD_R, NPC_FIFTH_DEAD_R]
NPC_FIFTH_DEAD_L = [NPC_FIFTH_DEAD_L, NPC_FIFTH_DEAD_L]

KEY = pygame.image.load(os.path.join('png', 'key.png'))
gate = pygame.image.load(os.path.join('png', 'gate.png'))
boss_gate = pygame.image.load(os.path.join('png', 'boos_gate.png'))

end_text = pygame.image.load(os.path.join('png', 'end_text.png'))
pause = pygame.image.load(os.path.join('png', 'pause.png'))
ded_text = pygame.image.load(os.path.join('png', 'umarles.png'))
options_text = pygame.image.load(os.path.join('png', 'options.png'))

sklep_poty =  pygame.image.load(os.path.join('png', 'sklep_poty.png'))
sklep_max_hp =  pygame.image.load(os.path.join('png', 'sklep_max_hp.png'))
sklep_sila =  pygame.image.load(os.path.join('png', 'sklep_sila.png'))
sklep_regen =  pygame.image.load(os.path.join('png', 'sklep_regen.png'))

pygame.display.set_caption('Prosta gra platformowa...')
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1920,1080



ramka_statystyki = pygame.image.load(os.path.join('png', 'ramka_statystyki.png'))
platform_background = pygame.image.load(os.path.join('png', 'transparent.png'))
DARKRED = pygame.color.THECOLORS['darkred']
title_image = pygame.image.load(os.path.join('png', 'we_we_v9.png'))
pause_img = pygame.image.load(os.path.join('png', 'pause.png'))
mapa_main = pygame.image.load(os.path.join('png', 'mapa_rdy_v4_edit.png'))

pause = False


## klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image, current_level = None):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = {}
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0
        self.level = current_level
        self.lifes = 150
        self.max_lifes = 150
        self.stance = 0
        self.orientation = 'right'
        self.keys = 0
        self.gold = 200
        self.potions = 3
        self.strenght = 10
        self.dusze = 0
        self.boss = 0
    
    def turn_right(self):
        self.movement_x = 6

    def turn_left(self):
        self.movement_x = -6

    def turn_down(self):
        self.movement_y = 6
        
    def turn_up(self):
        self.movement_y = -6
        
    def stop(self):
        self.movement_x = 0
        
    def stop_y(self):   
        self.movement_y = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count  = 0
        else:
            self.count += 1

    def fight(self, image_list):
        self.stance = 0
        if self.count < 2:
            attack = pygame.mixer.Sound("sounds/attack.wav")
            pygame.mixer.Sound.play(attack)
            self.image = image_list[0]
            self.stance = 1
        elif self.count < 3:
            self.image = image_list[1]
            self.stance = 0

        if self.count >= 3:
            self.count  = 0
        else:
            self.count += 1
            
    def use_potion(self):
        if(self.potions > 0):
            potion = pygame.mixer.Sound("sounds/potion.wav")
            pygame.mixer.Sound.play(potion)
            self.potions = self.potions - 1
            self.lifes = self.lifes + 50
        if(self.lifes>self.max_lifes):
            self.lifes=self.max_lifes        

    #zakupy_w_sklepie
    
    
    def zakupy_buy(self):
        colliding_shops = pygame.sprite.spritecollide(self, self.level.set_of_shops_potions, False)
        for x in colliding_shops:
            if(self.gold>=50):
                crash_sound = pygame.mixer.Sound("sounds/money.wav")
                pygame.mixer.Sound.play(crash_sound)
                self.gold = self.gold - 50
                self.potions = self.potions + 1
                
    def zakupy_sila(self):
        colliding_shops = pygame.sprite.spritecollide(self, self.level.set_of_shops_sila, False)
        for x in colliding_shops:
            if(self.gold>=100):
                crash_sound = pygame.mixer.Sound("sounds/money.wav")
                pygame.mixer.Sound.play(crash_sound)
                self.gold = self.gold - 100
                self.strenght = self.strenght + 10
                
    def zakupy_max_hp(self):
        colliding_shops = pygame.sprite.spritecollide(self, self.level.set_of_shops_max_hp, False)
        for x in colliding_shops:
            if(self.gold>=50):
                crash_sound = pygame.mixer.Sound("sounds/money.wav")
                pygame.mixer.Sound.play(crash_sound)
                self.gold = self.gold - 50
                self.max_lifes = self.max_lifes + 50

    def zakupy_regen(self):
        colliding_shops = pygame.sprite.spritecollide(self, self.level.set_of_shops_regen, False)
        for x in colliding_shops:
                heal = pygame.mixer.Sound("sounds/heal.wav")
                pygame.mixer.Sound.play(heal)
                self.lifes = self.max_lifes            
                

    def update(self):
        
        if(player.lifes <=0):
            self.image = platform_background
        
        #sprawdzanie kolizji z platformami blokujacymi tekstury oraz sklepami
        self.rect.x += self.movement_x

        #brama usuwanie
        colliding_brama = pygame.sprite.spritecollide(self, self.level.set_of_brama, False)
        for p in colliding_brama:
            if(self.keys==5):
                self.level.set_of_brama.remove(p)       
        
        colliding_brama = pygame.sprite.spritecollide(self, self.level.set_of_brama, False)
        colliding_brama_boss = pygame.sprite.spritecollide(self, self.level.set_of_brama_boss, False)
        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for p in colliding_platforms + colliding_brama + colliding_brama_boss:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        if self.movement_x > 0:
            self._move(image_right)
        if self.movement_x < 0:
            self._move(image_left)
     
        if self.movement_y > 0:
            self._move(image_down)
        if self.movement_y < 0:
            self._move(image_up)
        self.rect.y += self.movement_y

        colliding_brama_boss = pygame.sprite.spritecollide(self, self.level.set_of_brama_boss, False)
        for p in colliding_brama_boss:
            if(self.dusze==4):
                self.level.set_of_brama_boss.remove(p)

        colliding_brama = pygame.sprite.spritecollide(self, self.level.set_of_brama, False)
        colliding_brama_boss = pygame.sprite.spritecollide(self, self.level.set_of_brama_boss, False)
        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        for p in colliding_platforms + colliding_brama + colliding_brama_boss:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0


        
        # sprawdzamy kolizję z wrogami
        colliding_enmies = pygame.sprite.spritecollide(self, self.level.set_of_enemies, False)
   
        for enemy in colliding_enmies:    
            if enemy.lifes:
                self.lifes -= 0.3
            if enemy.lifes and self.stance is 1:   
                enemy.lifes = enemy.lifes - self.strenght/5      
            if  enemy.lifes <= 0 and enemy.count > 7:
                self.gold = self.gold + 150


 
        colliding_enmies = pygame.sprite.spritecollide(self, self.level.set_of_enemy_follow, False)
        #kolizja z wrogami(obroncy)
        for enemy in colliding_enmies:    
            if enemy.lifes:
                self.lifes -= 0.4
            if enemy.lifes and self.stance is 1:   
                enemy.lifes = enemy.lifes - self.strenght/5      
            if enemy.lifes <= 0 and enemy.count > 7:
                self.gold = self.gold + 150
                self.dusze = self.dusze + 1

         #kolizja z wrogami(boss)
        colliding_enmies = pygame.sprite.spritecollide(self, self.level.set_of_boss, False)
        for enemy in colliding_enmies:    
            if enemy.lifes:
                self.lifes -= 0.5
            if enemy.lifes and self.stance is 1:   
                enemy.lifes = enemy.lifes - self.strenght/5      
            if enemy.lifes <= 0 and enemy.count > 7:
                self.gold = self.gold + 500
                self.boss = self.boss + 1

        
        # rysowanie żyć na ekranie
        if(player.lifes > 0):
            label = myfont.render(str(round(self.lifes))+'/'+str(self.max_lifes), 1, (255,255,255))
            surface.blit(label, [910+self.movement_x,480+self.movement_y])


        #rysowanie statystyk/ekwipnku na ekranie
        hp_info = myfont.render('HP:' + str(round(self.lifes))+'/'+str(self.max_lifes), 1, (255,255,255))
        gold_info = myfont.render('Złoto:' + str(round(self.gold)), 1, (255,255,255))
        potions_info = myfont.render('Elikiry:' + str(round(self.potions)), 1, (255,255,255))
        key_info = myfont.render('Klucze:' + str(round(self.keys)), 1, (255,255,255))
        strenght_info = myfont.render('Siła:' + str(round(self.strenght)), 1, (255,255,255))
        surface.blit(ramka_statystyki, [10+self.movement_x,10+self.movement_y])
        surface.blit(hp_info, [18+self.movement_x,15+self.movement_y])
        surface.blit(strenght_info, [18+self.movement_x,45+self.movement_y])
        surface.blit(gold_info, [18+self.movement_x,75+self.movement_y])
        surface.blit(potions_info, [18+self.movement_x,105+self.movement_y])
        surface.blit(key_info, [18+self.movement_x,135+self.movement_y])
                     

        # sprawdzenie kolizji z przedmiotami
        colliding_items = pygame.sprite.spritecollide(self, self.level.set_of_items, False)
        for item in colliding_items:
            if item.name == 'key':
                keys = pygame.mixer.Sound("sounds/keys.wav")
                pygame.mixer.Sound.play(keys)
                self.keys = self.keys + 1
                item.kill()
        
    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.stance = 0
                self.turn_right()
                self.orientation = 'right'   
            if event.key == pygame.K_a:
                self.stance = 0
                self.turn_left()
                self.orientation = 'left'
            if event.key == pygame.K_w:
                self.stance = 0
                self.turn_up()
                self.orientation = 'up'
            if event.key == pygame.K_s:
                self.stance = 0
                self.turn_down()
                self.orientation = 'down'
            if event.key == pygame.K_SPACE :
                self.stance = 0
                attack = pygame.mixer.Sound("sounds/attack.wav")
                pygame.mixer.Sound.play(attack)
                if(self.orientation == 'right'):
                    self.image = fight_R1
                    self.fight(fight_right)
                if(self.orientation == 'left'):
                    self.image = fight_L1
                    self.fight(fight_left)
                if(self.orientation == 'up'):
                    self.image = fight_up1
                    self.fight(fight_up)
                if(self.orientation == 'down'):
                    self.image = fight_down1
                    self.fight(fight_down)
            if event.key == pygame.K_p:
                if(self.lifes!=self.max_lifes):
                    self.use_potion()
            if event.key == pygame.K_e:
                self.zakupy_buy()
                self.zakupy_sila()
                self.zakupy_max_hp()
                self.zakupy_regen()
     

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.stop()
                self.image = stand_R
            if event.key == pygame.K_a:
                self.stop()
                self.image = stand_L
            if event.key == pygame.K_w:
                self.stop_y()
                self.image = stand_up
            if event.key == pygame.K_s:
                self.stop_y()
                self.image = stand_down
            if event.key == pygame.K_SPACE:
                self.stop()
                self.stance = 0
                if(self.orientation == 'left'):
                    self.image = stand_L
                if(self.orientation == 'right'):    
                    self.image = stand_R
                if(self.orientation == 'up'):    
                    self.image = stand_up
                if(self.orientation == 'down'):    
                    self.image = stand_down  
            if event.key == pygame.K_e:
                self.stop()
                
class Level:
    def __init__(self):
        self.set_of_platforms = set()
        self.set_of_platformas = set()
        self.set_of_brama = set()
        self.set_of_brama_boss = set()
        self.set_of_shops = set()
        self.set_of_shops_sila = set()
        self.set_of_shops_potions = set()
        self.set_of_shops_max_hp = set()
        self.set_of_shops_regen = set()
        self.player = None
        self.world_shift = 0
        self.world_shift_y = 0
        self.set_of_npc = pygame.sprite.Group()
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_boss = pygame.sprite.Group()
        self.set_of_items = pygame.sprite.Group()
        self.set_of_shops = pygame.sprite.Group()
        self.set_of_shops_potions = pygame.sprite.Group()
        self.set_of_shops_sila = pygame.sprite.Group()
        self.set_of_shops_max_hp = pygame.sprite.Group()
        self.set_of_shops_regen = pygame.sprite.Group()
        self.set_of_enemy_follow = pygame.sprite.Group()
    

    def update(self):
        for platform in self.set_of_platforms:
            platform.update()
        for platform in self.set_of_platformas:
            platform.update()
        for platform in self.set_of_brama:
            platform.update()
        for platform in self.set_of_brama_boss:    
            platform.update() 
        self.set_of_enemies.update()
        self.set_of_enemy_follow.update()
        self.set_of_npc.update()
        self.set_of_boss.update()
##        self.set_of_items.update()
        
        # przesunięcie ekranu gdy gracz jest blisko prawej krawędzi        
        if self.player.rect.right >= 920:
            diff = self.player.rect.right - 920
            self.player.rect.right = 920
            self._shift_world(-diff)

        # przesunięcie ekranu gdy gracz jest blisko lewej krawędzi
        if self.player.rect.left <= 920:
            diff = 920 - self.player.rect.left
            self.player.rect.left = 920
            self._shift_world(diff)  


        # przesunięcie ekranu gdy gracz jest blisko gornej krawędzi
        if self.player.rect.bottom <= 600:
            diff = 600 - self.player.rect.bottom
            self.player.rect.bottom = 600
            self._shift_world_y(diff)

        
        # przesunięcie ekranu gdy gracz jest blisko dolnej krawędzi        
        if self.player.rect.top >= 500:
            diff = self.player.rect.top - 500
            self.player.rect.top = 500
            self._shift_world_y(-diff)
            
        
    def _shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.set_of_platforms:
            platform.rect.x += shift_x
            
        for platform in self.set_of_platformas:
            platform.rect.x += shift_x

        for platform in self.set_of_brama:
            platform.rect.x += shift_x

        for platform in self.set_of_brama_boss:
            platform.rect.x += shift_x    
            
        for enemy in self.set_of_enemies:
            enemy.rect.x += shift_x
            
        for enemy in self.set_of_boss:
            enemy.rect.x += shift_x
          
        for enemy in self.set_of_enemy_follow:
            enemy.rect.x += shift_x
            
        for item in self.set_of_items:
            item.rect.x += shift_x

        for item in self.set_of_shops_potions:
            item.rect.x += shift_x
            
        for item in self.set_of_shops_sila:
            item.rect.x += shift_x
            
        for item in self.set_of_shops_max_hp:
            item.rect.x += shift_x

        for item in self.set_of_shops_regen:
            item.rect.x += shift_x
            
        for item in self.set_of_npc:
            item.rect.x += shift_x    
            
    def _shift_world_y(self, shift_y):
        self.world_shift_y += shift_y
        for platform in self.set_of_platforms:
            platform.rect.y += shift_y
            
        for platform in self.set_of_platformas:
            platform.rect.y += shift_y

        for platform in self.set_of_brama:
            platform.rect.y += shift_y

        for platform in self.set_of_brama_boss:
            platform.rect.y += shift_y   
            
        for enemy in self.set_of_enemies:
            enemy.rect.y += shift_y

        for enemy in self.set_of_boss:
            enemy.rect.y += shift_y   

        for enemy in self.set_of_enemy_follow:
            enemy.rect.y += shift_y
            
        for item in self.set_of_items:
            item.rect.y += shift_y
            
        for item in self.set_of_shops_potions:
            item.rect.y += shift_y
            
        for item in self.set_of_shops_sila:
            item.rect.y += shift_y
            
        for item in self.set_of_shops_max_hp:
            item.rect.y += shift_y
            
        for item in self.set_of_shops_regen:
            item.rect.y += shift_y
            
        for item in self.set_of_npc:
            item.rect.y += shift_y     
         
    
    def draw(self, surface):
        surface.fill((0, 0, 0))
        map_x =+ self.world_shift
        map_y =+ self.world_shift_y
        surface.blit(mapa_main_s,(map_x-1360, map_y-1150))
        for platform in self.set_of_platforms:
            platform.draw(surface)
        for platform in self.set_of_platformas:
            platform.draw(surface)
        for platform in self.set_of_brama:
            platform.draw(surface)
        for platform in self.set_of_brama_boss:
            platform.draw(surface)       
        self.set_of_enemies.draw(surface)
        self.set_of_boss.draw(surface)
        self.set_of_enemy_follow.draw(surface)
        self.set_of_items.draw(surface)
        self.set_of_shops_potions.draw(surface)
        self.set_of_shops_sila.draw(surface)
        self.set_of_shops_max_hp.draw(surface)
        self.set_of_shops_regen.draw(surface)
        self.set_of_npc.draw(surface)
        

        

class Level_1(Level):
    def __init__(self):
        super().__init__()
        ws_platform_static = [[1900,100,0,-270],[50,1650,-35,-170],[50,88,1880,-170],[50,1408,1880,67],[555,97,1050,-57],[300,50,510, 30], [140,250,670,-180], [300,50, 5, 30],[135,250, 5, -180],[650,50, 120, -170],
                              [380,40, 220, -120] ,[920,260,-35,200],[920,260,1018,200],[850,200,-35,400],[850,200,1090,400],[250,150,1630,600], [50,165,1630,750],[90,165,1800,750],
                              [473,143,92,733],[307,103,92,1066],[223,183,1340,733],[227,143,1587,1023],[265,343,632,733], [265,343,1009,733], [140,263,632,903], [140,263,1134,903],
                              [45,50,930,1195],[45,50,930,1195], [770,260,0,1316], [770,260,1135,1316],[200,550,695,1360],[200,550,1010,1360],[850,70,0,1840],[850,70,1030,1840],[235,60,0,1940],[70,340,-85,1940],
                              [463,130,-100,2282],[20,540,-115,2282],[720,130,-105,2822],[10,640,-63,2822],[43,10,-55,3446],[10,50,-22,3455],[43,10,-13,3486],[10,50,20,3486],[145,10,10,3528],[10,180,150,3528],
                              [130,10,150,3695],[10,180,270,3695], [130,10,250,3737], [100,500,360,3277] ,[1500,10,360,3775],[250,50,1026,3735],[124,50,1112,3695], [250,50,1777,3735],[123,50,1818,3695],
                              [10,450,1942,3295],[1050,130,900,3279],[60,930,1942,2530],[5,930,1984,1830], [200,70,1860,1930], [123,35,1362,1920], [130,35,1562,1920], [250,220,695,2405],
                              [85,165,278,2405],[800,145,1235,2305],[85,475,1235,2305], [85,375,1235,2945], [87,175,528,2945], [250,130,460,3277], [125,50,530,3735],[165,50,1445,3735],
                              [50,140,-20,1905],[50,100,-100,2525],[50,100,-55,3150], [170,50,360,1905], [50,135,1940,2075], [210,140,1525,2730], [50,100,1901,2570], [50,120,1901,2860],
                              [50,50,1901,3235], [850,10,1900,-92],[850,10,1900,67],[70,900,2693,-982],[70,900,2693,67],[70,1300,3638,-482],[1200,90,2693,-470],[400,1000,2746,405],[600,1000,3256,405],
                              [250,90,3075, -50],[40,45,3015, -175],[40,45,3345, -175],[40,45,3015, 115],[40,45,3345, 115], [50,800,2830,1305], [50,800,3520,1305],[800,50,2830,1980],
                              [120,95,3142,1645], [60,95,2872,1645], [60,95,3470,1645],[210,85,3095,1940]]

        # tworzymy platformy
        for el in ws_platform_static:
            object_P = Platform(*el)
            self.set_of_platforms.add(object_P)

        #tworzymy brame
        ws_brama = [[20,130,1900,-55]]
        for el in ws_brama:
            object_P = Brama(*el)
            self.set_of_brama.add(object_P)
            
        #tworzymy brame do bossa
        ws_brama = [[130,20,3135,475]]
        for el in ws_brama:
            object_P = BramaBoss(*el)
            self.set_of_brama_boss.add(object_P)
            
    
        # tworzymy wrógów z platformami (snake)
        ws_enemy_platform = [[280,0,-55,2590],[280,0,-25,3300],[280,0,1505,3090], [280,0,1605,2630], [280,0,1205,3630]]
        for el in ws_enemy_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_enemy = PlatformEnemy(ZOMBIE_STAND_R, ZOMBIE_WALK_R,
                                           ZOMBIE_WALK_L,
                                           ZOMBIE_DEAD_R, ZOMBIE_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_enemies.add(platform_enemy)

        # tworzymy wrógów z platformami (obroncy)
        ws_enemy_platform = [[400,0,3050,-250],[400,0,3050,350],[180,0,2800,100],[180,0,3400,110]]
        for el in ws_enemy_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_enemy = betterPlatformEnemy(GUARDIAN_STAND_R, GUARDIAN_WALK_R,
                                           GUARDIAN_WALK_L,
                                           GUARDIAN_DEAD_R, GUARDIAN_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_enemy_follow.add(platform_enemy)

            
        # tworzymy BOSSA z platformami 
        ws_enemy_platform = [[700,0,2900, 1900]]
        for el in ws_enemy_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_enemy = PlatformBoss(BOSS_STAND_R, BOSS_WALK_R,
                                           BOSS_WALK_L,
                                           BOSS_DEAD_R, BOSS_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_boss.add(platform_enemy)


        # tworzymy npc z platformami (first)
        ws_npc_platform = [[300,0,250,0]]
        for el in ws_npc_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_npc_first = npc_first(NPC_FIRST_STAND_R, NPC_FIRST_WALK_R,
                                           NPC_FIRST_WALK_L,
                                           NPC_FIRST_DEAD_R, NPC_FIRST_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_npc.add(platform_npc_first)
            
            
        # tworzymy npc z platformami (second)
        ws_npc_platform = [[280,0,1320,1300]]
        for el in ws_npc_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_npc_second = npc_second(NPC_SECOND_STAND_R, NPC_SECOND_WALK_R,
                                           NPC_SECOND_WALK_L,
                                           NPC_SECOND_DEAD_R, NPC_SECOND_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_npc.add(platform_npc_second)

            
        # tworzymy npc z platformami (third)
        ws_npc_platform = [[420,0,120,1060]]
        for el in ws_npc_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_npc_third = npc_third(NPC_THIRD_STAND_R, NPC_THIRD_WALK_R,
                                           NPC_THIRD_WALK_L,
                                           NPC_THIRD_DEAD_R, NPC_THIRD_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_npc.add(platform_npc_third)
            
        # tworzymy npc z platformami (fourth)
        ws_npc_platform = [[180,0,1520,-80]]
        for el in ws_npc_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_npc_fourth  = npc_fourth (NPC_FOURTH_STAND_R, NPC_FOURTH_WALK_R,
                                           NPC_FOURTH_WALK_L,
                                           NPC_FOURTH_DEAD_R, NPC_FOURTH_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_npc.add(platform_npc_fourth)

        # tworzymy npc z platformami (fifth)
        ws_npc_platform = [[120,0,3155,70]]
        for el in ws_npc_platform:
            object_P = FakePlatform(*el)
            self.set_of_platformas.add(object_P)
            platform_npc_fifth  = npc_fifth (NPC_FIFTH_STAND_R, NPC_FIFTH_WALK_R,
                                           NPC_FIFTH_WALK_L,
                                           NPC_FIFTH_DEAD_R, NPC_FIFTH_DEAD_L,
                                           object_P,
                                           random.choice([-3,-2,-1,1,2,3]))
            self.set_of_npc.add(platform_npc_fifth)    
     

        
        # tworzymy przedmiot (klucz)
        key = Item(KEY, 'key')
        key.rect.x = 170
        key.rect.y = -85
        self.set_of_items.add(key)

        key = Item(KEY, 'key')
        key.rect.x = -85
        key.rect.y = 2490
        self.set_of_items.add(key)

        key = Item(KEY, 'key')
        key.rect.x = -55
        key.rect.y = 3300
        self.set_of_items.add(key)

        key = Item(KEY, 'key')
        key.rect.x = 1905
        key.rect.y = 2990
        self.set_of_items.add(key)

        key = Item(KEY, 'key')
        key.rect.x = 1905
        key.rect.y = 3530
        self.set_of_items.add(key)
        
     


        # tworzymy sklep (potiony)
        shop = Shop(sklep_poty, 'shop')
        shop.rect.x = 92
        shop.rect.y = 733
        self.set_of_shops_potions.add(shop)

        # tworzymy sklep (max_hp)
        shop = Shop(sklep_max_hp, 'shop')
        shop.rect.x = 1587
        shop.rect.y = 1023
        self.set_of_shops_max_hp.add(shop)

        # tworzymy sklep (sila)
        shop = Shop(sklep_sila, 'shop')
        shop.rect.x = 1340
        shop.rect.y = 733
        self.set_of_shops_sila.add(shop)

        # tworzymy sklep (regen)
        shop = Shop(sklep_regen, 'shop')
        shop.rect.x = 1631
        shop.rect.y = 600
        self.set_of_shops_regen.add(shop)
    
        

# klasa platformy
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        #surface.fill(LIGHTBLUE, self.rect)
        surface.blit(platform_background, self.rect)

class FakePlatform(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.fill(LIGHTBLUE, self.rect)
        #surface.blit(platform_background, self.rect)        
        
class Brama(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        #surface.fill(LIGHTBLUE, self.rect)
        surface.blit(gate, self.rect)

class BramaBoss(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        #surface.fill(LIGHTBLUE, self.rect)
        surface.blit(boss_gate, self.rect)

        

class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform = None, movement_x = 0, movement_y = 0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'right'
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_dead_right = image_dead_right
        self.image_dead_left = image_dead_left
        self.lifes = 150
        self.max_lifes = 150
        self.count = 0
    
            
        if self.platform:
            self.rect.bottom = self.platform.rect.top
            self.rect.centerx = random.randint(
                self.platform.rect.left + self.rect.width,
                self.platform.rect.right - self.rect.width)


    def update(self):
        if self.lifes <= 0 and self.count > 7:
            self.kill()
            
        # animacje
        if self.lifes:
            if self.movement_x > 0:
                self._move(self.image_right)
            if self.movement_x < 0:
                self._move(self.image_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_dead_right)
            else:
                self._move(self.image_dead_left)
            

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count  = 0
        else:
            self.count += 1


class PlatformEnemy(Enemy):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        label = myfont.render(str(round(self.lifes))+'/'+str(self.max_lifes), 1, (255,0,0))
        surface.blit(label, [self.rect.x-10,self.rect.y-20])
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'



            
class betterEnemy(pygame.sprite.Sprite):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform = None, movement_x = 0, movement_y = 0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'right'
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_dead_right = image_dead_right
        self.image_dead_left = image_dead_left
        self.lifes = 300
        self.max_lifes = 300
        self.count = 0
    
            
        if self.platform:
            self.rect.bottom = self.platform.rect.top
            self.rect.centerx = random.randint(
                self.platform.rect.left + self.rect.width,
                self.platform.rect.right - self.rect.width)


    def update(self):
        if self.lifes <= 0 and self.count > 7:
            self.kill()
        
        # animacje
        if self.lifes:
            if self.movement_x > 0:
                self._move(self.image_right)
            if self.movement_x < 0:
                self._move(self.image_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_dead_right)
            else:
                self._move(self.image_dead_left)
            

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count  = 0
        else:
            self.count += 1


class betterPlatformEnemy(betterEnemy):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        label = myfont.render(str(round(self.lifes))+'/'+str(self.max_lifes), 1, (255,0,0))
        surface.blit(label, [self.rect.x-10,self.rect.y-20])
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'

class Boss(pygame.sprite.Sprite):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform = None, movement_x = 0, movement_y = 0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'right'
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_dead_right = image_dead_right
        self.image_dead_left = image_dead_left
        self.lifes = 999
        self.max_lifes = 999
        self.count = 0
    
            
        if self.platform:
            self.rect.bottom = self.platform.rect.top
            self.rect.centerx = random.randint(
                self.platform.rect.left + self.rect.width,
                self.platform.rect.right - self.rect.width)


    def update(self):
        if self.lifes <= 0 and self.count > 7:
            self.kill()

        # animacje
        if self.lifes:
            if self.movement_x > 0:
                self._move(self.image_right)
            if self.movement_x < 0:
                self._move(self.image_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_dead_right)
            else:
                self._move(self.image_dead_left)
            

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count  = 0
        else:
            self.count += 1


class PlatformBoss(Boss):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        label = myfont.render(str(round(self.lifes))+'/'+str(self.max_lifes), 1, (255,0,0))
        surface.blit(label, [self.rect.x+50,self.rect.y-20])
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'
            
           
            
class Npc(pygame.sprite.Sprite):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform = None, movement_x = 0, movement_y = 0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'right'
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_dead_right = image_dead_right
        self.image_dead_left = image_dead_left
        self.lifes = 100
        self.max_lifes = 100
        self.count = 0
    
            
        if self.platform:
            self.rect.bottom = self.platform.rect.top
            self.rect.centerx = random.randint(
                self.platform.rect.left + self.rect.width,
                self.platform.rect.right - self.rect.width)


    def update(self):
        if not self.lifes and self.count > 7:
            self.kill()
        
        # animacje
        if self.lifes:
            if self.movement_x > 0:
                self._move(self.image_right)
            if self.movement_x < 0:
                self._move(self.image_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_dead_right)
            else:
                self._move(self.image_dead_left)
            

    def _move(self, image_list):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count  = 0
        else:
            self.count += 1


class npc_first(Npc):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'
            
class npc_second(Npc):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'
            
class npc_third(Npc):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        label = myfont.render('Proszę, pomóż nam pokonać potwora', 1, (0,255,0))
        label_second = myfont.render('znajdującego się na wschodzie! ', 1, (0,255,0))
        surface.blit(label, [self.rect.x-170,self.rect.y-40])
        surface.blit(label_second, [self.rect.x-150,self.rect.y-20])
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'
            
class npc_fourth(Npc):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        label = myfont.render('Aby otworzyć bramę musisz posiadać', 1, (0,255,0))
        label_second = myfont.render('pięć zaginionych kluczy! ', 1, (0,255,0))
        surface.blit(label, [self.rect.x-170,self.rect.y-40])
        surface.blit(label_second, [self.rect.x-110,self.rect.y-20])
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'

class npc_fifth(Npc):
    def update(self):
        super().update()
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        label = myfont.render('Aby dostac się do ', 1, (103,168,177))
        label_second = myfont.render('bestii musisz pokonać', 1, (103,168,177))
        label_third = myfont.render('czterech strażników! ', 1, (103,168,177))
        
        surface.blit(label, [self.rect.x-90,self.rect.y-60])
        surface.blit(label_second, [self.rect.x-100,self.rect.y-40])
        surface.blit(label_third, [self.rect.x-90,self.rect.y-20])
        if self.rect.left < self.platform.rect.left or\
           self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0:
            self.direction_of_movement = 'right'
    
        if self.movement_x < 0:
            self.direction_of_movement = 'left'            
            
class Item(pygame.sprite.Sprite):
    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name

class Shop(pygame.sprite.Sprite):
    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name          

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()
    
def load_image(name):
    image = pygame.image.load(name)
    return image

class Menu:
    lista = []
    pola = []
    rozmiar_fontu = 48
    font_path = 'data/coders_crux/coders_crux.ttf'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    ilosc_pol = 0
    kolor_tla = (20,18,24)
    kolor_tekstu =  (255,236,159)
    kolor_zaznaczenia = (30,20,52)
    pozycja_zaznaczenia = 0
    pozycja_wklejenia = (0,0)
    menu_width = 150
    menu_height = 550

    class Pole:
        tekst = ''
        pole = pygame.Surface
        pole_rect = pygame.Rect
        zaznaczenie_rect = pygame.Rect

    def move_menu(self, top, left):
        self.pozycja_wklejenia = (top,left) 

    def set_colors(self, text, selection, background):
        self.kolor_tla = background
        self.kolor_tekstu =  text
        self.kolor_zaznaczenia = selection
        
    def set_fontsize(self,font_size):
        self.rozmiar_fontu = font_size
        
    def set_font(self, path):
        self.font_path = path
        
    def get_position(self):
        return self.pozycja_zaznaczenia
    
    def init(self, lista, dest_surface):
        self.lista = lista
        self.dest_surface = dest_surface
        self.ilosc_pol = len(self.lista)
        self.stworz_strukture()        
        
    def draw(self,przesun=0):
        if przesun:
            self.pozycja_zaznaczenia += przesun 
            if self.pozycja_zaznaczenia == -1:
                self.pozycja_zaznaczenia = self.ilosc_pol - 1
            self.pozycja_zaznaczenia %= self.ilosc_pol
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.kolor_tla)
        zaznaczenie_rect = self.pola[self.pozycja_zaznaczenia].zaznaczenie_rect
        pygame.draw.rect(menu,self.kolor_zaznaczenia,zaznaczenie_rect)

        for i in range(self.ilosc_pol):
            menu.blit(self.pola[i].pole,self.pola[i].pole_rect)
        self.dest_surface.blit(menu,self.pozycja_wklejenia)
        return self.pozycja_zaznaczenia

    def stworz_strukture(self):
        przesuniecie = 0
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.rozmiar_fontu)
        for i in range(self.ilosc_pol):
            self.pola.append(self.Pole())
            self.pola[i].tekst = self.lista[i]
            self.pola[i].pole = self.font.render(self.pola[i].tekst, 1, self.kolor_tekstu)

            self.pola[i].pole_rect = self.pola[i].pole.get_rect()
            przesuniecie = int(self.rozmiar_fontu * 0.2)

            height = self.pola[i].pole_rect.height
            self.pola[i].pole_rect.left = przesuniecie
            self.pola[i].pole_rect.top = przesuniecie+(przesuniecie*2+height)*i

            width = self.pola[i].pole_rect.width+przesuniecie*2
            height = self.pola[i].pole_rect.height+przesuniecie*2            
            left = self.pola[i].pole_rect.left-przesuniecie
            top = self.pola[i].pole_rect.top-przesuniecie

            self.pola[i].zaznaczenie_rect = (left,top ,width*2, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.pozycja_wklejenia
        self.pozycja_wklejenia = (x+mx, y+my)
    
class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('png/menu/frame_00_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_01_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_02_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_03_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_04_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_05_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_06_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_07_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_08_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_09_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_10_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_11_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_12_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_13_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_14_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_15_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_16_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_17_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_18_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_19_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_20_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_21_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_22_delay-0.1s.gif'))
        self.images.append(load_image('png/menu/frame_23_delay-0.1s.gif'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 1920, 1080)
    
    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        t_end = time.time() + 0.096
        while time.time() < t_end:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        
if __name__ == "__main__":
    active_game = False

    if(active_game == False):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load("sounds/menu_soundtrack.mp3")
        theme = pygame.mixer.music.play(-1,0.0)
    
    surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)


    current_level = Level_1()
    player = Player(stand_R, current_level)
    boss = PlatformBoss(BOSS_STAND_R, BOSS_WALK_R,
                                           BOSS_WALK_L,
                                           BOSS_DEAD_R, BOSS_DEAD_L
                                           )
    current_level.player = player
    player.rect.center = surface.get_rect().center


    
    
    menu = Menu()#necessary
    menu.move_menu(800,400)#optional
    menu.init(['Start','Options','Quit'], surface)#necessary
    pygame.key.set_repeat(199,69)#(delay,interval)
    pygame.display.update()

    #ukrycie i blokada kursora
    pygame.mouse.set_visible(0)
    pygame.event.set_grab(1)
    mapa_main_s=mapa_main.convert()
    myfont = pygame.font.SysFont("monospace", 20)
    
    while 1:
        if(active_game == False):
            surface.blit(title_image,(50,30))
            menu.draw()
            my_group.update()
            my_group.draw(surface)
            surface.blit(title_image,(50,30))
            menu.draw()
            pygame.display.update()
            surface.blit(title_image,(50,30))
            menu.draw()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        menu.draw(-1) #here is the Menu class function
                    if event.key == K_DOWN:
                        menu.draw(1) #here is the Menu class function
                    if event.key == K_RETURN:
                        if menu.get_position() == 0:
                            active_game = True
                        if menu.get_position() == 1: #opcje rob cos jesli 1
                            surface.blit((options_text),(0,0))
                            pygame.display.update()
                            pause = True
                            while pause == True:
                                for event in pygame.event.get():
                                    if event.type==KEYDOWN:
                                        if event.key==K_RETURN:
                                            pause = False
                        if menu.get_position() == 2:#here is the Menu class function
                            pygame.display.quit()
                            pygame.mixer.music.stop()
                            sys.exit()
                    if event.key == K_ESCAPE:
                        pygame.display.quit()
                        sys.exit()

    
                        
            if active_game == True:

                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.load("sounds/game_soundtrack.mp3")
                theme = pygame.mixer.music.play(-1,1.2)
                
                while active_game == True:
        
                    for event in pygame.event.get():
                        player.get_event(event)
                        if event.type==KEYUP:
                            if event.key==K_ESCAPE:
                                surface.blit(pause_img,(0,0))
                                pygame.display.update()
                                pause = True
                                
                    while pause == True:
                        for event in pygame.event.get():
                            if event.type==KEYUP:
                                if event.key==K_ESCAPE: 
                                    pause = False
                                if event.key==K_q:
                                    pygame.mixer.music.stop()
                                    pygame.display.quit()
                                    sys.exit()
                                    
                    #if(player.lifes <= 0):
                    #    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
                    #    pygame.mixer.music.set_volume(0.3)
                    #    pygame.mixer.music.load("sounds/menu_soundtrack.mp3")
                    #    theme = pygame.mixer.music.play(-1,0.0)
                    #    active_game = False

                    if(player.lifes <= 0):
                        current_level.draw(surface)
                        current_level.update()
                        player.update()
                        player.draw(surface)
                        surface.blit(ded_text,(0,0))
                        pygame.display.flip()
                        clock.tick(140)
                        pause = True
                         
                    while pause == True:
                        for event in pygame.event.get():
                            if event.type==KEYUP:
                                if event.key==K_q: 
                                    pygame.mixer.music.stop()
                                    pygame.display.quit()
                                    sys.exit()
                                    
                    
                    if(player.boss >= 1):
                        current_level.draw(surface)
                        current_level.update()
                        player.update()
                        player.draw(surface)
                        surface.blit(end_text,(0,0))
                        pygame.display.flip()
                        clock.tick(140)
                        pause = True
                         
                    while pause == True:
                        for event in pygame.event.get():
                            if event.type==KEYUP:
                                if event.key==K_q: 
                                    pygame.mixer.music.stop()
                                    pygame.display.quit()
                                    sys.exit()
                            
                    
                    #rysowanie i aktualizacja obiektów
                    current_level.draw(surface)
                    player.update()
                    player.draw(surface)
                    current_level.update()
                    
                    #aktualizacja okna pygame
                    pygame.display.flip()
                    clock.tick(50)
                            
    
        
