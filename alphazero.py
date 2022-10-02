import math
import random
import colorama
import random
from colorama import Fore, Back, Style
colorama.init()
bc = Back.CYAN

def init():
    print("alphazero.maths.XX => maths formulas")
    print("alphazero.ph.XX => physics / chemistry formulas")
    print("alphazero.p2.XX => 2° Polynomial (ax²+bx+c) formulas")
    print("alphazero.pt.XX => Percentages formulas")
    print("alphazero.XX => Other calculations/misc (e.g alphazero.rand(min, max)")
    print("alphazero.console.write("") => print")
    print("msg => input")

####################################################################################
#########################CONSOLE terminal###########################################
####################################################################################

class console:
    write = print

msg = input

####################################################################################
#########################POURCENTAGE###########################################
####################################################################################


class pt:
    @staticmethod
    def of(value, percentage):
        return (percentage / 100) * value
        
    @staticmethod
    def percent(eff, efftotal):
        
        return eff/efftotal * 100
        
            
    @staticmethod
    def percent_reverse(percentage, efftotal):
        return percentage * efftotal / 100
        
        
         
####################################################################################
#########################POLYNOME 2ND DEGREE###########################################
####################################################################################





class p2:

    @staticmethod
    def alpha(a, b):
        div = 2 * a
        
        return (-b)/div
        
    @staticmethod
    def beta(a, b, c):
        div = 4 * a
        return (-(b)**2 + 4*a*c)/div
        
    @staticmethod
    def cano(a, b, c, sh):
        diva = 2 * a
        alpha = (-b)/diva
        divb = 4 * a
        beta = (-(b)**2 + 4*a*c)/divb
        
        x = 'x'
        if sh == True:
            print(f"Input: {a}x² | {b}x | {c}")
            print(f"canonic form: {a}({x} - {alpha})² + {beta}")
    @staticmethod
    def delta(a, b, c):
        return (b)**2 - 4*a*c
        
    @staticmethod
    def dcheck(a, b, c, sh):
        delta = (b)**2 - 4*a*c
        if sh == True:
            if delta > 0:
                msg = "Δ > 0; Positive."
            if delta == 0:
                msg = "Δ = 0"     
            if delta < 0:
                msg = "Δ < 0; Negative."
            print(msg, delta)
            
            


    @staticmethod
    def dp(a, b, delta, sh):
        div = 2 * a
        if delta >= 0:
            x1 = (-(b)-math.sqrt(delta))/div # à corriger
            x2 = (-(b)+math.sqrt(delta))/div # idem
            if sh == True:
                print(f"x1: {x1} \nx2: {x2}")
    @staticmethod   
    def dnull(a, b, sh):
        return -(b) / (2*a)
        
####################################################################################
#########################MATH###########################################
####################################################################################

class maths:
    @staticmethod
    def v(distance, time):
        return distance/time
    @staticmethod
    def d(v, time):
        return v*time
    @staticmethod
    def t(distance, v):
        return distance/v

    @staticmethod
    def pythagoras(a, b, c):
        if c == False:
            c1 = a**2 + b**2
            c1 = math.sqrt(c1)
            return c1
        if b == False:
            b1 = c**2 - a**2
            b1 = math.sqrt(b1)
            return b1
        if a == False:
            a1 = c**2 - b**2
            a1 = math.sqrt(a1)
            return a1
    @staticmethod
    def pyth_schema():
        print("    /|")
        print("   / | ")
        print("C /  | B")
        print(" /___| ")
        print("   A   ")

    @staticmethod
    def add(value1, value2):
        return value1 + value2
        
    
    @staticmethod
    def sub(v1, v2):
        return v1 - v2
        
    @staticmethod
    def mul(v1, v2):
        return v1 * v2
       
    
    @staticmethod
    def div(v1, v2):
        return v1 / v2
        

     
####################################################################################
#########################PHYSIQUE CHIMIE###########################################
####################################################################################        

class phc:
    @staticmethod
    def rho(mass, volume):
        return mass / volume
    @staticmethod
    def mass(rho, volume):
        return rho * volume
    @staticmethod
    def volume(mass, rho):
        return mass / rho
    
    @staticmethod
    def mol(mass, MolarMass):
        return mass / MolarMass
    @staticmethod
    def mass(mol, MolarMass):
        return mol * MolarMass
    @staticmethod
    def MolarMass(mass, mol):
        return mass / mol
    



    
####################################################################################
#########################OTHER###########################################
####################################################################################

def rand(a:int, b:int):
    return random.randint(a, b)




    

        