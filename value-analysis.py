import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_player_value(data):
    """
    Analyze player value vs wage to identify undervalued players
    """
    
    df = data[['ID','Name', 'Value', 'Wage', 'OVR']].copy()
    
    # Calculate value to wage ratio
    df['Value_to_Wage_Ratio'] = (df['Value'] / df['Wage']).round(2)
    
    # Calculate Z-scores for both Value and Wage
    df['Value_Z'] = (df['Value'] - df['Value'].mean()) / df['Value'].std()
    df['Wage_Z'] = (df['Wage'] - df['Wage'].mean()) / df['Wage'].std()
    
    # Define undervalued players as those with:
    # - Above average value (positive Value_Z)
    # - Below average wage (negative Wage_Z)
    # - High value-to-wage ratio
    undervalued = df[
        (df['Value_Z'] > 0) & 
        (df['Wage_Z'] < 0) & 
        (df['Value_to_Wage_Ratio'] > df['Value_to_Wage_Ratio'].median())
    ].sort_values('Value_to_Wage_Ratio', ascending=False)
    
    
    
    plt.figure(figsize=(12, 8))

    # wage_jitter = df['Wage'] * (1 + np.random.normal(0, 0.02, len(df)))
    
    # Scatter plot
    plt.scatter(df["Wage"], df['Value'], alpha=0.5, c='gray', label='All Players')
    plt.scatter(undervalued['Wage'], undervalued['Value'], 
               c='red', label='Underpaid Players')
    
    # Labels for undervalued players
    # for idx, row in undervalued.head(10).iterrows():
    #     plt.annotate(row['Name'],
    #                 (row['Wage'], row['Value']),
    #                 xytext=(5, 5),
    #                 textcoords='offset points',
    #                 fontsize=8,
    #                 bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    plt.xlabel('Weekly Wage (€)', fontsize=11)
    plt.ylabel('Market Value (€)', fontsize=11)
    plt.title('Player Value vs Wage Analysis\nRed points indicate underpaid players', 
              pad=20, fontsize=12, fontweight="bold")
    plt.legend()
    
    # Log scale for better visualization
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    stats_text = (
        f"Total Players: {len(df)}\n"
        f"Underpaid Players: {len(undervalued)}\n"
        f"Median Value/Wage Ratio: {df['Value_to_Wage_Ratio'].median():.1f}"
    )
    plt.text(0.02, 0.98, stats_text,
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.show()
    
    # Top undervalued players
    return undervalued[['ID','Name', 'OVR', 'Value', 'Wage', 'Value_to_Wage_Ratio']]
