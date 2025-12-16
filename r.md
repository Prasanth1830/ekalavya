 Pharmaceu cals  
About the business: A leading mul na onal generic pharmaceu cal company, with significant 
business in the US and a broad product por olio, seeks to diversify beyond the highly compe ve, 
low-margin generics market. The company aims to develop value-added, innova ve products by 
repurposing approved molecules for new indica ons, alterna ve dosage forms, or different pa ent 
popula ons—targe ng unmet medical needs. 
Problem statement: Iden fying such opportuni es requires extensive literature reviews, o en taking 
two to three months and involving mul ple itera ons to uncover viable product concepts. To 
accelerate this process, the company plans to adopt an Agen c AI solu on that integrates with 
various online sources and subscrip on-based databases. 
This AI-driven tool will enable users to interac vely explore poten al innova on cases, significantly 
reducing research me and increasing throughput. By enhancing the speed and quality of early-stage 
product evalua ons, the company aims to strengthen its pipeline with differen ated offerings that 
deliver greater clinical and commercial value. 
Goal: Teams must design an Agen c AI solu on where the Master Agent: 
• Can be linked to various regulatory websites, clinical trial websites, scien fic journals and paid 
databases (subscrip ons provided by the client), along with any internal databases of the client 
• Features a user interface that allows users to input prompts for finding informa on from the 
web, analyzing market data and summarize scien fic journals 
• Generates a summary report of the searches and save the report in an archival system 
Key deliverable: A 5 slider PPT showcasing the end-to-end journey from the ini al prompt of finding 
a molecule, iden fying its unmet needs, checking for ongoing clinical trials, exploring its probable 
use in other diseases, and determining if any patents have been filed, leading to the development of 
an innova ve product story. 
Agen c AI roles 
1. Master Agent (conversa on orchestrator) 
• Interprets user queries and breaks them into modular research tasks 
• Delegates tasks to domain-specific Worker Agents 
• Synthesizes responses from Worker Agents into coherent summaries with references 
• Responds with forma ed text, tables, charts or PDF reports as needed 
2. Worker Agents 
a. IQVIA Insights Agent 
• Queries IQVIA datasets for sales trends, volume shi s and therapy area dynamics 
• Outputs: Market size tables, CAGR trends, therapy-level compe on summaries 
b. EXIM Trends Agent 
• Extracts export-import data for APIs/formula ons across countries 
• Outputs: Trade volume charts, sourcing insights, import dependency tables 
c. Patent Landscape Agent 
• Searches USPTO and other IP databases for ac ve patents, expiry melines and FTO flags 
• Outputs: Patent status tables, compe ve filing heatmaps, PDF extracts of relevant patents 
d. Clinical Trials Agent 
• Fetches trial pipeline data from ClinicalTrials.gov or WHO ICTRP 
• Outputs: Tables of ac ve trials, sponsor profiles, trial phase distribu ons 
e. Internal Knowledge Agent 
• Retrieves and summarizes internal documents (e.g., MINS, strategy decks, field insights) 
• Outputs: Key takeaways, compara ve tables or downloadable briefing PDFs 
f. Web Intelligence Agent 
• Performs real- me web search for guidelines, scien fic publica ons, news and pa ent 
forums 
• Outputs: Hyperlinked summaries, quota ons from credible sources, guideline extracts 
g. Report Generator Agent 
• Formats the synthesized response into a polished PDF or Excel report 
• Outputs: PDF summaries with charts/tables, downloadable links in-chat 
ClinicalTrials.gov 
Data and system assump ons 
• Synthe c queries: The team will simulate at least 10 strategic ques ons that pharma planners 
might ask (e.g., “Which respiratory diseases show low compe on but high pa ent burden in 
India?”) 
Mock data sources: 
• IQVIA mock API: Returns market size, growth and compe tor data per therapy area 
• EXIM mock server: Simulated export or import volumes of APIs or formula ons 
• USPTO API clone: Mock API for patent filings, expiry melines and innova on trends 
• Clinical trials API stub: Simulated access to ongoing trials and their sponsors 
• Internal documents repository: Synthe c PDFs of past strategy decks and field reports 
• Web search proxy: Simulated web results for real- me signals and references 
• Report generator: Converts chatbot responses into a downloadable PDF summary 
• File upload (op onal): Upload mock internal document PDFs to be summarized by the agent 
Agen c AI Framework (CrewAI/LangGraph) 
1. Master Agent: Conversa on orchestrator 
• Understands por olio planning queries from the user 
• Decomposes ques ons and allocates subtasks to worker agents 
• Gathers, summarizes and formats findings into cohesive responses 
2. Worker Agents 
Agent responsibili es output type 
• IQVIA Insights Agent: Fetches market size, growth, compe tor data (tables and graphs) 
• EXIM Trade Agent: Summarizes import-export trends by molecule (tables, bullet insights) 
• Patent Landscape Agent: Lists relevant patent filings, expiry and FTO risks (patent tables, risk 
f
lags) 
• Clinical Trials Agent: Extracts trial pipeline informa on by indica on or MoA (trial summary 
tables) 
• Internal Insights Agent: Summarizes uploaded internal PDFs (key takeaways, PDF extracts) 
• Web Intelligence Agent: Performs mock web search for guidelines, RWE, news (text responses 
with links) 
• Report Generator Agent: Converts responses to PDF report (PDF download link in chat)