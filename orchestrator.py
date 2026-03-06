import pandas as pd
from pmo_engine import PMOEngine
from agent import PMOConsultantAgent

def run_pmo_automation():
    print("--- 🚀 Starting Agentic PMO Analysis ---")
    
    # 1. Initialize the Engine and Agent
    engine = PMOEngine('pmo_dataset.csv')
    consultant = PMOConsultantAgent()
    
    # 2. Identify At-Risk Projects (Python Logic)
    engine.calculate_metrics()
    at_risk_projects = engine.get_at_risk_projects()
    
    # 3. Format data for the AI
    # We convert the top 3 at-risk projects to a string format for the AI
    summary_for_ai = at_risk_projects[['Project_ID', 'CPI', 'SPI', 'Status_Notes']].head(3).to_string()
    
    print(f"Feeding {len(at_risk_projects)} at-risk projects to the Consultant Agent...")
    
    # 4. Generate AI Insight
    executive_brief = consultant.generate_brief(summary_for_ai)
    
    print("\n--- 📈 EXECUTIVE INTERVENTION BRIEF ---")
    print(executive_brief)
    print("\n--- ✅ Analysis Complete ---")

if __name__ == "__main__":
    run_pmo_automation()