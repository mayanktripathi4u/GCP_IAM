// Ensure that each Node Label has a specific color in Neo4j
LOAD CSV WITH HEADERS FROM 'https://your-url/gcp_iam.csv' AS row
MERGE (p:Project {name: row.project})
MERGE (r:Resource {name: row.resource, project: row.project})
MERGE (role:Role {name: row.role})

FOREACH (_ IN CASE WHEN row.identity_type = 'user' THEN [1] ELSE [] END |
    MERGE (i:User {name: row.identity})
    SET i.color = 'red'   // Assign color to User nodes
    MERGE (i)-[:HAS_ACCESS]->(role)
)
FOREACH (_ IN CASE WHEN row.identity_type = 'group' THEN [1] ELSE [] END |
    MERGE (g:Group {name: row.identity})
    SET g.color = 'orange'  // Assign color to Group nodes
    MERGE (g)-[:HAS_ACCESS]->(role)
)
FOREACH (_ IN CASE WHEN row.identity_type = 'serviceAccount' THEN [1] ELSE [] END |
    MERGE (sa:ServiceAccount {name: row.identity})
    SET sa.color = 'green'  // Assign color to ServiceAccount nodes
    MERGE (sa)-[:HAS_ACCESS]->(role)
)

MERGE (r)-[:ASSIGNED]->(role)
MERGE (p)-[:CONTAINS]->(r);
