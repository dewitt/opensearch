## Notice

## Introduction

The OpenSearch Suggestions extension offers a convention by which search
engines can return a set of search term completions for a given search
prefix. The search completions can be used by a search client to
dynamically present the end user with search term suggestions.

## Background

The [Google Suggest](http://www.google.com/webhp?complete=1&hl=en)
project pioneered a mechanism for dynamically presenting a list of
search term completions as the user interacts with the search interface.
The [Firefox](http://www.mozilla.com/firefox/) web browser was the first
to incorporate this technique into the browser search box to offer the
user dynamic search term suggestions, a technique subsequently adopted
by [Internet
Explorer](http://www.microsoft.com/windows/products/winfamily/ie/default.mspx),
[Safari](http://www.apple.com/safari/), and
[Chrome](http://www.google.com/chrome). This document is based on the
original [Firefox Search Service design
documentation](http://wiki.mozilla.org/Search_Service/Suggestions), and
subsequently updated for clarity and to include additional search
parameters.

## Overview

The search engine publishes an [OpenSearch description
document](Specifications/OpenSearch/1.1/Draft_3#OpenSearch_description_document "wikilink")
containing two [Url
elements](Specifications/OpenSearch/1.1/Draft_3#The_.22Url.22_element "wikilink").
The first `Url` element is of type
`type="application/x-suggestions+json"` and indicates to the client how
to retrieve a list of suggested searches for a given search prefix. The
second `Url` element is usually of `type="text/html"` and is used by the
search client to perform one of the suggested search queries.
Additionally, the second query template may request parameters about the
search suggestion that led to the final search query.

## Type

The following type is used to indicate that the response contains JSON
formatted search suggestions:

  -   
    `application/x-suggestions+json`

## Namespace

The XML namespace of the OpenSearch Suggestions Extension
    is:

  -   
    `http://www.opensearch.org/specifications/opensearch/extensions/suggestions/1.1`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch Description document.

## OpenSearch description document

Search engines that support search suggestions can use the OpenSearch
description document to publish URL templates for both retrieving the
list of suggestions and for performing follow-up search queries.

### Declaring a JSON-formatted search suggestion URL

Search engines should publish a `Url` element of
`type="application/x-suggestions+json"` to indicate that they can be
queried for a list of search suggestions in JSON format.

#### Example

Example of publishing the location of a JSON-formatted search suggestion
query:

<?xml version="1.0" encoding="UTF-8"?>

` `<OpenSearchDescription xmlns="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>">  
`   `**`<Url``
``type="application/x-suggestions+json"`**  
`        `**`template="http://example.com/suggest?q={searchTerms}"/>`**  
`   <!-- ... -->`  
` `</OpenSearchDescription>

### Declaring a URL for follow-up search queries

After the list of search suggestions has been retrieved, the client will
likely perform a full follow up search, as is documented using a
standard [Url
element](Specifications/OpenSearch/1.1/Draft_3#The_.22Url.22_element "wikilink"),
usually of `type="text/html"`, in the OpenSearch description document.
In addition to the usual query template parameters, this specification
introduces the `suggestionPrefix` and the `suggestionIndex` extension
parameters to provide additional context to the search engine.

The extension parameters are in the
`http://www.opensearch.org/specifications/opensearch/extensions/suggestions/1.1`
namespace, which must be explicitly declared as a [fully qualified
parameter
name](Specifications/OpenSearch/1.1/Draft_3#Fully_qualified_parameter_names "wikilink")
using an `xmlns` declaration.

These extension parameters could be used in any Url template, but the
meaning is defined here only when they are used in the context of a
follow-up search query generated from a list of suggested searches.

#### The "suggestionPrefix" parameter

When the search query was generated as a result of a search suggestion,
the `suggestionPrefix` variable is replaced by the string used to
generate the search suggestion.

Note the search server should use the "`?`" flag in the URL template
when requesting the `suggestionPrefix` parameter to indicate that this
parameter is optional and that a search can still be performed even if
the client does not recognize the suggestions extension.

#### The "suggestionIndex" parameter

When the search query was generated as a result of a search suggestion,
the `suggestionIndex` variable is replaced by the location of the
selected suggestion within the list, offset from 0.

Note the search server should use the "`?`" flag in the URL template
when requesting the `suggestionIndex` parameter to indicate that this
parameter is optional and that a search can still be performed even if
the client does not recognize the suggestions extension.

#### Example

Example of a Url template that accepts additional information when used
in conjunction with suggested
searches:

<?xml version="1.0" encoding="UTF-8"?>

` <OpenSearchDescription `  
`      xmlns="http://a9.com/-/spec/opensearch/1.1/"`  
`      `**`xmlns:suggestions="http://www.opensearch.org/specifications/opensearch/extensions/suggestions/1.1"`**`>`  
`   <Url type="text/html"`  
`        template="http://example.com?q={searchTerms}`  
`                  &amp;`**`prefix={suggestions:suggestionPrefix?}`**  
`                  &amp;`**`index={suggestions:suggestionIndex?}"`**`/>`  
`   <!-- ... -->`  
` `</OpenSearchDescription>

## JSON-formatted search suggestion responses

### Response format

The response body should be returned in [JavaScript Object
Notation](http://www.json.org/) as a JavaScript array of arrays.

### Response content

Search suggestions are returned as an ordered collection of values. The
four values are returned in the following order:

  - Query String
  - Completions
  - Descriptions
  - Query URLs

#### Suggestion prefix

Description: A single element echoing the requested search term. The
search client may validate that this value matches the expected
response.

Required: yes

Example:

` "sea"`

#### Search terms

Description: A list of suggested completions for the given search term.
These can be used as the value for the `searchTerms` parameter of a
subsequent search.

Required: yes

Example:

` ["sears",`  
`  "search engines",`  
`  "search engine",`  
`  "search",`  
`  "sears.com",`  
`  "seattle times"]`

#### Descriptions

Description: A list of human-readable strings that provide additional
information or context regarding the suggested completion.

Required: no

Example:

` ["7,390,000 results",`  
`  "17,900,000 results",`  
`  "25,700,000 results",`  
`  "1,220,000,000 results",`  
`  "1 result",`  
`  "17,600,000 results"]`

#### Query URLs

Description: A list of URLs that should be used by the search client to
request the suggested search term at the corresponding position in the
completions lists.

Required: no

Example:

` ["http://example.com?q=sears",`  
`   "http://example.com?q=search+engines",`  
`   "http://example.com?q=search+engine",`  
`   "http://example.com?q=search",`  
`   "http://example.com?q=sears.com",`  
`   "http://example.com?q=seattle+times"]`

### Example

The following is a full example of a JSON formatted search suggestions
response:

` ["sea",`  
`  ["sears",`  
`   "search engines",`  
`   "search engine",`  
`   "search",`  
`   "sears.com",`  
`   "seattle times"],`  
`  ["7,390,000 results",`  
`   "17,900,000 results",`  
`   "25,700,000 results",`  
`   "1,220,000,000 results",`  
`   "1 result",`  
`   "17,600,000 results"],`  
`  ["http://example.com?q=sears",`  
`   "http://example.com?q=search+engines",`  
`   "http://example.com?q=search+engine",`  
`   "http://example.com?q=search",`  
`   "http://example.com?q=sears.com",`  
`   "http://example.com?q=seattle+times"]]`

## Authors

This specification was edited by DeWitt Clinton
\<dewitt@opensearch.org\>, based on the work of Joe Hughes' search
suggestions documentation in Firefox and the Google search suggestions
format.

## License

This document is made available by [A9.com](http://a9.com) subject to
the terms of the [Creative Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
