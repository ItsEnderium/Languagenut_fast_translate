with open("input.txt","r+")as inp,open("1.txt","r+")as file1,open("2.txt","r+") as file2:
    file1.truncate()
    file1.write(inp.read().lower())
    file1.seek(0)
    lines=file1.readlines()
    file1.seek(0)
    file1.truncate()
    zeros=len(str(len(lines)))
    for i,line in enumerate(lines):
        newl=line.replace('\t',' | ')
        file1.write(f"{str(i+1).zfill(zeros)} | {newl}")
    file1.seek(0)
    content=file1.read()
    content=content.replace("à","a")
    content=content.replace("á","a")
    content=content.replace("â","a")
    content=content.replace("ã","a")
    content=content.replace("ä","a")
    content=content.replace("å","a")
    content=content.replace("ç","c")
    content=content.replace("ð","d")
    content=content.replace("è","e")
    content=content.replace("é","e")
    content=content.replace("ê","e")
    content=content.replace("ë","e")
    content=content.replace("ì","i")
    content=content.replace("í","i")
    content=content.replace("î","i")
    content=content.replace("ï","i")
    content=content.replace("ñ","n")
    content=content.replace("ò","o")
    content=content.replace("ó","o")
    content=content.replace("ô","o")
    content=content.replace("õ","o")
    content=content.replace("ö","o")
    content=content.replace("ø","o")
    content=content.replace("ù","u")
    content=content.replace("ú","u")
    content=content.replace("û","u")
    content=content.replace("ü","u")
    content=content.replace("ý","y")
    content=content.replace("ÿ","y")
    content=content.replace("æ","ae")
    content=content.replace("œ","oe")
    file2.write(content)
    file2.truncate()
    file1.seek(0)
    print(len(file1.readlines()),"items left.")
    while True:
        search=input("Search for a string or number: ").lower()
        print()
        results=[]
        file2.seek(0)
        for i in file2:
            if search in i:
                results.append(i.strip())
        print(len(results)if len(results)!=0else"No","result"+("s"if len(results)!=1else""),"found"+(":"if len(results)!=0else"."))
        for i in results:
            file2.seek(0)
            for l in file1:
                if i[:3]==l[:3]:
                    print(l.strip())
        if len(results)==1:
            f2=""
            file2.seek(0)
            for i in file2:
                if results[0] not in i:
                    f2+=i
            file2.seek(0)
            file2.write(f2)
            file2.truncate()
            file1.seek(0)
            lines=file1.readlines()
            f1=""
            for i in lines:
                if results[0] not in i:
                    f1+=i
            file1.seek(0)
            file1.write(f1)
            file1.truncate()
            file1.seek(0)
            print("Item removed,",len(file1.readlines()),"items left.")
        print()