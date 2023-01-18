cod_pais = "\n+55"
numeros = []

with open('telefones.txt', "r") as telefones:
    for telefone in telefones:
        with open('newfile.txt', 'a') as mod_file:
            numeros.append(telefone.replace("(", ""))
            numeros[0] = numeros[0].replace(")", "")
            numeros[0] = numeros[0].replace("-", "")
            numeros[0] = numeros[0].format(cod_pais)
            numeros[0] = "\n+55" + numeros[0]
            mod_file.write(numeros[0])
            mod_file.close()
            numeros.clear()
