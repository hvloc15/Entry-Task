from django.db import models, connection
from entry_task.exceptions import InsertError

class ActivityManager(models.Manager):

    def insert_to_database(self, *query_list):
        query = "INSERT INTO " + self.model._meta.db_table + "(event_id,user_id,date) VALUES (%s,%s,%s)"
        cursor = connection.cursor()
        try:
            cursor.execute(query, query_list)
        except:
            raise InsertError("Cannot insert to database. Data already exist in database")

    def get_list_users(self, eid):
        query = "SELECT tab2.username FROM "\
                + self.model._meta.db_table + " tab1 INNER JOIN user_info_tab tab2 on tab1.user_id = tab2.user_id " \
                + "WHERE tab1.event_id = %s"
        cursor = connection.cursor()
        cursor.execute(query, eid)
        result_list = []
        for row in cursor.fetchall():
            result_list.append(row[0])
        return result_list

    def get_user_records(self,user_id):
        return [dict(event_id=row.event_id,
                    date=row.date, )
                for row in self.defer("user_id").filter(user_id=user_id)]
