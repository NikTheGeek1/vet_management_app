from db.run_sql import run_sql
from models.pet import Pet
from models.treatment import Treatment
from models.visit import Visit
from repositories.owner_rep import OwnerRep
from repositories.vet_rep import VetRep
import datetime as dt
class PetRep:
    def __init__(self):
        self.table = "pets"

    def save(self, pet):
        sql = f"INSERT INTO {self.table} " + "(pet_name, dob, yo, animal_type, owner_id, vet_id, img, img_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
        values = [pet.name, pet.dob, pet.yo, pet.type, pet.owner.id, pet.vet.id, pet.image64, pet.image_type]
        results = run_sql(sql, values)
        pet.id = results[0]["id"]
        return pet

    def select_all(self):
        pets = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            owner = OwnerRep().select(row['owner_id'])
            vet = VetRep().select(row['vet_id'])
            pet = Pet(
                row["pet_name"],
                row["dob"],
                row["yo"],
                row['animal_type'],
                owner,
                vet,
                row['img'],
                row['img_type'],
                row['id']
            )
            pet.update_age()
            pets.append(pet)
        return pets

    def select(self, id):
        pet = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            owner = OwnerRep().select(result['owner_id'])
            vet = VetRep().select(result['vet_id'])
            pet = Pet(
                result["pet_name"],
                result["dob"],
                result["yo"],
                result['animal_type'],
                owner,
                vet,
                result['img'],
                result['img_type'],
                result['id']
            )
            pet.update_age()
        return pet

    def select_currently_in_pets(self):
        pets = []
        sql = f"SELECT * FROM visits"
        results = run_sql(sql)

        pets_ids = []
        for row in results:
            if row['check_out'] > dt.date.today():
                pet = self.select(row['pet_id'])
                if pet.id not in pets_ids:
                    pets.append(pet)
                    pets_ids.append(pet.id)
        return pets    

    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)
    
    def update(self, pet):
        sql = f"UPDATE {self.table} " + "SET (pet_name, dob, yo, vet_id, img, img_type) = (%s, %s, %s, %s, %s, %s) WHERE id = %s RETURNING *"
        values = [pet.name, pet.dob, pet.yo, pet.vet.id, pet.image64, pet.image_type, pet.id]
        run_sql(sql, values)

    def get_treatments(self, pet_id):
        treatments = []
        sql = """
        SELECT treatments.* FROM treatments
        INNER JOIN pets_treatments ON treatments.id = pets_treatments.treatment_id
        INNER JOIN pets ON pets_treatments.pet_id = pets.id
        WHERE pets.id = %s
        """
        values = [pet_id]
        results = run_sql(sql, values)

        for row in results:
            treatment = Treatment(row['title'], row['description'])
            treatments.append(treatment)
        return treatments

    def get_visits(self, pet_id):
        visits = []
        sql = "SELECT * FROM visits WHERE pet_id = %s"
        values = [pet_id]
        results = run_sql(sql, values)

        for row in results:
            visit = Visit(row['pet_id'], row['check_in'], row['check_out'], row['description'], row['id'])
            visits.append(visit)
        return visits



    def update_yos(self, pets):
        assert type(pets) == list, 'Pets is not a list in update_yos -- provide a list'
        for pet in pets:
            sql = f"UPDATE {self.table} " + "SET (pet_name, dob, yo, vet_id, img, img_type) = (%s, %s, %s, %s) WHERE id = %s"
            values = [pet.name, pet.dob, pet.yo, pet.vet_id, pet.image, pet.image_type, pet.id]
            run_sql(sql, values)
                

