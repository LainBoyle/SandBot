from dataclasses import dataclass
import random


@dataclass
class Chance:
    
    def __init__():
        return 
    
    def flipCoin(self):
        if random.randint(1, 2) == 1:
            return '**Heads**'
        else:
            return '**Tails**'
    
    def roll(self, command):
        [num, dice, modifier] = self.parseRollCommand(command)
        
        total = 0
        outString = "["
        
        if num == 1:
            return str(random.randint(1, dice) + modifier)
    
        for i in range(num):
            subTotal = random.randint(1, dice) + modifier
            total += subTotal
            outString = outString + str(subTotal)
            if i != num:
                outString += ","
        
        return outString + "] = " + str(total)
        
        
    
    def parseRollCommand(self, command):
        num = command.split('d')[0]
        diceandMod = command.split('d')[1]
        
        if num.strip() == "":
            num = 1
        
        num = int(num.strip())
            
        if "+" in diceandMod:
            dice = int(diceandMod.split("+")[0])
            modifier = int(diceandMod.split("+")[1])
        elif "-" in diceandMod:
            dice = int(diceandMod.split("-")[0])
            modifier = int(-(diceandMod.split("-")[1]))
        else:
            dice = int(diceandMod)
            modifier = 0
        
        return [num, dice, modifier]

        
        