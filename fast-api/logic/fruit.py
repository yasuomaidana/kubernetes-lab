from random import choices

FRUITS = (
    "apple",
    "banana",
    "cherry",
    "durian",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "jackfruit",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "pear",
    "quince",
    "raspberry",
    "strawberry",
    "tomato",
    "watermelon",
)


def get_fruit():
    """Get a random fruit from a list of fruits"""
    return choices(FRUITS)[0]
