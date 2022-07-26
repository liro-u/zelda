import pygame
from enum import Enum

# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
  'player':-26,
  'objects':-40,
  'grass':-10,
  'invisible':0,
}

class Action(Enum):
  # ui
  TOGGLE_UI = [pygame.K_m,pygame.K_ESCAPE]
  UI_RIGHT = [pygame.K_RIGHT,pygame.K_d]
  UI_LEFT = [pygame.K_LEFT,pygame.K_q]
  UI_SELECT = [pygame.K_SPACE]

  # movement
  MOVE_DOWN = [pygame.K_DOWN,pygame.K_s]
  MOVE_UP = [pygame.K_UP,pygame.K_z]
  MOVE_LEFT = [pygame.K_LEFT,pygame.K_q]
  MOVE_RIGHT = [pygame.K_RIGHT,pygame.K_d]

  # attack
  ATTACK = [pygame.K_SPACE]
  SWITCH_WEAPON = [pygame.K_a]

  # magic
  MAGIC = [pygame.K_LCTRL]
  SWITCH_MAGIC = [pygame.K_e]

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons
weapon_data = {
  'sword': {'cooldown':100,'damage':15,'graphic':'graphics/weapons/sword/full.png'},
  'lance': {'cooldown':400,'damage':30,'graphic':'graphics/weapons/lance/full.png'},
  'axe': {'cooldown':300,'damage':20,'graphic':'graphics/weapons/axe/full.png'},
  'rapier': {'cooldown':50,'damage':8,'graphic':'graphics/weapons/rapier/full.png'},
  'sai': {'cooldown':80,'damage':10,'graphic':'graphics/weapons/sai/full.png'},
}

# magic
magic_data = {
  'flame': {'cooldown':200,'strength':5,'cost':20,'graphic':'graphics/particles/flame/fire.png','sound':'audio/Fire.wav'},
  'heal': {'cooldown':300,'strength':20,'cost':10,'graphic':'graphics/particles/heal/heal.png','sound':'audio/heal.wav'},
}

# enemy
monster_data = {
  'squid': {'health':100,'exp':100,'damage':20,'attack_cooldown':600,'attack_type':'slash','attack_sound':'audio/attack/slash.wav','speed':3,'resistance':3,'attack_radius':80,'notice_radius':360},
  'raccoon': {'health':300,'exp':250,'damage':40,'attack_cooldown':1000,'attack_type':'claw','attack_sound':'audio/attack/claw.wav','speed':2,'resistance':3,'attack_radius':120,'notice_radius':400},
  'spirit': {'health':100,'exp':110,'damage':8,'attack_cooldown':400,'attack_type':'thunder','attack_sound':'audio/attack/fireball.wav','speed':4,'resistance':3,'attack_radius':60,'notice_radius':350},
  'bamboo': {'health':70,'exp':120,'damage':6,'attack_cooldown':600,'attack_type':'leaf_attack','attack_sound':'audio/attack/slash.wav','speed':3,'resistance':3,'attack_radius':50,'notice_radius':300},
}