from enum import Enum


class NamingCase(str, Enum):
    LOWER = "lower"
    UPPER = "upper"
    SNAKE = "snake"
    KEBAB = "kebab"
    TITLE = "title"
    CAMEL = "camel"
    PASCAL = "pascal"
