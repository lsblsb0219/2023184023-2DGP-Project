world = [[] for _ in range(4)]


def add_object(o, depth = 0):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def clear():
    for layer in world:
        layer.clear()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot delete non existing object')

def collide(a, b):
     left_a, bottom_a, right_a, top_a = a.get_bb()
     left_b, bottom_b, right_b, top_b = b.get_bb()

     if left_a > right_b: return False
     if right_a < left_b: return False
     if top_a < bottom_b: return False
     if bottom_a > top_b: return False

     return True