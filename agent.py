import os
from dotenv import load_dotenv
from google import genai

# 1. Load Governance & Security
load_dotenv()

class PMOConsultantAgent:
    def __init__(self):
        # Initialize the new genai Client using your Google Cloud API Key
        api_key = os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.model_id = 'gemini-2.5-flash' 
        
        # 2. Strategic System Prompt (The Governance Framework)
        self.system_instructions = """
        ROLE: Senior Strategic Program Manager & Management Consultant.
        
        OBJECTIVE: Analyze project health data (CPI, SPI, Risk Scores) and provide a 
        concise 'Executive Intervention Brief' for the Portfolio Steering Committee.
        
        STAKEHOLDER FLEXIBILITY RULES:
        - TONE: Professional, objective, and outcome-driven.
        - FOCUS: Highlight projects where CPI < 0.9 or SPI < 0.9 as 'CRITICAL'.
        - MITIGATION: Always suggest one technical and one organizational action.
        
        CONSTRAINTS: Do not exceed 150 words per brief. Do not use overly technical jargon.
        """

    def generate_brief(self, data_summary):
        # 3. Execution Logic
        full_prompt = f"{self.system_instructions}\n\nDATA TO ANALYZE:\n{data_summary}"
        
        try:
            # New SDK syntax for content generation
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=full_prompt,
            )
            return response.text
        except Exception as e:
            return f"Strategic Analysis Error: {str(e)}"

if __name__ == "__main__":
    # Test Block
    agent = PMOConsultantAgent()
    print("\n--- AI AGENT TEST START ---")
    sample_data = "PRJ-2026-005: CPI=0.82, SPI=1.1, Risk=8. Status: Resource attrition."
    print(agent.generate_brief(sample_data))
    print("--- AI AGENT TEST COMPLETE ---")