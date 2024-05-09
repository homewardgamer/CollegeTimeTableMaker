from .models import User, College, Faculties
import random

#generate a unique random id for a registering user
def generate_random_id():
    random_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_id_length = 8
    for y in range(random_id_length):
        random_id += characters[random.randint(0, len(characters)-1)]
    checkord = User.objects.filter(randomid=random_id).count()
    if checkord > 0:
        generate_random_id()
    return random_id

#generate a unique random id for a adding college
def generate_random_id_forcollege():
    random_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_id_length = 8
    for y in range(random_id_length):
        random_id += characters[random.randint(0, len(characters)-1)]
    checkord = College.objects.filter(randomid=random_id).count()
    if checkord > 0:
        generate_random_id_forcollege()
    return random_id

#generate a unique random id for a adding faculty
def generate_random_id_forfaculty():
    random_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_id_length = 8
    for y in range(random_id_length):
        random_id += characters[random.randint(0, len(characters)-1)]
    checkord = Faculties.objects.filter(randomid=random_id).count()
    if checkord > 0:
        generate_random_id_forfaculty()
    return random_id