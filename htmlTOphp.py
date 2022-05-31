import os

def replace_html_to_php ():
    debLigne = "$html .= \""
    finLigne = "\\n\";\n"
    files = os.listdir()
    for file in files:
        if file.endswith(r".php"):
            
            f = open(file, "r")
            temp = open(".temp.txt", "w")
            temp.write("<?php\n")
            lineF = f.readline().replace('\"', "\'")
            s = "$html = \"" + lineF.replace('\n', "") + finLigne
            temp.write(s)
            lineF = f.readline().replace('\t', "").replace('    ', "").replace('\"', "\'")
            while lineF != "":
                s = debLigne + lineF.replace('\n', "") + finLigne
                if s != debLigne + finLigne :
                    temp.write(s)
                lineF = f.readline().replace('\t', "").replace('    ', "").replace('\"', "\'")
            f.close()
            temp.write("echo($html);\n")
            temp.write("?>")
            temp.close()
            
            f = open(file, "w")
            temp = open(".temp.txt", "r")
            lineF = temp.readline()
            while lineF != "":
                f.write(lineF)
                lineF = temp.readline()
            temp.close()
            f.close()

replace_html_to_php()