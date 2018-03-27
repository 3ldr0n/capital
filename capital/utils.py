import random

def select_race():
    races = [
        'Redguard', 'Khajhit', 'Bosmer', 'Altmer', 'Nord', 'Imperial',
        'Argonian', 'Breton', 'Dunmer', 'Orsimer'
    ]
    return races[random.randint(0, (len(races) - 1))]
