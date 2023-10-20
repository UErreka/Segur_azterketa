kont=0
listLetras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
listVeces=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
txt = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIVCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCVI ET DKIRXNI KXVITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXVITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
kontLetra=0
#kontatu karaktereak
for caracter in txt:
    i=0
    sizeLista=len(listLetras)
    while i<sizeLista:
        if(listLetras[i]==caracter):
            kontLetra=kontLetra+1
            listVeces[i]+=1
        i=i+1
i=0
print(listVeces)
#Letrak ordenatu
listPortzentaiakESP=["E","A","O","L","S","N","D","R","U","I","T","C","P","M","Y","Q","B","H","G","F","V","J","Ñ","Z","X","K","W"]
konbinazioa = list(zip(listVeces, listLetras))
konbinazioaOrdenatuta=sorted(konbinazioa,reverse=True)
portzentaiakOrd,letrakOrd=zip(*konbinazioaOrdenatuta)
print("Horrela izan behar zen ordena")
print(listPortzentaiakESP)
print("=")
print(letrakOrd)
  #LETRAK ORDEZKATU
print("EMAITZA:")
i=0
txtBerria=""
for caracter in txt:
    i=0
    aux=False
    while i<sizeLista and aux==False:
        if(letrakOrd[i]==caracter):
            txtBerria+=listPortzentaiakESP[i]
            aux=True
        i=i+1
    if aux==False:
            txtBerria+=caracter
        

print(txtBerria)


print("EMAITZA ALDAKETA BATZUEKIN:")
listPortzentaiakESP=["E","A","R","O","I","N","L","D","C","U","S","T","M","P","B","F","V","Q","J","G","H","Z","X","Y","Ñ","K","W"]
i=0
txtBerria=""
for caracter in txt:
    i=0
    aux=False
    while i<sizeLista and aux==False:
        if(letrakOrd[i]==caracter):
            txtBerria+=listPortzentaiakESP[i]
            aux=True
        i=i+1
    if aux==False:
            txtBerria+=caracter
        
print(txtBerria)
