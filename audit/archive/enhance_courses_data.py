import json
import random

# Load existing courses
with open('website/assets/data/courses.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

# Augment courses with missing data required by the architecture
for c in courses:
    level = c.get('level', 'Certificate').lower()
    cat = c.get('category', '').lower()
    title = c.get('title', '').lower()

    # Duration
    if 'diploma' in level or 'diploma' in title:
        c['duration'] = "6 Months"
    elif 'level 4' in title or 'level 5' in title or 'advanced' in title:
        c['duration'] = "12 Weeks"
    elif 'level 3' in title:
        c['duration'] = "4 Weeks"
    elif 'train the trainer' in title:
        c['duration'] = "5 Days"
    else:
        c['duration'] = "3 Days (Intensive)"

    # Eligibility
    if 'diploma' in level or 'diploma' in title:
        c['eligibility'] = "12th Pass or Equivalent qualification."
    elif 'level 4' in title or 'level 5' in title:
        c['eligibility'] = "Graduation or Level 3 Safety Certification."
    else:
        c['eligibility'] = "10th Pass with basic understanding of English/Hindi."

    # Fee
    c['fee'] = "On Enquiry (Installments Available)"

    # Accreditation
    if 'eosh' in title:
        c['accreditation'] = "EOSH UK Approved"
    elif 'iosh' in title:
        c['accreditation'] = "IOSH Accredited"
    elif 'nebosh' in title:
        c['accreditation'] = "NEBOSH Certified"
    else:
        c['accreditation'] = "Government of India / BSS Approved"

    # Mode
    c['mode'] = "Classroom + Practical Field Drills"
    c['location'] = "Highline Campus, Karimnagar"

    # Audience
    c['audience'] = "This course is ideal for aspiring safety officers, site supervisors, HSE managers, and working professionals seeking to upgrade their qualifications for international opportunities."

    # Outcomes
    c['outcomes'] = [
        "Identify and control critical workplace hazards.",
        "Understand international HSE legal frameworks and compliance.",
        "Conduct thorough risk assessments and safety audits.",
        "Develop and implement emergency response strategies."
    ]

    # Modules
    c['modules'] = [
        "Module 1: Principles of Health and Safety",
        "Module 2: Risk Assessment Methodology",
        "Module 3: Hazard Control in the Workplace",
        "Module 4: Incident Investigation and Reporting",
        "Module 5: Practical Safety Drills and Application"
    ]

    # Certification
    c['certification'] = f"Upon successful completion of the assessments, candidates will be awarded the official {c.get('accreditation')} certificate, recognized globally by employers."

    # Batch Dates
    c['batch_dates'] = "Admissions Open - Flexible Weekday & Weekend Batches Available."

    # FAQs
    c['faqs'] = [
        {
            "q": "Are there placement opportunities after this course?",
            "a": "Yes, Highline offers 100% placement assistance, interview preparation, and resume building for our graduates."
        },
        {
            "q": "Can I pay the fees in installments?",
            "a": "Yes, flexible installment plans are available for most diploma and advanced certification tracks."
        },
        {
            "q": "Is this certification valid internationally?",
            "a": f"Absolutely. This {c.get('accreditation')} course is globally recognized, especially in the Gulf (GCC) countries and Europe."
        }
    ]

with open('website/assets/data/courses.json', 'w', encoding='utf-8') as f:
    json.dump(courses, f, indent=2)

print("courses.json enhanced.")
