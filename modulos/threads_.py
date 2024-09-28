from time import sleep
from threading import Thread
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        print(f'executando isso {self.tempo}')
        print(f'')
        sleep(self.tempo)
        print(self.texto)


"""t1 = MeuThread('Thread 1', 5)
t1.start()
t2 = MeuThread('Thread 2', 3)
t2.start()
t3 = MeuThread('Thread 3', 8)
t3.start()

for i in range(20):
    print(i)
    sleep(0.5)"""

def vai_demorar(texto,tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('hello world', 5))
t.start()
for i in range(20):
    print(i)
    sleep(0.5)