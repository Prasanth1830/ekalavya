import streamlit as st
import pandas as pd
import time

# --- Mock Data Functions (Simulating Worker Agents) ---

def iqvia_insights_agent(molecule):
    with st.spinner(f"🔬 **IQVIA Insights Agent:** Analyzing market for '{molecule}'..."):
        time.sleep(1.5)
        data = {
            'Therapy Area': ['Respiratory', 'Cardiology', 'Oncology'],
            'Market Size (USD Millions)': [1500, 2200, 3500],
            'CAGR (%)': [5.2, 4.1, 12.5],
            'Competition Level': ['High', 'Medium', 'High']
        }
        df = pd.DataFrame(data)
        st.table(df)
        return {
            "summary": f"The market for {molecule} shows significant activity, especially in Oncology.",
            "data": df
        }

def exim_trends_agent(molecule):
    with st.spinner(f"✈️ **EXIM Trends Agent:** Tracking trade for '{molecule}'..."):
        time.sleep(1.5)
        data = {
            'Country': ['India', 'China', 'USA', 'Germany'],
            'Export Volume (Tons)': [1200, 3000, 500, 800],
            'Import Volume (Tons)': [300, 150, 1500, 600]
        }
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index('Country'))
        return {
            "summary": f"China is a major exporter of {molecule}, while the USA is a major importer.",
            "data": df
        }

def patent_landscape_agent(molecule):
    with st.spinner(f"📜 **Patent Landscape Agent:** Scanning patents for '{molecule}'..."):
        time.sleep(1.5)
        data = {
            'Patent ID': ['US-2023-001A1', 'US-2021-002B2', 'EP-1234567B1'],
            'Assignee': ['PharmaCorp', 'BioGen', 'InnovatePharma'],
            'Expiry Date': ['2035-12-01', '2028-05-15', '2030-08-22'],
            'FTO Flag': ['Clear', 'Potential Risk', 'Clear']
        }
        df = pd.DataFrame(data)
        st.table(df)
        return {
            "summary": f"There are several active patents for {molecule}, with one potential FTO risk.",
            "data": df
        }

def clinical_trials_agent(indication):
    with st.spinner(f"🏥 **Clinical Trials Agent:** Investigating trials for '{indication}'..."):
        time.sleep(1.5)
        data = {
            'Trial ID': ['NCT12345', 'NCT67890', 'NCT54321'],
            'Sponsor': ['BigPharma', 'University Hospital', 'ResearchCo'],
            'Phase': ['Phase III', 'Phase II', 'Phase I'],
            'Status': ['Recruiting', 'Completed', 'Active']
        }
        df = pd.DataFrame(data)
        st.table(df)
        return {
            "summary": f"There are several ongoing clinical trials for {indication}, including a Phase III trial.",
            "data": df
        }

def internal_knowledge_agent(uploaded_file):
    with st.spinner(f"📄 **Internal Knowledge Agent:** Summarizing internal document '{uploaded_file.name}'..."):
        time.sleep(2)
        summary = f"""
The internal document '{uploaded_file.name}' highlights a strategic focus on respiratory diseases.
Key takeaways include:
- A gap in the market for pediatric formulations.
- Previous research on molecule X showed promise but was discontinued due to formulation challenges.
"""
        st.markdown(summary)
        return {"summary": summary}


def web_intelligence_agent(topic):
    with st.spinner(f"🌐 **Web Intelligence Agent:** Searching web for '{topic}'..."):
        time.sleep(1.5)
        summary = f"""
Recent publications suggest that '{topic}' is a growing area of research.
- [Link to a relevant scientific paper on PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- [News article about a recent breakthrough](https://www.fiercepharma.com/)
"""
        st.markdown(summary)
        return {
            "summary": summary
        }

def report_generator_agent(results):
    with st.spinner("📝 **Report Generator Agent:** Compiling report..."):
        time.sleep(1)
        report_content = "# AI-Powered Pharmaceutical Research Report\n\n"
        for key, value in results.items():
            report_content += f"## {key}\n\n"
            report_content += f"{value['summary']}\n\n"
            if "data" in value and isinstance(value["data"], pd.DataFrame):
                report_content += value["data"].to_markdown(index=False)
                report_content += "\n\n"
    return report_content

# --- Main Page UI ---

st.header("🔬 Pharma Agentic AI Solution")
st.write(