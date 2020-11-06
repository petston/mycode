
class cat:
    def sound(self):
        print("meow")

class dog:
    def sound(self):
        print("bow")


def makesound(animaltype):
    animaltype.sound()


catobj = cat()
dogobj = dog()
makesound(catobj)
makesound(dogobj)

