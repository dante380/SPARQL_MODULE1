from rdflib import Graph, Namespace

# Завантаження графу
graph = Graph()
graph.parse('countrues_info.ttl')

# Запит для отримання країн, де розмовляють на двох і більше мовах, згрупованих за континентами
query = """
SELECT ?country 
    WHERE {
        ?Country_Language :spoken_in ?country .
        filter contains(str(?Country_Language),"lang_2")
        
    }
"""

res = graph.query(query)
for row in res:
    print(row)