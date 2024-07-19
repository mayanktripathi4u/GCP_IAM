from google.cloud import iam_v1
from google.oauth2 import service_account
import pandas as pd

# Initialize the IAM client
# credentials = service_account.Credentials.from_service_account_file('path/to/your-service-account-file.json')
# iam_client = iam_v1.IAMClient(credentials=credentials)

iam_client = iam_v1.IAMClient()

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
