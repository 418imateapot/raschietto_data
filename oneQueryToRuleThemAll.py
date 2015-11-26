#!/usr/bin/env python
# coding: utf-8

import rdflib
from SPARQLWrapper import SPARQLWrapper
from json import JSONEncoder

sparql = SPARQLWrapper('http://tweb2015.cs.unibo.it:8080/data',returnFormat='json')
query = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX raschietto: <http://vitali.web.cs.unibo.it/raschietto/>
    PREFIX oa: <http://www.w3.org/ns/oa#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    #www.dlib.org/dlib/november14/beel/11beel_ver1

    SELECT ?id ?author ?title ?year ?comment ?url
   ?comment ?url
    WHERE {
      ?x raschietto:type "hasAuthor";
        oa:hasBody ?y.
      ?y rdf:object ?z.
      ?z rdfs:label ?author.
      ?y rdf:subject ?id.
      ?x1 raschietto:type "hasTitle";
        oa:hasBody ?y1.
      ?y1 rdf:object ?title.
 	  ?x2 raschietto:type "hasPublicationYear";
  		oa:hasBody ?y2.
  	  ?y2 rdf:object ?year.
  	  ?x3 raschietto:type "hasComment";
  		oa:hasBody ?y3.
  	  ?y3 rdf:object ?comment.
  	   ?x4 raschietto:type "hasURL";
  		oa:hasBody ?y4.
  	  ?y4 rdf:object ?url.
  	  }
    LIMIT 100
"""

sparql.setQuery(query)
print JSONEncoder().encode(sparql.query().convert())
