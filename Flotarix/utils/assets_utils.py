import utils.path_utils
import arcade

def execute_sound(sound: str):
    sound_path = utils.path_utils.get_relative_path(f"assets/sounds/{sound}")
    sound_effect = arcade.load_sound(sound_path)
    arcade.play_sound(sound_effect)