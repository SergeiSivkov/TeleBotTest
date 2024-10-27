from faker import Faker
import random

from sqlalchemy import select

from . import async_session
# Импортируйте ваши модели
from .models import User, Status, Task  # Предполагается, что эти модели уже
# определены

# Создание объекта Faker
fake = Faker()


async def populate_tasks(num_tasks: int):
    # Получаем существующих пользователей и статусы
    async with async_session() as session:

        result_users = await session.execute(select(User))
        users = result_users.scalars().all()

        result_statuses = await session.execute(select(Status))
        statuses = result_statuses.scalars().all()

        tasks = await session.execute(select(Task))
        tasks = tasks.scalars().all()
    
        if not users or not statuses:
            print(
                'Необходимо создать пользователей  и статусы перед '
                'заполнением задач.',
            )
            return
        elif len(tasks) > 0:
            print(f'Таблица задачь уже содержит сведения {tasks}')
            return
    
        for i in range(num_tasks):
            # Генерация случайных данных
            description = fake.sentence(
                nb_words=6)  # Генерация случайного описания задачи
            user = random.choice(users)  # Случайный пользователь
            status = random.choice(statuses)  # Случайный статус

            # Создание новой задачи
            new_task = Task(
                name=fake.sentence(nb_words=3),
                task_number=i,  # Устанавливаем номер задачи
                user_id=user.id,  # Владелец задачи
                operator_id=random.choice(
                    users).id if random.random() > 0.5 else None,
                # Случайный оператор (может быть None)
                last_updated_by_id=user.id,
                # Предполагаем, что задача обновлена владельцем
                status=status.id,  # Статус задачи
                description=description  # Описание задачи
            )
    
            # Параметр task_number будет вычислен автоматически через валидатор
            session.add(new_task)
            # Сохранение изменений в базе данных
        await session.commit()

        print(f'{num_tasks} задач(и) успешно добавлено в таблицу Task.')

