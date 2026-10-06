import re
with open('website/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the specific paragraph
c = re.sub(r'Highline has grown into an ISO 9001:2015 certified, IBSP approved, IOSH-accredited institute\.', 'Highline has grown into an EOSH Approved Training Provider, IOSH Approved Training Provider, and Bharat Sevak Samaj approved institute.', c)

# Hide 500+ milestone
c = re.sub(r'(\{title:\'500\+ students trained milestone\'.*?\},)', r'/* \1 */', c, flags=re.DOTALL)
# Hide ISO 9001:2015 milestone
c = re.sub(r'(\{title:\'ISO 9001:2015 certified quality\'.*?\},)', r'/* \1 */', c, flags=re.DOTALL)

with open('website/about.html', 'w', encoding='utf-8') as f:
    f.write(c)
