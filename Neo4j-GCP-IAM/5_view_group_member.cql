MATCH (i:Identity)-[:BELONGS_TO]->(g:Group)
RETURN i, g;
