from game import constants
from game.action import Action
from game.point import Point
# from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        #self._audio = AudioService()
        
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if len(cast["players"]) != 0:
            player = cast["players"][0] # there's only one
        
            blocks = cast["blocks"]

            collision_count = 0
            # destroy = -1
            for count in range(len(blocks)):
                if self._physics_service.is_collision(player, blocks[count]):
                    # destroy = count
                    # collision_count += 1

                    # self._audio.play_sound(constants.SOUND_BOUNCE)

                    player_dx = player.get_velocity().get_x() * -1
                    player_dy = player.get_velocity().get_y() * -1
                    
                    point = Point(player_dx, player_dy)
                    player.set_velocity(point)

                    
                
            # if destroy >= 0:
            #     bricks.pop(destroy)
                
            # if self._physics_service.is_collision(player, blocks):
            #     ball_dx = ball.get_velocity().get_x()
            #     ball_dy = ball.get_velocity().get_y()
                    
            #     point = Point(ball_dx, ball_dy * -1)
            #     ball.set_velocity(point)
                
            #     # self._audio.play_sound(constants.SOUND_BOUNCE)
                
                
                    