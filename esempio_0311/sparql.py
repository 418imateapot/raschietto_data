#!/usr/bin/env python
# coding: utf-8

import rdflib
from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper('http://tweb2015.cs.unibo.it:8080/data',returnFormat='json')

oldquery = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX fabio: <http://purl.org/spar/fabio/>

SELECT ?author WHERE {
    ?x a fabio:Work;
        dcterms:creator ?author.
    }
    LIMIT 10
"""
sparql.setQuery("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX fabio: <http://purl.org/spar/fabio/>
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX raschietto: <http://vitali.web.cs.unibo.it/raschietto/>
PREFIX xmls: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?x ?y ?z ?aaa ?author WHERE {
    ?x a oa:Annotation;
        raschietto:type "hasAuthor"^^xmls:normalizedString;
        oa:hasBody ?y .
    ?y rdf:object ?z .
    ?z rdf:subject ?aaa .
    ?z rdfs:label ?author .
    }
    LIMIT 10
""")


print sparql.query().convert()
