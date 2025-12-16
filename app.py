import streamlit as st
import yaml

st.set_page_config(
    page_title="Ekalavya - Home",
    page_icon="🤖",
    layout="wide"
)

st.header("Agents and Crews")

st.subheader("Available Agents")

# Mock data based on the structure of agents.yaml
agents_data = {
    'researcher': {
        'role': 'Senior Data Researcher',
        'goal': 'Uncover cutting-edge developments in a given topic',
        'backstory': "You're a seasoned researcher with a knack for uncovering the latest developments. Known for your ability to find the most relevant information and present it in a clear and concise manner."
    },
    'reporting_analyst': {
        'role': 'Reporting Analyst',
        'goal': 'Create detailed reports based on data analysis and research findings',
        'backstory': "You're a meticulous analyst with a keen eye for detail. You're known for your ability to turn complex data into clear and concise reports, making it easy for others to understand and act on the information you provide."
    }
}

cols = st.columns(len(agents_data))
for i, (agent_name, agent_details) in enumerate(agents_data.items()):
    with cols[i]:
        with st.container():
            st.info(f"**{agent_details['role']}**")
            st.write(f"**Goal:** {agent_details['goal']}")
            st.write(f"**Backstory:** {agent_details['backstory']}")

st.subheader("Crews")
st.write("A crew is a group of agents working together to achieve a common goal.")

with st.container():
    st.success("**Research Crew**")
    st.write("This crew is designed to perform comprehensive research on a given topic.")
    st.write("**Agents in this crew:** Senior Data Researcher, Reporting Analyst")
    st.button("Run Crew", key="run_crew_1")