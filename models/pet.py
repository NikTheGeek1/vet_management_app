import datetime as dt
class Pet:
    def __init__(self, name, dob, yo, type, owner, vet, image64, image_type, id = None):
        self.name = name
        self.dob = dob
        self.yo = yo
        self.type = type
        self.owner = owner
        self.vet = vet
        self.id = id
        self.image_type = image_type
        if (not image64):
            self.image64 = ''        
        else:
            self.image64 = image64

        if isinstance(dob, dt.date) and isinstance(yo, float):
            self.yo = self.dob_to_yo(self.dob)
        
        if (not dob):
            self.dob = self.yo_to_dob(self.yo)

        if (not yo):
            self.yo = self.dob_to_yo(self.dob)
             


    def update_age(self):
        pass
 
    def dob_to_yo(self, dob):
        days_from_birth = dt.date.today() - dob 
        days_from_birth = days_from_birth.days
        years = days_from_birth // 365
        years_remainder = days_from_birth % 365
        months = years_remainder // 29
        return years + (months / 100)

    def yo_to_dob(self, yo):
        years = int(yo // 1)
        only_months = yo - years
        months = int(only_months * 100)
        year = dt.date.today().year - years
        month = dt.date.today().month - months
        day = 1
        return dt.date(year, month, day)



        


