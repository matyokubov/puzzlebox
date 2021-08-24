import random
import json
num_list = json.load(open("config/game.json"))["nums-xy"]
rand_list = []

for xy in range(len(num_list)):
    rand_xy = random.choice(num_list)
    rand_list.append(rand_xy)
    num_list.pop(num_list.index(rand_xy))