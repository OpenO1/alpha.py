import math
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
bc = Back.CYAN


print(bc+"NOTE: ALPHA IS NOT MEANT FOR CODE PURPOSES.\nIT IS A 100% MATH MODULE USED TO SOLVE AND DO CALCULATIONS BY PUTTING VALUES IN THE () AS FUNCTION.\nOF COURSE YOU CAN STILL USE SOME OF THE FUNCTIONS IN YOUR CODE TO AVOID CODING IT/WINNING TIME.\nBUT REMIND THAT IT WASN'T MADE FOR THAT IN THE FIRST PLACE."+ Back.BLACK)


class Console:
    write = print




class pt:
    @staticmethod
    def of(value, percentage, sh):
        of= (percentage / 100) * value
        if sh == True:
            print(of) 
    @staticmethod
    def percent(eff, efftotal, sh):
        
        chance = eff/efftotal * 100
        if sh == True:
            print(f"{chance}% | ≈ {round(chance)}%")
            
    @staticmethod
    def percent_reverse(percentage, efftotal, sh):
        reverse = percentage * efftotal / 100
        if sh == True:
            print(f"{reverse} | ≈ {round(reverse)}")
        
         






class p2:

    @staticmethod
    def alpha(a, b, sh):
        div = 2 * a
        
        alpha = (-b)/div
        if sh == True:
            print("α:", alpha) 
    @staticmethod
    def beta(a, b, c, sh):
        div = 4 * a
        beta = (-(b)**2 + 4*a*c)/div
        if sh == True:
            print("β:", beta)
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
    def delta(a, b, c, sh):
        delta = (b)**2 - 4*a*c
        if sh == True:
            print(f"Δ: {delta}")
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
        alpha = -(b) / (2*a)
        if sh == True:
            print(f"x1 = x2 = α = {alpha}")


class maths:
    @staticmethod
    def pythagoras(a, b, c, sh):
        if c == False:
            c1 = a**2 + b**2
            c1 = math.sqrt(c1)
            if sh == True:
                print(c1)
        if b == False:
            b1 = c**2 - a**2
            b1 = math.sqrt(b1)
            if sh == True:
                print(b1)
        if a == False:
            a1 = c**2 - b**2
            a1 = math.sqrt(a1)
            if sh == True:
                print(a1)
    @staticmethod
    def pyth_schema():
        print("    /|")
        print("   / | ")
        print("C /  | B")
        print(" /___| ")
        print("   A   ")

    @staticmethod
    def add(value1, value2, sh):
        add = value1 + value2
        if sh == True:
            print(add)
    
    @staticmethod
    def sub(v1, v2, sh):
        sub = v1 - v2
        if sh == True:
            print(sub)

    @staticmethod
    def mul(v1, v2, sh):
        mul = v1 * v2
        if sh == True:
            print(mul)
    
    @staticmethod
    def div(v1, v2, sh):
        div = v1 / v2
        if sh == True:
            print(div)



    
    
def rand(a:int, b:int, sh):
    num = random.randint(a, b)
    if sh == True:
        print(num)




    

        