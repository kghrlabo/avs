# -*- coding: utf-8 -*-

"""Player"""

import os

player_option = os.getenv('PLAYER', 'default').lower()

if player_option.find('single') >= 0:
    from single_gstreamer_player import Player
else:
    from gstreamer_player import Player


__all__ = ['Player']



