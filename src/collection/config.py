APP_ID = "70717cc8"
APP_KEY = "9bcc5c8bfd435696e2d9dc270a0722b9"

# COUNTRIES = [

#     "us",
#     "gb",
#     "ca",
#     "au",
#     "nz",
#     "sg",
#     "in",
#     "de",
#     "fr",
#     "nl",
#     "pl",
#     "br",
#     "za",
#     "mx"

# ]
COUNTRIES = [

    "us",
    "ca",
    "au",
    "nz",
    "sg",
    "in",  
    "mx"

]
START_PAGE = 1
END_PAGE = 100
RESULTS_PER_PAGE=50
MAX_RETRIES=15
REQUEST_DELAY = 0.4
REQUEST_TIMEOUT=30
RANDOM_DELAY_MIN=0.2
RANDOM_DELAY_MAX=0.8
RATE_LIMIT_WAIT=300
SERVER_ERROR_WAIT=60
TIMEOUT_WAIT=60
CONNECTION_WAIT = 120
REQUEST_TIMEOUT = 30

UNKNOWN_ERROR_WAIT = 30

# ==========================
# CSV
# ==========================

SAVE_AFTER_EVERY_PAGE = True

REMOVE_DUPLICATES = True

# ==========================
# Logging
# ==========================

LOG_LEVEL = "INFO"

PRINT_EVERY_PAGE = True

PRINT_SEPARATOR = "=" * 80

# ==========================
# API
# ==========================

SORT_BY = "date"

RESULTS_PER_PAGE = 50

# ==========================
# Checkpoint
# ==========================

ENABLE_CHECKPOINT = True

CHECKPOINT_FOLDER = "checkpoint"

CHECKPOINT_FILE = "checkpoint/checkpoint.json"

# ==========================
# Dataset
# ==========================

DATA_FOLDER = "data/raw"

LOG_FOLDER = "data/logs"

KEYWORDS = [

########################
# Software
########################

"Software Engineer",
"Software Developer",
"Software Architect",
"Application Developer",
"Backend Developer",
"Frontend Developer",
"Full Stack Developer",
"Web Developer",
"Mobile Developer",
"Android Developer",
"iOS Developer",
"Desktop Developer",
"Game Developer",
"Embedded Engineer",
"Embedded Software Engineer",
"Firmware Engineer",
"Firmware Developer",
"Java Developer",
"Python Developer",
"C++ Developer",
"C Developer",
"C# Developer",
".NET Developer",
"Node.js Developer",
"React Developer",
"Angular Developer",
"Vue Developer",
"PHP Developer",
"Go Developer",
"Rust Developer",
"Ruby Developer",
"Perl Developer",
"Swift Developer",
"Kotlin Developer",
"Flutter Developer",
"React Native Developer",

########################
# Data
########################

"Data Scientist",
"Senior Data Scientist",
"Lead Data Scientist",
"Principal Data Scientist",
"Data Analyst",
"Business Analyst",
"Business Intelligence Analyst",
"BI Analyst",
"BI Developer",
"Data Engineer",
"Analytics Engineer",
"Machine Learning Engineer",
"AI Engineer",
"ML Engineer",
"Deep Learning Engineer",
"NLP Engineer",
"Computer Vision Engineer",
"MLOps Engineer",
"Prompt Engineer",
"LLM Engineer",
"Research Scientist",
"Research Engineer",
"Decision Scientist",
"Statistician",
"Data Architect",
"Data Consultant",
"Data Governance Specialist",
"Data Steward",

########################
# Cloud
########################

"AWS Engineer",
"Azure Engineer",
"GCP Engineer",
"Cloud Engineer",
"Cloud Architect",
"Cloud Administrator",
"Cloud Consultant",

########################
# DevOps
########################

"DevOps Engineer",
"Platform Engineer",
"Infrastructure Engineer",
"Site Reliability Engineer",
"Kubernetes Engineer",
"Docker Engineer",

########################
# Cybersecurity
########################

"Cyber Security Engineer",
"Security Engineer",
"SOC Analyst",
"Security Analyst",
"Penetration Tester",
"Ethical Hacker",
"Security Consultant",

########################
# Networking
########################

"Network Engineer",
"Network Administrator",
"System Administrator",
"Linux Engineer",
"Windows Administrator",
"IT Support Engineer",
"Desktop Support Engineer",
"Help Desk Technician",

########################
# QA
########################

"QA Engineer",
"QA Analyst",
"Automation Tester",
"Manual Tester",
"SDET",
"Test Engineer",
"Validation Engineer",
"Performance Tester",

]
KEYWORDS += [

# # ==========================
# # Software & Development
# # ==========================
# "Software Tester","QA Tester","Release Engineer","Build Engineer",
# "Application Engineer","Systems Engineer","Solutions Engineer",
# "Technical Support Engineer","Software Consultant",
# "Technical Consultant","ERP Consultant","SAP Consultant",
# "Oracle Developer","Oracle DBA","SQL Developer","Database Developer",
# "Database Administrator","CRM Consultant","Salesforce Administrator",
# "Salesforce Consultant","Dynamics 365 Consultant","ServiceNow Developer",
# "ServiceNow Administrator","DevSecOps Engineer","Integration Engineer",
# "API Developer","Microservices Developer",

# # ==========================
# # AI / Data
# # ==========================
# "AI Scientist","AI Consultant","Data Mining Engineer",
# "Data Visualization Engineer","Data Modeler","Data Modeller",
# "Big Data Engineer","ETL Engineer","ETL Developer",
# "Data Warehouse Engineer","Data Quality Engineer",
# "Data Quality Analyst","Analytics Consultant",
# "Business Intelligence Developer","Power BI Developer",
# "Tableau Developer","Visualization Analyst",

# # ==========================
# # Product
# # ==========================
# "Product Owner","Technical Product Owner",
# "Associate Product Manager","Senior Product Manager",
# "Principal Product Manager","Group Product Manager",
# "Product Marketing Manager","Product Designer",
# "Technical Program Manager",

# # ==========================
# # Management
# # ==========================
"Engineering Manager","Software Engineering Manager",
"Development Manager","Delivery Manager","Program Director",
"Project Coordinator","Technical Manager",
"IT Manager","Technology Manager","Operations Director",
"General Manager","Regional Manager","Area Manager",
"Branch Manager","Team Lead","Technical Lead",
"Engineering Lead","Development Lead",

# # ==========================
# # Finance
# # ==========================
# "Financial Controller","Finance Executive",
# "Finance Officer","Finance Director",
# "Chartered Accountant","Cost Accountant",
# "Management Accountant","Accounts Executive",
# "Accounts Payable","Accounts Receivable",
# "Payroll Executive","Payroll Specialist",
# "Treasury Manager","Tax Analyst",
# "Tax Consultant","Risk Manager",
# "Investment Analyst","Investment Manager",
# "Portfolio Manager","Wealth Manager",
# "Relationship Manager","Bank Manager",
# "Credit Manager","Loan Officer",
# "Equity Analyst","Research Analyst",

# # ==========================
# # Banking
# # ==========================
# "Bank Teller","Relationship Executive",
# "Credit Analyst","Mortgage Advisor",
# "Financial Advisor","Insurance Advisor",
# "Insurance Agent","Claims Adjuster",
# "Underwriter","Actuary",

# # ==========================
# # HR
# # ==========================
"HR Executive","HR Officer","HR Coordinator",
"HR Generalist","HR Specialist",
"HR Business Partner","Talent Acquisition Specialist",
"Talent Acquisition Manager","Recruitment Consultant",
"Recruitment Specialist","People Partner",
"People Operations Manager",

# # ==========================
# # Marketing
# # ==========================
# "Marketing Executive","Marketing Specialist",
# "Marketing Analyst","Brand Executive",
# "Brand Manager","Growth Manager",
# "Growth Marketing Manager","Performance Marketing Manager",
# "Performance Marketer","SEO Executive",
# "SEO Analyst","SEM Specialist",
# "PPC Manager","Digital Strategist",
# "Content Strategist","Social Media Executive",
# "Email Marketing Specialist","CRM Manager",

# # ==========================
# # Sales
# # ==========================
# "Sales Associate","Sales Consultant",
# "Sales Representative","Sales Coordinator",
# "Sales Advisor","Sales Officer",
# "Business Development Executive",
# "Business Development Representative",
# "Business Development Associate",
# "Inside Sales Executive",
# "Inside Sales Representative",
# "Account Executive","Account Manager",
# "Key Account Manager",

# # ==========================
# # Healthcare
# # ==========================
# "General Physician","Medical Officer",
# "Medical Doctor","Registered Nurse",
# "Nurse Practitioner","Clinical Nurse",
# "ICU Nurse","Staff Nurse",
# "Dentist","Dental Assistant",
# "Dental Hygienist","Pharmacist",
# "Clinical Pharmacist","Radiologist",
# "Radiographer","Lab Technician",
# "Medical Technologist","Medical Assistant",
# "Clinical Research Associate",
# "Clinical Research Coordinator",
# "Clinical Manager","Physician Assistant",
# "Veterinarian","Occupational Therapist",
# "Speech Therapist","Psychologist",
# "Counsellor","Social Worker",

# # ==========================
# # Engineering
# # ==========================
# "Mechanical Design Engineer",
# "Manufacturing Engineer",
# "Production Engineer",
# "Production Manager",
# "Production Supervisor",
# "Plant Engineer","Plant Manager",
# "Maintenance Engineer",
# "Maintenance Technician",
# "Maintenance Manager",
# "Automation Engineer",
# "Robotics Engineer",
# "PLC Programmer",
# "Instrumentation Engineer",
# "Electrical Technician",
# "Electronics Technician",
# "Civil Site Engineer",
# "Construction Engineer",
# "Site Supervisor",
# "Quantity Surveyor",
# "Survey Engineer",
# "Marine Engineer",
# "Mining Engineer",
# "Aerospace Engineer",
# "Automotive Engineer",
# "Environmental Engineer",

# # ==========================
# # Logistics
# # ==========================
# "Logistics Coordinator",
# "Supply Planner",
# "Supply Chain Analyst",
# "Warehouse Associate",
# "Warehouse Supervisor",
# "Warehouse Manager",
# "Inventory Analyst",
# "Inventory Controller",
# "Procurement Executive",
# "Procurement Officer",
# "Purchasing Specialist",
# "Sourcing Specialist",

# # ==========================
# # Hospitality
# # ==========================
# "Restaurant Manager",
# "Assistant Restaurant Manager",
# "Hotel Supervisor",
# "Front Office Executive",
# "Front Office Manager",
# "Guest Relations Executive",
# "Guest Service Associate",
# "Housekeeping Supervisor",
# "Housekeeping Manager",
# "Kitchen Manager",
# "Sous Chef","Executive Chef",
# "Commis Chef","Pastry Chef",
# "Bartender","Barista","Waiter","Waitress",

# # ==========================
# # Education
# # ==========================
# "School Teacher","Math Teacher",
# "Science Teacher","English Teacher",
# "Assistant Professor",
# "Associate Professor",
# "Professor","Lecturer",
# "Tutor","Trainer",
# "Corporate Trainer",
# "Research Fellow",
# "Research Assistant",

# # ==========================
# # Design
# # ==========================
# "Graphic Artist","Creative Designer",
# "Motion Graphics Designer",
# "Animator","Illustrator",
# "Industrial Designer",
# "Interior Designer",
# "Fashion Designer",
# "Web Designer",
# "UX Researcher",
# "UI Developer",

# # ==========================
# # Legal
# # ==========================
# "Legal Counsel","Corporate Lawyer",
# "Legal Executive","Legal Officer",
# "Legal Associate","Compliance Analyst",
# "Compliance Manager",
# "Company Secretary",
# "Paralegal",

# # ==========================
# # Retail
# # ==========================
# "Retail Associate","Retail Supervisor",
# "Store Associate","Store Supervisor",
# "Store Manager","Cashier",
# "Merchandiser","Visual Merchandiser",

# # ==========================
# # Manufacturing
# # ==========================
# "Machine Operator",
# "CNC Operator",
# "CNC Programmer",
# "Assembly Technician",
# "Assembly Operator",
# "Quality Inspector",
# "Quality Assurance Engineer",
# "Quality Control Engineer",
# "Production Operator",

# # ==========================
# # Government / Public
# # ==========================
# "Administrative Officer",
# "Administrative Assistant",
# "Office Administrator",
# "Office Assistant",
# "Executive Assistant",
# "Receptionist",
# "Clerk","Data Entry Operator",

# # ==========================
# # Generic
# # ==========================
# "Specialist","Executive","Officer",
# "Coordinator","Supervisor","Associate",
# "Consultant","Technician","Engineer",
# "Developer","Manager","Director",
# "Lead","Head","Principal",
# "Intern","Trainee","Apprentice"
]

# KEYWORDS+= [
#     "Artificial Intelligence",
#     "Machine Learning",
#     "Cyber Security",
#     "Cloud Computing",
#     "Healthcare",
#     "Finance",
#     "Banking",
#     "Insurance",
#     "Retail",
#     "Manufacturing",
#     "Construction",
#     "Education",
#     "Hospitality",
#     "Logistics",
#     "Automotive",
#     "Telecommunications",
#     "Energy",
#     "Oil and Gas",
#     "Pharmaceutical",
#     "Biotechnology",
#     "Government",
#     "Agriculture",
#     "E-commerce",
#     "Media",
#     "Aviation",
#     "Marine"
# ]
