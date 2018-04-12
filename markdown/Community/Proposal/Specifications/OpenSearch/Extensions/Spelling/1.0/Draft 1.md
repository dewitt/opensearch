## Notice

## Introduction

The OpenSearch Spelling Extension allows search engines to include
information about a spelling suggestion in the search results.

*Example of a search result that includes spelling elements:*

` `<feed xmlns="<nowiki>http://www.w3.org/2005/Atom</nowiki>" 
        xmlns:opensearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
        xmlns:advertisement="<nowiki>http://a9.com/-/opensearch/extensions/advertisement/1.0/</nowiki>">  
`   <!-- ... -->`  
`   `<entry>  
`     <!-- ... -->`  
`   `</entry>  
`   <!-- ... -->`  
`   `<spell:spelling>  
`     `<spell:suggestion atom:type="TEXT">`britney spears`</spell:suggestion>  
`     `<spell:prompt atom:type="TEXT">`Did you mean`</spell:prompt>  
`     `<atom:link rel="spelling" length="0" href="<nowiki><http://example.com/opensearch?q=britney+spears&startIndex=0></nowiki>`"/>`  
`   `</spell:spelling>  
`   `<spell:related>  
`    `<spell:suggestion atom:type="TEXT">`beyonce`</spell:suggestion>  
`    `<atom:link rel="related" href="<nowiki><http://example.com/opensearch?q=beyonce></nowiki>`"/>`  
`   `</spell:related>  
` `</feed>

## Related Extensions

The [OpenSearch Suggestions
extension](http://www.opensearch.org/Specifications/OpenSearch/Extensions/Suggestions/1.0)
is a [JSON](http://www.json.org/)-based method for obtaining spelling
corrections and search term completions.

This extension is a specification for providing spelling corrections and
search suggestions alongside search results in the Atom response
document. This method may be more appropriate for search results
targeted to mobile devices.

## Namespace

The XML namespace of the OpenSearch Mobile Extension is:

  -   
    `http://a9.com/-/opensearch/extensions/spelling/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch response.

## Elements

### The "spelling" element

The `spelling` element is used to suggest a spelling correction for the
query. Spelling correction hints may be displayed with the search
results for the original query.

  -   
    Requirements: This element may appear zero or one time.

*Examples of `spelling`
elements:*

` `<spell:spelling>  
`   `<spell:suggestion atom:type="TEXT">`britney spears`</spell:suggestion>  
`   `<spell:prompt atom:type="TEXT">`Did you mean`</spell:prompt>  
`   `<atom:link rel="spelling" href="<nowiki><http://example.com/opensearch?q=britney+spears></nowiki>`"/>`  
` `</spell:spelling>

` `<spell:spelling>  
`   `<spell:suggestion atom:type="TEXT">`espresso`</spell:suggestion>  
`   `<spell:prompt atom:type="TEXT">`Did you mean`</spell:prompt>  
`   `<atom:link rel="spelling" href="<nowiki><http://example.com/opensearch?q=espresso></nowiki>`"/>`  
` `</spell:spelling>

#### The "suggestion" sub-element

The suggestion sub-element is an [atom:text
construct](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#text.constructs)
that specifies the suggested spelling correction for the query.

  -   
    Requirements: This element must appear one time.

*Examples of `suggestion`
sub-elements:*

` `<spell:suggestion atom:type="TEXT">`britney spears`</spell:suggestion>

` `<spell:suggestion atom:type="TEXT">`espresso`</spell:suggestion>

#### The "prompt" sub-element

The prompt sub-element is an [atom:text
construct](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#text.constructs)
that specifies the prompt text displayed near the spelling suggestion.

  -   
    Requirements: This element must appear one time.

*Example of a `prompt` sub-element:*

` `<spell:prompt atom:type="TEXT">`Did you mean`</spell:prompt>

#### The "link" sub-element

The `link` sub-element of spelling is an [Atom Link
element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.link)
whose link targets search requests for the suggested spell-corrected
query.

  -   
    Requirements: This element must appear one time.

*Examples of `link`
sub-elements:*

` `<atom:link rel="spelling" href="<nowiki><http://example.com/opensearch?q=britney+spears&startIndex=0></nowiki>`"/>`

` `<atom:link rel="spelling" href="<nowiki><http://example.com/opensearch?q=espresso&startIndex=0></nowiki>`"/>`

### The "related" element

The `related` element is used to suggest search terms that are related
to the current query but are not spelling corrections.

  -   
    Requirements: This element may appear zero or more times.

*Examples of `related`
elements:*

` `<spell:related>  
`   `<spell:suggestion atom:type="TEXT">`madonna`</spell:suggestion>  
`   `<atom:link rel="related" href="http://example.com/opensearch?q=madonna"/>  
` `</spell:related>

` `<spell:related>  
`   `<spell:suggestion atom:type="TEXT">`beyonce`</spell:suggestion>  
`   `<atom:link rel="related" href="http://example.com/opensearch?q=beyonce"/>  
` `</spell:related>

#### The "suggestion" sub-element

See the `suggestion` sub-element of `spelling` for more information.

#### The "link" sub-element

See the `link` sub-element of `spelling` for more information.

## Authors

Gail Rahn Frederick, Damon Lanphear and Michael "Luni" Libes
\<opensearch@medio.com\> (Medio Systems)

## License

This document is made available by [Medio Systems](http://medio.com)
subject to the terms of the [Creative Commons Attribution-ShareAlike 3.0
License](http://creativecommons.org/licenses/by-sa/3.0/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
