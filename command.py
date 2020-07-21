"""

1st: match (n:TrialGene) return count(n)


2nd: match(n:TrialGene)-[r]-() return count(r)


3rd: match(n)-[r]-(n) return count(r)


4th: match p = allShortestPaths((source)-[r*..]-(destination)) where source.Name='BRCA1' AND destination.Name = 'NBR1' return [n IN NODES(p)| n.Name] as Paths


5th: match (n:TrialGene)-[r]->()

return n.Name as Node, count(r) as Outdegree

order by Outdegree desc


6th: match (n:TrialGene)-[r]-() with n as nodes, count(distinct r) as degree return degree, count(nodes) order by degree asc




----------------------------------------------------------------------------------------


option 1st: match (n)-[r]->(m) where m <> n return distinct n, m, count(r) as myCount order by myCount desc limit 1


option 2nd: match p=(n {Name:'BRCA1'})-[:AssociationType*..2]->(m) return p

"""




"""
Getting the database from raw github:
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/widyaageng/graphneo/master/gene_gene_associations_50k.csv" AS line
MERGE (n:TrialGene {Name:line.OFFICIAL_SYMBOL_A})
MERGE (m:TrialGene {Name:line.OFFICIAL_SYMBOL_B})
MERGE (n) -[:AssociationType {AssociatedWith:line.EXPERIMENTAL_SYSTEM}]-> (m)



"""
