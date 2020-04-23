# Test. Modeling Test
Instruction for modeling test. Fullstack developer profile

Related to [main document](https://github.com/pablogottifredi/boilerplate-python-script/blob/master/Readme.md)
## Goals
Simple test python docker and run script

## Spec
Provide a class design to represent the types and methods required to run a Pet behavior 

Optionally provide source code with the design proposed

### Espected behaviour

* The Pet has a name and kind/species
* Each kind of Pet has fear to another kinds of pets, but not with himself
* The Pet has functions like
    * Made noise
    * Move
    * Wake up
    * Sleep
* The Pet can be sleeping or awake
* If the Pet is awake
    * When run the move function, they moving
    * When run the noise function, they snarl
* If the Pet is sleeping
    * When run the move function, they ignoring the instruction
    * When run the noise function, they snore
* The Pet has several kinds of snarl, severals melodies, with a certain duration and decibel

### Desired design features
Additionaly to awake or sleep state, the pet must have a feel property, like happy/sad/other.

If the feel property is setted in happy, when run the noise function, they laught

If the feel property is setted in sad, when run the noise function, they cries
