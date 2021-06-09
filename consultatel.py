global R, B, C, Y, G, RT, CY, CO
CO = '\033[m'
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
CY = '\033[1;36m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

import sys
import time
import os
import signal
from colorama import Fore, Style
import atexit
import argparse
import random
import time
import hashlib
import json
import re
import requests
import urllib3
from bs4 import BeautifulSoup
import html5lib
import phonenumbers
import pyfiglet
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from urllib.parse import urlencode

def rekt():
   if platform.system() == "Windows":
      webbrowser.open_new_tab("https://youtu.be/1oAZVariAvk")
   else:
       os.system("termux-open-url https://youtu.be/1oAZVariAvk")

result = pyfiglet.figlet_format("Kiny", font = "cosmic"  )

def consultatel():
    print(f'{C}{G}{result}{C}')
    print(f'O que deseja fazer?')
    print(f'[{G}1{C}]Consultar operadora por numero')
    print(f'[{G}2{C}]Phone infoga')
    print(f'[{G}3{C}]Consulta completa[{G}GRATIS{C}] {C}[{R}OFF{C}]')
    choi = input('===>')
    if choi == '1' or choi == '01':
        consultaoperadora()
    elif choi == '2' or choi == '02':
        phoneinfoga()
    elif choi == '3' or choi == '03':
        primenumero()
    else:
        print(f'{C}[{R}i{C}] Opção inválida')
        time.sleep(3)


def primenumero():
    clear()
    rekt()
    pass
    #print(f'{C}{G}{result}{C}')
    #print(f'{C}[{G}i{C}] Digite o numero(ex: 219××××××××).')
    #requiem = input('===> ')
    #data = requests.get('vsfd hype/duality buscas, vou trocar e criptografar todas as api, quero ver pegar={}&reload='.format(requiem)).text
    #a = data.replace('<label "control-label" for="formGroupExampleInput5">','').replace('</label>','').replace('<span "form-control-static" "formGroupExampleInput5">','').replace('<div "row form-group">','').replace('</br>','').replace('<br>','').replace('<div "col-6">','').replace('<div "col-4">','').replace('</span>','').replace('<a href="#" title="CONSULTADO"','').replace('name="LinkEvoPlus"','').replace('data-"003.920.678-54">','').replace('<i "fa fa-search"></i>','').replace('</a>','').replace('(s&#xE1;bado)','(sábado)').replace('(ter&#xE7;a-feira)','(terça-feira)').replace('Data de Nascimento','Data de Nascimento:').replace('<div "col-2">','').replace('<div "col-10">','').replace('<div "title-block">','').replace('<style>','').replace('</style>','')
    #for i in range(0,10):
    	#try:
    		#a = api.replace(f'<h3 "title"><i "fa fa-list-ul"></i> Resultado ({i} encontrados)</h3>','')
    	#except:
    		#pass
    #print(a)

    #print(f'{C}[{Y}i{C}] Deseja fazer uma nova consulta?')
    #print('1.Sim')
    #print('2.Não')
    #OHNO = input("===>")
    #if OHNO == '1' or OHNO == '01':
        #primenumero()
    #if OHNO == '2' or OHNO == '02':
        #pass
    #else:
        #print(f'{C}[{R}i{C}] Opção inválida')
        #time.sleep(3)


def phoneinfoga():
    uagent = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
              "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
              "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
              "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
              "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"]

    number = ''  # Full number format; e.g: 3312345678
    localNumber = ''  # Local number format; e.g: 06 12 34 56 78
    internationalNumber = ''  # International number format; e.g: +33 6 12 34 56 78
    numberCountryCode = ''  # Dial code; e.g: 33
    numberCountry = ''  # Country; e.g: fr

    googleAbuseToken = ''
    customFormatting = ''

    os.system("clear")

    def search(req, stop):
        global googleAbuseToken
        global uagent
        chosenUserAgent = random.choice(uagent)
        reqSession = requests.Session()
        headers = {
            'User-Agent': chosenUserAgent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
            'Accept-Language': 'pt-br,pt;q=0.5',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Cookie': 'Cookie: CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg;                CONSENT=YES+RE.fr+20150809-08-0; 1P_JAR=2018-11-28-14; NID=148=aSdSHJz71rufCokaUC93nH3H7lOb8E7BNezDWV-PyyiHTXqWK5Y5hsvj7IAzhZAK04-      QNTXjYoLXVu_eiAJkiE46DlNn6JjjgCtY-7Fr0I4JaH-PZRb7WFgSTjiFqh0fw2cCWyN69DeP92dzMd572tQW2Z1gPwno3xuPrYC1T64wOud1DjZDhVAZkpk6UkBrU0PBcnLWL7YdL6IbEaCQlAI9BwaxoH_eywPVyS9V; SID=uAYeu3gT23GCz-ktdGInQuOSf-5SSzl3Plw11-CwsEYY0mqJLSiv7tFKeRpB_5iz8SH5lg.; HSID=AZmH_ctAfs0XbWOCJ; SSID=A0PcRJSylWIxJYTq_; APISID=HHB2bKfJ-2ZUL5-R/Ac0GK3qtM8EHkloNw; SAPISID=wQoxetHBpyo4pJKE/A2P6DUM9zGnStpIVt; SIDCC=ABtHo-EhFAa2AJrJIUgRGtRooWyVK0bAwiQ4UgDmKamfe88xOYBXM47FoL5oZaTxR3H-eOp7-rE; OTZ=4671861_52_52_123900_48_436380; OGPC=873035776-8:; OGP=-873035776:;'
        }

        try:
            REQ = urlencode({'q': req})
            URL = 'https://www.google.com/search?tbs=li:1&{}&amp;gws_rd=ssl&amp;gl=us '.format(
                REQ)
            r = reqSession.get(URL + googleAbuseToken, headers=headers)

            while r.status_code != 200:
                print(
                    '{}[{}ERROR{}] Você está temporariamente na lista negra da pesquisa do Google. Preencha o captcha no seguinte URL e copie / cole o conteúdo do cookie GOOGLE_ABUSE_EXEMPTION: {}'.format(
                        C, R, C, URL))
                token = input('\nGOOGLE_ABUSE_EXEMPTION=')
                googleAbuseToken = '&google_abuse=' + token
                r = reqSession.get(URL + googleAbuseToken, headers=headers)

            soup = BeautifulSoup(r.text, 'html5lib')

            results = soup.find("div", id="search").find_all("div", class_="g")

            links = []
            counter = 0

            for result in results:
                counter += 1

                if int(counter) > int(stop):
                    break

                url = result.find("a").get('href')
                url = re.sub(r'(?:\/url\?q\=)', '', url)
                url = re.sub(r'(?:\/url\?url\=)', '', url)
                url = re.sub(r'(?:\&sa\=)(?:.*)', '', url)
                url = re.sub(r'(?:\&rct\=)(?:.*)', '', url)

                if re.match(r"^(?:\/search\?q\=)", url) is not None:
                    url = 'https://google.com' + url

                if url is not None:
                    links.append(url)

            return links
        except Exception as e:
            print('{}[{}ERROR{}] O pedido falhou. Tente novamente.'.format(C, R, C))
            print(e)
            return []

    def formatNumber(InputNumber):
        return re.sub("(?:\+)?(?:[^[0-9]*)", "", InputNumber)

    def localScan(InputNumber):
        global number
        global localNumber
        global internationalNumber
        global numberCountryCode
        global numberCountry

        print('{}[{}i{}] Executando verificação local...'.format(C, Y, C))

        FormattedPhoneNumber = "+" + formatNumber(InputNumber)

        try:
            PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
            return False
        else:
            if not phonenumbers.is_valid_number(PhoneNumberObject):
                return False

            number = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace('+', '')
            numberCountryCode = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
            numberCountry = phonenumbers.region_code_for_country_code(
                int(numberCountryCode))

            localNumber = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace(numberCountryCode, '0')
            internationalNumber = phonenumbers.format_number(
                PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

            country = geocoder.country_name_for_number(PhoneNumberObject, "en")
            location = geocoder.description_for_number(PhoneNumberObject, "en")
            carrierName = carrier.name_for_number(PhoneNumberObject, 'en')

            print(f'Formato internacional:{B} {internationalNumber}')
            print(f'Formato local:{B} 0 {localNumber}')
            print(f'País: {B}{country} ({numberCountryCode})')
            print(f'Cidade/Estado:{B} {location}')
            print(f'Operadora:{B} {carrierName}')
            for timezoneResult in timezone.time_zones_for_number(PhoneNumberObject):
                print(f'Fuso horário:{B} {timezoneResult}')

            if phonenumbers.is_possible_number(PhoneNumberObject):
                print('O número é válido e possível.')
            else:
                print('O número é válido, mas pode não ser possível.')

    def numverifyScan():
        global number
        print('Executando scan com Numverify.com...')

        try:
            requestSecret = ''
            resp = requests.get('https://numverify.com/')
            soup = BeautifulSoup(resp.text, "html5lib")
        except Exception as e:
            print('Numverify.com não está disponível')
            return -1

        for tag in soup.find_all("input", type="hidden"):
            if tag['name'] == "scl_request_secret":
                requestSecret = tag['value']
                break

        apiKey = hashlib.md5(('number' + 'requestSecret').encode('utf-8')).hexdigest()

        headers = {
            'Host': 'numverify.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'application/json, text/javascript, /; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://numverify.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = requests.request(
                "GET",
                "https://numverify.com/php_helper_scripts/phone_api.php?secret_key={}&number={}".format(apiKey, number),
                data="", headers=headers)

            data = json.loads(response.content.decode('utf-8'))
        except Exception as e:
            print('Numverify.com não está disponível')
            return -1

        if response.content == "Unauthorized" or response.status_code != 200:
            print(("{}[{}ERROR{}] Ocorreu um erro ao chamar a API (solicitação incorreta ou chave de API incorreta)."))
            return -1

        if data["valid"] == False:
            print((
                      "{}[{}ERROR{}] especifique um número de telefone válido. Exemplo: +5585999999999 (DDD país + DDD estado + número"))
            sys.exit()

        InternationalNumber = '({}){}'.format(
            data["country_prefix"], data["local_format"])

        print(
            f'Número:{B} ({data["country_prefix"]}) {data["local_format"]}')
        print(
            f'País:{B} {data["country_name"]} ({data["country_code"]})')
        print(f'Cidade/Estado:{B} {data["location"]}')
        print(f'Operadora: {B}{data["carrier"]}')
        print(f'Tipo de linha:{B} {data["line_type"]}')

        if data["line_type"] == 'landline':
            print(("Provavelmente é um telefone fixo, mas ainda pode ser um número VoIP fixo."))
        elif data["line_type"] == 'mobile':
            print(("Provavelmente é um número de celular, mas ainda pode ser um número VoIP."))

    def ovhScan():
        global localNumber
        global numberCountry

        print('{}[{}ERROR{}]Executando OVH scan...'.format(C, R, C))

        querystring = {"País": numberCountry.lower()}

        headers = {
            'accept': "application/json",
            'cache-control': "no-cache"
        }

        try:
            response = requests.request(
                "GET", "https://api.ovh.com/1.0/telephony/number/detailedZones", data="", headers=headers,
                params=querystring)
            data = json.loads(response.content.decode('utf-8'))
        except Exception as e:
            print('API OVH inacessível. Talvez tente novamente mais tarde.')
            return -1

        if isinstance(data, list):
            askedNumber = "0" + localNumber.replace(localNumber[-4:], 'xxxx')

            for voip_number in data:
                if voip_number['number'] == askedNumber:
                    print(("1 resultado encontrado na base de dados OVH"))
                    print(
                        (f"Intervalo numérico:{B} {voip_number['number']}"))
                    print((f"Cidade:{B} {voip_number['city']}"))
                    print((
                              f"Código postal: {B} {voip_number['zipCode'] if voip_number['zipCode'] is not None else askForExit()}"))

    def replaceVariables(string):
        global number
        global internationalNumber
        global localNumber

        string = string.replace('$n', number)
        string = string.replace('$i', internationalNumber)
        string = string.replace('$l', localNumber)

        return string

    def osintIndividualScan():
        global number
        global internationalNumber
        global numberCountryCode
        global customFormatting

        dorks = json.load(open('osint/individuals.json'))

        for dork in dorks:
            if dork['dialCode'] is None or dork['dialCode'] == numberCountryCode:
                if customFormatting:
                    dorkRequest = replaceVariables(
                        dork['request']) + ' | intext:"{}"'.format(customFormatting)
                else:
                    dorkRequest = replaceVariables(dork['request'])

                print(
                    ("Procurando footprints em {}...".format(dork['site'])))

                for result in search(dorkRequest, stop=dork['stop']):
                    print(("URL: " + result))
            else:
                return -1

    def osintReputationScan():
        global number
        global internationalNumber
        global customFormatting

        dorks = json.load(open('osint/reputation.json'))

        for dork in dorks:
            if customFormatting:
                dorkRequest = replaceVariables(
                    dork['request']) + ' | intext:"{}"'.format(customFormatting)
            else:
                dorkRequest = replaceVariables(dork['request'])

            print(("Procurando por {}...".format(dork['title'])))
            for result in search(dorkRequest, stop=dork['stop']):
                print(("URL: " + result))

    def osintSocialMediaScan():
        global number
        global internationalNumber
        global customFormatting

        dorks = json.load(open('osint/social_medias.json'))

        for dork in dorks:
            if customFormatting:
                dorkRequest = replaceVariables(
                    dork['request']) + ' | intext:"{}"'.format(customFormatting)
            else:
                dorkRequest = replaceVariables(dork['request'])

            print(
                ("Procurando footprints em {}...".format(dork['site'])))

            for result in search(dorkRequest, stop=dork['stop']):
                print(("URL: " + result))

    def osintDisposableNumScan():
        global number

        dorks = json.load(open('osint/disposable_num_providers.json'))

        for dork in dorks:
            dorkRequest = replaceVariables(dork['request'])

            print(
                ("Procurando footprints em {}...".format(dork['site'])))

            for result in search(dorkRequest, stop=dork['stop']):
                print(("Result found: {}".format(dork['site'])))
                print(("URL: " + result))
                askForExit()

    def osintScan(rerun=False):
        global number
        global localNumber
        global internationalNumber
        global numberCountryCode
        global customFormatting

        print('Execução de reconhecimento de footprints OSINT...')

        if not rerun:
            print(("Gerando scan URL em 411.com..."))
            print("Scan URL: https://www.411.com/phone/{}".format(
                internationalNumber.replace('+', '').replace(' ', '-')))

            askingCustomPayload = input(
                'Você gostaria de usar um formato adicional para este número?[y/n] ')

        if rerun or askingCustomPayload == 'y' or askingCustomPayload == 'yes':
            customFormatting = input('Custom format: ')

        print(('Páginas Web footprints'))

        print(("Pesquisando footprints em páginas da web... (limit=10)"))
        if customFormatting:
            req = '{} | intext:"{}" | intext:"{}" | intext:"{}"'.format(
                number, number, internationalNumber, customFormatting)
        else:
            req = '{} | intext:"{}" | intext:"{}"'.format(
                number, number, internationalNumber)

        for result in search(req, stop=10):
            print(("Resultado encontrado: " + result))

        print(("Procurando documentos... (limit=10)"))
        if customFormatting:
            req = '[ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:txt     | ext:xls] && [intext:"{}"]'.format(
                customFormatting)
        else:
            req = '[ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:txt | ext:xls] && [intext:"{}" | intext:"{}"]'.format(
                internationalNumber, localNumber)
        for result in search(req, stop=10):
            print(("Resultado encontrado: " + result))

        print(('Footprints de reputação...'))

        osintReputationScan()

        print(("Gerando URL em scamcallfighters.com..."))
        print(
            'http://www.scamcallfighters.com/search-phone-{}.html'.format(number))

        tmpNumAsk = input(
            "Você gostaria de pesquisar footprints de provedores de números temporários?[y/n]")

        if tmpNumAsk.lower() != 'n' and tmpNumAsk.lower() != 'no':
            print(('Footprints em provedores de números temporários'))

            try:
                print(("Pesquisando número de telefone em tempophone.com..."))
                response = requests.request(
                    "GET", "https://tempophone.com/api/v1/phones")
                data = json.loads(response.content.decode('utf-8'))
                for voip_number in data['objects']:
                    if voip_number['phone'] == formatNumber(number):
                        print(
                            ("Encontrado um provedor de número temporário: tempophone.com"))
                        askForExit()
            except Exception as e:
                print(("Não foi possível acessar a API tempophone.com. Pulando etapa..."))

            osintDisposableNumScan()

        print(('Footprints de mídia social'))

        osintSocialMediaScan()

        print(('Footprints de listas telefônicas'))

        if numberCountryCode == '+1':
            print(("Gerando URL em TruePeopleSearch.com... "))
            print('https://www.truepeoplesearch.com/results?phoneno={}'.format(
                internationalNumber.replace(' ', '')))

        osintIndividualScan()

        retry_input = input(
            "Você gostaria de executar novamente a varredura OSINT? (por exemplo, para usar um formato diferente)[s/n]")

        if retry_input.lower() == 'y' or retry_input.lower() == 'yes':
            osintScan(True)
        else:
            return -1

    def askForExit():
        if not output:
            user_input = input("Continuar scanning?[y/n] ")

            if user_input.lower() == 'y' or user_input.lower() == 'yes':
                return -1
            else:

                sys.exit()

    def scanNumber(InputNumber):
        global number
        global localNumber
        global internationalNumber
        global numberCountryCode
        global numberCountry
        clear()
        print(f"Buscando informações para{B} {formatNumber(InputNumber)}{C}...")

        localScan(InputNumber)

        if not 'number':
            print((f"Erro: o número{B}{formatNumber(InputNumber)}{C} inválido."))
            # again()

        numverifyScan()
        ovhScan()
        osintScan()

        print("Scan concluído.")
        # again()

        # if not no_ansi and not output:
        # print(Style.RESET_ALL)

    def download_file(url, target_path):
        response = requests.get(url, stream=True)
        handle = open(target_path, "wb")
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)

        osintFiles = [
            'disposable_num_providers.json',
            'individuals.json',
            'reputation.json',
            'social_medias.json'
        ]

    def main():

        requests.packages.urllib3.disable_warnings()
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
        except AttributeError:
            pass

    number = input(f"{C}[{G}i{C}] Informe os números (sem espaços, parênteses e traço): {B}")
    scanNumber(number)

    def again():
        again = input("\n" + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
        if again == "s" or again == "sim":
            os.system("clear)
            main()
        elif again == "nao" or again == "n":
            pass

    main()
