from dataclasses import dataclass


@dataclass
class auth_param:
    username: str
    password: str


@dataclass
class time_interval:
    begin: int
    end: int
