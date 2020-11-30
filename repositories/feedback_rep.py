from db.run_sql import run_sql
from models.feedback import Feedback
from repositories.owner_rep import OwnerRep


class FeedbackRep:
    def __init__(self):
        self.table = "feedbacks"

    def save(self, feedback):
        sql = (
            f"INSERT INTO {self.table} "
            + "(qos, fs, cf, recommend, suggestions, other_comment, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
        )
        values = [
            feedback.qos,
            feedback.fs,
            feedback.cf,
            feedback.recommend,
            feedback.suggestions,
            feedback.other_comment,
            feedback.owner.id,
        ]
        results = run_sql(sql, values)
        feedback.id = results[0]["id"]
        return feedback

    def select_all(self):
        feedbacks = []
        sql = f"SELECT * FROM {self.table}"
        results = run_sql(sql)

        for row in results:
            owner = OwnerRep().select(row["owner_id"])
            feedback = Feedback(
                row["qos"],
                row["fs"],
                row["cf"],
                row["recommend"],
                row["suggestions"],
                row["other_comment"],
                owner,
                row["id"],
            )
            feedbacks.append(feedback)
        return feedbacks

    def select(self, id):
        feedback = None
        sql = f"SELECT * FROM {self.table} " + "WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]

        if result is not None:
            owner = OwnerRep().select(result["owner_id"])
            feedback = Feedback(
                result["qos"],
                result["fs"],
                result["cf"],
                result["recommend"],
                result["suggestions"],
                result["other_comment"],
                owner,
                result["id"],
            )
        return feedback

    def delete_all(self):
        sql = f"DELETE FROM {self.table}"
        run_sql(sql)

    def delete(self, id):
        sql = f"DELETE FROM {self.table} " + "WHERE id = %s"
        values = [id]
        run_sql(sql, values)
