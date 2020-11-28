from db.run_sql import run_sql
from models.treatment import Treatment
from models.pet import Pet
from models.pet_treatment import PetTreatment

class PetTreatmentsRep:
    def __init__(self):
        self.table = 'pets_treatments'

    def save(self, pet_treatment):
        sql = f"INSERT INTO {self.table} " + "(pet_id, treatment_id) VALUES (%s, %s) RETURNING id"
        values = [pet_treatment.pet_id, pet_treatment.treatment_id]
        results = run_sql(sql, values)
        pet_treatment.id = results[0]['id']
        return pet_treatment

    def select_all(self):
        pets_treatments = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            pet_treatment = PetTreatment(
                row["pet_id"],
                row["treatment_id"],
                row["id"],
            )
            pets_treatments.append(pet_treatment)
        return pets_treatments

    def select(self, id):
        pet_treatment = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            pet_treatment = PetTreatment(
                result["pet_id"],
                result["treatment_id"],
                result["id"],
            )
        return pet_treatment
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)