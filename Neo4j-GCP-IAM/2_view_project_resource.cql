MATCH (p:Project)-[:CONTAINS]->(r:Resource)
RETURN p, r;
