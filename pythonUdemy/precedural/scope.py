 
def is_prime(num):
    if num <=1:
        return False
    if num <=3:
        return True
    if num%2==0 or num%3==0:
        return False
    return True
     
result=is_prime(1)
if result:
    print("c'est un nombre premier :",result)
else:
    print("le nombre n'est pas premier: ",result)