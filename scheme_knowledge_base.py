SCHEMES = [

# =====================================================
# MARRIAGE SCHEMES
# =====================================================

{
"name": "Kalyana Lakshmi",
"category": "marriage_support",

"eligibility": {
    "age_min": 18,
    "religion_exclude": ["muslim"],
    "income_max": 200000,
    "community": ["sc","st","bc","ebc"]
},

"benefits": "₹1,00,116 financial assistance for marriage expenses",

"application": "Apply through Telangana ePASS or MeeSeva",

"documents": [
"Aadhaar Card",
"Income Certificate",
"Caste Certificate",
"Bank Passbook",
"Marriage Confirmation Certificate"
],

"notes": "For SC/ST/BC/EBC brides only"
},

{
"name": "Shaadi Mubarak",
"category": "marriage_support",

"eligibility": {
    "age_min": 18,
    "religion_only": ["muslim","sikh","christian","parsi","jain","buddhist"],
    "income_max": 200000
},

"benefits": "₹1,00,116 one-time marriage assistance",

"application": "Apply via Telangana ePASS portal",

"documents": [
"Aadhaar Card",
"Income Certificate",
"Bank Passbook"
],

"notes": "Only minority community brides eligible"
},

# =====================================================
# PREGNANCY / DELIVERY
# =====================================================

{
"name": "KCR Nutrition Kit",
"category": "pregnancy_support",

"eligibility": {
    "pregnant": True,
    "age_min": 18,
    "income_max": 120000,
    "children_limit": 2
},

"benefits": "Monthly nutrition kit + supplements during pregnancy",

"application": "Register through Anganwadi worker",

"documents": [
"Aadhaar",
"Income Certificate",
"Pregnancy Checkup Proof"
],

"notes": "Given during 2nd & 3rd trimester"
},

{
"name": "MCH Kit Scheme",
"category": "pregnancy_support",

"eligibility": {
    "pregnant": True,
    "delivery_in_govt_hospital": True,
    "children_limit": 2
},

"benefits": "₹12,000-₹13,000 financial aid + baby care kit",

"application": "Register at Government Hospital / PHC",

"documents": [
"Aadhaar",
"Bank Details",
"Mobile Number"
],

"notes": "Only for government hospital delivery"
},

{
"name": "Arogya Lakshmi",
"category": "nutrition_support",

"eligibility": {
    "pregnant_or_lactating": True
},

"benefits": "Daily nutritious meal, eggs, milk & supplements",

"application": "Registered automatically via Anganwadi",

"documents": [
"Aadhaar",
"Ration Card"
],

"notes": "All KCR Kit beneficiaries are eligible"
},

# =====================================================
# PENSION
# =====================================================

{
"name": "Aasara Pension - Widow",
"category": "pension_support",

"eligibility": {
    "widow": True,
    "age_min": 18
},

"benefits": "₹2016 monthly pension",

"application": "Apply at MeeSeva / Gram Panchayat",

"documents": [
"Aadhaar",
"Husband Death Certificate",
"Bank Passbook"
],

"notes": "For destitute widows"
},

{
"name": "Aasara Pension - Old Age",
"category": "pension_support",

"eligibility": {
    "age_min": 57
},

"benefits": "₹2016 monthly pension",

"application": "Village Secretariat / MeeSeva",

"documents": [
"Aadhaar",
"Age Proof",
"Bank Passbook"
],

"notes": "For senior citizens"
},

{
"name": "Aasara Pension - Single Women",
"category": "pension_support",

"eligibility": {
    "single_woman": True,
    "age_min": 35
},

"benefits": "₹2016 monthly pension",

"application": "MeeSeva",

"documents": [
"Aadhaar",
"Residence Proof",
"Bank Passbook"
],

"notes": "For divorced/unmarried women"
},

# =====================================================
# HEALTH
# =====================================================

{
"name": "Rajiv Aarogyasri",
"category": "health_support",

"eligibility": {
    "serious_illness": True,
    "low_income_family": True
},

"benefits": "Free medical treatment up to ₹10 lakh",

"application": "Visit government/empanelled hospital",

"documents": [
"Ration Card",
"BPL/White Card"
],

"notes": "Covers cancer, heart, kidney surgeries"
},

# =====================================================
# EMPLOYMENT / FINANCIAL
# =====================================================

{
"name": "Minority Mahila Yojana",
"category": "employment_support",

"eligibility": {
    "minority_woman": True,
    "age_min": 21,
    "age_max": 55,
    "income_max": 200000
},

"benefits": "₹50,000 business financial support",

"application": "Apply on OBMMS portal",

"documents": [
"Aadhaar",
"Income Certificate",
"Bank Details"
],

"notes": "For minority widows/divorcee women"
},

{
"name": "Free Sewing Machine Scheme",
"category": "employment_support",

"eligibility": {
    "skill_in_tailoring": True,
    "minority_woman": True,
    "age_min": 18,
    "age_max": 55
},

"benefits": "Free sewing machine",

"application": "Apply via OBMMS portal",

"documents": [
"Aadhaar",
"Training Certificate",
"Income Certificate"
],

"notes": "For unemployed minority women"
},

# =====================================================
# GENERAL WOMEN BENEFITS
# =====================================================

{
"name": "Mahalakshmi Scheme",
"category": "financial_support",

"eligibility": {
    "woman": True,
    "income_max": 200000
},

"benefits": "₹2500 monthly + ₹500 LPG + free bus travel",

"application": "Praja Palana centre",

"documents": [
"Aadhaar",
"Ration Card",
"Bank Account"
],

"notes": "For women heads of families"
},

{
"name": "Indiramma Saree Scheme",
"category": "financial_support",

"eligibility": {
    "woman": True
},

"benefits": "Free saree distribution",

"application": "No application required",

"documents": [
"Aadhaar"
],

"notes": "Distributed via government camps"
}

]