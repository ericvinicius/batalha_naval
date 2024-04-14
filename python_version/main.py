from src import input_validator

print("Jogo em desenvolvimento!")

size = input("digite o tamanho do tabuleiro (Ex: 2x3) -> ")  
height, width = input_validator.validate_size(size)


print(f"Altura: {height}")
print(f"Largura: {width}")


