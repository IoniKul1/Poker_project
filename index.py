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
    # Ingresar los parámetros mediante input
    cartas = str(input("Ingrese las cartas (de mayor a menor): "))
    suited = bool(input("¿Las cartas son del mismo palo? (True/False): "))
    stack_ft = int(input("Ingrese el valor de stack_ft: "))
    posicion = int(input("Ingrese el valor de posición: "))
    rivales = int(input("Ingrese el valor de los rivales: "))
    fish =  bool(input("¿Las cartas son del mismo palo? (True/False): "))

    #if (cartas in cartas_validas):
        #if(rivales = 1):
         #   posicion_rival = str(input("Que posición tiene tu rival: "))#bb= big blind, sb= small blind, btn= button
          #      if(posicion_rival == "bb"):
                    
           #     if(posicion_rival == "sb"):
                
            #    if(posicion_rival == "btn"):
                
        #if(rivales = 2)
    
    # Ejemplo de devolución de resultados
    return cartas, suited, stack_ft, posicion, rivales

# Llamar a la función para probarla
resultado = mi_funcion()
print(resultado)