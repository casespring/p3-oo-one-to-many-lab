class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("Pet type is not valid")
        self._pet_type = pet_type
        

class Owner:
    def __init__(self, name):
        self.name = name 

    def pets(self):
        my_pets = []
        for pets in Pet.all:
            if pets.owner == self:
                my_pets.append(pets)
        return my_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
       return sorted(self.pets(), key=lambda pet: pet.name)


owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)

print(owner.get_sorted_pets())