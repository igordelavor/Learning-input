def frequencia_de_caracteres():
    name = str(input("Digite a string: "))
    all_freq = {}
    for i in name:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print ("Frequencia de caracterres :\n "+  str(all_freq))
frequencia_de_caracteres()