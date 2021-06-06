import requests,time
# 00000000272
Sair = False
while(Sair == False):
    def cpf_validate(numbers):
        cpfzao = [int(char) for char in numbers if char.isdigit()]

        if len(cpfzao) != 11:
            return False
        if cpfzao == cpfzao[::-1]:
            return False
        for i in range(9, 11):
            value = sum((cpfzao[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != cpfzao[i]:
                return False
        return True
    cpf = input("Digite o CPF: ")
    if cpf_validate(cpf):
        xd = requests.get('https://api.isaaclock.site/data/v1/{}'.format(cpf))
        api = xd.json()
        try:
    	    print(f'''Nome : {api['fullName']}
    	    CPF : {api['docNumber']}
    	    Nome da Mãe : {api['mae']}
    	    Aniversário : {api['nascAt']}
    	    Estado : {api['uf']}
    	    Cidade : {api['city']}
    	    CEP : {api['cep']}
    	    Logradouro : {api['logra']}
    	    Bairro : {api['bairro']}
    	    Número da Casa: {api['number']}
    	    Complemento : {api['compl']}''')
        except(AttributeError):
    	    print("sus")
    	
        choice = input("SUS: ")
        if choice == '1' or choice == '01':
            pass
        elif choice == '2' or choice == '02':
            Sair=True
        else:
            print('Opcao invalida!')
            time.sleep(3)
    else:
        print("CPF informado é inválido")
        time.sleep(3)
