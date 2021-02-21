import random, math

BOARD_SIZE = 5

# 2点間の距離を返す関数
def calc_distance(pos1, pos2):
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]
    return math.sqrt(diff_x**2 + diff_y**2)

def generate_position(size):
    x = random.randrange(0, size)
    y = random.randrange(0, size)
    return (x, y)

def move_position(direction, pos):
    current_x, current_y = pos # 現在位置を代入

    if direction == "n":
        current_y -= 1
    elif direction == "s":
        current_y += 1
    elif direction == "w":
        direction -= 1
    elif direction == "e":
        direction += 1
    return (current_x, current_y)

def suika_wari():
    suika_pos = generate_position(BOARD_SIZE)
    player_pos = generate_position(BOARD_SIZE)

    # x軸、y軸どちらか一方でも一致していなければ処理を繰り返す
    while (suika_pos != player_pos):
        distance = calc_distance(suika_pos, player_pos)
        print("スイカへの距離", distance)

        c = input("news")
        player_pos = move_position(c, player_pos)

    print("スイカを割りました")

suika_wari()