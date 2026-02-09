#!/usr/bin/env python3
import json
import datetime
import os

def update_tracker():
    # Load existing data or create new
    if os.path.exists('job-data.json'):
        with open('job-data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {
            'applications': [],
            'weekly_goal': 5,
            'stats': {'sent': 0, 'interviews': 0, 'offers': 0}
        }
    
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Update APPLICATIONS.md
    with open('APPLICATIONS.md', 'w') as f:
        f.write(f"# Job Applications Tracker\n\n")
        f.write(f"## Week of {today}\n\n")
        f.write(f"**Goal**: {data['weekly_goal']} applications/week\n")
        
        # Count this week's applications
        week_number = datetime.datetime.now().strftime('%Y-%W')
        this_week = len([a for a in data['applications'] if a.get('week') == week_number])
        f.write(f"**Sent this week**: {this_week}\n\n")
        
        f.write("### Companies to Apply:\n")
        for i in range(1, 6):
            f.write(f"- [ ] Company {i}\n")
        
        f.write(f"\n*Last updated: {datetime.datetime.now()}*\n")
    
    # Save data
    data['last_updated'] = today
    with open('job-data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("✅ Job tracker updated!")

if __name__ == '__main__':
    update_tracker()
