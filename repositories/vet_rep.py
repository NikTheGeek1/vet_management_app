from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet

class VetRep:
    def __init__(self):
        self.table = "vets"

    def save(self, vet):
        sql = f"INSERT INTO {self.table} " + "(first_name, last_name) VALUES (%s, %s) RETURNING id"
        values = [vet.first_name, vet.last_name]
        results = run_sql(sql, values)
        vet.id = results[0]["id"]
        return vet

    def select_all(self, sort = False):
        vets = []
        if sort:
            sql = f"SELECT * FROM {self.table} ORDER BY last_name ASC"
        else:
            sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            vet = Vet(
                row["first_name"],
                row["last_name"],
                row['id']
            )
            vets.append(vet)
        return vets

    def select(self, id):
        vet = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            vet = Vet(
                result["first_name"],
                result["last_name"],
                result['id']
            )
        return vet
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)

    def get_pets(self, vet_id):
        pets = []
        sql = "SELECT * FROM pets WHERE vet_id = %s"
        values = [vet_id]
        results = run_sql(sql, values)

        for row in results:
            pet = Pet(
                row['pet_name'], 
                row['dob'], 
                row['yo'], 
                row['animal_type'], 
                row['owner_id'], 
                row['vet_id'], 
                row['img'],
                row['img_type'], 
                row['id']
            )
            pets.append(pet)
        return pets

    def update(self, first_name, last_name, id):
        sql = f"UPDATE {self.table} " + "SET (first_name, last_name) = (%s, %s) WHERE id = %s RETURNING *"
        values = [first_name, last_name, id]
        run_sql(sql, values)
    
    