# Pet in Python 3.7
import random 
class Noise:
    def __init__(self, name: str, melody: str, decibel: int):
        self.__name = name 
        self.__melody = melody 
        self.__decibel = decibel 
    def getName(self):
        return self.__name 
    def getMelody(self):
        return self.__melody 

class Species:
    def __init__(self, kind:str, defaultSnarl: Noise):
        self.__kind = kind 
        self.__snarls = [] 
        self.__snarls.append(defaultSnarl) 
        self.__fear = [] 
        self.__snorle = Noise('snorle','Zzzzzz',5) 
        self.__laught = Noise('laught','hahaha',10) 
        self.__cry = Noise('cry','snifff',10) 
    def getKind(self):
        return self.__kind 
    def getFear(self):
        return self.__fear 
    def getSnorle(self):
        return self.__snorle 
    def getLaught(self):
        return self.__laught 
    def getCry(self):
        return self.__cry 
    def getSnarls(self):
        return self.__snarls 
    def addSnarl( self, snarl: Noise ):
        self.__snarls.append( snarl ) 	
    def addFear( self, someToFear  ):
        if ( type(self) == type(someToFear) and (self.__kind != someToFear.getKind()) ):
            self.__fear.append( someToFear )  

from enum import Enum
class Feelings(Enum):
    HAPPY = 1
    JOYFUL = 2
    NORMAL = 3
    AFFLICTED = 4
    SAD = 5

class Pet:
    def __init__(self, name: str , species: Species):
        self.__name = name 
        self.__species = species 
        self.__state = "awake" 
        self.__moves = 0 
        self.__feel = Feelings.NORMAL 
           
    def getSpecies(self):
    	return self.__species  
    def getMoves(self):
    	return self.__moves 
    def getName(self):
    	return self.__name 
    def setFeel( self, feel: Feelings):
        self.__feel = feel 
    def areYouSleep(self):
    	return self.__state =="sleeping"  
    def madeNoise( self ):
        if self.__state == "awake":
            if (self.__feel == Feelings.NORMAL):
                snarls = self.__species.getSnarls() 
                rnd = random.randrange(0,len(snarls))
                return snarls[rnd].getMelody() 
            elif (self.__feel == Feelings.SAD or self.__feel == Feelings.AFFLICTED):
                return self.__species.getCry().getMelody() 
            else:
                return self.__species.getLaught().getMelody() 
        else:
            return self.__species.getSnorle().getMelody() 
        return "aNoise" 
    def move( self ):
        if (self.__state == "awake"):
            self.__moves+=1 
    def wakeUp( self ):
        if (self.__state == "sleeping"):
            self.__state = "awake" 
    def sleep( self ):
        if (self.__state == "awake"):
            self.__state = "sleeping"
  
            
print("CONFIGURE SPECIES") 
        
s1 = Noise("meow","meeeooow",15)
s2 = Noise("miau","miauuu",10)
s3 = Noise("wigh","wiiiiggh",35)
cat = Species("cat",s1  ) 
cat.addSnarl(s2) 
cat.addSnarl(s3) 
print( cat.getKind() )
snarls = cat.getSnarls()
for x in range(len(snarls)):
    print(snarls[x].getName())


s4 = Noise("au","auuau au",15)
s5 = Noise("wolf","wolf wolf wolf",35)

dog = Species("dog",s4) 
dog.addSnarl(s5) 
print( dog.getKind() ) 
snarls = dog.getSnarls()
for x in range(len(snarls)):
    print(snarls[x].getName())

s6 = Noise("ufff","ufff",10)
s7 = Noise("scream","aaaaaaaaaaggh",45)
human = Species("human",s6) 
human.addSnarl(s7) 
print( human.getKind() ) 
snarls = human.getSnarls()
for x in range(len(snarls)):
    print(snarls[x].getName())

dog.addFear( human ) 
dog.addFear( dog ) 
cat.addFear( human ) 
cat.addFear( dog ) 
cat.addFear( cat ) 
print(dog.getKind() + " fears")
for f in dog.getFear():
    print(f.getKind())

print(cat.getKind() + " fears")
for f in cat.getFear():
    print(f.getKind())


print("CREATE PETS") 

pet1 = Pet("Tom", cat)
pet2 = Pet("Garfield", cat)
pet3 = Pet("Goliat", dog)
pet4 = Pet("Pablo", human)
print(pet1.getName())
print(pet1.getSpecies().getKind())
print(pet2.getName())
print(pet2.getSpecies().getKind())
print(pet3.getName())
print(pet3.getSpecies().getKind())
print(pet4.getName())
print(pet4.getSpecies().getKind())


print("PLAY WITH PETS") 
print(pet1.getName())
print(pet1.getSpecies().getKind())

print( "Are you sleep" , pet1.areYouSleep())
pet1.wakeUp()
pet1.wakeUp()
print( "Are you sleep" , pet1.areYouSleep())
pet1.sleep()
print( "Are you sleep" , pet1.areYouSleep())
print( "Current moves", pet1.getMoves())
pet1.move() 
print( "Current moves", pet1.getMoves())
pet1.wakeUp() 
pet1.move() 
print( "Current moves", pet1.getMoves())
print( "Are you sleep" , pet1.areYouSleep())
print( "Made noises!") 
print( pet1.madeNoise())
print( pet1.madeNoise())
print( pet1.madeNoise())
print( pet1.madeNoise())
print( pet1.madeNoise())

pet1.sleep() 
print( pet1.madeNoise())
print( pet1.madeNoise())
pet1.wakeUp() 
print( pet1.madeNoise())

print("Setting Happy") 
pet1.setFeel( Feelings.HAPPY )
print( pet1.madeNoise())
print("Setting Normal") 
pet1.setFeel( Feelings.NORMAL )
print( pet1.madeNoise())
print("Setting Sad") 
pet1.setFeel( Feelings.SAD )
print( pet1.madeNoise())
print("Setting Normal") 
pet1.setFeel( Feelings.NORMAL )
print( pet1.madeNoise())
print( pet1.madeNoise())
print( pet1.madeNoise())
