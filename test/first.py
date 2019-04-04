from translate import Translator
import  re
import os

def order(elem):
    return elem[1]

def order2(elem):
    return elem[0]

fileNames = []
#extracting file names
for data in os.listdir("."):
    if data.endswith(".srt"):
        fileNames.append(data)


fileNames.sort(key=order)
tmpList = []
for i in range (0,10):
    tmpList.append(fileNames[i])
#print(tmpList)

for x in tmpList:
    fileNames.remove(x)
fileNames.sort(key=order2)
fileNames = tmpList + fileNames

writeFile = open("testfile.txt","w")
complete = ""
#translator = Translator(to_lang="German")
for file in tmpList:
    t = open(file)
    for line in t.readlines():
        text = re.sub(r'\d', "", line)
        text = re.sub(r'::,', "", text)
        text = re.sub(r'-->', "", text)
        # text = re.sub(r'\s', " ", text)
        text = re.sub(r'\n', " ", text)
        #text = re.sub(r',', " ", text)
        text = re.sub(" ", " ", text)
        complete += text
    complete += "\n\n"
    writeFile.write(complete)
    complete = ""
    #t = open("1 - Introduction to Design Alternatives - lang_en.srt", "r")
#complete = ""

#for line in t.readlines():
    #text = re.sub(r'\d', "", line)
    #text = re.sub(r'::,', "", text)
    #text = re.sub(r'-->', "", text)
    #text = re.sub(r'\s', " ", text)
    #text = re.sub(r'\n', "", text)
    #text = re.sub(r',', " ", text)
    #text = re.sub(r' ', " ", text)
    #complete += text

#print (complete)



#complete1 = complete.split(".")
#for sentence in complete1:
    #print(sentence)
    #translation = translator.translate(sentence)
    #print(translation)




