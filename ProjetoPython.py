#-----------------------------------Código Base do Banco QuemPoupaTem!-------------------------------------------#

#-----------------------------------importa o diretorio de Data e a hora das transações-------------------------------------------#
import datetime
import time
#-----------------------------------Apaga o arquivo e auxilia para apargarmos o Cliente-------------------------------------------#  
import os
#-----------------------------------Salva a função do tempo do computador com a data-------------------------------------------#
now = datetime.datetime.now()

senha = 0 

print("Bem vindo ao QuemPoupaTem!")
print("Para iniciarmos a sua Operação, por favor selecione o que está procurando em nosso menu: ")
#-----------------------------------Esse é a Função do Hub Principal-------------------------------------------#
def hubdeinfo():
    time.sleep(3)
    print()
    print("1 - Novo Cliente ")
    print("2 - Apaga Cliente ")
    print("3 - Debita ")
    print("4 - Deposita ")
    print("5 - Saldo ")
    print("6 - Extrato ")
    print()
    print()
    print()
    print("0 - Sai ")
    print()
    comando = int(input("Digite aqui a Opção desejada: "))
    
    if comando == 1:
        return NovoCliente()

    if comando == 2:
        return ApagaCliente()

    if comando == 3:
        return Debita()

    if comando == 4:
        return Deposita()

    if comando == 5:
        return Saldo()

    if comando == 6:
        return Extrato()
    
    if comando == 0:
        print("Tchau,até logo!")
        print("Obrigado Pela Preferência! ")
        return

    elif 6<=comando<=1000000000000000000000000:
        print()
        print()
        print("Tente outro Número!")
        print()
        hubdeinfo()


#-----------------------Função que salva os dados do Cliente Novo---------------------------#
def NovoCliente():
    nome = str(input("Por favor, Digite seu Nome Completo: "))
    print()
    cpf = str(input("Por favor, Digite seu 'CPF' (Apenas os Números!): "))
    print()
    print("Escolha qual será a sua Nova Conta?")
    print()
    print(" 'Conta Salário' - Cobra uma Taxa de 5% a cada débito realizado e não permite que deixe a conta com saldo negativo")
    print()
    print(" 'Conta Comum' - Cobra uma Taxa de 3% a cada débito realizado e permite um saldo negativo de até (R$ 500,00)")
    print()
    print(" 'Conta Plus' - Cobra uma Taxa de 1% a cada débito realizado e permite um saldo negativo de até (R$ 5.000,00)")
    print()
    TipoDaConta = str(input("Digite Aqui um tipo!: ")) 
    ValorInicial = str(input("Entre com o valor inicial da conta em reais: "))
    SenhaDoUsuário = str(input("Escolha uma senha: "))
    
    #-----------------------Verifica se o que o Usuario Escreveu está Certo---------------------------#
    
    if TipoDaConta =="Conta Salário" or TipoDaConta =="Conta Comum" or TipoDaConta =="Conta Plus" :
        arquivo = open('%s.txt'%cpf,'a')#----Abre o arquivo---#
        arquivo.write("%s\n%s\n%s\n%s\n%s\n" %(nome, cpf, TipoDaConta, ValorInicial, SenhaDoUsuário))#----Escreve no arquivo---#
        arquivo.close()#----Fecha e salva o arquivo---#
        hubdeinfo()
    
       


#------------------------Função que Apaga O cliente Pelo CPF! ---------------------------#
          
def ApagaCliente():
    cpf = str(input("Digite seu CPF: "))
    senhatest = str(input("Digite sua senha: "))
    arquivo = open("%s.txt" %cpf)#----Abre o arquivo---#
    lista = arquivo.readlines()#----Lê o arquivo e salva na variável lista---#
    senha = lista[4]#----Pega a linha 4 do arquivo e salva na variável "Senha"---#
    senha = senha.strip()#----Pega a variável "Senha" e tira os "\n"---#
    #-----------------------Verifica se que a senha do cliente está certa! ---------------------------#
    if senha == senhatest:
        confirma = str(input("Você 'Confirma' isso ? 'SIM' ou 'NÃO': "))
        #----Pede uma confirmação ao cliente para realizar a tarefa!---#  
        if confirma == "SIM":
            os.remove("%s.txt" %cpf )
            print("Cliente Apagado Com sucesso!")
            return hubdeinfo()
           
        if confirma == "NÃO":
            print("Ok operação Cancelada!")
            return hubdeinfo()
                  
#------------------------Função que Debita Pelo CPF e Senha! ---------------------------#
def Debita():
    cpf = str(input("Digite seu CPF: "))
    senhatest = str(input("Digite sua senha: "))
    arquivo = open("%s.txt" %cpf,"r")
    lista = arquivo.readlines()#----Lê o arquivo e salva na variável lista---#
    senha = lista[4]#----Pega a linha 4 do arquivo e salva na variável "Senha"---#
    senha = senha.strip()#----Pega a variável "Senha" e tira os "\n"---#
    arquivo.close()#----Fecha e salva o arquivo---#
    #-----------------------Verifica se que a senha do cliente está certa! ---------------------------#
    if senha == senhatest:
        conta = lista[2]#----Pega a linha 2 do arquivo e salva na variável---#
        conta = conta.strip()#----Pega a variável e tira os "\n"---#
        debito = float(input("Por favor, digite a quantia que deseja debitar de sua %s: " %conta))
        extrato = lista[3]#----Pega a linha 2 do arquivo e salva na variável ---#
        extrato = extrato.strip()#----Pega a variável e tira os "\n"---#
        var1 = float(extrato)#----Transforma em float a variavel---#
        confirma = str(input("Você 'Confirma' isso ? 'SIM' ou 'NÃO': "))
        #----Verifica qual o tipo da conta do Usuário---#
        if conta == "Conta Salário":
            tarifa = 0.05*debito
            totaldebitado = debito + tarifa
            var2 = var1 - totaldebitado#---Conta de matemática---# 
            if var2 <= 0:
                print("Transação Negada!")
                print("Você tem na conta %s" %var1)
                return Debita()
                
            if confirma == "SIM":
                if var2 >= 0:
                    arquivo = open("%s.txt" %cpf,"w")
                    print("Transação Aceita!")
                    print("Você tem na conta %s" %var2)
                    lista[3] = str(var2)+'\n' 
                    for valor in lista:
                        arquivo.write(valor)

                    arquivo.close()
                    arquivo = open("%s.txt" %cpf,"a")
                    
                    lista = str(now)+'\n'+ "-"+str(totaldebitado)+ '\n'+ str(tarifa)+'\n' + str(var2)+'\n'
                    for data in lista:
                        arquivo.write(data)

                    arquivo.close()
                    return hubdeinfo()  
                    
        if conta == "Conta Comum":
            tarifa = 0.03*debito
            totaldebitado = debito + tarifa
            var2 = var1 - totaldebitado
            
            if var2 <= -500:
                print("Transação Negada!")
                print("Você tem na conta %s" %var1)
                return Debita()
                
            if confirma == "SIM":
                if var2 >= 0:
                    arquivo = open("%s.txt" %cpf,"w")
                    print("Transação Aceita!")
                    print("Você tem na conta %s" %var2)
                    lista[3] = str(var2)+'\n' 
                    for valor in lista:
                        arquivo.write(valor)
                
                    arquivo.close()
                    arquivo = open("%s.txt" %cpf,"a")
                    
                    lista = str(now)+'\n'+ "-"+str(totaldebitado)+ '\n'+ str(tarifa)+'\n' + str(var2)+'\n'
                    for data in lista:
                        arquivo.write(data)

                    arquivo.close()
                    return hubdeinfo()  

        if conta == "Conta Plus":
            tarifa = 0.01*debito
            totaldebitado = debito + tarifa
            var2 = var1 - totaldebitado
            if var2 <= -5000:
                print("Transação Negada!")
                print("Você tem na conta %s" %var1)
                return Debita()
                
            if confirma == "SIM":
                if var2 >= 0:
                    arquivo = open("%s.txt" %cpf,"w")
                    print("Transação Aceita!")
                    print("Você tem na conta %s" %var2)
                    lista[3] = str(var2)+'\n' 
                    for valor in lista:
                        arquivo.write(valor)
                
                    arquivo.close()
                    arquivo = open("%s.txt" %cpf,"a")
                    
                    lista = str(now)+'\n'+ "-"+str(totaldebitado)+ '\n'+ str(tarifa)+'\n' + str(var2)+'\n'
                    for data in lista:
                        arquivo.write(data)

                    arquivo.close()
                    return hubdeinfo()  
                   
        if confirma == "NÃO":
            print("Transação Negada!")
            return hubdeinfo()

#------------------------Função que Deposita Pelo CPF ! ---------------------------#
def Deposita():
    cpf = str(input("Digite seu CPF: "))
    arquivo = open("%s.txt" %cpf,"r")
    lista = arquivo.readlines()
    conta = lista[2]
    conta = conta.strip()
    deposito = float(input("Por favor, digite a quantia que deseja depositar de sua %s: " %conta))
    extrato = lista[3]
    extrato = extrato.strip()
    var1 = float(extrato)
    confirma = str(input("Você 'Confirma' isso ? 'SIM' ou 'NÃO': "))
    tarifa = 0 
    var2 = var1 + deposito
    arquivo.close()
    if var2 <= 0:
        print("Transação Negada!")
        print("Você tem na conta %s" %var1)
        return Deposita()
                
    if confirma == "SIM":
        if var2 >= 0:
            arquivo = open("%s.txt" %cpf,"w")
            print("Transação Aceita!")
            print("Você tem na conta %s" %var2)
            lista[3] = str(var2)+'\n' 
            for valor in lista:
                arquivo.write(valor)
                
            arquivo.close()
            arquivo = open("%s.txt" %cpf,"a")
            
            lista = str(now)+'\n'+ "+"+str(deposito)+ '\n'+ str(tarifa)+'\n' + str(var2)+'\n'
            for data in lista:
                arquivo.write(data)
             
            arquivo.close()
            
            return hubdeinfo()   
                    
        
    if confirma == "NÃO":
        print("Transação Negada!")
        return hubdeinfo()

#------------------------Função que vê o Saldo Do Cliente pelo CPF ! ---------------------------#
def Saldo():
    cpf = str(input("Digite seu CPF: "))
    senhatest = str(input("Digite sua senha: "))
    arquivo = open("%s.txt" %cpf,"r")
    lista = arquivo.readlines()
    cpftest = lista[1]
    cpftest = cpftest.strip()
    senha = lista[4]
    senha = senha.strip()
    arquivo.close()
    
    if senha == senhatest and cpf == cpftest:
        extrato = lista[3]
        extrato = extrato.strip()
        var1 = float(extrato)
        confirma = str(input("Você 'Confirma' isso ? 'SIM' ou 'NÃO': "))           
        
        if confirma == "SIM":
            print("Você tem na conta %s reais" %var1)
            return hubdeinfo()   
                    
        
        if confirma == "NÃO":
            print("Transação Negada!")
            return hubdeinfo()
    else:
        print(" 'Senha' ou 'CPF' incorreto tente novamente!")
        return Saldo()

#------------------------Função que vê o Extrato Do Cliente pelo CPF e Senha ! ---------------------------#
def Extrato():
    linha1 = 0
    linha2 = 0
    linha3 = 0
    linha4 = 0
    x=5
    cpf = str(input("Digite seu CPF: "))
    senhatest = str(input("Digite sua senha: "))
    arquivo = open("%s.txt" %cpf,"r")
    lista = arquivo.readlines()
    cpftest = lista[1]
    cpftest = cpftest.strip()
    senha = lista[4]
    senha = senha.strip()
    nome = lista[0]
    nome = nome.strip()
    conta = lista[2]
    conta = conta.strip()
    arquivo.close()
    if senha == senhatest and cpf == cpftest:
        confirma = str(input("Você 'Confirma' isso ? 'SIM' ou 'NÃO': "))           
        
        if confirma == "SIM":
            print("Nome: %s"%(nome))
            print("CPF: %s"%(cpftest))
            print("Conta: %s"%(conta))
            for x in range(5,len(lista),4):
                linha1 = lista[x]
                linha1 = linha1.strip()
                x =x+1
                linha2 = lista[x]
                linha2 = linha2.strip()
                x =x+1
                linha3 = lista[x]
                linha3 = linha3.strip()
                x =x+1
                linha4 = lista[x]
                linha4 = linha4.strip() 
                print("Data:  %s  %s  Tarifa:  %s  Saldo:  %s" %(linha1,linha2,linha3,linha4) )

            return hubdeinfo()   
                    
        
        if confirma == "NÃO":
            print("Transação Negada!")
            return hubdeinfo()
    else:
        print(" 'Senha' ou 'CPF' incorreto tente novamente!")
        return Extrato()
#===============================================================================================================================================================#

if __name__ == "__main__":
    hubdeinfo()
    



