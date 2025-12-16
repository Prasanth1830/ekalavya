import streamlit as st
import sys
import os
from datetime import datetime

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from crewai_template.crew import CrewaiTemplate
except ImportError:
    st.error("❌ Error: Could not import CrewaiTemplate. Please ensure you're in the project root directory.")
    st.stop()

st.header("🚀 CrewAI Demos")
st.write("Choose your AI crew mission:")

menu_options = {
    "🔬 Technology Research (OpenCV Analysis)": "1",
    "📊 Market Analysis (Electric Vehicles)": "2",
    "🏢 Business Intelligence (AI Startups)": "3",
    "🎨 Content Strategy (Social Media)": "4",
    "🔧 Technical Analysis (Cloud Architecture)": "5",
    "💡 Innovation Research (Quantum Computing)": "6",
    "🌟 Custom Topic (Your Choice)": "7",
    "❓ Help & Information": "8",
}

choice_label = st.selectbox("Select a mission:", options=list(menu_options.keys()))
choice = menu_options[choice_label]

if choice == "8":
    st.info("""
🔍 CrewAI Template Demo Help
============================

This demo showcases how AI agents collaborate to research topics and generate insights.

🤖 What happens during a demo:
1. Research Agent investigates the topic using various sources
2. Reporting Analyst synthesizes findings into a comprehensive report
3. Final report is saved to 'report.md' in the project directory

⚡ Features demonstrated:
• Multi-agent collaboration
• Real-time task execution
• Comprehensive research and analysis
• Professional report generation
• Configurable workflows

🎯 Best practices:
• Be specific with your topics for better results
• Use focus areas to guide the analysis direction
• Check the generated report.md for detailed insights

🔧 Technical details:
• Powered by CrewAI framework
• Uses OpenAI GPT models
• Includes web research capabilities
• Generates markdown reports

🐳 Docker Commands:
• Run this demo: docker compose run --rm crew python demo.py
• Run examples: docker compose run --rm crew python examples/business_analysis_example.py
• Interactive shell: docker compose run --rm crew python
• Main application: docker compose up
""")
elif choice == "7":
    st.subheader("🌟 Custom Topic Analysis")
    topic = st.text_input("Enter your research topic:")
    focus_areas = st.text_input("Enter focus areas (optional):")
    if st.button("Run Custom Analysis"):
        if not topic:
            st.warning("❌ No topic provided.")
        else:
            config = {
                "name": "Custom Analysis",
                "inputs": {
                    "topic": topic,
                    "focus_areas": focus_areas or "comprehensive analysis",
                    "analysis_depth": "detailed",
                    "current_year": str(datetime.now().year)
                }
            }
            st.write(f"🚀 Starting {config['name']}...")
            st.write(f"📊 Topic: {config['inputs']['topic']}")
            if 'focus_areas' in config['inputs']:
                st.write(f"🎯 Focus: {config['inputs']['focus_areas']}")

            with st.spinner("⏱️ Crew is running... This may take a few minutes..."):
                try:
                    # Initialize and run the crew
                    crew = CrewaiTemplate().crew()
                    result = crew.kickoff(inputs=config['inputs'])

                    st.success("✅ Analysis Complete!")
                    st.markdown("📄 **Detailed report saved to: `report.md`**")
                    st.markdown("🎉 **Check the file for comprehensive insights!**")

                    st.markdown("---")
                    st.subheader("Crew Execution Result:")
                    st.markdown(result)

                except Exception as e:
                    st.error(f"❌ Error during analysis: {e}")
                    st.warning("💡 Make sure you have: \n- Valid OpenAI API key in .env file\n- Internet connection for research\n- All dependencies installed")

else:
    configs = {
        "1": {
            "name": "Technology Research",
            "inputs": {
                "topic": "OpenCV Computer Vision Library",
                "focus_areas": "latest features, performance improvements, real-world applications",
                "analysis_depth": "comprehensive",
                "current_year": str(datetime.now().year)
            }
        },
        "2": {
            "name": "Market Analysis",
            "inputs": {
                "topic": "Electric Vehicle Market Trends",
                "industry": "Automotive",
                "region": "Global",
                "timeframe": "2024-2026",
                "focus_areas": "market growth, key players, adoption barriers, opportunities",
                "current_year": str(datetime.now().year)
            }
        },
        "3": {
            "name": "Business Intelligence",
            "inputs": {
                "topic": "AI Startup Ecosystem",
                "analysis_type": "business intelligence",
                "focus_areas": "funding trends, successful companies, market gaps, investment opportunities",
                "current_year": str(datetime.now().year)
            }
        },
        "4": {
            "name": "Content Strategy",
            "inputs": {
                "topic": "Social Media Marketing for B2B SaaS",
                "content_type": "strategy development",
                "target_audience": "business decision makers",
                "focus_areas": "platform selection, content formats, engagement tactics, ROI measurement",
                "current_year": str(datetime.now().year)
            }
        },
        "5": {
            "name": "Technical Analysis",
            "inputs": {
                "topic": "Cloud Architecture Best Practices",
                "technical_focus": "scalability and security",
                "focus_areas": "microservices, containerization, security patterns, cost optimization",
                "current_year": str(datetime.now().year)
            }
        },
        "6": {
            "name": "Innovation Research",
            "inputs": {
                "topic": "Quantum Computing Applications",
                "research_type": "emerging technology",
                "focus_areas": "practical applications, current limitations, future potential, investment landscape",
                "current_year": str(datetime.now().year)
            }
        }
    }
    config = configs.get(choice)
    st.subheader(f"🚀 {config['name']}")
    st.write(f"**Topic:** {config['inputs']['topic']}")
    if 'focus_areas' in config['inputs']:
        st.write(f"**Focus Areas:** {config['inputs']['focus_areas']}")

    if st.button(f"Run {config['name']}"):
        st.write(f"🚀 Starting {config['name']}...")
        st.write(f"📊 Topic: {config['inputs']['topic']}")
        if 'focus_areas' in config['inputs']:
            st.write(f"🎯 Focus: {config['inputs']['focus_areas']}")
        
        with st.spinner("⏱️ Crew is running... This may take a few minutes..."):
            try:
                # Initialize and run the crew
                crew = CrewaiTemplate().crew()
                result = crew.kickoff(inputs=config['inputs'])

                st.success("✅ Analysis Complete!")
                st.markdown("📄 **Detailed report saved to: `report.md`**")
                st.markdown("🎉 **Check the file for comprehensive insights!**")

                st.markdown("---")
                st.subheader("Crew Execution Result:")
                st.markdown(result)

            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")
                st.warning("💡 Make sure you have: \n- Valid OpenAI API key in .env file\n- Internet connection for research\n- All dependencies installed")
