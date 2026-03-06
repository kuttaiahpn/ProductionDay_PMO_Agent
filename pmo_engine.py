import pandas as pd

class PMOEngine:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def calculate_metrics(self):
        # CPI (Cost Performance Index) = EV / AC
        self.df['CPI'] = (self.df['Earned_Value_USD'] / self.df['Actual_Cost_USD']).round(2)
        
        # SPI (Schedule Performance Index) = EV / PV (Planned Value)
        self.df['SPI'] = (self.df['Earned_Value_USD'] / self.df['Planned_Value_USD']).round(2)
        
        return self.df

    def get_at_risk_projects(self):
        # A PMO standard: CPI < 1.0 means over budget; SPI < 1.0 means behind schedule
        at_risk = self.df[(self.df['CPI'] < 0.9) | (self.df['SPI'] < 0.9)]
        return at_risk

if __name__ == "__main__":
    engine = PMOEngine('pmo_dataset.csv')
    processed_df = engine.calculate_metrics()
    at_risk_df = engine.get_at_risk_projects()
    
    print("\n--- PMO Engine Analysis ---")
    print(f"Total Projects Analyzed: {len(processed_df)}")
    print(f"Projects Requiring Intervention: {len(at_risk_df)}")
    print("\nTop 3 At-Risk Projects:")
    print(at_risk_df[['Project_ID', 'CPI', 'SPI', 'Status_Notes']].head(3))