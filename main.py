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
    replaced_content=content.replace("à","a")
    replaced_content=replaced_content.replace("â","a")
    replaced_content=replaced_content.replace("ä","a")
    replaced_content=replaced_content.replace("æ","ae")
    replaced_content=replaced_content.replace("ç","c")
    replaced_content=replaced_content.replace("è","e")
    replaced_content=replaced_content.replace("é","e")
    replaced_content=replaced_content.replace("ê","e")
    replaced_content=replaced_content.replace("ë","e")
    replaced_content=replaced_content.replace("î","i")
    replaced_content=replaced_content.replace("ï","i")
    replaced_content=replaced_content.replace("ô","o")
    replaced_content=replaced_content.replace("œ","oe")
    replaced_content=replaced_content.replace("ù","u")
    replaced_content=replaced_content.replace("û","u")
    replaced_content=replaced_content.replace("ü","u")
    file2.write(replaced_content)
    file2.truncate()
    file1.seek(0)
    print(len(file1.readlines()),"items left.")
    while True:
        search=input("Search for a string or number: ")
        print()
        results=[]
        file1.seek(0)
        for i in file1:
            if search in i:
                results.append(i.strip())
        print(len(results)if len(results)!=0else"No","result"+("s"if len(results)!=1else""),"found"+(":"if len(results)!=0else"."))
        for i in results:
            print(i)
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