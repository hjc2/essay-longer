
from numpy import true_divide
import requests
from bs4 import BeautifulSoup

def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]

toggle = 0

with open("translation.txt") as f:

    code = " ".join([l.rstrip("\n") for l in f]).split(" ")

output = []

for l in code:
    syn = synonyms(l)
    if(len(syn) != 0):
        output.append(max(synonyms(l),key=len))
    else:
        output.append(l)

    if(toggle > 5):
        toggle = 0
        print("          ", end="\r")
    else:
        print("*" * toggle, end="\r")
        toggle += 1

print(output)
output = " ".join(output)

print(code)
print(output)

#print(syn)
#print(max(syn, key=len))
