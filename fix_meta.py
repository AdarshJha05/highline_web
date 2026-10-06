import re
for filename in ['website/index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'content=\"ISO 9001:2015 certified, IBSP approved and IOSH accredited.*?\"', r'content="EOSH Approved, IOSH and Bharat Sevak Samaj authorized fire & safety training in Karimnagar. DFS, ADHSE, IOSH, NEBOSH IGC, construction and oil & gas safety diplomas with practical drills."', c)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)
