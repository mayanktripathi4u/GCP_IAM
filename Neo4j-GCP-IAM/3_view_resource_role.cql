MATCH (r:Resource)-[:ASSIGNED]->(role:Role)
RETURN r, role;
