

#Exercicio 1 - Classes e Objetos

class Pessoa: 

    def __init__ (self, nome, idade):

        self.nome = nome 
        self.idade = idade 

    def apresentar(self):

        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos.")

    def aniversario(self):

        self.idade += 1 
        print(f"Feliz aniversário {self.nome}, agora você tem {self.idade} anos!!.")

p1 = Pessoa("Ana", 25)
p2 = Pessoa("Carlos", 30)

p1.apresentar()
p1.aniversario()
p1.apresentar()

print("---")

p1.apresentar()
p1.aniversario()
p1.apresentar()

#Exercicio 2 - Classe ContaBancaria 

class ContaBancaria: 

    def __init__ (self, titular,saldo=0):

        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor): 
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else: 
            print("Valor de depósito inválido.")
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else: 
            print("Saldo insuficiente ou valor inválido para o saque.")

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")
print("\n--- Conta bancária do João ---")

conta_joao = ContaBancaria("João", 1000)   
conta_joao.exibir_saldo()

print(f"--- João depositou R$ 500,00 ---")

conta_joao.depositar(500)
conta_joao.exibir_saldo()

print(f"--- João sacou R$ 300,00 ---")

conta_joao.sacar(300)
conta_joao.exibir_saldo()

print(f"--- Saldo final de João ---")

conta_joao.exibir_saldo()

#Exercício 3 – Classe Retangulo
        
class Retangulo:

    def __init__(self, largura, altura):

        self.largura = largura
        self.altura = altura    
    
    def area(self):

        print(f"A área do retângulo é de: {self.largura * self.altura}")

    def perimetro(self):

        print(f"O perímetro do retângulo é de: {2 * (self.largura + self.altura)}")
    
print(f"\n--- Retângulo de largura 5 e altura 3. ---")

retangulo1 = Retangulo(5, 3)
retangulo1.area()
retangulo1.perimetro()


#Exercício 4 – Classe Aluno

class Aluno: 

    def __init__(self, nome, notas=None):
        self.nome = nome
        self.notas = notas if notas else []
        
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"Nota {nota} adicionada para {self.nome}")
        else:
            print(f"Nota Inválida! Deve estar entre 0 e 10.")
        
    def media(self):
        if len(self.notas) == 0:
            return 0 
        return sum(self.notas) / len(self.notas)

    def situacao(self): 
        media = self.media()
        if media >= 7:
            return "Aprovado"
        else: 
            return "Reprovado"
        
    def mostra_boletim(self): 
        media = self.media()
        situacao = self.situacao()
        print(f"--- Boletim de {self.nome} ---")
        print(f"Notas: {self.notas}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")

aluna_maria = Aluno("Maria")

print("\n--- Adicionando notas de Maria ---")
aluna_maria.adicionar_nota(8.0)
aluna_maria.adicionar_nota(6.5)
aluna_maria.adicionar_nota(7.5)

aluna_maria.mostra_boletim()

    

