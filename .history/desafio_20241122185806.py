
heroi=str(input("Qual o nome do seu herói?"))
XP=float(input("Qual o XP do seu herói?"))
if XP <=1000:
    print("O seu" , heroi ," é nivel Ferro")
elif XP >1000 and XP <=2000:
    print("Você é nível Bronze")
elif XP >2000 and XP <=5000:
    print("Você é nível Prata")
elif XP >5000 and XP <=7000:
    print("Você é nível Ouro")
elif XP >7000 and XP <=8000:
    print("Você é nível Platina")
elif XP >8000 and XP <=9000:
    print("Você é nível Ascendente")
elif XP >9000 and XP <=10000:
    print("Você é nível Imortal")
elif XP >=10000:
    print("Você é nível Radiante")