def decimal_to_roman(num):
    if not (0 < num < 4000):
        raise ValueError("Numero fuera de rango, debe estar entre el 1 y el 3999")
    
    val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    simb = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    num_rom = ""
    i = 0
    while num > 0:
        count = num // val[i]
        num_rom += simb[i] * count
        num -= val[i] * count
        i += 1
    return num_rom

