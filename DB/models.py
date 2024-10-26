import enum

from sqlalchemy import (
    Integer, String, Enum, Boolean,
    ForeignKey, Text, BigInteger,
)
from sqlalchemy.orm import relationship, validates, mapped_column

from .database import Base


class RoleEnum(enum.Enum):
    ADMIN = 'ADMIN'
    OPERATOR = 'OPERATOR'
    USER = 'USER'


class Status(Base):
    ...


class User(Base):
    username = mapped_column(String)
    tgid = mapped_column(BigInteger, unique=True, index=True)
    role = mapped_column(Enum(RoleEnum), nullable=False, default=RoleEnum.USER)
    is_active = mapped_column(Boolean)

    # Связи с задачами (связь один-ко-многим с Task)
    tasks = relationship(
        'Task',
        back_populates='owner',
        foreign_keys='Task.user_id',
    )  # Владелец задач
    tasks_as_operator = relationship(
        'Task',
        back_populates='operator',
        foreign_keys='Task.operator_id',
    )  # Задачи, где пользователь оператор
    tasks_updated = relationship(
        'Task',
        back_populates='last_modified_by',
        foreign_keys='Task.last_updated_by_id',
    )  # Задачи, которые обновил

    def __repr__(self):
        # Получаем все атрибуты объекта и их значения
        fields = ', '.join(
            f"{key}={value!r}" for key, value in vars(self).items())
        return f"<{self.__class__.__name__}({fields})>"


class Task(Base):
    task_number = mapped_column(Integer, nullable=False)
    user_id = mapped_column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
    )  # Ссылка на владельца заявки
    operator_id = mapped_column(Integer, ForeignKey('user.id'), nullable=True)  # Ссылка на оператора
    last_updated_by_id = mapped_column(
        Integer,
        ForeignKey('user.id'),
        nullable=True,
    )  # Ссылка на пользователя, который обновил статус
    status = mapped_column(Integer, ForeignKey('status.id'), nullable=False)
    description = mapped_column(Text, nullable=True)  # Описание заявки

    # Связи
    operator = relationship(
        'User',
        back_populates='tasks_as_operator',
        foreign_keys=[operator_id],
    )  # Оператор, исполняющий задачу
    owner = relationship(
        'User',
        back_populates='tasks',
        foreign_keys=[user_id],
    )  # Владелец задачи
    last_modified_by = relationship(
        'User',
        back_populates='tasks_updated',
        foreign_keys=[last_updated_by_id],
    )  # Обновивший задачу


    @validates('task_number')
    def validate_task_number(self, key, task_number):
        # Получаем все задачи текущего пользователя
        user_tasks = self.owner.tasks
        # Если у пользователя уже есть задачи, находим максимальный номер
        if user_tasks:
            max_task_number = max(task.task_number for task in user_tasks)
            # Увеличиваем номер задачи на 1
            return max_task_number + 1
        return 1  # Если задач нет, начинаем с 1

    def __repr__(self):
        return (
            f'Задача № {self.task_number} (название: {self.name}) '
            f'создана: {self.created_at.strftime("%Y-%m-%d %H:%M:%S")} '
            f'пользователем: {self.owner.username} - '
            f'оператор: '
            f'{self.operator.username if self.operator else "не назначен"} - '
            f'текущий статус: {self.status}'
        )
