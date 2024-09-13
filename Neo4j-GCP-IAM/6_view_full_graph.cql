MATCH (p:Project)-[:CONTAINS]->(r:Resource)-[:ASSIGNED]->(role:Role),
      (i:Identity)-[:HAS_ACCESS]->(role),
      (i)-[:BELONGS_TO]->(g:Group)
RETURN p, r, role, i, g;
