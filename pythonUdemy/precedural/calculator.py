
def addition(n1,n2):
    return n1+n2

def soustraction(n1,n2):
    if n1>n2:
        return n1-n2
    return n2-n1

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2==0:
        return None
    return n1/n2

calculatrice ={
    
        '+':addition,
        '*':multiplication,
        '-':soustraction,
        '/':division
    }

somme =0

while True:
    number =input("taper le nombre 1:\n")
    number2 =input("traper le second nombre:\n")
    
    if number.isdigit() and number2.isdigit():
        nbre =int(number)
        nbre2 =int(number2)
        
        signe_cal= input("donner le signe pour effectuer le calcul entre n1 et n2\n")
        
        if signe_cal in calculatrice :
                somme=calculatrice[signe_cal](nbre,nbre2)
        else:
            print("Opérateur invalide! Veuillez entrer +, -, *, ou /")
            continue
    else:
        print("Veuillez renseigner des chiffres numériques.")
        continue
    print(f"Le résultat est: {somme}")
    
    sorti_boucle =input("taper oui ou non \n")
    
    if sorti_boucle =='oui':
        continue
    else:
        break