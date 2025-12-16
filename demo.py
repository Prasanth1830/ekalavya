#!/usr/bin/env python
"""
🚀 CrewAI Template Demo
======================

Interactive demo showcasing the power of CrewAI with multiple use cases.
This script demonstrates different agent configurations and workflows.

Usage (Docker):
    docker compose run --rm crew python demo.py

Or direct execution:
    python demo.py
"""

import os
import sys
from datetime import datetime

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from crewai_template.crew import CrewaiTemplate
except ImportError:
    print("❌ Error: Could not import CrewaiTemplate. Please ensure you're in the project root directory.")
    print("💡 If running outside Docker, make sure to run: docker compose run --rm crew python demo.py")
    sys.exit(1)

def print_header():
    """Print the demo header with ASCII art."""
    print("""
🚀 ===================================================== 🚀
   ____                    _    ___   _____
  / ___|_ __ _____      __ / \\  |_ _| |_   _|__ _ __ ___  _ __
 | |   | '__/ _ \\ \\ /\\ / // _ \\  | |    | |/ _ \\ '_ ` _ \\| '_ \\
 | |___| | |  __/\\ V  V // ___ \\ | |    | |  __/ | | | | | |_) |
  \\____|_|  \\___| \\_/\\_//_/   \\_\\___|   |_|\\___|_| |_| |_| .__/
                                                       |_|
🤖 ===================================================== 🤖

    Welcome to the CrewAI Template Demo!
    Watch AI agents collaborate in real-time 🎬

""")

def show_menu():
    """Display the interactive menu."""
    print("🎯 Choose your AI crew mission:")
    print()
    print("1. 🔬 Technology Research (OpenCV Analysis)")
    print("2. 📊 Market Analysis (Electric Vehicles)")
    print("3. 🏢 Business Intelligence (AI Startups)")
    print("4. 🎨 Content Strategy (Social Media)")
    print("5. 🔧 Technical Analysis (Cloud Architecture)")
    print("6. 💡 Innovation Research (Quantum Computing)")
    print("7. 🌟 Custom Topic (Your Choice)")
    print("8. ❓ Help & Information")
    print("9. 🚪 Exit")
    print()

def get_demo_config(choice):
    """Get configuration based on user choice."""
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
    return configs.get(choice)

def run_custom_demo():
    """Run a custom demo with user-provided topic."""
    print("🌟 Custom Topic Analysis")
    print("=" * 30)

    topic = input("Enter your research topic: ").strip()
    if not topic:
        print("❌ No topic provided. Returning to menu...")
        return None

    focus_areas = input("Enter focus areas (optional): ").strip()

    config = {
        "name": "Custom Analysis",
        "inputs": {
            "topic": topic,
            "focus_areas": focus_areas or "comprehensive analysis",
            "analysis_depth": "detailed",
            "current_year": str(datetime.now().year)
        }
    }

    return config

def show_help():
    """Show help information."""
    print("""
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

Press Enter to return to the menu...
""")
    input()

def run_demo(config):
    """Run the selected demo configuration."""
    if not config:
        return

    print(f"\n🚀 Starting {config['name']}...")
    print("=" * 50)
    print(f"📊 Topic: {config['inputs']['topic']}")
    if 'focus_areas' in config['inputs']:
        print(f"🎯 Focus: {config['inputs']['focus_areas']}")
    print("⏱️  This may take a few minutes...")
    print()

    try:
        # Initialize and run the crew
        crew = CrewaiTemplate().crew()
        result = crew.kickoff(inputs=config['inputs'])

        print("\n" + "=" * 60)
        print("✅ Analysis Complete!")
        print("📄 Detailed report saved to: report.md")
        print("🎉 Check the file for comprehensive insights!")
        print("=" * 60)

        return result

    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        print("💡 Make sure you have:")
        print("   • Valid OpenAI API key in .env file")
        print("   • Internet connection for research")
        print("   • All dependencies installed")
        return None

def main():
    """Main demo loop."""
    print_header()

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "9":
            print("\n👋 Thanks for trying CrewAI Template!")
            print("🚀 Ready to build your own AI crews? Check out the examples/ directory!")
            break
        elif choice == "8":
            show_help()
        elif choice == "7":
            config = run_custom_demo()
            if config:
                run_demo(config)
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            config = get_demo_config(choice)
            run_demo(config)
        else:
            print("❌ Invalid choice. Please enter a number from 1-9.")

        if choice != "8":  # Don't pause after help
            input("\nPress Enter to continue...")
            print("\n" * 2)

if __name__ == "__main__":
    main()
