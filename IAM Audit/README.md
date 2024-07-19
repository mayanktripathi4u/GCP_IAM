# GCP IAM Audit
Creating a comprehensive dashboard to visualize GCP IAM data involves several steps:

1. Pulling IAM data from GCP
2. Processing and analyzing the data
3. Sending the processed data to a visualization tool like Looker Studio

# Step 1: Pulling IAM Data from GCP
First, you need to pull the necessary IAM data from GCP. You can use the google-cloud-iam library to fetch roles, permissions, and policy bindings.

# Step 2: Processing and Analyzing the Data
Next, you need to process and analyze the IAM data to identify high-risk permissions, groups with many permissions, etc.

# Step 3: Sending Data to Looker Studio
Finally, you need to send the processed data to Looker Studio for visualization. You can use Google Sheets as an intermediary data source since Looker Studio can easily connect to Google Sheets.

Here’s an end-to-end solution:

# Step 1: Pulling IAM Data from GCP
First, install the necessary libraries:
```
pip install google-cloud-iam google-auth google-api-python-client pandas gspread oauth2client
```
Next, use the following Python script to pull IAM data:
```
from google.cloud import iam_v1
from google.oauth2 import service_account
import pandas as pd

# Initialize the IAM client
credentials = service_account.Credentials.from_service_account_file('path/to/your-service-account-file.json')
iam_client = iam_v1.IAMClient(credentials=credentials)

project_id = 'your-project-id'

def get_roles_permissions():
    roles_permissions = {}
    roles = iam_client.list_roles(parent=f'projects/{project_id}')
    
    for role in roles:
        role_name = role.name
        permissions = role.included_permissions
        roles_permissions[role_name] = permissions
    
    return roles_permissions

def get_policy_bindings():
    policy = iam_client.get_iam_policy(resource=f'projects/{project_id}')
    bindings = policy.bindings
    return bindings

roles_permissions = get_roles_permissions()
policy_bindings = get_policy_bindings()

# Process and analyze the data
def analyze_iam_data(roles_permissions, policy_bindings):
    data = []
    for binding in policy_bindings:
        role = binding.role
        for member in binding.members:
            data.append({'member': member, 'role': role, 'permissions': roles_permissions.get(role, [])})
    
    df = pd.DataFrame(data)
    return df

iam_df = analyze_iam_data(roles_permissions, policy_bindings)

# Save the data to a CSV file
iam_df.to_csv('iam_data.csv', index=False)
```

# Step 2: Processing and Analyzing the Data
You can further process the data using pandas to identify high-risk permissions and groups with many permissions:
```
def identify_high_risk_permissions(df):
    high_risk_permissions = ['iam.serviceAccounts.create', 'resourcemanager.projects.delete']
    df['high_risk'] = df['permissions'].apply(lambda perms: any(perm in perms for perm in high_risk_permissions))
    return df[df['high_risk']]

high_risk_df = identify_high_risk_permissions(iam_df)

def groups_with_many_permissions(df):
    groups_df = df[df['member'].str.contains('group:')]
    group_permissions_count = groups_df.groupby('member')['permissions'].apply(lambda perms: len(set([item for sublist in perms for item in sublist])))
    return group_permissions_count.sort_values(ascending=False)

groups_permissions_df = groups_with_many_permissions(iam_df)

# Save the analysis to CSV files
high_risk_df.to_csv('high_risk_permissions.csv', index=False)
groups_permissions_df.to_csv('groups_permissions_count.csv')
```

# Step 3: Sending Data to Looker Studio
You can use Google Sheets as an intermediary to visualize data in Looker Studio. The gspread library can help you upload the processed data to Google Sheets.
```
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheets(sheet_name, df):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your-service-account-file.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(sheet_name).sheet1

    # Clear existing data
    sheet.clear()

    # Update sheet with new data
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

upload_to_google_sheets('IAM Data', iam_df)
upload_to_google_sheets('High Risk Permissions', high_risk_df)
upload_to_google_sheets('Groups Permissions Count', groups_permissions_df)
```
# Creating Visualizations in Looker Studio
1. Connect Google Sheets to Looker Studio:
* Open Looker Studio (formerly Google Data Studio).
* Create a new data source and connect it to the Google Sheets where you uploaded your IAM data.
2. Create Dashboards and Visualizations:
* Use the connected data source to create various charts and graphs.
* For example, create a bar chart to show the number of permissions each group has, or a pie chart to visualize the distribution of high-risk permissions.
3. Share the Dashboard:
* Once your dashboard is ready, you can share it with your team or embed it in your internal tools.


By following these steps, you can create an interactive dashboard to visualize GCP IAM data, helping you monitor high-risk permissions and manage IAM roles effectively.








python -m venv .iam_audit
source .iam_audit/bin/activate