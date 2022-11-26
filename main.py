class Somatoria:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.resultado = 0

    def entrada(self):
        self.n1 = int(input('Digite o primeiro número: '))
        self.n2 = int(input('Digite o segundo numero: '))

    def soma(self):
        self.resultado = self.n1 + self.n2
        self.resultado = self.resultado

    def print_resultado(self):
        print(f'A soma de {self.n1} mais {self.n2} é igual a {self.resultado}')


teste = Somatoria()
teste.entrada()
teste.soma()
teste.print_resultado()

