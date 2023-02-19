import re

f = open("domains.xml", "r")
content_domains = f.read()
f.close()
#########################################################

resultat = re.findall(r"\.[a-z]{2,4}[\|<|\n]", content_domains)
print(resultat)
