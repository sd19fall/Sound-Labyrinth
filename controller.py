import pygame

class Controller:
    """Handle user input and translate to a useable format.

    The class holds functions useful for retrieving user input and varables
    describing the state of monitored user inputs.

    Class variables:
    ping_keys - A dictionary of boolians monitoring the inputs used for pinging
        the user's environment. True means the user is supplying an input in the
        given direction.
    move_keys - A dictionary of boolians monitoring the inputs used for moving
        the user around their environment. True means the user is supplying an
        input in the given direction.
    move_keys - A dictionary of boolians monitoring the inputs used for
        accessing the user's inventory. True means the user is supplying an
        input for the given inventory slot.
    """

    def __init__():
        """Initalize the Controller class with default variable values"""

        #variables to store the states of the controll keys
        #values are true while the key is pressed and false when the key is not
        ping_keys = {'front':False,'back':False,'left':False,'right':False}
        move_keys = {'north':False,'south':False,'west':False,'east':False}
        inventory_keys = {'1':False,'2':False,'3':False,'4':False,'5':False}


    def read_input():
        """Read the inputs to the game

        The function will read inputs from the keyboard and will update the
        controller's variables of ping_keys, move_keys, and inventory_keys to
        reflect the current status of the monitored keys on the keyboard.

        Keyword arguments: None
        Return values: None
        """


        #get which keys are pressed
        pressed_keys = pygame.key.getpressed()

        #update the values of the ping controlling keys
        ping_keys['front'] = pressed_keys[pygame.K_UP]
        ping_keys['back'] = pressed_keys[pygame.K_DOWN]
        ping_keys['left'] = pressed_keys[pygame.K_LEFT]
        ping_keys['right'] = pressed_keys[pygame.K_RIGHT]

        #update the values of the movment controlling keys
        move_keys['north'] = pressed_keys[pygame.K_w]
        move_keys['south'] = pressed_keys[pygame.K_s]
        move_keys['west'] = pressed_keys[pygame.K_a]
        move_keys['east'] = pressed_keys[pygame.K_d]

        #update the values of the inventory slot controlling keys
        inventory_keys['1'] = pressed_keys[pygame.K_1]
        inventory_keys['2'] = pressed_keys[pygame.K_2]
        inventory_keys['3'] = pressed_keys[pygame.K_3]
        inventory_keys['4'] = pressed_keys[pygame.K_4]
        inventory_keys['5'] = pressed_keys[pygame.K_5]
