class DadosPessoais:
    def __init__(self):
        self.nome = None
        self.idade = 0
        self.local_nascimento = None

    def entradadados(self):
        print('***** INSIRA SEUS DADOS PESSOAIS *****')
        self.nome = input('Informe o seu nome: ')
        self.idade = int(input('Informe a sua idade: '))
        self.local_nascimento = input('Informe seu local de nascimento: ')

    def teste_idade(self):
        if self.idade >= 18:
            print('Essa pessoa é maior de idade')
        else:
            print('Essa pessoa é menor de idade')

    def formulario(self):
        print('**** DADOS FORNECIDOS ****')
        print(f'NOME: {self.nome}\nIDADE: {self.idade} anos\nLOCAL DE NASCIMENTO: {self.local_nascimento}')


p1 = DadosPessoais()
p1.entradadados()
p1.formulario()
p1.teste_idade()
