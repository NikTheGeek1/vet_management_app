from db.run_sql import run_sql
from models.pet import Pet
from models.treatment import Treatment
from models.visit import Visit

class PetRep:
    def __init__(self):
        self.table = "pets"

    def save(self, pet):
        sql = f"INSERT INTO {self.table} " + "(name, dob, yo, animal_type, owner_id, vet_id, img) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
        values = [pet.name, pet.dob, pet.yo, pet.animal_type, pet.owner_id, pet.vet_id, pet.image]
        results = run_sql(sql, values)
        pet.id = results[0]["id"]
        return pet

    def select_all(self):
        pets = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            pet = Pet(
                row["name"],
                row["dob"],
                row["yo"],
                row['animal_type'],
                row['owner_id'],
                row['vet_id'],
                row['img'],
                row['id']
            )
            pets.append(pet)
        return pets

    def select(self, id):
        pet = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            pet = Pet(
                result["name"],
                result["dob"],
                result["yo"],
                result['animal_type'],
                result['owner_id'],
                result['vet_id'],
                result['img'],
                result['id']
            )
        return pet
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)
    
    def update(self, pet):
        sql = f"UPDATE {self.table} " + "SET (name, dob, yo, vet_id, img) = (%s, %s, %s, %s) WHERE id = %s"
        values = [pet.name, pet.dob, pet.yo, pet.vet_id, pet.image]
        run_sql(sql, values)

    def get_treatments(self, pet_id):
        treatments = []
        sql = """
        SELECT treatments.* FROM treatments
        INNER JOIN pets_treatments ON treatments.id = pets_treatments.treatment_id
        INNER JOIN pets ON pets_treatments.pet_id = pet.id
        WHERE id = %s
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

