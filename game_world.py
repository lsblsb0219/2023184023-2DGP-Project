world = [[] for _ in range(4)]
collision_pairs = {}

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [ [], [] ] # 리스트 초기화
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol

def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            if o is not None:  # None 객체를 처리
                o.draw()

def remove_collision_object(o): # 충돌 객체 제거 함수
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

    pass

def clear():
    global collision_pairs
    for layer in world:
        layer.clear()
    collision_pairs.clear()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
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


def handle_collisions():
    global collision_pairs

    pairs_copy = collision_pairs.copy()

    # 게임월드에 등록된 충돌 정보를 바탕으로, 실제 충돌 검사를 수행.
    for group, pairs in pairs_copy.items():
        for a in pairs[0]: # A 리스트에서 하나 뽑고,
            for b in pairs[1]: # B 리스트에서 하나 뽑고,
                if not (hasattr(a, 'get_bb') and hasattr(b, 'get_bb')):  # get_bb 메서드 확인
                    continue
                if not a.get_bb() or not b.get_bb():  # get_bb 결과 확인
                    continue
                if collide(a, b):
                    print(f'{group} collide')
                    a.handle_collision(group, b) # 충돌한 상대가 누군지 알려줌 -> b와 충돌했어
                    b.handle_collision(group, a) # a와 충돌했어