import urllib.request

url = "https://www.gunviolencearchive.org/last-72-hours"
# Function to fetch data from the website
def fetch_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode("utf-8")
            return html_content
    except Exception as e:
        print("Failed to fetch data from the website:", e)
        return None

# Function to parse the data and extract relevant information
def parse_data(html_content):
    if html_content is None:
        return None
    incidents = {}
    # Find the table rows containing incident data
    start_index = html_content.find('<tbody>')
    end_index = html_content.find('</tbody>', start_index)
    table_data = html_content[start_index:end_index]
    rows = table_data.split('<tr>')
    for row in rows:
        if 'views-row' in row:
            state_start = row.find('<td class="views-field views-field-field-state">') + len('<td class="views-field views-field-field-state">')
            state_end = row.find('</td>', state_start)
            state = row[state_start:state_end].strip()
            incidents[state] = incidents.get(state, 0) + 1
    return incidents

# Function to find the state(s) with the largest number of gun violence incidents
def find_largest_incidents(incidents):
    if not incidents:
        return None
    max_count = max(incidents.values())
    states = [state for state, count in incidents.items() if count == max_count]
    return states

# Main function
def main():
    url = "https://www.gunviolencearchive.org/last-72-hours"
    html_content = fetch_data(url)
    incidents = parse_data(html_content)
    largest_incidents = find_largest_incidents(incidents)
    if largest_incidents:
        if len(largest_incidents) == 1:
            print(f"The state with the largest number of gun violence incidents in the last 72 hours is: {largest_incidents[0]}")
        else:
            print(f"The states with the largest number of gun violence incidents in the last 72 hours are: {', '.join(largest_incidents)}")
    else:
        print("Failed to retrieve data or no incidents found.")

if __name__ == "__main__":
    main()
