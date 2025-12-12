# prompts.py

SYSTEM_PROMPT = """You are an expert NFL analyst helping a user pick winners for their Pick'em league. 
Your goal is to provide concise, data-driven analysis for the current week's games.
"""

ANALYSIS_PROMPT = """
Determine the current weeks NFL game matchups.
For each game, provide:
1. Matchup (Team A vs Team B)
2. Predicted Winner and 1 line description on whether or not the favored team will beat the spread.
3. Confidence Level (Low, Medium, High)
4. Key Reason for the pick (1-2 sentences)

Format the output as structured data (JSON) so it can be easily parsed into a dataframe.
"""
