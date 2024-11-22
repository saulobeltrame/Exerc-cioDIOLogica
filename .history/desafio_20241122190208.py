#exercício dio logica de programação
heroi=str(input("Qual o nome do seu herói?"))
XP=float(input("Qual o XP do seu herói?"))
if XP <=1000:
    print("O", heroi ,"é nivel Ferro")
elif XP >1000 and XP <=2000:
    print("O", heroi ,"é nível Bronze")
elif XP >2000 and XP <=5000:
    print("O", heroi ,"é nível Prata")
elif XP >5000 and XP <=7000:
    print("O", heroi ,"é nível Ouro")
elif XP >7000 and XP <=8000:
    print("O", heroi ,"é nível Platina")
elif XP >8000 and XP <=9000:
    print("O", heroi ,"é nível Ascendente")
elif XP >9000 and XP <=10000:
    print("O", heroi ,"é nível Imortal")
elif XP >=10000:
    print("O", heroi ,"é nível Radiante")