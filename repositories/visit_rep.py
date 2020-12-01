from db.run_sql import run_sql
from models.visit import Visit

class VisitRep:
    def __init__(self):
        self.table = "visits"

    def save(self, visit):
        sql = f"INSERT INTO {self.table} " + "(pet_id, check_in, check_out, description) VALUES (%s, %s, %s, %s) RETURNING id"
        values = [visit.pet_id, visit.check_in, visit.check_out, visit.description]
        results = run_sql(sql, values)
        visit.id = results[0]["id"]
        return visit

    def select_all(self):
        visits = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            visit = Visit(
                row['pet_id'],
                row["check_in"],
                row["check_out"],
                row['description'],
                row["id"],
            )
            visits.append(visit)
        return visits

    def select(self, id):
        visit = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            visit = Visit(
                result['pet_id'],
                result["check_in"],
                result["check_out"],
                result['description'],
                result["id"],
            )
        return visit
        
    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)


    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)


    