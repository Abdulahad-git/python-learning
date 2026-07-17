import json
text=input("Your Name Please:\n")
file=open('Demoo.txt','a');
text=text;
fdata=json.dump(text,file)

