from bot_interface import *
import math

class Boy(BotBase):
    init_boost = False

    def process(self, gamestate):
        if not self.init_boost:
            self.init_boost = not self.init_boost
            return Action(20, 0.95, 1, 1)

        t = gamestate.tick
        if t % 100 < 50:
            return Action(-2, 1.1, 1, 1)
        else:
            return Action(-2, -1, -1.1, 1)
    

GameState(Boy()).connect()