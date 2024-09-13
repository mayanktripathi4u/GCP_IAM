MATCH (i:Identity)-[:HAS_ACCESS]->(role:Role)
RETURN i, role;
