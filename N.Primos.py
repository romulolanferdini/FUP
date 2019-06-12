numero = int (input ("Digite um númeror maior que 0: "))

divisor = 1
contador = 0

numero1 = (numero/2)

while (divisor <= numero):
   if (numero % divisor==0):
      print ("É divisivel por", divisor)
      divisor =+ 1
      contador =+ 1

   if (contador >= numero1):
      i = numero
      print ("É divisivel por", divisor)
      divisor =+1
      contador =+ 1

   else:
      divisor =+ 1
if(contador==2):
   print ("O número requisitado é primo!")

else:
   print ("Numero não é primo, possui", contador, "divisores")