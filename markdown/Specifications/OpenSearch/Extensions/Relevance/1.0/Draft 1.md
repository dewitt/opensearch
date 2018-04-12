## Notice

## Introduction

The OpenSearch Relevance Extension allows search engines indicate a
relative score in a particular domain for an individual search result.

*Example of a search result that includes a relevance score:*

` `<feed xmlns="<nowiki>http://www.w3.org/2005/Atom</nowiki>" 
        xmlns:opensearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
        xmlns:relevance="<nowiki>http://a9.com/-/opensearch/extensions/relevance/1.0/</nowiki>">  
`   <!-- ... -->`  
`   `<entry>  
`     `

<title>

New York
History

</title>

`     `<link href="<nowiki><http://www.columbia.edu/cu/lweb/eguids/amerihist/nyc.html></nowiki>`"/>`  
`     `<id><urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a></id>  
`     `<updated>`2003-12-13T18:30:02Z`</updated>  
`     `<content type="text">  
`       ... Harlem.NYC - A virtual tour and information on `  
`       businesses ...  with historic photos of Columbia's own New York `  
`       neighborhood ... Internet Resources for the City's History. ...`  
`     `</content>  
`     `<relevance:score>`0.95`</relevance:score>  
`   `</entry>  
`   <!-- ... -->`  
` `</feed>

## Namespace

The XML namespace of the OpenSearch Relevance Extension is:

  -   
    <code>http://a9.com/-/opensearch/extensions/relevance/1.0/

</code>

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch response.

## Elements

The OpenSearch Relevance extension introduces the following element.

### The "score" element

Contains a string indicating a relative assessment of relevance for a
particular search result with respect to the search query.

Decimal values less than 0 should be considered equal to 0.

Decimal values greater than 1 should be considered equal to 1.

Unparseable or empty values can be ignored by the client.

  -   
    Restrictions: The value must contain a decimal representation of a
    real number between 0 and 1, inclusive.
    Requirements: This element may appear zero or one time.

The `score` element is used to indicate a relative assessment of
relevance for a particular search result with respect to the search
query.

*Examples of `score` elements:*

` `<relevance:score>`0.3`</relevance:score>  
` `  
` `<relevance:score>`0.924`</relevance:score>  
` `  
` `<relevance:score>`0.12`</relevance:score>

## Author

DeWitt Clinton \<dewitt@opensearch.org\>

## License

This document is made available by [A9.com](http://a9.com) subject to
the terms of the [Creative Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
