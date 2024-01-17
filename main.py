def pattern_generator(length):
    pattern = "htr"
    result = pattern * (length // 3) + pattern[:length % 3]
    return result

length = int(input("ingresa la longitud: "))
print(pattern_generator(length))
