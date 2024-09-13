// Load GCP IAM data from CSV
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mayanktripathi4u/GCP_IAM/main/Neo4j-GCP-IAM/gcp_iam_sample.csv' AS row
RETURN row
