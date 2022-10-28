# -*- coding: utf-8 -*-
"""Funcoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6AyEo-mm3H8rb4F8vRULUQxqzvgbYZf

Alunos: - Matheus da Silva Costa
        - Alexandre Davila Dias da Costa

1.	Receba o valor da hora, minutos e segundos e que retorne a quantidade de segundos existentes.
"""

def tempo(hora, minuto):
  hora = hora*3600
  minuto = minuto*60
  return (hora+minuto)

hora = int(input("Insira a hora: "))
minuto = int(input("Insira os minutos: "))
segundo = int(input("Insira os segundos: "))
print("Total de segundos: ", tempo(hora, minuto)+segundo)

"""2.	Receba o preço de um produto e um percentual de reajuste, e que retorne o novo preço do produto de acordo com o reajuste."""

def new(produto, reajuste):
  div = reajuste/100
  mult = produto*div
  novo = mult+produto
  return(novo)
produto = int(input("Insira o valor do produto: "))
reajuste = int(input("Insira a porcentagem do reajuste: "))
print("O novo valor do produto é: ",new(produto, reajuste))

"""3.	Receba dois números inteiros e que retorne a diferença entre o maior e o menor."""

def diferenca(numero1, numero2):
  if(numero1>=numero2):
    new = numero1-numero2
  elif(numero2>numero1):
    new = numero2-numero1
  return(new)

numero1 = int(input("Insira o valor do primeiro numero inteiro: "))
numero2 = int(input("Insira o valor do outro numero inteiro: "))
print("A diferença entre os números é: ", diferenca(numero1,numero2))

"""4.	Receba um número inteiro e que retorne True se o número for primo, e False, caso contrário."""

def load(numero):
  for i in range (2, numero):
    if (numero%i==0):
      return False
  return True
numero = int(input("Insira um numero inteiro para verificar se o mesmo é primo ou não: "))
load(numero)

"""5.	Receba dois números inteiros e que imprima todos os números primos no intervalo entre o primeiro e o segundo número (inclusive). Utilize a função anterior para verificar se um determinado número é primo."""

def primo(numero, numero2):
  for i in range (numero, numero2+1):
    if load(i):
      print(i)
numero = int(input("Insira o menor inteiro: "))
numero2 = int(input("Insira o maior inteiro: "))
primo(numero, numero2)

"""6.	Receba o sexo e idade de um cliente de uma determinada academia, e que retorne o valor da mensalidade a pagar, de acordo com a tabela"""

def valor(genero, idade):
  if genero == "m":
    if idade <= 15:
      print("Seu valor de mensalidade é R$60,00" )
    if idade <= 18 and idade>=16:
      print("Seu valor de mensalidade é R$75,00" )
    if idade <= 30 and idade>=19:
      print("Seu valor de mensalidade é R$90,00" )
    if idade <= 40 and idade>=31:
      print("Seu valor de mensalidade é R$85,00" )
    if idade > 40:
      print("Seu valor de mensalidade é R$80,00" )
  if genero == "f":
    if idade <= 15:
      print("Seu valor de mensalidade é R$60,00" )
    if idade <= 25 and idade>=19:
      print("Seu valor de mensalidade é R$90,00" )
    if idade <= 40 and idade>=26:
      print("Seu valor de mensalidade é R$90,00" )
    if idade > 40:
      print("Seu valor de mensalidade é R$85,00" )

genero = str(input("Insira m para masculino e f para feminino conforme seu gênero: "))
idade = int(input("Insira a sua idade: "))
valor(genero, idade)

"""7.	Receba dois números inteiros e que retorne como primeiro valor o menor, e como segundo valor, o maior entre eles."""

def verificar(numero, numero2):
  if numero>numero2:
    print(numero)
    print(numero2)
  elif numero2>numero:
    print(numero2)
    print(numero)
  else:
    print("Os numeros sao iguais")

numero = int(input("Insira um inteiro: "))
numero2 = int(input("Insira outro inteiro: "))
verificar(numero, numero2)

"""8.	Receba os coeficientes a,b e c de uma equação de segundo grau e que retorne as duas raízes da equação. Se não existirem raízes reais, retorne dois objetos nulos (None, None)"""

from math import sqrt
def equacao(a,b,c):
  delta = (b*b)-4*a*c
  if delta>0:
    raiz_a = (-b+sqrt(delta))/2*a
    raiz_b = (-b-sqrt(delta))/2*a
    print("Primeira raiz: ",raiz_a,"\n Segunda raiz: ", raiz_b)
  if delta<0:
    return (None, None)

a = int(input("Insira o coeficiente a: "))
b = int(input("Insira o coeficiente b: "))
c = int(input("Insira o coeficiente c: "))
equacao(a,b,c)

"""9.	Receba o peso e a altura de uma pessoa, e que retorne o seu IMC: 
IMC = peso/altura2

"""

def imc(peso, altura):
  return(peso/(altura*altura))

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc(peso, altura)

"""10.	Receba o peso e a altura de uma pessoa, e que retorne o seu IMC e a classificação do seu peso, de acordo com o seu IMC (utilize a função anterior para calcular o IMC): """

def classificacao(peso, altura):
  if imc(peso, altura)<20:
    print("Seu IMC é %.2f"%imc(peso, altura))
    print("abaixo do peso")
  elif imc(peso, altura)<25 and imc(peso, altura)>=20:
    print("Seu IMC é %.2f"%imc(peso, altura))
    print("Peso normal")
  elif imc(peso, altura)<30 and imc(peso, altura)>=25:
    print("Seu IMC é %.2f"%imc(peso, altura))
    print("Sobre Peso")
  elif imc(peso, altura)<40 and imc(peso, altura)>=30:
    print("Seu IMC é %.2f"%imc(peso, altura))
    print("Obeso")
  elif imc(peso, altura)>=40:
    print("Seu IMC é %.2f"%imc(peso, altura))
    print("Obeso Mórbido")

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
classificacao(peso, altura)