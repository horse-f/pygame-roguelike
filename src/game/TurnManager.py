
turnQueue = []
lastTurn = 0

def turn(cost, callback=None):
    global turnQueue
    turnQueue.append({
        'cost': cost,
        'callback': callback
    })

def update():
    global turnQueue
    global lastTurn
    if(len(turnQueue) > 0):
        turn = turnQueue.pop(0)
        lastTurn = turn['cost']
        if(turn['callback'] is not None):
            turn['callback']()

    
def peekTurn():
    global lastTurn
    return lastTurn

def clear():
    global lastTurn
    lastTurn = 0