# Highline Fire & Safety Training Institute - Project Context

This document provides context for anyone (human or AI) picking up development on this project.

## 📁 Project Overview & Location
- **Local Path:** `c:\Users\jhash\Downloads\highline-main\highline-main`
- **GitHub Repository:** [https://github.com/AdarshJha05/Highline_web](https://github.com/AdarshJha05/Highline_web)
- **Deployment:** Pre-configured for Vercel via `vercel.json`. The `website/` folder is the deployment root.

## 🛠️ Tech Stack
- **Pure Static Site:** HTML, CSS, Vanilla JavaScript.
- **No Build Step:** No React, No Next.js, no bundlers, no npm dependencies.
- **Styling:** Custom CSS located in `website/assets/css/styles.css`.
- **Interactivity:** Vanilla JS located in `website/assets/js/site.js`.

## 📂 Project Structure
```text
highline-main/
├── website/                  # The actual website files (Vercel Output Directory)
│   ├── index.html            # Home page
│   ├── about.html            # About page
│   ├── contact.html          # Contact page
│   ├── assets/
│   │   ├── css/styles.css
│   │   ├── js/site.js
│   │   └── img/              # Images
│   └── README.md             # Website specific documentation
├── design_handoff.../        # Original design files and prototypes
├── vercel.json               # Vercel deployment configuration
└── README.md                 # Root repository readme
```

## 🚀 How to Run Locally
Run a local HTTP server targeting the `website` directory.
```bash
python -m http.server 8000 --directory website
```
Then navigate to `http://localhost:8000`

## 📝 Recent Work & Next Steps
1. **Version Control:** The project was initialized with Git and pushed to the GitHub repository mentioned above.
2. **Deployment Ready:** Confirmed that `vercel.json` is correctly set up to deploy the `website/` directory.
3. **Data Extraction (New Content):** We recently extracted all text from the **"EOSH Qualification & Partnership Guide 2026"** PDF into a structured markdown format.
    - This extracted data includes comprehensive lists of courses (Health & Safety, Fire Safety, First Aid, etc.), diploma programs, accreditations, and company benefits.
    - **Goal for Next Steps:** This newly extracted EOSH data needs to be integrated into the website. This might involve creating a new `courses.html` or `qualifications.html` page, or updating the existing pages to reflect this comprehensive list of offerings. 

*(If you are an AI assistant reading this, ask the user to provide the extracted EOSH data or how they would like to integrate it into the current static site).*
