print('Encontrando letras de "PYTHON" em palavras de um texto')
print()

texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

textoSemAcentuacao = texto.replace(',', '').replace('.', '')
textoLower = textoSemAcentuacao.lower()
textoSplit = textoLower.split()
python = ['p', 'y', 't', 'h', 'o', 'n']
palavras = []

print(textoSplit)
print()

for palavra in textoSplit:
    for letra in python:
        if letra in palavra:
            palavras.append(palavra)
            break

print(f'Palavras que possuem alguma das letras de "PYTHON": {palavras}.')
