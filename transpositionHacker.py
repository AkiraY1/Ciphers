import detectEnglish, TranspositionDecrypt

def main():
    myMessage = "Nd tnVyaoat siroedI sts i netn Dt h enrenh a-ogeas e ,ebt1 orlpaay rrt9po me leasee hdoocwla .anPy rsihyrb kdasa tai soEf nitp llg yvasdc.aaleop esoea rly,orartmmlSew  diny,eilhnahs od  ,cyetyehar da    ssret,aannoad..  ?  ydofni  bwbg, t ddSSroei s 2 nhhoufrula0v’eetlolnul2et  hdr.lrl0r wwe e ip,)beoord Tk  .avuu.etheuo lell she pfTlnddTte c  hy   hr glshe ntmeooiooe aehasywrcmruberke nlke nudee ae w ois a anrwofnqettdc sarolu oeito’skoieh nsib  ,dn et pojca .eprrtaneh s  a yorscishLcrf  a tlheiltaisgw do ka mncieorrwesoi rnrfeto sfloege n uce yra  h bllsh.dmcoehrdo e e onraa c(rTrim  dtwka h fmhb  awspet eerlwko esosnroehertre ht tfo khs pesaht’u,eowu  ge sp yneseaert ,s arhvbn’hf hwle eodsealeei orua. vo rttr t  honweyh f aAorgo  eseelnui ulw clvldstaliaorte  eefdvsna rty, t i lttyho hewniych eutorogn hrf  hb r  t eatkebekifwhaminyyv naoetimo  eo c relewhwrnttt ny. aay h hie  wdsohehindmEh  ne enn,evattergrgo metwo  r scwbr o haea eheys aarabsnir hcndttihtc,oehn , le h n ioe Ci b bcwlyaaOtwrwuea"

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print("Failed to hack encryption")
    else:
        print(hackedMessage)

def hackTransposition(message):
    print("Hacking...")
    print("(Press Ctrl-C (Windows) or Ctrl-D (Mac and Linux) to quit at any time.)")

    for key in range(1, len(message)):
        print("Trying key #%s..." % (key))
        decryptedText = TranspositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything to continue hacking: ')
            response  = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    
    return None

if __name__ == '__main__':
    main()
