print("Bem-vindo ao Quiz da Idade Media")
nome=(input("Qual seu apelido?"))
print("Muito bem, " + nome + " PREPARADO(A)? Será 11 perguntas, sendo 2 dissertativa (5pontos)e 9 de alternativas (2pontos)")
print("Boa sorte!!! "+ nome)
pontos = 0

print("1- Em que ano começou oficialmente a Idade Média?")
print("a: 476 d.C")
print("b: 1492 d.C")
print("c: 395 d.C")
resposta1 = input("Sua resposta: ")

if resposta1 == "a":
    print("Correto!")
    pontos += 2
elif resposta1 == "b":
    print("Errado!")
elif resposta1 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("2- Qual era o sistema social e econômico dominante na Idade Média?")
print("a: Capitalismo")
print("b: Feudalismo")
print("c: Socialismo")
resposta2 = input("Sua resposta: ")

if resposta2 == "b":
    print("Correto!")
    pontos += 2
elif resposta2 == "a":
    print("Errado!")
elif resposta2 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("3- Quem eram os cavaleiros medievais?")
print("a: Servos que trabalhavam na terra")
print("b: Guerreiros a serviço dos senhores feudais")
print("c: Comerciantes que viajavam pelas cidades")
resposta3 = input("Sua resposta: ")

if resposta3 == "b":
    print("Correto!")
    pontos += 1
elif resposta3 == "c":
    print("Errado!")
elif resposta3 == "a":
    print("Errado!")
else:
  print("Opção inválida!")

print("4- Qual era a religião predominante na Europa medieval?")
print("a: Cristianismo")
print("b: Islamismo")
print("c: Hinduísmo")
resposta4 = input("Sua resposta: ")

if resposta4 == "a":
    print("Correto!")
    pontos += 2
elif resposta4 == "b":
    print("Errado!")
elif resposta4 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("5- Quem tinha grande poder político e econômico durante a Idade Média?")
print("a: Os camponeses")
print("b: A nobreza e a Igreja")
print("c: Os comerciantes")
resposta5 = input("Sua resposta: ")

if resposta5 == "b":
    print("Correto!")
    pontos += 2
elif resposta5 == "a":
    print("Errado!")
elif resposta5 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("6- Qual era a principal ocupação dos servos?")
print("a: Comércio")
print("b: Trabalho na terra")
print("c: Artesanato")
resposta6 = input("Sua resposta: ")

if resposta6 == "b":
    print("Correto!")
    pontos += 2
elif resposta6 == "a":
    print("Errado!")
elif resposta6 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("7- Como era chamada a terra concedida pelo senhor feudal ao vassalo em troca de serviços?")
print("a: Feudo")
print("b: Mansão")
print("c: Castelo")
resposta7 = input("Sua resposta: ")

if resposta7 == "a":
    print("Correto!")
    pontos += 2
elif resposta7 == "b":
    print("Errado!")
elif resposta7 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("8- Como as cidades e o comércio evoluíram durante a Idade Média?")
print("a: Crescimento urbano e comercial")
print("b: Comércio exclusivo por via terrestre")
print("c: Declínio das cidades")
resposta8 = input("Sua resposta: ")

if resposta8 == "a":
    print("Correto!")
    pontos += 2
elif resposta8 == "b":
    print("Errado!")
elif resposta8 == "c":
    print("Errado!")
else:
  print("Opção inválida!")

print("9- Qual era o título dado ao líder supremo da igreja Católica na Idade Média?")
print("Resposta dissetativa")
print("DICA:4 letras")
resposta9 = input("Sua resposta: ")

if resposta9 == "papa":
    print("Correto!")
    pontos += 5
else:
  print("Errado!")

print("10- Qual era o nome da guerra religiosa promovida pela igreja para recuperar a Terra Santa?")
print("Resposta dissetativa")
print("DICA:8 letras")
resposta10 = input("Sua resposta: ")

if resposta10== "cruzadas":
    print("Correto!")
    pontos += 5
else:
  print("Errado!")


print("11- Os nobres que doavam terras aos outros nobres eram os ____, enquanto os _______ eram os nobres que recebiam essas terras.")
print("a: Burgueses – servos")
print("b: Vassalos - suseranos")
print("c: Suseranos – vassalos.")
resposta11 = input("Sua resposta: ")

if resposta11 == "c":
    print("Correto!")
    pontos += 2
elif resposta11 == "b":
    print("Errado!")
elif resposta11 == "a":
    print("Errado!")
else:
  print("Opção inválida!")

print("Fim do Quiz!")
print(f"PARABENSSSS!  voce fez {pontos} pontos.")

