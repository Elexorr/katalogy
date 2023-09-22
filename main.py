import urllib.request
import os

kats = ['And', 'Ant', 'Aps', 'Aqr', 'Aql', 'Ara', 'Ari', 'Aur', 'Boo', 'Cae', 'Cam', 'Cnc', 'CVn', 'CMa', 'CMi', 'Cap', 'Car', 'Cas', 'Cen', 'Cep', 'Cet', 'Cha', 'Cir', 'Com','Col', 'CrA', 'CrB', 'Crv', 'Crt', 'Cru', 'Cyg', 'Del', 'Dor', 'Dra', 'Equ', 'Eri', 'For', 'Gem', 'Gru', 'Her', 'Hor', 'Hya', 'Hyi', 'Ind', 'Lac', 'Leo', 'LMi', 'Lep', 'Lib', 'Lup', 'Lyn', 'Lyr', 'Men', 'Mic', 'Mon', 'Mus', 'Nor', 'Oct', 'Oph', 'Ori', 'Pav', 'Peg', 'Per', 'Phe', 'Pic', 'Psc', 'PsA', 'Pup', 'Pyx', 'Ret', 'Sge', 'Sgr', 'Sco', 'Scl', 'Sct', 'Ser', 'Sex', 'Tau', 'Tel', 'Tri', 'TrA', 'Tuc', 'UMa', 'UMi', 'Vel', 'Vir', 'Vol', 'Vul']

with open('final.csv', 'w') as k:
    k.write('GCVS,STAR,CONST.,RA(2000),DEC,Type,V [mag],P [days],Spec\n')
    for j in range(0, len(kats)):
        url = 'https://www.as.up.krakow.pl/ephem/'+kats[j]+'.htm'
        # filename = kats[i]+'.htm'
        # page = requests.get('https://www.as.up.krakow.pl/ephem/LEP.HTM')
        urllib.request.urlretrieve(url, kats[j]+'.txt')
        filename = kats[j]+'.txt'
        f = open(filename)
        lines = f.readlines()
        f.close()
        os.remove(kats[j] + '.txt')
        lines = lines[129:len(lines)]
        filename = kats[j]+'_short'+'.txt'
        with open(filename, 'w') as f:
            for i in range(0, len(lines)-1):
                print(lines[i])
                lines[i]=lines[i][0:6]+','+lines[i][68:74]+','+lines[i][75:78]+','+lines[i][85:98]+','+lines[i][100:112]+','+lines[i][117:121]+','+lines[i][126:131]+','+lines[i][135:149]+','+lines[i][154:len(lines[i])]
                print(lines[i])
                f.write(lines[i])
                k.write(lines[i])
            f.close()
        os.remove(kats[j] + '_short' + '.txt')
k.close()
text = open("final.csv", "r")
text = ''.join([i for i in text]).replace(" ", "")
x = open("final2.csv", "w")
x.writelines(text)
x.close()

    # with open(filename, 'wb+') as f:
    #     f.write(page.content)
    #     # lines=f.readlines()
    #     # print(len(lines))
    #     f.close()




        # with open(filename, 'r') as fin:
        #     data = fin.read().splitlines(True)
        # with open(filename, 'w') as fout:
        #     fout.writelines(data[1:5])

    # print(url)

# print(kats)
# page = requests.get('https://www.as.up.krakow.pl/ephem/LEP.HTM')
# with open('test.html', 'wb+') as f:
#     f.write(page.content)