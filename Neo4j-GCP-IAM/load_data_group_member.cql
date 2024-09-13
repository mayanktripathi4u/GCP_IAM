// Load Group Membership data from CSV
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mayanktripathi4u/GCP_IAM/main/Neo4j-GCP-IAM/gcp_groups.csv' AS row

// Create or match Group nodes
MERGE (g:Group {name: row.group_name})

// Create or match Identity nodes (User or Service Account)
MERGE (i:Identity {name: row.member_identity, type: row.member_type})

// Create BELONGS_TO relationship between Identity and Group
MERGE (i)-[:BELONGS_TO]->(g);
