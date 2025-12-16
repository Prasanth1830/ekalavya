# CrewAI Template

A production-ready template for building AI crews using CrewAI - the cutting-edge framework for orchestrating collaborative AI agents.

## 🌟 What Makes This Template Special

- **🤖 Multi-Agent Collaboration**: Watch AI agents work together like a real team
- **🔧 Production-Ready**: Docker containerization, proper logging, and error handling
- **📊 Rich Reporting**: Automatic report generation with structured outputs
- **🛠️ Extensible Tools**: Easy-to-add custom tools for any domain
- **⚡ Latest CrewAI**: Always updated to the newest CrewAI version (0.134.0+)
- **🎯 Real Examples**: Working examples that demonstrate powerful AI workflows

## 🚀 Quick Start

1. **Clone and Setup**:
```bash
git clone https://github.com/scotthavird/crewai-template
cd crewai-template
./setup.sh your_project_name
```

2. **Configure Environment**:
```bash
cp .env.example .env
# Add your OpenAI API key to .env
```

3. **Launch Your AI Crew**:
```bash
docker compose up --build
```

Watch your AI agents collaborate in real-time! 🎬

## 💡 Use Case Examples

This template can be adapted for various exciting use cases:

### 🔬 Research & Analysis
- **Market Research**: Agents gather data, analyze trends, create reports
- **Academic Research**: Literature review, data analysis, paper writing
- **Competitive Intelligence**: Monitor competitors, analyze strategies

### 📈 Business Intelligence
- **Financial Analysis**: Data collection, trend analysis, investment recommendations
- **Product Development**: Market research, feature analysis, roadmap planning
- **Risk Assessment**: Data gathering, risk modeling, mitigation strategies

### 🎨 Content Creation
- **Blog Writing**: Research topics, write articles, optimize for SEO
- **Social Media**: Content planning, post creation, engagement analysis
- **Marketing Campaigns**: Strategy development, content creation, performance tracking

### 🔧 Technical Projects
- **Code Review**: Analyze codebases, identify issues, suggest improvements
- **Documentation**: Generate technical docs, API references, tutorials
- **System Analysis**: Architecture review, performance optimization

## 🏗️ Project Structure

```
src/your_project_name/
├── main.py                 # 🎯 Entry point & configuration
├── crew.py                # 🤖 Agent & crew definitions
├── config/
│   ├── agents.yaml        # 👥 Agent personalities & roles
│   └── tasks.yaml         # 📋 Task definitions & workflows
└── tools/
    ├── custom_tool.py     # 🛠️ Your custom tools
    ├── web_scraper.py     # 🌐 Web scraping capabilities
    ├── data_analyzer.py   # 📊 Data analysis tools
    └── file_manager.py    # 📁 File operations
```

## 🎭 Agent Personalities

Our template includes pre-configured agent archetypes:

- **🔍 Senior Researcher**: Deep analysis, fact-checking, comprehensive investigation
- **📊 Reporting Analyst**: Data synthesis, clear communication, structured reporting
- **🎨 Creative Writer**: Engaging content, storytelling, audience adaptation
- **🔧 Technical Expert**: Code analysis, system design, best practices

## 🛠️ Built-in Tools

The template comes with powerful tools out of the box:

- **🌐 Web Research Tool**: Intelligent web scraping and data extraction
- **📊 Data Analysis Tool**: Statistical analysis and visualization
- **📁 File Management Tool**: Read, write, and organize files
- **🔍 Search Tool**: Advanced search capabilities across multiple sources
- **📈 Reporting Tool**: Generate professional reports in multiple formats

## 🚀 Advanced Features

### 🔄 Workflow Orchestration
```python
# Define complex multi-step workflows
workflow = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,  # or Process.hierarchical
    verbose=True
)
```

### 📊 Real-time Monitoring
- Live agent status updates
- Task progress tracking
- Performance metrics
- Error handling and recovery

### 🎯 Customizable Outputs
- Markdown reports
- JSON data exports
- PDF generation
- Interactive dashboards

## 🔧 Configuration Examples

### Quick Research Project
```yaml
# agents.yaml
researcher:
  role: "AI Research Specialist"
  goal: "Discover cutting-edge developments in {topic}"
  backstory: "Expert in finding and analyzing the latest innovations"
```

### Business Analysis Crew
```yaml
# tasks.yaml
market_analysis:
  description: "Analyze market trends for {product}"
  expected_output: "Comprehensive market analysis with actionable insights"
  agent: market_analyst
```

## 🎬 Live Demo

Want to see it in action? Check out these example runs:

1. **Interactive Demo**: `docker compose run --rm crew python demo.py`
2. **Business Analysis**: `docker compose run --rm crew python examples/business_analysis_example.py`
3. **Default Research**: `docker compose up` (OpenCV research)

## 🚀 Getting Started Examples

### Example 1: Market Research
```bash
docker compose run --rm crew python -c "
from src.crewai_template.crew import CrewaiTemplate
crew = CrewaiTemplate().crew()
result = crew.kickoff(inputs={
    'topic': 'Electric Vehicle Market 2025',
    'industry': 'Automotive',
    'region': 'North America'
})
"
```

### Example 2: Technical Analysis
```bash
docker compose run --rm crew python -c "
from src.crewai_template.crew import CrewaiTemplate
crew = CrewaiTemplate().crew()
result = crew.kickoff(inputs={
    'topic': 'Kubernetes Security Best Practices',
    'depth': 'comprehensive',
    'audience': 'DevOps Engineers'
})
"
```

### Example 3: Content Strategy
```bash
docker compose run --rm crew python -c "
from src.crewai_template.crew import CrewaiTemplate
crew = CrewaiTemplate().crew()
result = crew.kickoff(inputs={
    'topic': 'AI in Healthcare',
    'format': 'blog series',
    'target_audience': 'healthcare professionals'
})
"
```

## 🎯 Development Commands

All development happens inside Docker containers:

```bash
# Interactive demo with menu
docker compose run --rm crew python demo.py

# Run specific examples
docker compose run --rm crew python examples/business_analysis_example.py

# Interactive Python shell
docker compose run --rm crew python

# Shell access for debugging
docker compose run --rm crew bash

# Check installed packages
docker compose run --rm crew pip list

# Run tests
docker compose run --rm crew python -m pytest
```

## 🔧 Adding Dependencies

1. **Add to pyproject.toml**:
```toml
dependencies = [
    "crewai[tools]>=0.134.0,<1.0.0",
    "requests>=2.31.0",
    "your-new-package>=1.0.0",
]
```

2. **Rebuild container**:
```bash
docker compose build
```

3. **Test new dependency**:
```bash
docker compose run --rm crew python -c "import your_new_package; print('Success!')"
```

## 🎯 Next Steps

1. **Customize Your Agents**: Edit `config/agents.yaml` to define unique personalities
2. **Design Your Workflow**: Modify `config/tasks.yaml` for your specific use case
3. **Add Custom Tools**: Extend functionality in the `tools/` directory
4. **Scale Your Crew**: Add more agents for complex workflows
5. **Deploy to Production**: Use the included Docker setup for deployment

## 🤝 Contributing

We love contributions! Whether it's:
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎯 New use case examples

## 📚 Learn More

- [CrewAI Documentation](https://docs.crewai.com)
- [Agent Configuration Guide](https://docs.crewai.com/concepts/agents)
- [Task Orchestration](https://docs.crewai.com/concepts/tasks)
- [Custom Tools Development](https://docs.crewai.com/concepts/tools)

---

**Ready to build the future with AI agents?** 🚀 Start your journey today!
