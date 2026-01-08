n1 =int(input('Digite um número: '))

print('Analisando o numero {}{}{}, o seu antecessor é {}{}{}, e o seu sucessor é {}{}{}'.format('\033[31m',n1,'\033[m','\033[32m',(n1-1),'\033[m', '\033[35m',(n1+1),'\033[m'))