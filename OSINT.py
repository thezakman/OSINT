# -*- coding: UTF-8 -*-
# @TheZakMan - 02/02/2022
# Versão 0.4

import clipboard # pip install clipboard - https://pypi.org/project/clipboard/
import curses
import webbrowser

print("""\

 _____  _____ _____  _   _ _____ 
|  _  |/  ___|_   _|| \ | |_   _|
| | | |\ `--.  | |  |  \| | | |  
| | | | `--. \ | |  | . ` | | |  
\ \_/ //\__/ /_| |__| |\  |_| |  
 \___(_)____(_)___(_)_| \_(_)_/  
    Olha Só Intel No Terminal                    
""")

host = input("HOST: ")

titulos = ["[Documentos]", "[Listagem de Diretório]", "[Arquivos de Config]","[Databases]","[Backups]","[Paginas de Login]","[Erros]","[SQLi]","[HAILMARY?]","[REPOSITÓRIOS]"]
dorks = ['site:{} ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:pdf'.format(str(host)),
         'site:{} intitle:index.of'.format(str(host)),
         'site:{} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env | ext:log'.format(str(host)),
         'site:{} ext:sql | ext:dbf | ext:mdb'.format(str(host)),
         'site:{} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup'.format(str(host)),
         'site:{} inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth | intitle:"acessar" | intitle:"entrar"'.format(str(host)),
         'site:{} "PHP Parse error" | "PHP Warning" | "PHP Error" | intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'.format(str(host)),
         'site:{} ext:php | ext:asp | ext:aspx | ext:php5'.format(str(host)),
         'site:pastebin.com | site:postman.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com "{}"'.format(str(host)),
         'site:github.com | site:gitlab.com intext:{}'.format(str(host))
         ]
         


def character(stdscr):
    attributes = {}
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    attributes['highlighted'] = curses.color_pair(2)
    
    c = 0
    option = 0
    while c != 10:  # Enter em ASCII
        stdscr.erase()
        stdscr.addstr("Selecione a opção desejada:\n\n", curses.A_UNDERLINE)
        for i in range(len(titulos)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(titulos[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(titulos) - 1:
            option += 1

    stdscr.addstr("\n[DORK Gerado]:")
    stdscr.addstr("\n"+dorks[int(option)])
    
    clipboard.copy(dorks[int(option)])
    webbrowser.open('https://www.google.com/search?q={}'.format(dorks[int(option)]))
    
    stdscr.getch()
    curses.wrapper(character)
   
try:
    while True:
        curses.wrapper(character)
        break

except KeyboardInterrupt:
    print("[!] Programa finalizado com CTRL+C")
    pass
