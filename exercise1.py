cadena_digitos_str = input("Ingresa la cadena de digitos:  ")
number_sequence = []

suma_total = 0
try:
    for i in cadena_digitos_str:
        number_sequence.append(int(i))

    for i_out in number_sequence:
        veces_repeticion = number_sequence.count(i_out)
        if veces_repeticion > 1:

            for i in range(0,veces_repeticion):
                if veces_repeticion>2:
                    suma_total += i_out
                number_sequence.remove(i_out)
            suma_total += i_out
            
    print(f"Suma Total {suma_total}")
except:
    print("En algun lado no ingresaste un número")        

    