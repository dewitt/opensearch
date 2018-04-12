## Notice

## Introduction

There is an increasing demand for search engines to be able to
categorize resources using classification entities (or concepts) defined
in taxonomies. That implies for the resource authors to be able to tag
resources with concepts defined in authoritative taxonomies, and for the
search engine to provide semantic search abilities.

The OpenSearch Semantic extension offers a standard way to query a
repository of resources using such semantic abilities.

## Overview

The search engine publishes an [OpenSearch description
document](Specifications/OpenSearch/1.1/Draft_3#OpenSearch_description_document "wikilink")
containing two groups of [Url
elements](Specifications/OpenSearch/1.1/Draft_3#The_.22Url.22_element "wikilink").
The first set of `Url` elements have a `rel` attribute with
`http://a9.com/-/opensearch/extensions/semantic/1.0/taxonomies` as a
value; it indicates to the client how to retrieve a list of taxonomies
understood by the search engine. The second set of `Url` elements are
the regular `Url` from the OpenSearch core specification, where the
semantic operators described below can be used.

## Background

The Semantic Web is building up, and several standardization efforts are
looking into ways to

  - represent taxonomies or concept trees (RDF, OWL, SKOS, WSML, ...)
  - semantically annotate resources on the web using elements from those
    taxonomies (ISO metadata, microformats, folksonomies, ...)
  - devise querying schemes to exploit those semantic annotations
    (SPARQL)

Different subsets of these technologies are used in different domains.
But a common feature of all these systems is that taxonomies, concepts
or other semantic entities can be unambiguously identified by URI. This
allows the expression of relations (or predicates) involving concepts or
entities defined in different taxonomies from different domains, using
different representations languages.

Therefore, a simple semantic querying scheme can be devised to be
applicable to all these domains, using URIs as semantic entities
identifiers, and a simple set of semantic operators.

## Namespace

The XML namespace of the OpenSearch Semantic Extension is:

  -   
    `http://a9.com/-/opensearch/extensions/semantic/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch Description document.

## OpenSearch description document

Search engines that support semantic search can use the OpenSearch
description document to publish URL templates for both retrieving the
taxonomies and for performing follow-up semantic search queries.

### Declaring URLs to get the list of available taxonomies

Search engines should publish one or more `Url` elements with
`rel="http://a9.com/-/opensearch/extensions/semantic/1.0/taxonomies"` to
indicate that they can be queried for a list of taxonomies that they
support. Each `Url` can declare a different `type` .

Taxonomy endpoints should support the `identifier` attribute, allowing
the client to request a specific taxonomy.

#### Example

Example of declaration of taxonomy list endpoints with JSON and RDF
encodings:

<?xml version="1.0" encoding="UTF-8"?>

` <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/"`  
`                     '''xmlns:semantic="http://a9.com/-/opensearch/extensions/semantic/1.0/">`  
`   `**`<Url``
``type="application/json"`**  
`        `**`rel="`<http://a9.com/-/opensearch/extensions/semantic/1.0/taxonomies>`"`**  
`        `**`template="http://example.com/taxonomies.json?q={searchTerms}&identifier={identifier}"/>`**  
`   `**`<Url``
``type="application/rdf+xml"`**  
`        `**`rel="`<http://a9.com/-/opensearch/extensions/semantic/1.0/taxonomies>`"`**  
`        `**`template="http://example.com/taxonomies.rdf?q={searchTerms}&identifier={identifier}"/>`**  
`   <!-- ... -->`  
` `</OpenSearchDescription>

#### JSON-encoded taxonomy list

Taxonomy URL endpoints can be defined for any encoding type. Encodings
such as OWL, SKOS, WSML are meant to represent taxonomies, and their
respective specifications cover the encoding of such taxonomies.
Therefore, only the JSON encoding will be described here, at it is the
preferred mean for a browser to retrieve taxonomies.

Taxonomies lists are returned as an array of taxonomy elements.

Each taxonomy is represented as an object with the following properties
:

  - title : a human readable name for the taxonomy
  - identifier : a URI uniquely identifying this taxonomy
  - childrenConcepts : an array of children concepts of this taxonomy

Each concept is represented as an object with the following properties :

  - title : a human readable name for the concept
  - identifier : a URI uniquely identifying this
  - childrenConcepts : an array of children concepts of this taxonomy
  - (optional) classifiedObjectsCount : the number of items classified
    by this concept in the search engine

This JSON encoding of concept trees is very simple and is not meant to
be a JSON equivalent of encodings such as OWL or even
SKOS.

##### Example

` [{"title": "Wine categories",`  
`   "identifier": "`<urn:example:taxonomy:wines>`"`  
`   "childrenConcepts": [`  
`     {"title": "White Wine",`  
`      "identifier": "`<urn:example:taxonomy:wines#White>`",`  
`      "childrenConcepts": [`  
`        {"title": "Sauterne",`  
`         "identifier": "`<urn:example:taxonomy:wines#Sauterne>`"},`  
`        {"title": "Chardonnay",`  
`         "identifier": "`<urn:example:taxonomy:wines#Chardonnay>`"}]},`  
`     {"title": "Red Wine",`  
`      "identifier": "`<urn:example:taxonomy:wines#Red>`",`  
`      "childrenConcepts": [`  
`        {"title": "Bordeaux Red",`  
`         "identifier": "`<urn:example:taxonomy:wines#BordeauxRed>`" },`  
`        {"title": "Syrah",`  
`         "identifier": "`<urn:example:taxonomy:wines#Syrah>`" }]},    `  
`    ...],},`  
`  ...]`

### Search parameters

After the list of taxonomies has been retrieved, the client can use some
of the following parameters to query the search engine using concepts
from the taxonomies retrieved.

#### The "classifiedAs" parameter

Replaced with comma-separated list of URIs of concepts that must
classify the search results. If multiple concepts are specified, search
results will have to be classified by all these concepts. If the search
engine has semantic inference capabilities, this operator should match
records that are classified by any concept that is equivalent to or a
subconcept of the specified concepts, where 'subconcept of' and
'equivalent to' are the formal relations defined in the
[RDF](http://www.w3.org/TR/rdf-mt/#RDFSINTERP) and
[OWL](http://www.w3.org/TR/owl-ref/#equivalentClass-def) specification,
resp. `rdfs:subClassOf` and `owl:equivalentClass`.

Using this parameter is equivalent to using the `relation` and `related`
parameters (below) with values being respectively `rdf:Type` and the
value of `classifiedAs`. I.e. satisfying the following statement :

`?result rdf:Type `<classifiedAs value>

Note the search server should use the "`?`" flag in the URL template
when requesting the `classifiedAs` parameter to indicate that this
parameter is optional and that a search can still be performed even if
the client does not recognize the semantic extension.

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&classifiedAs={semantic:classifiedAs?}&format=html`

</code>

Example request, looking for english music bands, using the DBPedia
taxonomy (see
<http://dbpedia.org/class/yago/EnglishMusicalGroups>):

<code>

` http://example.com/?classifiedAs=http://dbpedia.org/class/yago/EnglishMusicalGroups&format=html`

</code>

#### The "related" parameter

Replaced with comma-separated list of URIs of entities that the results
must be related to. If multiple entities are specified, search results
will have to be related to all these entities. The semantics of
"related" can be specified using the `relation` parameter. If that
parameter is not specified, it is up to the search engine to decide what
semantic relation (or predicate) has to be satisfied.

Note the search server should use the "`?`" flag in the URL template
when requesting the `classifiedAs` parameter to indicate that this
parameter is optional and that a search can still be performed even if
the client does not recognize the semantic extension.

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&related={semantic:related?}&format=rss`

</code>

Example request on a FOAF-enabled search engine where the default
`relation` is `foaf:knows`. This request looks for an acquaintance of
<urn:foaf:john.doe> that matches the doctor keyword.

<code>

` http://example.com/?q=doctor&related=urn:foaf:john.doe&format=rss`

</code>

#### The "relation" parameter

Always used in conjunction with `related`. Replaced with comma-separated
list of URIs identifying relations (or predicates) that must be
satisfied with the `related` parameter, i.e. the results of the query
must satisfy the statement : `?result <relation URI> <related URI>`

If multiple relations are specified, search results will have to satisfy
all these relations. If the search engine has semantic inference
capabilities, this operator should match records that satisfy any
relation that is equivalent to or an inherited relation of the specified
relation, where 'inherited' and 'equivalent to' are the formal
properties defined in the [RDF](http://www.w3.org/TR/rdf-mt/#RDFSINTERP)
and [OWL](http://www.w3.org/TR/owl-ref/#equivalentClass-def)
specification, resp. `rdfs:subPropertyOf` and `owl:equivalentClass`.

Note the search server should use the "`?`" flag in the URL template
when requesting the `classifiedAs` parameter to indicate that this
parameter is optional and that a search can still be performed even if
the client does not recognize the semantic extension.

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&related={semantic:related?}&relation={semantic:relation?}&format=kml`

</code>

Example request, with a search engine supporting the [GeoNames
ontology](http://www.geonames.org/ontology/). This request looks for a
hotel nearby Trafalgar Square (identified by its GeoName URI
<http://sws.geonames.org/6619832>) :
<code>

` http://example.com/?q=hotel&related=http://sws.geonames.org/6619832&relation=http://www.geonames.org/ontology%23nearby&format=kml`

</code>

## Authors

This specification was edited by Philippe Duchesne
\<pduchesne@gmail.com\>.

## License

This document is made available subject to the terms of the [Creative
Commons Attribution-ShareAlike 3.0
License](http://creativecommons.org/licenses/by-sa/3.0/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
