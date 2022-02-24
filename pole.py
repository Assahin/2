slovo=input('введите слово')
a=len(slovo)
ugad=''
n=0
for i in range(a):
    ugad=ugad+'*'
slovo=list(slovo)
ugad=list(ugad)
while ugad!=slovo:
    bukva=input('введите букву')
    if bukva in slovo:
        print('есть такая буква')
        for i in range(a):
            if slovo[i]==bukva:
                ugad[i]=bukva
        print(ugad)
    else:
        print('нет такой буквы')
    n=n+1
print(ugad,' число попыток:',n)