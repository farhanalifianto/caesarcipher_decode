apx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    
def chr(plt,sr,deenx):
    msgx=""
    if deenx =="de":
        sr = sr *-1
    for let in plt:
        pos = apx.index(let)
        np = pos - sr
        new_t = apx[np]
        msgx += new_t
    print(msgx)

endgame = True
while endgame:
    deen = input("en or de ?= ")
    msg = input("msg= ")
    srx = int(input("shift= "))
    chr(deenx=deen,plt=msg,sr=srx)
    ag = input("again?y/n")
    if ag =="n":
        endgame = False
