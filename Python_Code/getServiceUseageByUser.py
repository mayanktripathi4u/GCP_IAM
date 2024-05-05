from google.cloud import monitoring_v3
from google.oauth2 import service_account
from datetime import datetime, timedelta, timezone

def get_active_users(project_id, days=30):
    credentials = service_account.Credentials.from_service_account_file('mySAKeys.json')
    client = monitoring_v3.MetricServiceClient(credentials=credentials)
    
    # Get the end time for the query (current time)
    # end_time = datetime.utcnow() # This is deprecated
    end_time = datetime.now(timezone.utc)
    
    # Calculate the start time (30 days ago)
    start_time = end_time - timedelta(days=days)
    
    # Define the query
    query = f'resource.type="gce_instance" AND metric.type="compute.googleapis.com/instance/cpu/utilization" AND metric.label.instance_name="*"'
    
    # now = time.time()
    # seconds = int(now)
    # nanos = int((now - seconds) * 10**9)

    interval = monitoring_v3.TimeInterval(
    {
        "end_time": end_time,
        "start_time": start_time,
    }
)
    
    # Make the request
    name = f'projects/{project_id}'
    results = client.list_time_series(
        name=name,
        filter=query,
        # interval_start=start_time,
        # interval_end=end_time,
        interval = interval,
        view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
    )
    
    # Extract active users from the results
    active_users = set()
    for result in results:
        active_users.add(result.resource.labels.get('instance_id'))
    
    return active_users

def get_all_users():
    # Fetch all users, groups, and service accounts from GCP IAM
    # You can use the IAM API or gcloud command-line tool to fetch this data
    # For simplicity, assume you have a function or command to fetch this data
    all_users = set()  # Replace this with actual list of users, groups, and service accounts
    return all_users

# Example usage
project_id = "proud-climber-421817"
active_users = get_active_users(project_id)
all_users = get_all_users()

# Identify inactive users
inactive_users = all_users - active_users

print("Active Users:")
print(active_users)
print("Inactive Users (not used services in the last 30 days):")
print(inactive_users)
