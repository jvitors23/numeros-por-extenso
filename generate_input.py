import random


with open('input.txt', 'a') as f:
    for i in range(1000):
        number_size = random.randint(0, 9)
        random_number = random.random()*(10**number_size - 0)
        f.write('{:.2f}\n'.format(random_number).replace('.', ','))
