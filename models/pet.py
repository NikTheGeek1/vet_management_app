import datetime as dt
class Pet:
    def __init__(self, name, dob, yo, type, owner_id, vet_id, image, id = None):
        self.name = name
        self.dob = dob
        self.yo = yo
        self.type = type
        self.owner_id = owner_id
        self.vet_id = vet_id
        self.image = image


    def update_age(self):
        pass
    
    def convert_to_image(self):
        pass

    def dob_to_yo(self):
        days_from_birth = dt.date.today() - self.dob 
        days_from_birth = days_from_birth.days
        years = days_from_birth // 365
        years_remainder = days_from_birth % 365
        months = years_remainder // 29
        self.yo = years + (months / 100)
