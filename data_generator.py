import pandas as pd
import numpy as np

def generate_pmo_data(n_projects=20):
    # Reproducibility - vital for Audit and Governance
    np.random.seed(42)
    
    sectors = ['Banking', 'Healthcare', 'Public Sector', 'Telecom']
    project_names = [f"PRJ-2026-{i:03d}" for i in range(1, n_projects + 1)]
    
    # 1. Base Data Structure
    df = pd.DataFrame({
        'Project_ID': project_names,
        'Sector': [np.random.choice(sectors) for _ in range(n_projects)],
        'Planned_Value_USD': np.random.randint(500000, 2000000, n_projects)
    })
    
    # 2. Progress Metrics (Simulating Sabbatical Upskilling in NumPy)
    df['Percent_Complete'] = np.random.uniform(0.1, 0.95, n_projects).round(2)
    df['Earned_Value_USD'] = (df['Planned_Value_USD'] * df['Percent_Complete']).astype(int)
    
    # Actual Cost - simulating variance (some under, many over budget)
    df['Actual_Cost_USD'] = (df['Earned_Value_USD'] * np.random.uniform(0.8, 1.4, n_projects)).astype(int)
    
    # 3. Qualitative Attributes (For the AI Agent to analyze later)
    df['Risk_Score'] = np.random.randint(1, 11, n_projects)
    status_options = [
        "Stakeholder misalignment", "Legacy migration issues", 
        "Resource attrition", "On track", "UAT feedback pending"
    ]
    df['Status_Notes'] = [np.random.choice(status_options) for _ in range(n_projects)]

    # 4. Save Deliverable
    df.to_csv('pmo_dataset.csv', index=False)
    print("--- SUCCESS ---")
    print("Deliverable: pmo_dataset.csv generated with 20 records.")

if __name__ == "__main__":
    generate_pmo_data()