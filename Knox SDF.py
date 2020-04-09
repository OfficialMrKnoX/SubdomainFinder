'''imports'''
import requests
import time
import urllib
import sys
import os
os.system('cls')
'''software information'''
author = "Mr KnoX"
toolname = "KNOX SDF"
version = 1.0
year = 2020
prtani = time.sleep(1)

'''software banner'''
def banner():
    ani_dly = 0.08
    global author, toolname, version, year
    print(f'\u001b[31;1m██╗  ██╗███╗   ██╗ ██████╗ ██╗  ██╗       ███████╗██████╗ ███████╗')
    time.sleep(ani_dly)
    print(f'██║ ██╔╝████╗  ██║██╔═══██╗╚██╗██╔╝       ██╔════╝██╔══██╗██╔════╝')
    time.sleep(ani_dly)
    print(f'█████╔╝ ██╔██╗ ██║██║   ██║ ╚███╔╝        ███████╗██║  ██║█████╗  ')
    time.sleep(ani_dly)
    print(f'██╔═██╗ ██║╚██╗██║██║   ██║ ██╔██╗        ╚════██║██║  ██║██╔══╝  ')
    time.sleep(ani_dly)
    print(f'██║  ██╗██║ ╚████║╚██████╔╝██╔╝ ██╗       ███████║██████╔╝██║     ')
    time.sleep(ani_dly)
    print(f'╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝       ╚══════╝╚═════╝ ╚═╝   ')
    time.sleep(ani_dly)
    print(f'''\u001b[34;1m Version: {version} | Copyright: {author} | Year: {year}\n''')
    time.sleep(0.5)

'''Get target domain from user'''
def get_chk_domain():
    print('\u001b[33;1m(Example: example.com)')
    target = input('\u001b[37mEnter target domain: ')
    link = f'http://www.{target}'
    try:
        print('\u001b[36mChecking domain...\n\u001b[37m')
        if 'http://www.www.' in link:
            link = link.replace('http://www.www.', 'http://www.')
        chk_url = urllib.request.urlopen(link)
        resp = chk_url.code
        if resp == 200:
            target = link.replace('http://www.', '')
            return target
        else:
            print('[*] Invalid domain, try again...')
    except:
        print("[*] Some error in connection")
        sys.exit(1)
    
'''Write output on a file'''
def write_to_file(domain, subdomain):
    global file_name
    file_name = f'''{domain}-subdomains(Knox SDF).txt'''
    with open(file_name, 'a') as opFile:
        opFile.write(subdomain+'\n')

'''Main function'''
def main():
    global file_name
    banner()
    target = get_chk_domain()
    crt_output = []
    link = f'''https://crt.sh/?q=%.{target}&output=json'''
    try:
        req = requests.get(link)
    except:
        print('[*] Check your internet connection...')
    finally:
        if req.status_code != 200:
            print('[*] Infromation not availabel.')
            sys.exit(1)
        else:
            for (sd_id, value) in enumerate(req.json()):
                crt_output.append(value['name_value'])
            subd = sorted(set(crt_output))
            for x in subd:
                print(x)
                write_to_file(target, x)
            '''count subdomain'''
            sd_count = 0
            with open(file_name, 'r') as fr:
                for lines in fr:
                    sd_count = sd_count + 1
            print(f'\u001b[32m [**] Knox SDF found totle {sd_count} subdomains [**]\u001b[37m')
            sys.exit(1)

if __name__ == "__main__":
    main()
