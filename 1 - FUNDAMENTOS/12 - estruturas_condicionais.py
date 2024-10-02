# if, elif e else:
# -----------------------------

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe sua idade: "))

# 1° Forma:

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar a CHN.")

# if idade < MAIOR_IDADE:
#     print("Ainda não pode tirar CNH.")


# 2° Forma:

# if idade >= MAIOR_IDADE:
#     print("Maior de idade, pode tirar a CHN.")

# else:
#     print("Ainda não pode tirar CNH.")


# 3° Forma:

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

elif idade == IDADE_ESPECIAL:
    print("Pode realizar aulas teóricas, mas não aulas práticas.")

else:
    print("Ainda não pode tirar CNH.")



