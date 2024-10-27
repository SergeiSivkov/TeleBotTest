import os
import json

users_db = None
tasks_db = None


class DBEmulator:
    def __init__(self, class_name):
        self.class_name = class_name
        self.db_file = f'{self.class_name}.json'
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file)

    def insert(self, **kwargs):
        # Генерация id на основе длины словаря
        new_id = len(self.data) + 1
        record = {'id': new_id}
        record.update(kwargs)  # Добавляем остальные поля динамически
        self.data[new_id] = record
        self.save_data()
        return record

    def get(self, record_id):
        return self.data.get(record_id)

    def get_tgid(self, user_id):
        return self.data.get(user_id)

    def update(self, record_id, **kwargs):
        if record_id in self.data:
            self.data[record_id].update(kwargs)
            self.save_data()
            return self.data[record_id]
        else:
            return None

    def delete(self, record_id):
        if record_id in self.data:
            del self.data[record_id]
            self.save_data()

    def all(self):
        return list(self.data.values())

def create_DB ():
    global users_db, tasks_db
    users_db = DBEmulator("users")
    ''' id | task_id | name | status |'''

    tasks_db = DBEmulator("tasks")
    ''' id | user_id | name | block | date_reg | role |'''

    print("Базы данных инициализированы")

