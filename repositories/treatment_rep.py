from db.run_sql import run_sql
from models.pet import Pet
from models.treatment import Treatment

class TreatmentRep:
    def __init__(self):
        self.table = "treatments"

    def save(self, treatment):
        sql = f"INSERT INTO {self.table} " + "(title, description) VALUES (%s, %s) RETURNING id"
        values = [treatment.title, treatment.description]
        results = run_sql(sql, values)
        treatment.id = results[0]["id"]
        return treatment

    def select_all(self):
        treatments = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            treatment = Treatment(
                row["title"],
                row["description"],
                row["id"]
            )
            treatments.append(treatment)
        return treatments

    def select(self, id):
        treatment = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            treatment = Treatment(
                result["title"],
                result["description"],
                result["id"]
            )
        return treatment
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)
    
    def update(self, treatment):
        sql = f"UPDATE {self.table} " + "SET (title, description) = (%s, %s) WHERE id = %s"
        values = [treatment.title, treatment.description, treatment.id]
        run_sql(sql, values)

    def get_pets(self, treatment_id):
        pets = []
        sql = """
        SELECT pets.* FROM pets
        INNER JOIN pets_treatments ON pet.id = pets_treatments.pet_id 
        INNER JOIN treatments ON pets_treatments.treatment_id = treatment.id
        WHERE treatments.id = %s 
        """
        values = [treatment_id]
        results = run_sql(sql, values)

        for row in results:
            pet = Pet(
                row['name'],
                row['dob'],
                row['yo'],
                row['type'],
                row['owner_id'],
                row['vet_id'],
                row['image'],
                row['id']
            )
            pets.append(pet)
        return pets

