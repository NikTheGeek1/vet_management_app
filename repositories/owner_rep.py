from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet
from models.feedback import Feedback
from models.testimonial import Testimonial

class OwnerRep:
    def __init__(self):
        self.table = "owners"

    def save(self, owner):
        sql = f"INSERT INTO {self.table} " + "(first_name, last_name, email, phone, registered) VALUES (%s, %s, %s, %s, %s) RETURNING id"
        values = [owner.first_name, owner.last_name, owner.email, owner.phone, owner.registered]
        results = run_sql(sql, values)
        owner.id = results[0]["id"]
        return owner

    def select_all(self):
        owners = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            owner = Owner(
                row["first_name"],
                row["last_name"],
                row["email"],
                row['phone'],
                row['registered'],
                row['id']
            )
            owners.append(owner)
        return owners

    def select(self, id):
        owner = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            owner = Owner(
                result["first_name"],
                result["last_name"],
                result["email"],
                result['phone'],
                result['registered'],
                result['id']
            )
        return owner
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)
    
    def update(self, owner):
        sql = f"UPDATE {self.table} " + "SET (email, phone) = (%s, %s) WHERE id = %s"
        values = [owner.email, owner.phone, owner.id]
        run_sql(sql, values)

    def get_pets(self, owner_id):
        pets = []
        sql = "SELECT * FROM pets WHERE owner_id = %s"
        values = [owner_id]
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

    def get_feedbacks(self, owner_id):
        feedbacks = []
        sql = "SELECT * FROM feedbacks WHERE owner_id = %s"
        values = [owner_id]
        results = run_sql(sql, values)

        for row in results:
            feedback = Feedback(
                row['qos'],
                row['fs'],
                row['cf'],
                row['recommend'],
                row['suggestions'],
                row['other_comment'],
                row['owner_id'],
                row['id']
            )
            feedbacks.append(feedback)
        return feedbacks

    def get_testimonial(self, owner_id):
        testimonial = None
        sql = "SELECT * FROM testimonials WHERE owner_id = %s"
        values = [owner_id]
        result = run_sql(sql, values)[0]

        if result is not None:
            testimonial = Testimonial(result['testimonial'], result['owner_id'], result['id'])

        return testimonial

    