traditional_frequencies = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
your_frequencies =        "SLXWVAUDZFCNMRXTOIGPKHEQYBJ" #suppongo che PDV == THE e che ANSU == FLAG

text = 'PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU. PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV. AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V. EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ L V PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP. ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}'
F_text = ''
index = []

for i in text:
    if i in your_frequencies:
        #index.append(traditional_frequencies.index(i))
        F_text += traditional_frequencies[your_frequencies.index(i)]
    else:
        F_text += i

print(F_text)