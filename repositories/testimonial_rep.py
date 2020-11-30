from db.run_sql import run_sql
from models.testimonial import Testimonial
from repositories.owner_rep import OwnerRep

class TestimonialRep:
    def __init__(self):
        self.table = "testimonials"

    def save(self, testimonial):
        sql = f"INSERT INTO {self.table} " + "(testimonial, owner_id) VALUES (%s, %s) RETURNING id"
        values = [testimonial.testimonial, testimonial.owner.id]
        results = run_sql(sql, values)
        testimonial.id = results[0]["id"]
        return testimonial

    def select_all(self):
        testimonials = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            owner = OwnerRep().select(row["owner_id"])
            testimonial = Testimonial(
                row["testimonial"],
                owner,
                row["id"],
            )
            testimonials.append(testimonial)
        return testimonials

    def select(self, id):
        testimonial = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            owner = OwnerRep().select(result["owner_id"])
            testimonial = Testimonial(
                result["testimonial"],
                owner,
                result["id"],
            )
        return testimonial
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)

