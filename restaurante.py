class Restaurante:
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
       return f'{self.nome} | {self.categoria}'

restaurante_praça = Restaurante('praça','gourmet')
restaurante_pizza = Restaurante('pizza','italiana')

restaurantes = [restaurante_pizza,restaurante_praça]

print( restaurante_praça)
print(restaurante_pizza)
