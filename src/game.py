import random
import os


def clear(): return os.system('cls')


class Game():

    NPC_LIST = ["R", "O", "Y", "G", "B", "P"]
    LOCATION_LIST = ["Market", "Gym", "Beach", "Coffee Shop", "Park", "Office"]

    def __init__(self):
        self.round = 0
        self.players = self.getPlayers()
        self.impostor = random.choice(self.NPC_LIST)
        self.interactions = self.generateInteractions()

    def getPlayers(self):
        players = []
        player_count = int(input("Number of Players: "))
        for i in range(1, player_count + 1):
            players.append(input("Player " + str(i) + " Name: "))
        clear()
        return players

    def generateInteractions(self):
        interactions = {}
        for player in self.NPC_LIST:
            interactions[player] = dict()
        for player in self.NPC_LIST:
            temp = self.NPC_LIST.copy()
            temp.remove(player)
            for i in range(random.randint(2, 3)):
                randomPlayer = random.choice(temp)
                randomLocation = random.randint(0, len(self.LOCATION_LIST) - 1)
                interactions[player][randomPlayer] = [
                    randomLocation, "", "No Intel"]
                interactions[randomPlayer][player] = [
                    randomLocation, "", "No Intel"]
                temp.remove(randomPlayer)
        temp = self.NPC_LIST.copy()
        temp.remove(self.impostor)
        current = random.choice(temp)
        break_at_end = False
        while len(temp) > 0:
            for npc in interactions:
                for key in interactions[npc]:
                    randKey = random.choice(list(interactions.keys()))
                    interactions[npc][key][1] = str(randKey) + " and "
                    interactions[key][npc][1] = str(randKey) + " and "
                    randInnerKey = random.choice(
                        list(interactions[randKey].keys()))
                    interactions[npc][key][1] += str(randInnerKey)
                    interactions[key][npc][1] += str(randInnerKey)
                    location = interactions[randKey][randInnerKey][0]
                    interactions[npc][key][1] += (" at the " +
                                                  self.LOCATION_LIST[location])
                    interactions[key][npc][1] += (" at the " +
                                                  self.LOCATION_LIST[location])
                    if not break_at_end and random.randint(0, 3) == 1 and interactions[npc][key][2] == 'No Intel':
                        interactions[npc][key][2] = current + \
                            " is not the impostor"
                        interactions[key][npc][2] = current + \
                            " is not the impostor"
                        temp.remove(current)
                        if len(temp) != 0:
                            current = random.choice(temp)
                        else:
                            break_at_end = True
            if break_at_end:
                break
        return interactions

    def play(self):
        clear()
        while True:
            self.round += 1
            for player in self.players:
                try:
                    # print(game.interactions)
                    print("NPCs: ", end="")
                    for i in range(len(self.NPC_LIST)):
                        npc = self.NPC_LIST[i]
                        print(npc, end=" ")
                    print("")
                    print("Locations: ", end="")
                    for i in range(len(self.LOCATION_LIST)):
                        location = self.LOCATION_LIST[i]
                        print("[" + str(i+1) + "] " + location, end="  ")
                    print("\n")
                    npcs = input(player + ", NPCs to listen to (separated by space): ").upper()
                    npcs = npcs.split()
                    if len(npcs) > 2:
                        location = npcs[2]
                    else: 
                        location = int(input(player + ", Location of NPCs (use # above): "))
                    print("")
                    if npcs[0][0] in self.interactions[npcs[1][0]] and self.interactions[npcs[1][0]][npcs[0][0]][0] + 1 == location:
                        print(self.interactions[npcs[1][0]][npcs[0][0]][1])
                        print(self.interactions[npcs[1][0]][npcs[0][0]][2])
                    else:
                        print('Conversation is Private')
                    cont = input('\nPress Enter to continue, or G to guess the impostor: ')
                    clear()
                    if (cont.upper() == 'G'):
                        imp = input('Who is the impostor? ')
                        if imp.upper()[0] == self.impostor:
                            print('The winner is ' + player + '!')
                            return
                        else:
                            print('Incorrect')
                except:
                    input('Error occured. Press Enter to continue...')
                    clear()
                    continue

clear()
game = Game()
game.play()
