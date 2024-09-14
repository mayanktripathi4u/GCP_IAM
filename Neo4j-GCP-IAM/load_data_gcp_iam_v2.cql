// To create separate nodes based on identity_type, I have modify the Cypher query to create distinct node labels such as User, Group, and ServiceAccount instead of just one generic Identity node. 
// This will allow us to manage the different types of identities more cleanly and style them separately.

LOAD CSV WITH HEADERS FROM 'https://your-url/gcp_iam.csv' AS row
MERGE (p:Project {name: row.project})
MERGE (r:Resource {name: row.resource, project: row.project})
MERGE (role:Role {name: row.role})

FOREACH (_ IN CASE WHEN row.identity_type = 'user' THEN [1] ELSE [] END |
    MERGE (i:User {name: row.identity})
    MERGE (i)-[:HAS_ACCESS]->(role)
)
FOREACH (_ IN CASE WHEN row.identity_type = 'group' THEN [1] ELSE [] END |
    MERGE (g:Group {name: row.identity})
    MERGE (g)-[:HAS_ACCESS]->(role)
)
FOREACH (_ IN CASE WHEN row.identity_type = 'serviceAccount' THEN [1] ELSE [] END |
    MERGE (sa:ServiceAccount {name: row.identity})
    MERGE (sa)-[:HAS_ACCESS]->(role)
)

MERGE (r)-[:ASSIGNED]->(role)
MERGE (p)-[:CONTAINS]->(r);
