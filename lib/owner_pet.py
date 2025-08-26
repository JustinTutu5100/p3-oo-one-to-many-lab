# __define-ocg__ Owner–Pet relationship lab
# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """
        Return all pets belonging to this owner
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Add an owner to the pet if it's a Pet instance
        """
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self

    def get_sorted_pets(self):
        """
        Return a sorted list of this owner's pets by name
        """
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    # class variables
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # validate type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type

        # owner can be None or an Owner
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")
        self.owner = owner

        # add to all pets collection
        Pet.all.append(self)
