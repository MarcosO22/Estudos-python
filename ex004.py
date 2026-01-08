

a = input('digite algo = ')
def cor  (valor):
    verde = '\033[32m'
    vermelho = '\033[31m'
    reset = '\033[0m'
    return  f"{verde}Verdadeiro{reset}" if valor else  f"{vermelho}Falso{reset}"
print('o tipo primitivo e ', type (a))
print('Só tem espaços? ',cor( a.isspace()))
print('e um numero? ',cor(  a.isnumeric()))
print('e alfabetico? ',cor(  a.isalpha()))
print('e alfanumerico? ',cor(  a.isalnum()))
print('e maiuscula? ',cor(  a.isupper()))
print('Esta em minuscula? ',cor(  a.islower()))
print("esta capitalizada? ",cor(a.istitle()))
print('nao sei ', cor( a.isdigit()))
print('o que e =', cor( a.isdecimal()))
