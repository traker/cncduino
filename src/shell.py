'''
Created on 26 mai 2011

@author: guill
'''
prompt = "CNC >>"


def start():
    raw_comshell = ""
    while raw_comshell != "quit":
        raw_comshell = raw_input(prompt)
        comshell = raw_comshell.split(" ")
        imprimecrean(comshell)
        #execute la commande qui ce trouve dans comshell

def imprimecrean(raw):
        n = ""
        for i in raw:
            n = n +" "+ i
        print n

if __name__ == '__main__':
    start()