import streamlit as st

st.set_page_config(page_title="Prospect Research Intake", layout="centered")

st.title("🔍 Prospect Research App – Phase 1")
st.markdown("Fill in the core company information below. AI will take care of the rest.")

st.header("🟩 Company Information")

company_name = st.text_input("Company Name", placeholder="e.g., Acme Biotech")
website = st.text_input("Company Website", placeholder="https://www.acmebio.com")
industry_category = st.text_input("Industry Category", placeholder="e.g., MedTech, Fintech")
business_verticals = st.text_input("Business Vertical(s)", placeholder="e.g., Oncology, B2B SaaS, D2C")
region = st.text_input("Region / HQ Location", placeholder="e.g., Bengaluru, India")

st.header("🟧 Competitors (Optional)")

competitor_1 = st.text_input("Competitor 1 Name")
competitor_2 = st.text_input("Competitor 2 Name")
competitor_3 = st.text_input("Competitor 3 Name")
competitor_4 = st.text_input("Competitor 4 Name")
competitor_5 = st.text_input("Competitor 5 Name")

st.divider()

if st.button("Submit"):
    submitted_data = {
        "Company Name": company_name,
        "Website": website,
        "Industry Category": industry_category,
        "Business Verticals": business_verticals,
        "Region": region,
        "Competitors": [c for c in [competitor_1, competitor_2, competitor_3, competitor_4, competitor_5] if c]
    }
    
    st.success("✅ Prospect input submitted successfully!")
    st.json(submitted_data)

    st.info("Next step: AI research and analysis will run on this input.")
