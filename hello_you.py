# Pergunta o nome do usuário

name = input("Qual o seu nome?: ")
print(name)

# Pergunta a idade do usuário

age = input("Qual a sua idade?: ")

# Pergunta a cidade onde o usário mora

city = input("Onde você mora?: ")

# Pergunta o que o usário gosta

love = input("O que você gosta de fazer?: ")

# Cria o output text

string = "Seu nome é {} e você tem {} anos. Você mora em {} e gosta de {}"
output = string.format(name, age, city, love)

# Print do output na tela

print(output)