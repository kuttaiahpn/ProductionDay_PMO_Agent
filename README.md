🚀 Agentic PMO Co-Pilot: 
AI-Driven Portfolio Governance : Agentic PMO Co-Pilot is a sophisticated "Digital Twin" for Program Managers. It bridges the gap between raw project data and strategic decision-making by combining Earned Value Management (EVM) principles with Generative AI (Gemini 2.5 Flash).This tool doesn't just show you "what" happened; it tells you "why" it matters and "how" to fix it.

🏗️ Core ArchitectureThe solution is built on a modular three-tier architecture:Data Layer: Simulates and processes high-fidelity portfolio data (USD 20M+ scale).Engine Layer: A Python-based EVM processor that calculates CPI, SPI, and Risk indices.Intelligence Layer: A Generative AI agent (Gemini 2.5) acting as a Senior Strategic Consultant.

🧮 Backend Logic: The EVM EngineThe system moves beyond subjective RAG (Red-Amber-Green) status reporting by utilizing objective mathematical indices:CPI (Cost Performance Index): $CPI = \frac{EV}{AC}$Governance Threshold: Values < 0.9 trigger a Financial Risk Alert.SPI (Schedule Performance Index): $SPI = \frac{EV}{PV}$Governance Threshold: Values < 0.9 trigger a Timeline Delay Alert.

💻 Tech StackLanguage: Python 3.xFramework: Streamlit (Web UI)Analysis: Pandas & NumPyVisuals: Plotly ExpressAI: Google Gemini 2.5 Flash APIDevOps: Git, GitHub, Dotenv (Security), Streamlit Cloud (Production)🚀 Deployment & InstallationLocal SetupClone the Repo:DOSgit clone https://github.com/YOUR_USERNAME/ProductionDay_PMO_Agent.git
cd ProductionDay_PMO_Agent
Environment Configuration:Create a .env file and add your API key:PlaintextGOOGLE_API_KEY=your_gemini_api_key
Install Dependencies:DOSpip install -r requirements.txt
Run the App:DOSstreamlit run app.py

🎨 Dashboard & InsightsThe current MVP features a real-time data table with conditional formatting and an AI Strategic Intervention Brief.Roadmap: The Multi-Agent FuturePhase 1 (Complete): EVM Engine & Single Agent Integration.Phase 2: Interactive Health Heatmaps & Risk Radar Charts.Phase 3: Multi-Agent Orchestration (MAS) — introducing a Financial Auditor Agent, a Risk Sentinel Agent, and a Stakeholder Sentiment Agent.

👨‍💼 Developed By: Kuttaiah P N | Strategic Program Manager | AI-Enabled PMO