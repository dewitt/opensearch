## Notice

## Overview

The OpenSearch parameter extension is an enhancement to the [OpenSearch
description
document](Specifications/OpenSearch/1.1#OpenSearch_description_document "wikilink")
that enables an augmented query parameter mechanism via structured XML.
The extension also includes a mechanism for specifying alternate HTTP
request methods, such as POST, and a mechanism for specifying alternate
request encodings, such as " multipart/form-data".

*Example of a Url element that uses the OpenSearch parameter extension
to specify a POST search
interface:*

` `<Url xmlns:parameters="<nowiki>http://a9.com/-/spec/opensearch/extensions/parameters/1.0/</nowiki>"
       type="text/html"
       template="h<nowiki>ttp://example.com/search</nowiki>"
       parameters:method="POST"
       parameters:enctype="application/x-www-form-urlencoded">  
`   `<parameters:Parameter name="q" value="{searchTerms}"/>  
`   `<parameters:Parameter name="count" value="{itemsPerPage}" minimum="0"/>  
`   `<parameters:Parameter name="start" value="{startIndex}" minimum="0"/>  
` `</Url>

## Namespace

The XML Namespaces URI for the OpenSearch parameter extension is:

  -   
    http://a9.com/-/spec/opensearch/extensions/parameters/1.0/

## Elements

### The "Url" element

The OpenSearch parameter extension adds two new attributes to the ["Url"
element](Specifications/OpenSearch/1.1#The_"Url"_element "wikilink") in
the [OpenSearch description
document](Specifications/OpenSearch/1.1#OpenSearch_description_document "wikilink").

*The new attributes must be explicitly associated with the [OpenSearch
parameter extension namespace](#Namespace "wikilink") via a valid XML
prefix.*

  -   
    New Attributes:
      -   
        `method` - Contains a case-insensitive string that identifies
        the HTTP request method that the search client should use to
        perform the search request.
          -   
            Restrictions: Must be a valid [HTTP request
            method](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9),
            as specified in RFC 2616.
            Default: "get"
            Requirements: This attribute is optional.
        `enctype` - Contains a string that identifies the content
        encoding the search client should use to perform the search
        request.
          -   
            Default: "application/x-www-form-urlencoded"
            Requirements: This attribute is optional.

*Example of a Url element that specifies a HTTP POST
query:*

` `<Url xmlns:parameters="<nowiki><http://a9.com/-/spec/opensearch/extensions/parameters/1.0/></nowiki>`"`  
`      type="application/atom+xml"`  
`      template="http://example.com/search?q={searchTerms}"`  
`      parameters:method="POST"`  
`      parameters:enctype="application/x-www-form-urlencoded" />`

### The "Parameter" element

Describes a name/value pair to be included in the search request.

  -   
    Parent: Url
    Attributes:
      -   
        `name` - Contains the name of the parameter.
          -   
            Restrictions: Must be a valid parameter name for format
            identified by the "enctype" parameter on the containing
            "Url" element.
            Requirements: This attribute is **required**.
        `value` - Contains a string that will be processed according to
        the rules of the [OpenSearch URL template
        syntax](Specifications/OpenSearch/1.1#OpenSearch_URL_template_syntax "wikilink").
          -   
            Default: ""
            Requirements: This attribute is optional.
        `minimum` - Contains a string that identifies the minimum number
        of times this parameter must be included in the search request.
          -   
            Restrictions: The value must be a non-negative integer.
            Default: "1"
            Requirements: This attribute is optional.
        `maximum` - Contains a string that identifies the maximim number
        of times this parameter must be included in the search request.
        The literal string "\*" will be interpreted to mean that the
        parameter may repeat an arbitrary number of times.
          -   
            Restrictions: The value must be a non-negative integer or
            the literal string "\*".
            Default: "1"
            Requirements: This attribute is optional.

*Example of a Parameter element used to represent a simple required core
search parameter:*

` `<Parameter name="q" value="{searchTerms}" />

*Example of a Parameter element used to represent a simple optional core
search parameter:*

` `<Parameter name="start" value="{startIndex}" minimum="0" />

*Example of a Parameter element used to represent a repeating custom
search
parameter:*

` `<Parameter xmlns:custom="<nowiki><http://example.com/opensearchextensions/1.0/></nowiki>`" `  
`            name="tag"`  
`            value="{custom:tag}"`  
`            minimum="0"`  
`            maximum="*" />`

## Processing Rules

*In general, the search client should follow the mechanisms for
formulating the HTTP request according the encoding type specified via
the "enctype" parameter. The OpenSeach parameter extension is intended
to be open-ended and flexible and allow for future encoding types to be
included as they are developed.*

#### The "application/x-www-form-urlencoded" encoding type

The search request will constructed as type
application/x-www-form-urlencoded, as specified in [Section 17.13.4.1
Form content
types](http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.1) of
the [XHTML 4.0.1 specification](http://www.w3.org/TR/html401/).

#### The "multipart/form-data" encoding type

The search request will constructed as type multipart/form-data, as
specified in [Section 17.13.4.2 Form content
types](http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) of
the [XHTML 4.0.1 specification](http://www.w3.org/TR/html401/).

## Author

DeWitt Clinton \<dewitt@opensearch.org\>

## License

This document is made available by [A9.com](http://a9.com) subject to
the terms of the [Creative Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
