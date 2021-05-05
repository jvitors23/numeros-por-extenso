import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

translate_matrix = [
    ['', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove'],
    ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
        'sessenta', 'setenta', 'oitenta', 'noventa'],
    ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
        'seiscentos', 'setecentos', 'oitocentos', 'novecentos'],
    ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', ]
]


def get_string(number):
    """Dada uma string de um número de tamanho 3 XXX (centena, dezena e unidade. Com '0' a esquerda caso preciso)
        retorna a string do número escrito por extenso"""
    if type(number) != str or len(number) != 3:
        raise ValueError(
            "O argumento number deve ser uma string de comprimento 3 representando o numéro.")

    numero_por_extenso = ''
    for idx in range(0, 3):
        next_string = translate_matrix[2 - idx][int(number[idx])]
        if next_string != '':
            # Caso especial da dezena iniciada por 1 (10,11,12,13...)
            if idx == 1 and int(number[idx]) == 1:
                next_string = translate_matrix[3][int(number[idx+1])]
                numero_por_extenso += next_string
                break
            # Só pra escrita ficar mais natural, da maneira como falamos
            if idx != 2 and number[idx+1:] != '0':
                next_string += ' e '
            numero_por_extenso += next_string
    return numero_por_extenso


with open(input_file, 'r') as f_input:
    f_output = open(output_file, 'a')
    for line in f_input.readlines():
        number = line.strip()
        reais, centavos = number.split(',')

        # Completa as strings com '0' a esquerda pra ficarem na forma XXX.XXX.XXX,XXX
        if len(reais) < 9:
            reais = '0'*(9-len(reais)) + reais
        centavos = '0' + centavos

        # A cada 3 numeros eu monto uma string daquela parte escrita por extenso
        milhoes = reais[0:3]
        milhares = reais[3:6]
        centenas = reais[6:]

        string_milhoes = get_string(milhoes) + ' milhões '
        string_milhares = get_string(milhares) + ' mil '
        string_centenas = get_string(centenas)
        centavos_string = get_string(centavos) + ' centavos'

        # tratamento de alguns casos particulares
        if int(milhoes) == 1:
            string_milhoes = 'um milhão de '
        elif int(milhoes) == 100:
            string_milhoes = 'cem milhões '

        # pra não ficar "um mil"
        if int(milhares) == 1:
            string_milhares = 'mil '
        # pq uso "cento" na minha matriz
        elif int(milhares) == 100:
            string_milhares = 'cem mil '

        # pq uso "cento" na minha matriz
        if int(centenas) == 100:
            string_centenas = 'e cem'

        # Montagem da string final
        reais_string = ''
        if int(milhoes) != 0:
            reais_string += string_milhoes

        if int(milhares) != 0:
            reais_string += string_milhares

        if int(centenas) != 0:
            # Só pra escrita ficar mais natural, da maneira como falamos
            if int(centenas[0]) == 0 and (int(milhares) != 0 or int(milhoes) != 0):
                reais_string = reais_string + ' e '
            reais_string += string_centenas

        reais_string = reais_string.replace("  ", " ")
        centavos_string = centavos_string.replace("  ", " ")
        final_string = reais_string + ' reais '

        if int(reais) == 1:
            final_string = 'um real'
        elif int(reais) == 100:
            final_string = 'cem reais'
        elif int(reais) == 0:
            final_string = ''

        if int(centavos) == 0:
            centavos_string = ''
        if int(centavos) == 1:
            centavos_string = ' um centavo '

        if int(centavos) == 0 and int(reais) == 0:
            final_string = 'zero reais e zero centavos'

        if int(centavos) != 0:
            if int(reais) == 0:
                final_string += centavos_string
            else:
                final_string += ' e ' + centavos_string

        f_output.write(final_string.replace("  ", " ").strip()+'\n')

    f_output.close()
