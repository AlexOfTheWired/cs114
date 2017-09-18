
import pprint
import random
import sys
import os

""" Text based game where user makes decisions which affect
a series of encounters with enemies """
class Character(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

        self.dead = False

    def attack(self, player, enemy):
        rand_damage = random.randint(8, 32)
        enemy.hp -= rand_damage
        print(rand_damage, " damage!")
        return enemy


    def update(self):
        if self.hp < 0:
            self.dead = True
            self.hp = 0


class Player():
    def __init__( self, name ):

        self.name      = name
        self.hp        = 100
        self.attack    = 10
        self.defense   = 10
        self.inventory = []

    def prompt_player_name(self):

        return input("Player Name: ")

    def set_player_name(self):

        return setattr(self, "name", name)

class Enemy():
    def __init__(self, name):

        self.name      = name
        self.hp        = 50
        self.attack    = 10
        self.defense   = 10
        self.inventory = []

class Story():

    def display_intro_01(self):
        intro_01 =(
        "You are awoken to a cold pitch dark room. \n"
        "The faint light from other cryopods begin to illuminate the room dimly. \n"
        "you stumble out of your pod. \n"
        "A disembodied voice echoes in the vacinity. \n"
        "Disembodied Voice: \"Hello, Unit-23. You have just come out of a 32-Year cryosleep.\" \n"
        "\"Temporary amnesia is a side effect of sleep... do you remember your name?\" \n"
        )

        return intro_01

    def display_intro_02(self):
        intro_02 = (
        "\n\n"
        "Disembodied Voice: \"Ah yes, " + player.name + ". It is nice see you are alive. \n"
        "all other occupants have become decea-\" \n"
        "The AI has suddenly stopped talking, and a serious metalic noises echo in the area. \n"
        "You hear something scampering towards you in the darkness. \n"
        "Its aggressive shuffling draws closer to you until you can barely make it out. \n"
        "it\'s the Cryobay AI. It lunges towards you! \n\n"
        )
        return intro_02

    def display_story_01(self):
        story_01 = (
        "\n\n"
        "You have narrowly beaten the AI. \n"
        "The room is dead silent again, with the exception of your pounding heart. \n"
        "You feel around the room for a light switch, hoping to navigate the surrounding area more easily. \n"
        "Finally the lights com on by themselves and you can see the door into the main corridoor. \n"
        )
        return story_01

    def display_story_02(self):
        story_02 = (
        "As you walk into the hallway you see a trail of blood leading down the corridor. \n"
        "You follow it. \n"
        "Suddenly you hear the snarling of a Dog behind you. \n"
        "It\'s eyes are glazed over and blood oozes from its mouth. \n"
        "The Zombie Dog Lunges at you."
        )
        return story_02

class Logic():

    def game_over(self):
        if self.dead == True:
            return sys.quit()

    def game_complete(self, oppo1, oppo2):
        if oppo1.hp > 0 and oppo2.hp <= 0:
            print (player.name + " has escaped the ship!")
            return sys.exit()

    def continue_CMD(self):
        return input('Press any key to continue')



    def fight(self, oppo1, oppo2):
        while (oppo1.hp > 0) and (oppo2.hp > 0):
            print(oppo1.name, " attacks ", oppo2.name)
            character.attack(oppo2, oppo1)
            if oppo2.hp <= 0:
                character.update(oppo2)
                self.game_complete(oppo1, oppo2)
            else:
                print(oppo2.name, " attacks ", oppo1.name)
                character.attack(oppo1, oppo2)
            if oppo1.hp <= 0:
                character.update(oppo2)
                print(oppo2.name, " is winner")
                self.game_over(oppo1)
        print(player.name + ': ' , oppo1.hp)
        print(enemy1.name + ': ', oppo2.hp)

    def encounter(self, player, opponent):
        if player.hp > 70:
            self.fight(player, opponent)
            # if player['HP'] <= 0:
            #     return game_over(player)
            input('Press any key to continue')
        elif enemy.name == "Zombie AI":
            self.fight(player, opponent)
            # return player
        else:
            get_item(player)
            input('Press any key to continue')


player    = Player("default")
enemy1    = Enemy("Zombie AI")
enemy2    = Enemy("Zombie Dog")
story     = Story()
logic     = Logic()
character = Character(player.name, player.hp)

def main():

    print(story.display_intro_01())

    name = player.prompt_player_name()

    player.name = name

    print(story.display_intro_02())

    logic.continue_CMD()

    print("Encounter 1: \n\n")

    logic.encounter(player, enemy1)

    print(story.display_story_01())

    logic.continue_CMD()

    print(story.display_story_02())

    print("Encounter 2:")

    logic.encounter(player, enemy2)

    logic.game_complete(player, enemy2)


if __name__ == '__main__':
    main()
