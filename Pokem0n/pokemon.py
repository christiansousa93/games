
import random

nomesEletrico = ("Pikachu", "Electabuzz", "Pichu", "Raichu")
nomesAquatico = ("Squirtle", "Blastoise","Wartotle")


class Pokemon:
    def __init__(self, nome="", especie = "", ataque=0, defesa=0, hp=0):

        if (nome == ""):
            self._nome = "Geraldo"
        else:
            self._nome = nome

        self._especie = especie

        if (ataque == 0):
            self._ataque = random.randint(30, 50)
        else:
            self._ataque = ataque

        if (defesa == 0):
            self._defesa = random.randint(20, 30)
        else:
            self._defesa = ataque

        if (hp == 0):
            self._hp = random.randint(50, 100)
        else:
            self._hp = hp


class PokemonEletrico(Pokemon):
    def __init__(self, nome="", especie ="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)
        if (nome == ""):
            self._nome = nomesEletrico[random.randint(0,len(nomesEletrico)-1)]
        else:
            self._nome = nome

        if (especie == ""):
            self._especie = nomesEletrico[random.randint(0,len(nomesEletrico)-1)]
        else:
            self.especie = especie

        self._tipo = "Elétrico"
        self._movimento = "Choque do Trovão"

        match self._especie:
            case "Pikachu":
                if (ataque == 0):
                    self._ataque = random.randint(40, 60)
                else:
                    self._ataque = ataque

                if (defesa == 0):
                    self._defesa = random.randint(10, 30)
                else:
                    self._defesa = ataque

                if (hp == 0):
                    self._hp = random.randint(30, 80)
                else:
                    self._hp = hp

            case "Pichu":
                if (ataque == 0):
                    self._ataque = random.randint(20, 40)
                else:
                    self._ataque = ataque

                if (defesa == 0):
                    self._defesa = random.randint(10, 20)
                else:
                    self._defesa = ataque

                if (hp == 0):
                    self._hp = random.randint(30, 50)
                else:
                    self._hp = hp
            case _: 
                print("Usou o método super")
                    


if __name__ == "__main__":
    pokemon1 = Pokemon("Marcos", 10, 10, 10)
    print(vars(pokemon1))

    pokemon2 = Pokemon()

    pokemon3 = PokemonEletrico(nome = "José")
    print(vars(pokemon2))
    print(vars(pokemon3))
    
    
    
    
    import random

nomesEletrico = ("Pikachu", "Electabuzz", "Pichu", "Raichu")
nomesAquatico = ("Squirtle", "Blastoise","Wartotle")


class Pokemon:
    def __init__(self, nome="", especie = "", ataque=0, defesa=0, hp=0):

        if (nome == ""):
            self._nome = "Geraldo"
        else:
            self._nome = nome

        self._especie = especie

        if (ataque == 0):
            self._ataque = random.randint(30, 50)
        else:
            self._ataque = ataque

        if (defesa == 0):
            self._defesa = random.randint(20, 30)
        else:
            self._defesa = ataque

        if (hp == 0):
            self._hp = random.randint(50, 100)
        else:
            self._hp = hp

    def criarAtributos(self, ataqueInicio, ataqueFinal, defesaInicio, defesaFinal, hpInicio, hpFinal):
        self._ataque = random.randint(ataqueInicio,ataqueFinal)
        self._defesa = random.randint(defesaInicio,defesaFinal)
        self._hp = random.randint(hpInicio,hpFinal)

class PokemonEletrico(Pokemon):
    def __init__(self, nome="", especie ="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)

        if (especie == ""):
            self._especie = nomesEletrico[random.randint(0,len(nomesEletrico)-1)]
        else:
            self._especie = especie

        if (nome == ""):
            self._nome = self._especie
        else:
            self._nome = nome

        

        self._tipo = "Elétrico"
        self._movimento = "Choque do Trovão"

        match self._especie:
            case "Pikachu":
                self.criarAtributos(40,60,10,20,50,80)

            case "Pichu":
                self.criarAtributos(20,30,10,20,30,50)
            case _: 
                print("Usou o método super")
        if(ataque !=0):
            self._ataque = ataque
        if(defesa !=0):
            self._defesa = defesa
        if(hp !=0):
            self._hp = hp

class PokemonAquatico(Pokemon):
    def __init__(self, nome="", especie="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)

        if (especie == ""):
            self._especie = nomesAquatico[random.randint(0,len(nomesAquatico)-1)]
        else:
            self._especie = especie

        if (nome == ""):
            self._nome = self._especie
        else:
            self._nome = nome

        

        self._tipo = "Aquatico"
        self._movimento = "Jato de Água"

        match self._especie:
            case "Squirtle":
                self.criarAtributos(40,60,10,20,50,80)

            case "Wartotle":
                self.criarAtributos(20,30,10,20,30,50)
            case _: 
                print("Usou o método super")
        if(ataque !=0):
            self._ataque = ataque
        if(defesa !=0):
            self._defesa = defesa
        if(hp !=0):
            self._hp = hp
                    


if __name__ == "__main__":
    pokemon1 = Pokemon("Marcos", 10, 10, 10)
    print(vars(pokemon1))

    pokemon2 = Pokemon()

    pokemon3 = PokemonEletrico(nome = "José", especie="Pikachu", hp=600)
    pokemon4 = PokemonAquatico()
    print(vars(pokemon2))
    print(vars(pokemon3))
    print(vars(pokemon4))
    
    
    import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")






if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    Charizard.fight(Blastoise) # Get them to fight