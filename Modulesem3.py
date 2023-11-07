from SPARQLWrapper import SPARQLWrapper, JSON

# Ініціалізація SPARQLWrapper з URL Wikidata Query Service
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

query = """
SELECT ?method ?methodLabel ?subsection ?subsectionLabel WHERE {
  ?method wdt:P31/wdt:P279* wd:Q11660;     # wd:Q11660 corresponds to "machine learning algorithm" on Wikidata
          wdt:P279 ?subsection.             # P279 is the property for "subclass of"
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

sparql.setQuery(query)

sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    job = result['subsection']['value']
    methodLabel = result['methodLabel']['value']
    subsectionLabel = result['subsectionLabel']['value']
    print(f"Назва Методу: {methodLabel},\n Алгоритм: {subsectionLabel},\n Посилання на сутність: {job} \n")
