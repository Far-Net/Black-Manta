from tqdm import tqdm #loading
from random import choice #random banner
from sys import exit, stdout #exit and artistic part of Black Manta 
from time import strftime, sleep #hour and delay for conections
from pyfiglet import figlet_format #banner
from os import system, getlogin #execute system commands, get rot acess
from socket import gethostbyname, gaierror, socket, AF_INET, SOCK_STREAM, timeout #this is for whois and ports
from socks import set_default_proxy, SOCKS5, socksocket, GeneralProxyError, ProxyConnectionError #service tor, proxychains
from whois import whois #whois service
import dns.resolver #this is from host service
from subprocess import run #this is service tor too

#Tor service
run(['service', 'tor', 'start'], check=True)

set_default_proxy(SOCKS5, '127.0.0.1', 9050)
socket = socksocket
for i in range(25):
        for chars in ['.', '..', '...', '....']:
            stdout.write('\rIsso pode demorar alguns segundos' + chars.ljust(4))
            stdout.flush()
            sleep(0.1)
sleep(25)

#Art Black Manta
hour = strftime('%H:%M:%S')

def loading():
    for i in tqdm(range(100), desc='carregando', ncols=70, colour='magenta'):
        sleep(0.01)

system('clear')
print(('\033[1;35m[!]\033[m Iniciando o Black Manta\n'))
loading()
sleep(3)
system('clear')

def banner():
    fonts = ['isometric1', 'isometric2', 'slant', 'bubble', 'block']
    banner = figlet_format('black manta', font = choice(fonts))
    print('{}{}{}'.format('\033[1;35m', banner, '\033[m'))
    frases = [f'\nWhere are you, \033[1;32m{getlogin()}\033[m?', 'I can see everything!', '\033[1;36mThe world is your...\033[m', 'This is not \033[1;31mTR3B\033[m', 'You cant go on thinking...', 'Have you touched the grass today?', 'Why does everything mysteryous have to be \033[1;35mpurple\033[m?']
    print(choice(frases))
    print('')
    sleep(5)
    system('clear')
banner()

#Ports
def varredura():
    try:
        endereco_web = input('\n┌──[ Endereço web ]\n└─>> ').strip()
        print('\n\033[1;35m[1]\033[m Portas importantes \n\033[1;35m[2]\033[m Apenas uma porta\n')
        pergunta = int(input('Escolha: '))

        if pergunta == 1:
            portas_importantes = [80, 443, 8080, 8443, 22, 3389, 21, 3306, 1433, 5432, 27017, 25, 110, 143, 465, 587, 993]
            for p in portas_importantes:
                conect = socket(AF_INET, SOCK_STREAM)
                conect.settimeout(20.0)

                try:
                    resultado = conect.connect_ex((endereco_web, p))

                    if resultado == 0:
                        print(f'> Porta {p} \033[1;32maberta\033[m')
                    else: 
                        print(f'< Porta {p} \033[1;31mfechada\033[m')

                except(GeneralProxyError, ProxyConnectionError) as proxy_error:
                    print(f'\033[1;33m[!]\033[m Erro de proxy na porta {p}: o Tor não respondeu a tempo ou está desconectado')
                    conect.close()
                    continue

                except(timeout, TimeoutError):
                    print(f'< Porta {p} \033[1;31mfiltrada / protegidada\033[m')
                    conect.close()
                    continue

                finally:
                    conect.close()

        elif pergunta == 2:
            porta = input('\n┌──[ Porta ]\n└─>> ')
            conect = socket(AF_INET, SOCK_STREAM)
            conect.settimeout(20.0)

            try:
                resultado = conect.connect_ex((endereco_web, porta))

                if resultado == 0:
                    print(f'> Porta {porta} \033[1;32maberta\033[m')
                else: 
                    print(f'< Porta {porta} \033[1;31mfechada\033[m')
            
            except(GeneralProxyError, ProxyConnectionError) as proxy_error:
                print(f'\033[1;33m[!]\033[m Erro de proxy na porta {porta}: o Tor não respondeu a tempo ou está desconectado')
                conect.close()

            except(timeout, TimeoutError):
                print(f'< Porta {porta} \033[1;31mfiltrada / protegidada\033[m')
                conect.close()

            finally:
                conect.close()
        else:
            black_manta()

    except KeyboardInterrupt:
        black_manta()

#Identfy
def who():
    try:
        endereco_web = input('\n┌──[ Endereço web ]\n└─>> ').strip()
        print(f'\n| Resolvendo endereço IP de \033[1;35{endereco_web}\033[m')
        endereco_ip = gethostbyname(endereco_web)
        print(f'| Endereço IP de \033[1;35m{endereco_web}\033[m ---> \033[1;32m{endereco_ip}\033[m\n')

        dados = whois(endereco_web)
        print('='*80)
        print(f'> Registro: \033[1;35m{dados.registrar}\033[m')
        print(f'> Organização: \033[1;35m{dados.org}\033[m')
        print(f'> País: \033[1;35m{dados.country}\033[m')
        print(f'> Criado: \033[1;35m{dados.creation_date}\033[m')
        print(f'> Expirar: \033[1;35m{dados.expiration_date}\033[m')
        print(f'> Serviores: \033[1;35m{dados.name_servers}\033[m')
        print('='*80)

        #Escaneador de portas
        pergunta = input('┌──[ Varredura de portas (S/N) ]\n└─>> ').upper().strip()
        if pergunta == 'S' or pergunta == 'SS' or pergunta == 'SIM':
            portas_importantes = [80, 443, 8080, 8443, 22, 3389, 21, 3306, 1433, 5432, 27017, 25, 110, 143, 465, 587, 993]
            for p in portas_importantes:
                conect = socket(AF_INET, SOCK_STREAM)
                conect.settimeout(20.0)

                try:
                    resultado = conect.connect_ex((endereco_web, p))

                    if resultado == 0:
                        print(f'> Porta {p} \033[1;32maberta\033[m')
                    else: 
                        print(f'< Porta {p} \033[1;31mfechada\033[m')

                except(GeneralProxyError, ProxyConnectionError) as proxy_error:
                    print(f'\033[1;33m[!]\033[m Erro de proxy na porta {p}: o Tor não respondeu a tempo ou está desconectado')
                    conect.close()
                    continue

                except(timeout, TimeoutError):
                    print(f'< Porta {p} \033[1;31mfiltrada / protegidada\033[m')
                    conect.close()
                    continue

                finally:
                    conect.close()
        else:
            black_manta()

    except KeyboardInterrupt:
        black_manta()
        
    except gaierror:
        print('\033[1;31m[!]\033[m Não foi possível concluir o processo...\n')
        tentar = input('┌──[ Tentar novamente? (S/N) ]\n└─>> ').upper().strip()

        if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
            who()
        else:
            black_manta()

    tentar = input('\n┌──\033[1;33m[!]\033[m Tentar novamente? (S/N) ]\n└─>> ').upper().strip()
    if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
        system('clear')
        who()
    else:
        print('')
        black_manta()

#Informations
def host():
    try:
        endereco_web = input('\n┌──[ Endereço web ]\n└─>> ').strip()

        print('')
        print('='*80)

        try:
            ipv4 = dns.resolver.resolve(endereco_web, 'A')
            for ip in ipv4:
                print(f'> Endereço IP: \033[1;35m{ip}\033[m')
        except Exception:
            print('\n\033[1;31m[!]\033[m Erro ao tentar consultar o IP')

            tentar = input('┌──[ Tentar novamente? (S/N) ]\n└─>> ').upper().strip()

            if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
                host()
            else:
                black_manta()

        try:
            ipv6 = dns.resolver.resolve(endereco_web, 'AAAA')
            for ip in ipv6:
                print(f'> Endereço IPv6: \033[1;35m{ip}\033[m')
        except Exception:
            print('\n\033[1;31m[!]\033[m Erro ao tentar consultar o IPv6')

            tentar = input('┌──[ Tentar novamente? (S/N) ]\n└─>> ').upper().strip()

            if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
                host()
            else:
                black_manta()
        
        try:
            mail = dns.resolver.resolve(endereco_web, 'MX')
            for servidor in mail:
                print(f'> {endereco_web} envia emails para \033[1;35m{servidor.exchange}\033[m')
        except Exception:
            print('\n\033[1;31m[!]\033[m Erro ao tentar consultar o servidor de emails')

            tentar = input('┌──[ Tentar novamente? (S/N) ]\n└─>> ').upper().strip()

            if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
                host()
            else:
                black_manta()

        try:
            server = dns.resolver.resolve(endereco_web, 'NS')
            for nome_servidor in server:
                print(f'> Serviores: \033[1;35m{nome_servidor.target}\033[m')
        except Exception:
            print('\n\033[1;31m[!]\033[m Erro ao tentar consultar os serviores\n')

            tentar = input('┌──[ Tentar novamente? (S/N) ]\n└─>> ').upper().strip()

            if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
                host()
            else:
                black_manta()
        
        print('='*80)

        #Ports
        pergunta = input('┌──[ Varredura de portas? (S/N) ]\n└─>> ').upper().strip()
        if pergunta == 'S' or pergunta == 'SS' or pergunta == 'SIM':
            portas_importantes = [80, 443, 8080, 8443, 22, 3389, 21, 3306, 1433, 5432, 27017, 25, 110, 143, 465, 587, 993]
            for p in portas_importantes:
                conect = socket(AF_INET, SOCK_STREAM)
                conect.settimeout(20.0)

                try:
                    resultado = conect.connect_ex((endereco_web, p))

                    if resultado == 0:
                        print(f'> Porta {p} \033[1;32maberta\033[m')
                    else: 
                        print(f'< Porta {p} \033[1;31mfechada\033[m')

                except(GeneralProxyError, ProxyConnectionError) as proxy_error:
                    print(f'\033[1;33m[!]\033[m Erro de proxy na porta {p}: o Tor não respondeu a tempo ou está desconectado')
                    conect.close()
                    continue

                except(timeout, TimeoutError):
                    print(f'< Porta {p} \033[1;31mfiltrada / protegidada\033[m')
                    conect.close()
                    continue

                finally:
                    conect.close()
        else:
            black_manta()

        tentar = input('\n┌──\033[1;33m[!]\033[m Tentar novamente? (S/N) ]\n└─>> ').upper().strip()

        if tentar == 'S' or tentar == 'SS' or tentar == 'SIM':
            system('clear')
            host()
        else:
            print('')
            black_manta()
    except KeyboardInterrupt:
        black_manta()
    
#Help
def helpp():
    print('='*80)
    print('\nport ---> Varredura de portas \nwho ---> Identificar alvo \nhost ---> Mais informações do alvo \nstart service ---> rode o serviço tor \nstop service ---> pare o serviço tor \nstatus ---> informações do serviço tor \nclear or cls ---> limpar o terminal \nreboot ---> reiniciar Black Manta \nexit ---> pare de rodar o Black Manta\n')
    print('='*80)
    print('')
helpp()
        
#The brain of Black Manta
def black_manta():
    while True:
        try:
            manta = input(f'┌──[ \033[1;35mBlack Manta\033[m {hour} ]\n└─>> ').strip()

            if manta == 'help' or manta == 'h':
                helpp()

            if manta == 'reboot':
                system('clear')
                print('\033[1;35m[!]\033[m Reiniciando...')
                sleep(2)
                system('clear')
                banner()
                black_manta()

            if manta == 'clear' or manta == 'cls':
                system('clear')
            
            if manta == 'port' or manta == 'ports':
                varredura()

            if manta == 'who':
                who()

            if manta == 'host':
                host()

            if manta == 'status':
                print('')
                system('service tor status')
                print('')
            elif manta == 'start service':
                run(['service', 'tor', 'start'], check=True)
                set_default_proxy(SOCKS5, '127.0.0.1', 9050)
                socket = socksocket
            elif manta == 'stop service':
                system('service tor stop')

            if manta == 'exit':
                print('\n\033[1;31m[!]\033[m Saindo...')
                sleep(2)
                system('clear')
                exit()
        except KeyboardInterrupt:
            print('\n\033[1;31m[!]\033[m Saindo...')
            sleep(2)
            system('clear')
            exit()
black_manta()
