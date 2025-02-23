class Heroi:
    def __init__(self, nome, idade, tipo, level):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.level = level

    def atacar(self):
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken",
            "rogue": "adagas"
        }
        ataque = ataques.get(self.tipo.lower(), "um ataque desconhecido")
        print(f"O {self.tipo} atacou usando {ataque}.")


# Exemplo de uso
heroi1 = Heroi("Merlin", 150, "mago", 50)
heroi2 = Heroi("Arthur", 30, "guerreiro", 51)
heroi3 = Heroi("Backstabber", 33, "rogue", 60)

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()