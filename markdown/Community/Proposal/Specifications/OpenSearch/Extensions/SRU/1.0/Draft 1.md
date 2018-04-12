## Notice

## Introduction

This OpenSearch SRU Extension allows SRU (Search and Retrieval via URL)
queries to be used within OpenSearch contexts. It makes the full SRU
request parameter set available to OpenSearch implementations. This SRU
Extension is aligned with the SRU 2.0 specification.

For further information on SRU see:

1.  [SRU Home Page](http://www.loc.gov/standards/sru/)
2.  [SRU 1.2 Specs (Stable)](http://www.loc.gov/standards/sru/specs/)
3.  [SRU 2.0 Specs (Public
    Drafts)](http://www.oasis-open.org/committees/documents.php?wg_abbrev=search-ws)

## Namespace

The XML namespace of the OpenSearch SRU Extension is:

`http://a9.com/-/opensearch/extensions/sru/2.0/`

This namespace and the corresponding namespace prefix "`sru`" must be
included when the SRU Extension is used in an OpenSearch Description
document.

## Example

Example of a detailed OpenSearch description document that describes a
search engine that accept temporal search
parameters.

<?xml version="1.0" encoding="UTF-8"?>

<OpenSearchDescription xmlns="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
                        xmlns:sru="<nowiki>http://a9.com/-/opensearch/extensions/sru/2.0/</nowiki>">  
`  <!-- Admin Details -->`  
`  `<ShortName>`nature.com`</ShortName>  
`  `<LongName>`OpenSearch interface for nature.com`</LongName>  
`  `<Description>`The nature.com OpenSearch service provides a structured resource discovery facility for content hosted on nature.com. The service implements the SRU (Search and Retrieval via URL) protocol for interacting with the nature.com database. It can be accessed both natively using the SRU protocol as well as by means of the widely adopted OpenSearch conventions. `</Description>  
`  `<Tags>`nature.com opensearch sru`</Tags>  
`  `<Contact>`interfaces@nature.com`</Contact>  
`  <!-- URL Template for ATOM -->`  
`  `<Url type="application/atom+xml"
        indexOffset="1"
        template="<nowiki>[`http://www.nature.com/opensearch/request?version=1.1&operation=searchRetrieve&query={searchTerms}&queryType={sru:queryType`](http://www.nature.com/opensearch/request?version=1.1&operation=searchRetrieve&query=%7BsearchTerms%7D&queryType=%7Bsru:queryType)`?}&httpAccept=application/atom%2Bxml&recordPacking=unpacked&startRecord={startIndex?}&maximumRecords={count?}&sortKeys={sru:sortKeys?}&stylesheet={sru:stylesheet?}`</nowiki>`"/>`  
`  <!-- URL Template for SRU -->`  
`  `<Url type="application/sru+xml"
        indexOffset="1"
        template="<nowiki>[`http://www.nature.com/opensearch/request?version=1.1&operation=searchRetrieve&query={searchTerms}&queryType={sru:queryType`](http://www.nature.com/opensearch/request?version=1.1&operation=searchRetrieve&query=%7BsearchTerms%7D&queryType=%7Bsru:queryType)`?}&httpAccept=application/sru%2Bxml&startRecord={startIndex?}&maximumRecords={count?}&sortKeys={sru:sortKeys?}&stylesheet={sru:stylesheet?}`</nowiki>`"/>`  
`  <!-- Example Queries -->`  
`  `<Query role="example" sru:queryType="searchTerms" searchTerms="vampire" />  
`  `<Query role="example" sru:queryType="cql" searchTerms="vampire" />  
`  `<Query role="example" sru:queryType="cql" searchTerms="cql.keywords=vampire" />  
`  `<Query role="example" sru:queryType="cql" sru:sortKeys="title,pam,1" searchTerms="cql.keywords=vampire" />  
`  `<Query role="example" sru:queryType="cql" sru:stylesheet="<nowiki><http://example.org/example.xsl></nowiki>`" searchTerms="cql.keywords=vampire" />`  
`  <!-- Control Params -->`  
`  `<Language>`en-us`</Language>  
`  `<OutputEncoding>`UTF-8`</OutputEncoding>  
`  `<InputEncoding>`UTF-8`</InputEncoding>  
`  `<SyndicationRight>`open`</SyndicationRight>  
`  `<AdultContent>`false`</AdultContent>  
`  `<Attribution>`© 2009 Nature Publishing Group.`</Attribution>  
</OpenSearchDescription>

## Parameters

### The "queryType" parameter

`http://example.com/?query={searchTerms}&queryTerms={sru:queryType}`

The SRU parameter "`queryType`" is a string indicating the type of query
supplied in the SRU parameter "`query`" or OpenSearch parameter
"`searchTerms`" - but see below for discussion of the parameter to be
used. If "`queryType`" is omitted, the default is "`cql`", however this
default may be overridden by the server, which may indicate a default
query type via Explain. The server indicates all query types supported
via Explain.

The string "`searchTerms`" is a reserved value for query type. When
"`searchTerms`" is used as the query type, the query may (but need not)
consist of a list of terms separated by space (e.g. “`cat hat rat`”).
The server processes the query however it chooses.

### The "query" parameter

`http://example.com/?query={searchTerms}&query={sru:query}`

*(Note: This SRU parameter is provided for completeness only. The SRU
parameter "`query`" is a synonym for the OpenSearch parameter
"`searchTerms`" which should be used in preference in OpenSearch URL
templates.)*

The SRU parameter "`query`" is a query expressed in the query language
indicated by "`queryType`" (or the default, if "`queryType`" is
omitted).

### The "startRecord" parameter

`http://example.com/?query={searchTerms}&startRecord={sru:startRecord}`

*(Note: This SRU parameter is provided for completeness only. The SRU
parameter "`startRecord`" is a synonym for the OpenSearch parameter
"`startIndex`" which should be used in preference in OpenSearch URL
templates.)*

The SRU parameter "`startRecord`" specifies the start of the range of
the result set records. This is a positive integer, optional, and its
default if omitted is
1.

### The "maximumRecords" parameter

`http://example.com/?query={searchTerms}&maximumRecords={sru:maximumRecords}`

*(Note: This SRU parameter is provided for completeness only. The SRU
parameter "`maximumRecords`" is a synonym for the OpenSearch parameter
"`count`" which should be used in preference in OpenSearch URL
templates.)*

The SRU parameter "`maximumRecords`" specifies that the number of
records supplied is not to exceed maximumRecords. This is a non-negative
integer, optional, and if omitted, the server may choose any value. (The
server may return less than this number of records, for example if there
are fewer matching records than requested, but MUST NOT return more.)

### The "recordPacking" parameter

`http://example.com/?query={searchTerms}&stylesheet={sru:recordPacking}`

The SRU parameter "`recordPacking`" specifies a packing for record data
whose value is "`string`" or "`xml`" (default is "`xml`" if omitted). If
the value of the parameter is "`string`", then the server should perform
the conversion (escape the relevant characters) before transferring
records. If the value is "`xml`", then it should embed the XML directly
into the
response.

### The "recordSchema" parameter

`http://example.com/?query={searchTerms}&recordSchema={sru:recordSchema}`

The SRU parameter "`recordSchema`" identifies the XML schema of the
records to be supplied in the response. The value of the parameter is
the short name that the server assigns to the identifier for the schema,
as listed in the server’s Explain file. The default value if not
supplied is determined by the server.

Example:

`http://example.com/?query=dinosaur&recordSchema=mods`

### The "resultSetTTL" parameter

`http://example.com/?query={searchTerms}&resulSetTTL={sru:resulSetTTL}`

The SRU parameter "`resultSetTTL`" specifies a period of time (in
seconds) that the server should maintain the result set to be created.
(Note that the server may choose not to fulfill this request, and may
respond with a different value.)

### The "sortKeys" parameter

`http://example.com/?query={searchTerms}&sortKeys={sru:sortKeys}`

The SRU parameter "`sortKeys`" specifies a request for the server to
sort the result set. The "`sortKeys`" parameter consists of one or more
sort keys, each with sub-parameters:

  - `path`
      - Mandatory. An XPath expression for a tagpath to be used in the
        sort.
  - `sortSchema`
      - Optional. A short name for a URI identifying an XML schema to
        which the XPath expression applies. (The short name to URI
        mapping is included in the server’s Explain file.)
  - `ascending`
      - Optional. Boolean, default "`true`".
  - `caseSensitive`
      - Optional. Boolean, default "`false`".
  - `missingValue`
      - Optional. Default is "`highValue`".

See the SRU specification for details on representing the "`sortKeys`"
parameter value. But essentially this is a space-separated list of sort
keys, with individual sort keys comprised of a comma-separated sequence
of sub-parameters in the order listed above.

Example:

`http://example.com/?query=news&sortKeys=title,onix date,onix,,0`

This example specifies a sort primarily by "`title`" from the "`onix`"
schema (with defaults of "`ascending`", "`insensitive`" and
"`highValue`" for non-specified sub-parameters), and secondarily by
"`date`" also from the "`onix`" schema and "`insensitive`" (with
defaults of "`ascending`" and "highValue" for non-specified
sub-parameters).

### The "stylesheet" parameter

`http://example.com/?query={searchTerms}&stylesheet={sru:stylesheet}`

The SRU parameter "`stylesheet`" specifies the URL for a stylesheet to
be used for the display of the response to the user.

Example:

`http://example.com/?query=dinosaur&stylesheet=master.xsl`

### The "rendering" parameter

`http://example.com/?query={searchTerms}&rendering={sru:rendering}`

The SRU parameter "`rendering`" determines whether the stylesheet is to
be rendered by the server or client. Its value is "`client`" or
"`server`". If omitted, the default is "`client`".

## Accept Parameters

### The "httpAccept" parameter

`http://example.com/?query={searchTerms}&httpAccept={sru:httpAccept}`

The SRU parameter "`httpAccept`" may be supplied to indicate the
preferred format of the response in lieu of the "`Accept`" header field
described in the HTTP Protocol specification. (For reference, see
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>.) The value is
an internet media type. For example if the client wants the response to
be supplied in the ATOM format, the value of the parameter is
"`application/atom+xml`".

The default value for the response type is "`application/sru+xml`".

Example:

`http://example.com/?query=dinosaur&httpAccept=application/atom+xml`

This example specifies a query ("`dinosaur`") to an SRU server with
results returned as an ATOM
document.

### The "httpAcceptCharset" parameter

`http://example.com/?query={searchTerms}&httpAcceptCharset={sru:httpAcceptCharset}`

The SRU parameter "`httpAcceptCharset`" may be supplied in lieu of the
"`Accept-Charset`" header field described in the HTTP Protocol
specification. (For reference, see
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>.)

### The "httpAcceptEncoding" parameter

`http://example.com/?query={searchTerms}&httpAcceptEncoding={sru:httpAcceptEncoding}`

The SRU parameter "`httpAcceptEncoding`" may be supplied in lieu of the
"`Accept-Encoding`" header field described in the HTTP Protocol
specification. (For reference, see
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>.)

### The "httpAcceptLanguage" parameter

`http://example.com/?query={searchTerms}&httpAcceptLanguage={sru:httpAcceptLanguage}`

The SRU parameter "`httpAcceptLanguage`" may be supplied in lieu of the
"`Accept-Language`" header field described in the HTTP Protocol
specification. (For reference, see
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>.)

### The "httpAcceptRanges" parameter

`http://example.com/?query={searchTerms}&httpAcceptRanges={sru:httpAcceptRanges}`

The SRU parameter "`httpAcceptRanges`" may be supplied in lieu of the
"`Accept-Ranges`" header field described in the HTTP Protocol
specification. (For reference, see
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>.)

## Facet Parameters

### The "facetLimit" parameter

`http://example.com/?query={searchTerms}&facetLimit={sru:facetLimit}`

The SRU parameter "`facetLimit`" specifies the maximum number of counts
that should be reported per facet field. The "`facetLimit`" parameter
can be specified on a per field basis to indicate a separate limit for
certain fields.

Example:

`http://example.com/?query=news&facetLimit:dc.subject=100`

This example sets the limit to 100 for the "`dc.subject`" index.

Example:

`http://example.com/?query=news&facetLimit=10&facetLimit:dc.subject=100`

This example sets the limit to 100 for "`dc.subject`" and 10 for all
other fields. The "`facetStart`" parameter

`http://example.com/?query={searchTerms}&facetStart={sru:facetStart}`

The SRU parameter "`facetStart`" specifies an offset (1-based) into the
list of counts, to allow paging. The default value is 1 (meaning start
with the first count). This parameter can be specified on a per field
basis.

Example:

`http://example.com/?query=news&facetStart=10`

This example means begin with the 10th count.

Example:

`http://example.com/?query=news&facetStart:dc.subject=10`

This example means begin with the 10th count for "`dc.subject`".

### The "facetSort" parameter

`http://example.com/?query={searchTerms}&facetSort={sru:facetSort}`

The SRU parameter "`facetSort`" is a sort specification for the facet
results. It is non-repeatable, and has the following components:

  - `sortBy`
      - One of the following:
          - "`recordCount`"
          - "`alphanumeric`"
  - `order`
      - Optional, one of:
          - "`ascending`" (default for "`alphanumeric`")
          - "`descending`" (default for "`recordCount`" or
            "`occurrence`")
  - `caseSensitivity`
      - Optional, and meaningful only for "`alphanumeric`". One of:
          - "`caseSensitive`"
          - "`caseInsensitive`"
(default)

Example:

`http://example.com/?query=news&facetSort=recordCount`

Example:

`http://example.com/?query=news&facetSort=alphanumeric,descending,caseSensitive`

### The "facetRangeField" parameter

`http://example.com/?query={searchTerms}&facetRangeField={sru:facetRangeField}`

The SRU parameter "`facetRangeField`" specifies the name of an index to
be treated as a range facet. It is
repeatable.

Example:

`http://example.com/?query=news&facetRangeField=dateOfPublication`

### The "facetLowValue" parameter

`http://example.com/?query={searchTerms}&facetLowValue={sru:facetLowValue}`

The SRU parameter "`facetLowValue`" specifies the lowest value of the
specified facet range field for which facet counts should be
reported.

Example:

`http://example.com/?query=news&facetLowValue:dateOfPublication=20010101`

### The "facetHighValue" parameter

`http://example.com/?query={searchTerms}&facetHighValue={sru:facetHighValue}`

The SRU parameter "`facetHighValue`" specifies the highest value of the
specified facet range field for which facet counts should be
reported.

Example:

`http://example.com/?query=news&facetHighValue:dateOfPublication=20040404`

### The "facetCount" parameter

`http://example.com/?query={searchTerms}&facetCount={sru:facetCount}`

The SRU parameter "`facetCount`" may be used to request the facet count
for a specific term. The parameter may be repeated, but should not be
used in conjunction with any other facet parameter.

Example:

`http://example.com/?query=news&facetCount:dc.subject=history`

## Extension Parameters

### The "extension" parameter

`http://example.com/?query={searchTerms}&x-...={sru:extension}`

The SRU extension parameter takes on the name of the extension. It must
begin with "`x-`" (lowercase `x` followed by hyphen). SRU will never
include an official extension with a name beginning with "`x-`", so this
will never clash with a mainstream extension name.

See the SRU specification for details on naming the SRU extension
parameter.

Example:

`http://example.com/?query=news&x-info4-onSearchFail=scan`

## Author

Tony Hammond \<t.hammond@nature.com\>

## License

This document is made available subject to the terms of the [Creative
Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).
