// Load GCP IAM data from CSV
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mayanktripathi4u/GCP_IAM/main/Neo4j-GCP-IAM/gcp_iam_sample.csv' AS row

// Create or match Project nodes
MERGE (p:Project {name: row.project})

// Create or match Resource nodes
MERGE (r:Resource {name: row.resource, project: row.project})

// Create or match Role nodes
MERGE (role:Role {name: row.role})

// Create or match Identity nodes (User or Service Account)
MERGE (i:Identity {name: row.identity, type: row.identity_type})

// Create relationships
// Resource -> Role (ASSIGNED)
MERGE (r)-[:ASSIGNED]->(role)

// Identity -> Role (HAS_ACCESS)
MERGE (i)-[:HAS_ACCESS]->(role)

// Project -> Resource (CONTAINS)
MERGE (p)-[:CONTAINS]->(r);
