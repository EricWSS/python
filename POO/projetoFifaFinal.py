class Time:
    def __init__(self, nome, cidade, mascote):
        self.nome = nome
        self.cidade = cidade
        self.mascote = mascote

#Forma tradicional
class Jogador(Time):
    def __init__(self, nome, cidade, mascote, nome_jogador, nome_time, numero_camisa):
        super().__init__(nome, cidade, mascote)  
        self.nome_jogador = nome_jogador
        self.numero_camisa = numero_camisa

#Forma contraída
class Jogador(Time):
    def __init__(self, nome_jogador, nome_time, numero_camisa):
        super().__init__(nome_time, None, None)  
        self.nome_jogador = nome_jogador
        self.numero_camisa = numero_camisa


meu_time = Time("Time A", "Cidade A", "Mascote A")

# Forma tradicional
meu_jogador = Jogador("Time A", "Cidade A", "Mascote A","Jogador 1", "Time A", 10) 
# Forma contraída
meu_jogador1 = Jogador("Jogador 1", meu_time.nome, 10) 
print(meu_jogador.__dict__)
print(meu_jogador1.__dict__)



class Tecnico(Time):
    def __init__(self, nome_tecnico, nome_time, esquema_tatico):
        # Chamando o construtor da classe pai (Time)
        super().__init__(nome_time, None, None)

        # Adicionando informações específicas do técnico
        self.nome_tecnico = nome_tecnico
        self.esquema_tatico = esquema_tatico

    def dar_coletiva(self):
        return f"O técnico {self.nome_tecnico} está dando uma coletiva de imprensa. Esquema tático: {self.esquema_tatico}"



class Auxiliar(Time):
    def __init__(self, nome_auxiliar, nome_time):
        # Chamando o construtor da classe pai (Time)
        super().__init__(nome_time, None, None)

        # Adicionando informações específicas do auxiliar
        self.nome_auxiliar = nome_auxiliar

    def dar_coletiva(self):
        return f"O auxiliar {self.nome_auxiliar} está dando uma coletiva de imprensa."


class PreparadorFisico(Time):
    def __init__(self, nome_preparador, nome_time, parte_elenco):
        # Chamando o construtor da classe pai (Time)
        super().__init__(nome_time, None, None)

        # Adicionando informações específicas do preparador físico
        self.nome_preparador = nome_preparador
        self.parte_elenco = parte_elenco

    def dar_coletiva(self):
        return f"O preparador físico {self.nome_preparador} está dando uma coletiva de imprensa. Parte do elenco: {self.parte_elenco}"
