import json

with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

print(f"Total courses found: {len(courses)}")

# Expected titles based on Section 4
expected_courses = [
    "Advance Diploma in Health, Safety & Environment (ADHSE)",
    "Diploma in Fire Safety",
    "Diploma in Construction Safety",
    "Certificate in Scaffolding Safety",
    "Certificate in Risk Assessment",
    "Certificate in Basic First Aid",
    "Certificate in Work Permit Receiver (WPR)",
    "Diploma in Industrial Safety",
    "Diploma in Oil & Gas Safety",
    "EOSH (Environment, Occupational Safety & Health)",
    "OSHA (Occupational Safety and Health Administration)",
    "IOSH Managing Safely, Version 5.0",
    "NEBOSH-oriented training",
    "IASP OSHA 30-hour General Industry",
    "BSS Advanced Diploma in Occupational Safety, Health & Environmental Management",
    "BSS Advanced Diploma in Fire & Industrial Safety Management"
]

actual_titles = [c.get("title", "") for c in courses]

# Check for extra/missing
missing = [t for t in expected_courses if not any(t.lower() in a.lower() for a in actual_titles)]
extra = [a for a in actual_titles if not any(t.lower() in a.lower() for t in expected_courses)]

print(f"Missing expected courses: {len(missing)}")
for m in missing:
    print(f"  - {m}")
    
print(f"Extra courses found: {len(extra)}")

# Check fields in a sample course
if len(courses) > 0:
    sample = courses[0]
    print(f"Fields in sample course: {list(sample.keys())}")
    
# Check accreditation control field
has_accreditation_control = all('accreditationStatus' in c or 'exactWording' in c for c in courses)
print(f"Has exact accreditation control fields (accreditationStatus/exactWording): {has_accreditation_control}")
