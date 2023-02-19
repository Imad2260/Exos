import re

f = open("data.txt", "r")
content_data = f.read()
f.close()
##############################################################

resultat = re.findall(r"[a-zA-Z]+[\s]", content_data)
print(resultat)
