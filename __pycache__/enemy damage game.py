print("game for enemy damage")
import random
playerhp = 500
enemyattack1 = 100
enemyattcak2 = 200
while playerhp >100:
    damage = random .randrange(enemyattack1,enemyattcak2)
    playerhp = playerhp - damage
    if playerhp ==30:  
        print("enemy attack is", damage, playerhp, ":")
