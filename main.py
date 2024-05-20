with open("input.txt", "r+")as file1,open("1.txt","r+") as file2:
    content=file1.read()
    replaced_content=content.replace(" à","a").lower()
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
    while True:
        search=input("Enter a string to search for in 1.txt: ")
        results=[]
        file2.seek(0)
        for line in file2:
            if search in line:
                results.append(line)
        print(len(results),"result"+("s"if len(results)!=1else""),"found")
        for i in results:
            print(i)
        if len(results)==1:
            f2=""
            file2.seek(0)
            for i in file2:
                if i!=results[0]:
                    f2+=i
            file2.seek(0)
            file2.write(f2)
            file2.truncate()
            file1.seek(0)
            file1.write(f2)
            file1.truncate()