        #clubs (♧), diamonds (♢), hearts (♥) and spades (♤)
cartas_validas = ['As', 'Ah', 'Ad', 'Ac',
                  'Ks', 'Kh', 'Kd', 'Kc',
                  'Qs', 'Qh', 'Qd', 'Qc',
                  'Js', 'Jh', 'Jd', 'Jc',
                  'Ts', 'Th', 'Td', 'Tc',
                  '9s', '9h', '9d', '9c',
                  '8s', '8h', '8d', '8c',
                  '7s', '7h', '7d', '7c',
                  '6s', '6h', '6d', '6c',
                  '5s', '5h', '5d', '5c',
                  '4s', '4h', '4d', '4c',
                  '3s', '3h', '3d', '3c',
                  '2s', '2h', '2d', '2c']

def mi_funcion():

    bb = int(input("ingrese su cantidad de bb: "))
    cartas = list(input("Ingrese las cartas (de mayor a menor, separadas por un espacio): ").split())
    stack_ft = int(input("Ingrese el valor de stack_ft: "))
    posicion = str(input("¿Qué posición tienes (bb/sb/btn): "))
    rivales = int(input("Ingrese cantidad de rivales: "))
    fish = bool(input("¿Es pro? (True/False): "))

    if cartas[0][1] == cartas[1][1]:
        suited = True

    if cartas[0] and cartas[1] in cartas_validas:
        if rivales == 1:
            posicion_rival = str(input("¿Qué posición tiene tu rival? (bb/sb/btn): "))

            if posicion_rival == "bb" and posicion == "sb":

                if bb in [20,21,22,23,24,25]:

                    if cartas[0][0] == "A" and cartas[1][0] == "A":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "K":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "7" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "6" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "5" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "4" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "3" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "2" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] == "K":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "9" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "Q" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "J" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "T" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "9" and cartas[1][0] == "9":
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "8" and cartas[1][0] == "8":
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "7" and cartas[1][0] == "7":
                        return print("Raise 3x")
                    elif cartas[0][0] == "7" and cartas[1][0] == "2":
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "6" and cartas[1][0] == "6":
                        return print("All-in")

                    elif cartas[0][0] == "5" and cartas[1][0] == "5":
                        return print("All-in")

                    elif cartas[0][0] == "4" and cartas[1][0] == "4":
                        return print("All-in")

                    elif cartas[0][0] == "3" and cartas[1][0] == "3":
                        return print("All-in")

                    elif cartas[0][0] == "2" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    else:
                        return print("Check")
                
                if bb in [14,15,16,17,18,19]:

                    if cartas[0][0] == "A" and cartas[1][0] == "A":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "K" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==True:
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "A" and cartas[1][0] == "K" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "7":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "6":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "5":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "4":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "3":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] == "K":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "9" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "Q" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "J" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "T" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "9" and cartas[1][0] == "9":
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "8" and cartas[1][0] == "8":
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "7" and cartas[1][0] == "7":
                        return print("Raise 3x")
                    elif cartas[0][0] == "7" and cartas[1][0] == "2":
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "6" and cartas[1][0] == "6":
                        return print("All-in")

                    elif cartas[0][0] == "5" and cartas[1][0] == "5":
                        return print("All-in")

                    elif cartas[0][0] == "4" and cartas[1][0] == "4":
                        return print("All-in")

                    elif cartas[0][0] == "3" and cartas[1][0] == "3":
                        return print("All-in")

                    elif cartas[0][0] == "2" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    else:
                        return print("Check")

                if bb in [9,10,11,12,13]:

                    if cartas[0][0] == "A" and cartas[1][0] == "A":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "K" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==True:
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "A" and cartas[1][0] == "K" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "7":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "6":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "5":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "4":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "3":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] == "K":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "J" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "9" and suited==True:
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] == "J" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "T" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "9" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "8" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "7" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "6" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "5" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "4":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "3":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "2":
                        return print("All-in")

                    elif cartas[0][0] == "Q" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "J" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "T" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "9" and cartas[1][0] == "9":
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "8" and cartas[1][0] == "8":
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "7" and cartas[1][0] == "7":
                        return print("Raise 3x")
                    elif cartas[0][0] == "7" and cartas[1][0] == "2":
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "6" and cartas[1][0] == "6":
                        return print("All-in")

                    elif cartas[0][0] == "5" and cartas[1][0] == "5":
                        return print("All-in")

                    elif cartas[0][0] == "4" and cartas[1][0] == "4":
                        return print("All-in")

                    elif cartas[0][0] == "3" and cartas[1][0] == "3":
                        return print("All-in")

                    elif cartas[0][0] == "2" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    else:
                        return print("Check")
                    
                if bb in [7,8]:

                    if cartas[0][0] == "A" and cartas[1][0] == "A":
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "K" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==True:
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "A" and cartas[1][0] == "K" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "Q" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "J" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "T" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "9" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "8" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "7":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "6":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "5":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "4":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "3":
                        return print("All-in")
                    elif cartas[0][0] == "A" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] == "K":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "J" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "9" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "K" and cartas[1][0] == "8" and suited==True
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] == "J" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "T" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "9" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "8" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "7":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "6":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "5":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "4":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "3":
                        return print("All-in")
                    elif cartas[0][0] == "K" and cartas[1][0] == "2":
                        return print("All-in")

                    elif cartas[0][0] == "Q" and cartas[1][0] == "Q":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "5" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "4" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "3" and suited==False:
                        return print("All-in")
                    elif cartas[0][0] == "Q" and cartas[1][0] == "2" and suited==False:
                        return print("All-in")

                    elif cartas[0][0] == "J" and cartas[1][0] == "J":
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "T" and suited==True:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "5" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "J" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "T" and cartas[1][0] == "T":
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "T" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "9" and cartas[1][0] == "9":
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "4" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "9" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "8" and cartas[1][0] == "8":
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "3" and suited==False:
                        return print("Raise 3x")
                    elif cartas[0][0] == "8" and cartas[1][0] == "2" and suited==False:
                        return print("Raise 3x")

                    elif cartas[0][0] == "7" and cartas[1][0] == "7":
                        return print("Raise 3x")
                    elif cartas[0][0] == "7" and cartas[1][0] == "2":
                        return print("Raise 3x")
                    
                    elif cartas[0][0] == "6" and cartas[1][0] == "6":
                        return print("All-in")

                    elif cartas[0][0] == "5" and cartas[1][0] == "5":
                        return print("All-in")

                    elif cartas[0][0] == "4" and cartas[1][0] == "4":
                        return print("All-in")

                    elif cartas[0][0] == "3" and cartas[1][0] == "3":
                        return print("All-in")

                    elif cartas[0][0] == "2" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    else:
                        return print("Check")

                if bb in [6,5,4,3,2,1]:

                    if cartas[0][0] == "A" and cartas[1][0] != "A":
                        return print("All-in")
                    
                    elif cartas[0][0] == "K" and cartas[1][0] != "K":
                        return print("All-in")
                    
                    elif cartas[0][0] == "Q" and cartas[1][0] != "Q":
                        return print("All-in")
                    
                    elif cartas[0][0] == "J" and cartas[1][0] == "T" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "J" and cartas[1][0] == "9" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "T" and cartas[1][0] == "T":
                        return print("All-in")
                    elif cartas[0][0] == "T" and cartas[1][0] == "9" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "T" and cartas[1][0] == "8" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "9" and cartas[1][0] == "9":
                        return print("All-in")
                    elif cartas[0][0] == "9" and cartas[1][0] == "8" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "9" and cartas[1][0] == "7" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "8" and cartas[1][0] == "8":
                        return print("All-in")
                    elif cartas[0][0] == "8" and cartas[1][0] == "7" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "8" and cartas[1][0] == "6" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "7" and cartas[1][0] == "7":
                        return print("All-in")
                    elif cartas[0][0] == "7" and cartas[1][0] == "6" and suited==True:
                        return print("All-in")
                    elif cartas[0][0] == "7" and cartas[1][0] == "5" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "6" and cartas[1][0] == "6":
                        return print("All-in")
                    elif cartas[0][0] == "6" and cartas[1][0] == "5" and suited==True:
                        return print("All-in")
                    
                    elif cartas[0][0] == "5" and cartas[1][0] == "5":
                        return print("All-in")
                    elif cartas[0][0] == "4" and cartas[1][0] == "4":
                        return print("All-in")
                    elif cartas[0][0] == "3" and cartas[1][0] == "3":
                        return print("All-in")
                    elif cartas[0][0] == "2" and cartas[1][0] == "2":
                        return print("All-in")
                    
                    else:
                        return("Check")
                    
            elif posicion_rival == "sb":
                print("fold")
            elif posicion_rival == "btn":
                print("fold")

        elif rivales == 2:
            print("call")

    # Ejemplo de devolución de resultados
    return cartas, suited, stack_ft, posicion, rivales, fish

# Llamar a la función para probarla
resultado = mi_funcion()
print(resultado)

