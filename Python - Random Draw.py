import time
import random 

teamKey = 0
playerKey = 0
playersNumber = 5

team = [i for i in range (1,playersNumber+1)]
player = [i for i in range (1,playersNumber+1)]

PLAYERS = {
    1 : 'AMR',
    2 : 'AHMED',
    3 : 'DEMBELI',
    4 : 'SEEDA',
    5 : 'OZMO'
}

TEAMS = {
    1 : 'Barca',
    2 : 'Real',
    3 : 'Milan',
    4 : 'City',
    5 : 'Paris'
}

print('------------------')
print('! Draw Result : !')

for i in range (playersNumber):

    teamKey = random.choice(team)
    team.remove(teamKey)
    
    playerKey = random.choice(player)
    player.remove(playerKey)
    
    PLAYERS [playerKey] += ' - ' + TEAMS [teamKey]
    print('[',i+1 ,'] ',PLAYERS[playerKey])
    time.sleep(0.5)
    
print('------------------')

