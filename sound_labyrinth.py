"""TODO:

fix bug with multiple walls displaying (Sungyu) - DONE (?)
    maybe make a wall hide all the other walls when pinged

display controls information/ instructions (Kyle)

remove delay on sound pings (kyle) -- DONE(?)
    please do not use sleep()  -- only used if we want a delay to show the pings

Build speech synthesizer (kyle)

Clean up model.py code for pinging (kyle) - DONE

Build function for npc dialogue (Sungyu)
def speach("string")
    play voice synthesizer
    display text
    return none

Make NPC class (Tim) - DONE

Build introductory NPC of the grim reaper to introduce you to the world and your situation (Tim) - DONE

Build introductory level design for level(Tim)
"""

import model
import pygame
import os

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.mixer.init()
    m = model.Model()
    m.run_game()
