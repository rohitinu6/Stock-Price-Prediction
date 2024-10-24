import requests
from collections import defaultdict

# GitHub API URL for closed pull requests
API_URL = "https://api.github.com/repos/rohitinu6/Stock-Price-Prediction/pulls?state=closed"

GITHUB_TOKEN = None

# Points mapping based on the label names
points_map = {
    "level1": 10,
    "level2": 25,
    "level3": 45
}

# Function to fetch closed pull requests
def get_closed_prs():
    headers = {}
    
    if GITHUB_TOKEN:
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch PRs: {response.status_code} {response.text}")
    
    return response.json()

leaderboard = defaultdict(lambda: {"points": 0, "avatar_url": ""})

prs = get_closed_prs()

# Loop through each PR and calculate points based on the labels
for pr in prs:
    user = pr['user']['login']  # Get the username
    avatar_url = pr['user']['avatar_url']  # Get the avatar URL
    labels = pr['labels']  # Get the labels associated with the PR

    # Loop through labels and add points based on the level
    for label in labels:
        label_name = label['name']
        if label_name in points_map:
            leaderboard[user]["points"] += points_map[label_name]
            leaderboard[user]["avatar_url"] = avatar_url  # Store avatar URL

# Generate the leaderboard in markdown format
def generate_leaderboard_md(leaderboard):
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1]["points"], reverse=True)
    
    md_content = "# Leaderboard\n\n"
    md_content += "| Avatar | Username | Points |\n"
    md_content += "|--------|----------|--------|\n"
    
    for user, data in sorted_leaderboard:
        points = data["points"]
        avatar_url = data["avatar_url"]
        md_content += f'| <img src="{avatar_url}" width="50" height="50"> | {user} | {points} |\n'
    
    return md_content

# Generate the leaderboard markdown and save it to a file
leaderboard_md = generate_leaderboard_md(leaderboard)
with open('leaderboard.md', 'w') as f:
    f.write(leaderboard_md)

