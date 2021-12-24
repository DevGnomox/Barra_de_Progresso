from tqdm import tqdm
import time

for i in tqdm(range(10)):
    time.sleep(1)

lista = [1, 2, 3, 10, 15]

for item in tqdm(lista):
    time.sleep(1)

with tqdm(total=100) as barra_progresso:
    for i in range(10):
        time.sleep(1)
        barra_progresso.update(10)

