from random import randint

def attack(ac, modifier, damage):
    roll = randint(1,20)
    if roll == 1 or roll + modifier < ac:
        return 0
    elif roll == 20 or roll + modifier >= ac + 10:
        return damage() + damage()
    else:
        return damage()

def flail(ac):
    return attack(ac, 14, lambda: randint(1,6) + randint(1,6) + 5)

def fist(ac):
    return attack(ac, 10, lambda: randint(1,4) + randint(1,4) + 5)


if __name__ == '__main__':
    ac = 19
    init_hp = 34
    
    onehit = 0
    twohit = 0
    threehit = 0
    alive = 0
    for x in range(300000):
        hp = init_hp
        hp -= flail(ac)
        if hp < 0:
            onehit += 1
            continue
        hp -= flail(ac)
        if hp < 0:
            twohit += 1
            continue
        hp -= fist(ac)
        if hp < 0:
            threehit += 1
        else:
            alive +=1
    print(onehit, twohit, threehit, alive)
