# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 23:41:18 2022

@author: Juan Elier Rosales Rosas
@version: 1.0
@Empresa: Universidad Autonoma Metropolitana unidad Lerma

"""
import matplotlib.pyplot as plt
import numpy as np
import math

#Funcion para el seno
def seno(z):
    return np.sin(z)

#Lee el angulo y lo convierte a flotante
calculo = float(input("¿De qué angulo quieres calcular el seno? "))
#Convierte a radianes el angulo
radx = math.radians(calculo)
#Realiza el calculo del seno
i = np.sin(radx)
print(i)

#Parametros para la función seno
a=0
b = 2*np.pi
#Pone ciertos puntos dependiendo cuantos puntos quiera el usuario
puntos = float(input("Cada cuantos grados quieres poner un punto: "))
x =np.linspace(a,b,int(360/puntos+1))
y=np.linspace(a,b,1000)
f=seno(x)
J=seno(y)
#Grafica la función seno
plt.plot(y,J)
#Grafica los puntos
plt.plot(x,f,"o")
plt.grid(True)
