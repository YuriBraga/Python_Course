# Ler o ano de nascimento e mostrar a categoria do nadador (mirim até 9,
# infantil até 14, junior até 19, senior até 25, master acima 25)

from datetime import date
atual = date.today().year

nasc = int(input('\033[1;36mData de nascimento: \033[m'))
idd = atual - nasc
print('O atleta tem {} anos.'.format(idd))
if idd <= 9:
    print('Sua categoria é \033[1;36mMirim.\033[m')
elif idd <= 14:
    print('Sua categoria é \033[1;36mInfantil.\033[m')
elif idd <= 19:
    print('Sua categoria é \033[1;36mJunior.\033[m')
elif idd <= 25:
    print('Sua categoria é \033[1;36mSênior.\033[m')
else:
    # isto é, idd > 25
    print('Sua categoria é \033[1;36mMaster.\033[m')
