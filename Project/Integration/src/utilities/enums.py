import enum


class TypeEvent(enum.Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    MESSAGE = 'MESSAGE'
    ADDED_TO_SPACE = 'ADDED_TO_SPACE'
    REMOVED_FROM_SPACE = 'REMOVED_FROM_SPACE'
    CARD_CLICKED = 'CARD_CLICKED'


class TypeSpace(enum.Enum):
    ROOM = 'ROOM'
    DM = 'DM'


class CardsButtons(enum.Enum):
    SELECT_MENU = 'selectMenu'


class Role(enum.Enum):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMINISTRATIVE = 'ADMINISTRATIVE'
