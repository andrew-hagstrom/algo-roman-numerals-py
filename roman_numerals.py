def to_roman(num):
    output = ""
    print(output)
    roman_map = {
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1,}
    
    for ltr in roman_map: 
        times = num // roman_map[ltr]
        if times >= 1:
            for i in range(times):
                output += ltr
                num -= roman_map[ltr]
        else: 
            continue 
    print(output)
    return output
to_roman(9)
to_roman(4)


def to_roman(num):
    output=""
    roman_map = { 
        'M': 1000,
        'CM': 900, 
        'D': 500, 
        'CD': 400, 
        'C': 100, 
        'L': 50, 
        'XL': 40, 
        'X': 10, 
        'IX': 9, 
        'V': 5, 
        'IV': 4, 
        'I': 1,
    }
   
    for ltr in roman_map: 
        times = num // roman_map[ltr]
        if times >= 1:
            for i in range(times):
                output += ltr
                num -= roman_map[ltr]
        else: 
            continue 
    print(output)
    return output 
to_roman(944)
to_roman(44)
to_roman(14)
to_roman(9)
to_roman(4)
            
