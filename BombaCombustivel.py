class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {round(litros_abastecidos,2)} litros de {self.tipo_combustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Valor a ser pago: R${round(valor_pagar,2)}")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade



bomba = BombaCombustivel("Gasolina", 5.50, 1000)

bomba.abastecer_por_valor(50)  
bomba.abastecer_por_litro(10)  
bomba.alterar_valor(6.00)  
bomba.alterar_combustivel("Etanol")  
bomba.alterar_quantidade_combustivel(1500)  

print(f"Tipo de Combustível: {bomba.tipo_combustivel}")
print(f"Valor por Litro: R${bomba.valor_litro}")
print(f"Quantidade de Combustível: {bomba.quantidade_combustivel} litros")
