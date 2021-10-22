S=input('Introduceti sirul:')
c,d,e,f,g=S,S,S,S,S
a=S.count('A')
print(a)
for i in range(len(S)):
    if S[i]=='A':
        c=S.replace(S[i],'*')
    if S[i]=='B':
        d=S.replace(S[i],'')
b=S.count('MA')
print(b)
z=S.count('TA')
f=S.replace('TA','')
e=S.replace('MA','TA')
for i in range(0,0-len(S),-1):
    g=S.replace(S[abs(i)],S[i])
print(a,b,c,d,e,f,g)