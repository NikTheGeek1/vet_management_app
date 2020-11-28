class Pet:
    def __init__(self, name, dob, yo, type, owner_id, vet_id, image, id = None):
        self.name = name
        self.dob = dob
        self.yo = yo
        self.type = type
        self.owner = owner_id
        self.vet = vet_id
        self.image = image


    def update_age(self):
        pass
    
    def convert_to_image(self):
        pass