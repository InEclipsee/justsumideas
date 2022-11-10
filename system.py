from dataclasses import dataclass
import random
from datetime import datetime
from tabnanny import check
from uuid import RFC_4122


def prob():
    random.seed(datetime.now())
    res = random.randint(1,6)
    return res

def checkMorir(entity):
    if entity.hp <= 0:
        entity.hp = 0
        return entity.hp <= 0

class equipamiento():
    probo = 0
    def __init__(self, name, desc, durab, mat):
        self.name = name
        self.desc = desc 
        self.durab = durab
        self.dActual = durab
        self.mat = mat
        self.tag = 'None'
    
    def reparar(self):
        probo = prob()
        if probo%2 == 0:
            self.dActual = self.durab
            print('Durabilidad:', self.dActual)
            return 'Reparado con éxito!'
        else:
            self.dActual = self.dActual/2
            print('Durabilidad:', self.dActual)
            return 'Cuidao k hiciste cagar el objeto!'

class arma(equipamiento):
    def __init__(self, name, desc, durab, mat, atq):
        super().__init__(name, desc, durab, mat)
        self.atq = atq
        self.tag = 'Hand'
        self.type = 'None'
        self.estado = 'None'
    
    def afilar(self):
        probo = prob()
        if self.type == 'Afilado':
            if probo%2 == 0:
                self.estado = 'God'
                return 'Afilado con éxito!'
            else:
                self.dActual = self.dActual/2
                print('Durabilidad:', self.dActual)
                return 'Cuidao k hiciste cagar el arma!'
        else:
            print('No es arma con filo saco wea!')

class armadura(equipamiento):
    def __init__(self, name, desc, durab, mat, defe):
        super().__init__(name, desc, durab, mat)
        self.defe = defe
        self.tag = 'Body'

none = arma('None', 'None', -1, 'None', 1)
noneA = armadura('None', 'None', -1, 'None', 1)

class char():
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio
        self.weapon = none
        self.armor = noneA
        self.atq = 1
        self.hp = 100
        self.defe = 5
    
    def equip(self, equipment):
        if equipment.tag == 'Hand':
            self.weapon = equipment
            self.atq = equipment.atq
            print(f'{equipment.name} equipado satisfactoriamrairemiemeMENTE!')
        if equipment.tag == 'Body':
            self.armor = equipment
            self.defe = equipment.defe
            print(f'{equipment.name} equipado satisfactoriamrairemiemeMENTE!')
    
    def mostrarInventario(self):
        print('\nNombre:', self.name)
        print('Biografía:', self.bio)
        print('Vida:', self.hp)
        print('\n====== EQUIPAMIENTO ======')
        print('Arma:', self.weapon.name)
        print('Armor:', self.armor.name, '\n')

    def atacar(self, enemigo):
        crit = False
        if checkMorir(enemigo):
            print('Ya esta muerto')
        else:
            atqVar = random.randint(round(self.atq*0.9),round(self.atq*1.10))
            calcDano = atqVar - enemigo.defe
            if calcDano<0:
                calcDano = 0
            if enemigo.defe > atqVar:
                print(self.name, 'No puede atacar')
            elif enemigo.defe == calcDano:
                print('Estan a mano')
            else:
                probo = prob()
                
                if probo == 6:
                    crit = True
                    enemigo.hp -= calcDano * 2
                    dano = calcDano * 2
                    
                    print('Critico!')
                else:
                    enemigo.hp -= calcDano
                    dano = calcDano

                print(self.name, 'inflige', dano, 'a', enemigo.name, '\n')
                if enemigo.hp <= 0:
                    if crit == True:
                        enemigo.hp = 0
                        print(self.name, 'se hizo cagar a', enemigo.name, '\n')
                    else:
                        enemigo.hp = 0
                        print(enemigo.name, 'se murió uvu!\n')
    def getHP(self):
        return self.hp
    
    def getATK(self):
        return self.atq
    
    def getDEF(self):
        return self.defe
