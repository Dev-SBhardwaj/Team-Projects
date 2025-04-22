import requests
import pandas as pd
from datetime import datetime
import time

def get_player_stats():
    base_url = "https://api.cricapi.com/v1"
    api_key = "your_api_here"
    
    try:
        # List of T20 players we want to track
        top_t20_players = [
            "Suryakumar Yadav", "Mohammad Rizwan", "Babar Azam",
            "Aiden Markram", "Devon Conway", "Jos Buttler",
            "Glenn Phillips", "Virat Kohli", "Rohit Sharma",
            "David Warner"
        ]
        
        players_data = []
        
        # First get all player IDs using the search API
        print("\nFetching player information...")
        for player_name in top_t20_players:
            try:
                # Search for player
                search_url = f"{base_url}/search"
                search_params = {
                    "apikey": api_key,
                    "search": player_name
                }
                
                print(f"Searching for {player_name}...")
                search_response = requests.get(search_url, params=search_params)
                search_data = search_response.json()
                
                if search_data.get('status') == "success" and search_data.get('data'):
                    # Find the exact player match
                    player_matches = [p for p in search_data['data'] 
                                   if isinstance(p, dict) and 
                                   'name' in p and 
                                   p['name'].lower() == player_name.lower()]
                    
                    if player_matches:
                        player = player_matches[0]
                        print(f"Found player: {player['name']}")
                        
                        # Get detailed player info
                        info_url = f"{base_url}/player_info"
                        info_params = {
                            "apikey": api_key,
                            "id": player.get('id')
                        }
                        
                        info_response = requests.get(info_url, params=info_params)
                        info_data = info_response.json()
                        
                        if info_data.get('status') == "success" and info_data.get('data'):
                            player_info = info_data['data']
                            
                            # Basic player details
                            stats = {
                                'Name': player_name,
                                'Country': player_info.get('country', 'N/A'),
                                'Role': player_info.get('role', 'N/A'),
                                'Batting Style': player_info.get('battingStyle', 'N/A')
                            }
                            
                            # Add T20 statistics if available
                            if 'stats' in player_info:
                                t20_stats = next((
                                    stat for stat in player_info['stats']
                                    if isinstance(stat, dict) and 
                                    't20' in stat.get('fn', '').lower()
                                ), {})
                                
                                if t20_stats:
                                    stats.update({
                                        'T20 Matches': t20_stats.get('mat', '0'),
                                        'T20 Runs': t20_stats.get('runs', '0'),
                                        'T20 Average': t20_stats.get('avg', '0'),
                                        'T20 Strike Rate': t20_stats.get('sr', '0'),
                                        'T20 Fifties': t20_stats.get('50', '0'),
                                        'T20 Hundreds': t20_stats.get('100', '0'),
                                        'T20 Best Score': t20_stats.get('hs', '0'),
                                        'Last Updated': datetime.now().strftime("%Y-%m-%d")
                                    })
                            
                            players_data.append(stats)
                            print(f"Added T20 stats for {player_name}")
                    else:
                        print(f"No exact match found for {player_name}")
                else:
                    print(f"No data found for {player_name}")
                    print(f"API Response: {search_data}")
                
                time.sleep(1)  # Respect API rate limiting
                
            except Exception as e:
                print(f"Error processing {player_name}: {str(e)}")
                continue
        
        if not players_data:
            print("No player data could be retrieved")
            return None
            
        # Create DataFrame
        df = pd.DataFrame(players_data)
        
        # Convert numeric columns
        numeric_columns = ['T20 Matches', 'T20 Runs', 'T20 Fifties', 'T20 Hundreds']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Format floating point columns
        float_columns = ['T20 Average', 'T20 Strike Rate']
        for col in float_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').round(2)
        
        # Save to CSV
        output_file = f"t20_player_stats_{datetime.now().strftime('%Y-%m-%d')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\nData saved to {output_file}")
        
        # Display statistics
        print("\nT20 Player Statistics Summary:")
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_rows', None)
        
        display_cols = ['Name', 'Country', 'T20 Runs', 'T20 Average', 
                       'T20 Strike Rate', 'T20 Fifties', 'T20 Hundreds']
        if all(col in df.columns for col in display_cols):
            print(df[display_cols].sort_values('T20 Runs', ascending=False).to_string(index=False))
        else:
            print("Could not display all statistics. Available columns:", df.columns.tolist())
        
        return df
        
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return None

if __name__ == "__main__":
    print("T20 Cricket Player Statistics")
    print("============================")
    stats = get_player_stats()