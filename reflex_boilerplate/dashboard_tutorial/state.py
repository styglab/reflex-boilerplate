import reflex as rx
from collections import Counter

from .schema import User

class State(rx.State):
    users: list[User] = [
        User(
            name="Danilo Sousa",
            email="danilo@example.com",
            gender="Male",
        ),
        User(
            name="Zahra Ambessa",
            email="zahra@example.com",
            gender="Female",
        ),
    ]
    users_for_graph: list[dict] = []
    
    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()
    
    def transform_data(self):
        gender_counts = Counter(
            user.gender for user in self.users
        )
        
        self.users_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]

