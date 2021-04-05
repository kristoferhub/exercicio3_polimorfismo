"""
- Nome: Kristofer R.K
Trabalho 2:
- Polimorfismo

"""
# Classe Veiculo:

class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def imprimirInformacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Quantidade de Rodas: {self.qtdRodas}')
        print(f'Modelo: {self.modelo}')
        print(f'Velocidade: {self.velocidade}')
        
    def acelerar(self, valor):
        self.velocidade =  self.velocidade + valor
        return('Acelerou')

    def frear(self, valor):
        self.velocidade =  self.velocidade - valor
        return('Freiou')

# Classe Bicicleta:

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f'Número de Marchas: {self.numMarchas}')
        print(f'Bagageiro: {self.bagageiro}')


# Classe Automovel:

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f'Potência do Motor: {self.potenciaDoMotor}')
        
        

# Classe Moto:

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.partidaEletrica = partidaEletrica
        
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print(f'Partida Elétrica: {self.partidaEletrica}')


# Classe Carro

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.qtdPortas = qtdPortas
        
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print(f'Quantidade de Portas: {self.qtdPortas}')



# TESTES !!!!

#Bike:

bike = Bicicleta('Fisher', 2, 'Fisher runing', 6, 'Não')
print(bike.acelerar(15))
print(bike.frear(3))
bike.imprimirInformacoes()

print('')

# Moto:

moto = Moto('Yamaha', 2, 'MT-09', '10.50 CV', 'Sim')
print(moto.acelerar(60))
print(moto.frear(10))
moto.imprimirInformacoes()

print('')

# Carro:

carro = Carro('Fiat', 4, 'Palio Adventure', '130 CV', 4)
print(carro.acelerar(100))
print(carro.frear(20))
carro.imprimirInformacoes()

        
