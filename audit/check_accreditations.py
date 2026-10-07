import os
import re

terms = [
    "EOSH approved", "EOSH accredited", "EOSH authorised", "EOSH Partner",
    "NEBOSH accredited", "NEBOSH approved", "NEBOSH authorised", "International General Certificate",
    "Government Recognized", "OSHA Authorized", "IBSP", "ISO", "internationally accredited", "internationally recognized",
    "100%", "placement", "guaranteed job", "LPA", "salary"
]

def search_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        content = f.read()
                        for term in terms:
                            matches = re.finditer(term, content, re.IGNORECASE)
                            for match in matches:
                                start = max(0, match.start() - 30)
                                end = min(len(content), match.end() + 30)
                                snippet = content[start:end].replace('\n', ' ')
                                print(f"[{term}] found in {path}: ...{snippet}...")
                    except Exception as e:
                        print(f"Error reading {path}: {e}")

search_files('website')
