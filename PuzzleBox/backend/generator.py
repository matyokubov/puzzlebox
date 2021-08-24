# O'yin uchun bosh algoritm
# a = x+y+z+n+k topish
import random
import json
def funk(max1, l):
    a1 = max1
    objs = []
    total_kg1 = 0
    for r in range(max1):
        if max1 < 0:
            continue
        else:
            r1 = random.randint(6, 10)
            objs.append(r1)
            max1-=r1
            total_kg1+=r1

    aa = a1-total_kg1
    ii = objs.index(max(objs))
    objs[ii]+=aa
    try:
        objs.pop(objs.index(0))
    except:
        pass
    if len(objs) != l:
        error()
    return objs

def get_area1_objs():
    global m1,l1,r1
    try:
        r1 = funk(m1, l1)
    except:
        get_area1_objs()

def get_area2_objs():
    global m2,l2,r2
    try:
        r2 = funk(m2, l2)
    except:
        get_area2_objs()

lvl_file = json.load(open("backend/level.json"))
r1 = []; m1 = lvl_file["m1"]; l1 = lvl_file["l1"]
r2 = []; m2 = lvl_file["m2"]; l2 = lvl_file["l2"]
get_area1_objs()
get_area2_objs()

mm1 = m1; mm2 = m2

if l1==2 and l2==3:
    r1.append(random.randint(2, 10))
    r1.append(random.randint(2, 10))
    r2.append(random.randint(2, 10))
    r2.append(random.randint(2, 10))
    r2.append(random.randint(2, 10))
elif l1==3 and l2==4:
    r1.append(random.randint(2, 10))
    r2.append(random.randint(2, 10))
    r2.append(random.randint(2, 10))
elif l1==5 and l2==4:
    r2.append(random.randint(2, 10))
