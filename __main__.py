import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import raylibpy
import random
from game import constants, handle_collisions_action
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.move_actors_action import MoveActorsAction
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
#from game.audio_service import AudioService

from game.solid_blocks import SolidBlock

def main():
    cast = {}

    cast["solid_blocks"] = []
    solid_blocks = []
    for row in range(6):
        for column in range(8):
            solid_block = SolidBlock(row,column)
            solid_blocks.append(solid_block)
    cast["solid_blocks"] = solid_blocks
    
    cast["power_ups"] = []
    cast["blocks"] = []
    cast["players"] = []

    player1 = Actor()
    player1.set_width(20)
    player1.set_height(20)

    player_position = Point(20, 20)


    player1.set_position(player_position)

    cast["players"].append(player1)

    player2 = Actor()
    player2.set_width(20)
    player2.set_height(20)

    player_position = Point(810, 610)


    player2.set_position(player_position)

    cast["players"].append(player2)



    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    # audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [handle_collisions_action, move_actors_action]
    script["output"] = [draw_actors_action]
    
    output_service.open_window("Playing with Fire")
    #audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()

