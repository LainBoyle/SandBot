from dataclasses import dataclass
import random


@dataclass
class Chance:
    
    def __init__():
        return 
    
    def flipCoin():
        if random.randint(1, 2) == 1:
            return '**Heads**'
        else:
            return '**Tails**'
    
    def roll(command):
        [num, dice, modifier] = Chance.parseRollCommand(command)
        
        total = 0
        outString = "["
        
        if num == 1:
            return str(random.randint(1, dice) + modifier)
    
        for i in range(num):
            subTotal = random.randint(1, dice) + modifier
            total += subTotal
            outString = outString + str(subTotal)
            if i < (num-1):
                outString += ", "
        
        return outString + "] = " + str(total)
        
        
    
    def parseRollCommand(command):
        commandNum = command.split('d')[0]
        diceandMod = command.split('d')[1]
        
        num = commandNum.replace("!roll ", "")
        if num.strip() == "":
            num = 1
        
        num = int(num)
            
        if "+" in diceandMod:
            dice = int(diceandMod.split("+")[0])
            modifier = int(diceandMod.split("+")[1])
        elif "-" in diceandMod:
            dice = int(diceandMod.split("-")[0])
            modifier = -int(diceandMod.split("-")[1])
        else:
            dice = int(diceandMod)
            modifier = 0
        
        return [num, dice, modifier]

        
        