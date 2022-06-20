"""Assigment:
    Read a string from the user.

    If the string is CAT, say "Meow".
    If the string is DOG, say "Woof". 
"""    
animal = input("Escolha entre Cachorro e Gato: ")

if animal == "Cachorro":
    print("Woof")
elif animal == "Gato":
    print("Meow")
else:
    print("Você deveria ter escolhido entre cachorro e gato")