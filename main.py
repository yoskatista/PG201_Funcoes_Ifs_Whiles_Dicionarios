"""def nomes_cidades(cidade,pais):
    unir = cidade + ", " + pais
    return unir

print(nomes_cidades('Santiago','Chile'))
print(nomes_cidades('Salvador','Brasil'))
print(nomes_cidades('New York','Eua'))"""

def make_album(nome_artista, titulo_album,musicas_album):
    dicionario_album = {'nome':nome_artista,'titulo':titulo_album,'músicas':musicas_album}
    return dicionario_album

while True:
    nome_artista = input('Qual o nome do artista')
    titulo_album = input("Nome do album")
    musicas_album = input("Quantia de musicas")
    print(make_album(nome_artista,titulo_album,musicas_album))
    print('Digite q para sair')
    if nome_artista == 'q' or nome_artista == "Q":
        print("Terminado")
        break
    if titulo_album == "Q" or titulo_album == "q":
        print("FIM")
        break
    elif musicas_album == "Q" or musicas_album == "q":
        print("Encerrado")
        break


print(make_album('Ozzy Osbourne','paranoid',musicas_album=8))
print(make_album('Ozzy Osbourne','Heaven and Hell',musicas_album=8))
print(make_album('Ozzy Osbourne','Black Sabath',musicas_album=7))
