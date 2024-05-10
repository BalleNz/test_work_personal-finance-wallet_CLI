from database_operations import Database
import datetime


# id, date, category, sum, annotation
class Operations():
    def __init__(self, database: Database):
        self.__database = database

    def get_balance_and_records(self):
        balance = 0
        rows = self.__database.read()
        for row in rows:  # fetch records
            if row["category"] == "Прибыль":
                balance += int(row["sum"])

            elif row["category"] == "Расход":
                balance -= int(row["sum"])

            print(' '.join(row.values()), end="")

        print('\n')
        print(f"Ваш баланс: {balance}\n")

    def push_record(self, record_category: str, record_sum: str, record_annotation: str):
        record_id = str(int(self.__database.read().pop()["id"]) + 1)  # get last id + 1
        record_date = datetime.date.today().isoformat()

        row = record_id + " " + record_date + " " + record_category + " " + record_sum + " " + record_annotation
        self.__database.write(row)

    def edit_record(self, record_id: str, record_category: str, record_sum: str, record_annotation: str):
        record_date = datetime.date.today().isoformat()

        row = record_id + " " + record_date + " " + record_category + " " + record_sum + " " + record_annotation
        self.__database.rewrite(record_id, row)

    def search_records(self, record_category: str, record_sum: str, record_date: str):
        rows = self.__database.read()
        for row in rows:
            if record_category:
                if not row["category"] == record_category:
                    continue
            if record_sum:
                if not row["sum"] == record_sum:
                    continue
            if record_date:
                if not row["date"] == record_date:
                    continue
            print(' '.join(row.values()), end="")
        print('\n')