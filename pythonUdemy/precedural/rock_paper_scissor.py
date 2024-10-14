import random

choices = ['rock', 'paper', 'scissors']

while True:
    # Choix aléatoire de l'ordinateur
    computer_choice = random.choice(choices)

    # Entrée de l'utilisateur
    user_input = input("Votre choix (rock, paper, scissors) ou 'quit' pour arrêter : ").strip().lower()

    if user_input == 'quit':
        print("Merci d'avoir joué ! À bientôt.")
        break

    if user_input not in choices:
        print("Choix invalide. Veuillez réessayer.\n")
        continue

    print(f"Vous avez choisi : {user_input}")
    print(f"L'ordinateur a choisi : {computer_choice}")

    if user_input == computer_choice:
        print("Résultat : Match nul !\n")
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'paper' and computer_choice == 'rock') or \
         (user_input == 'scissors' and computer_choice == 'paper'):
        print("Résultat : BRAVO! Vous avez gagné !\n")
    else:
        print("Résultat : Dommage! Vous avez perdu est l'odinateur a gagner.\n")