import random

def select_race():
    races = [
        'Redguard', 'Khajhit', 'Bosmer', 'High elf', 'Nord', 'Imperial',

    ]
    return races[random.randint(0, (len(races) - 1))]
