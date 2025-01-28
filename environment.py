from pettingzoo.classic import connect_four_v3

def make_env(render='rgb_array'):
    env = connect_four_v3.env(render_mode=render)
    return env

