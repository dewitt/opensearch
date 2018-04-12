## Notice

## Introduction

The OpenSearch Referrer extension allows search engines to request a
query parameter from search clients to indicate the source of the
search. This parameter could be used to identify the particular search
client, the version of the search client, additional information about
the source of the search, or similar.

## Namespace

The XML namespace of the OpenSearch Referrer Extension is:

  -   
    `http://a9.com/-/opensearch/extensions/referrer/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch Description document.

## Parameters

The OpenSearch Referrer Extension introduces the following parameter to
be used in OpenSearch URL templates.

### The "source" parameter

Replaced with a string identifying the search client that performed the
search request.

## Example URL Template

*Example: An OpenSearch URL template with an optional source
parameter:*

<?xml version="1.0" encoding="UTF-8"?>

` <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/"`  
`   `**`xmlns:referrer="http://a9.com/-/opensearch/extensions/referrer/1.0/"`**`>`  
`   `<Url type="application/atom+xml"
      template="<nowiki>[`http://example.com/{searchTerms}`](http://example.com/%7BsearchTerms%7D)</nowiki>`?`**`src={referrer:source?}`**`"/>`  
`   <!-- ... -->`  
` `</OpenSearchDescription>

## Source Values

Values for the `source` parameter are not dictated by this
specification. Search clients should make known and publish the list of
values that they indend to send as a source parameter.

For example, Internet Explorer 7 could send one of the following values,
depending on where in the browser a search originated:

  -   
    "IE-SearchBox"

Or,

  -   
    "IE-Address"

The A9.com website could send the following value:

  -   
    "a9.com"

The Firefox web browser could send the following value:

  -   
    "firefox-a"

''Note: Those values are used as examples only. Please refer to the
documentation for the particular search client to determine the actual
"source" values.

## Optional Parameters

The search server should use the "`?`" flag in the URL template when
requesting the `source` parameter to indicate that this parameter is
optional and that a search can still be performed even if the client
does not recognize the extension.

## Author

DeWitt Clinton \<dewitt@opensearch.org\>

## Contributors

Michael Fagan \<mifa@a9.com\>

## License

This document is made available by [A9.com](http://a9.com) subject to
the terms of the [Creative Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
