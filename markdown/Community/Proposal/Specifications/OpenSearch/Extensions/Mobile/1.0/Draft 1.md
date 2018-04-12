## Notice

## Introduction

Mobile uses of the Internet differ from PC-based access patterns. The
purpose of the OpenSearch Mobile extensions is to provide a standard
mechanism for querying mobile-centric and PC-centric data providers and
displaying results relevant for mobile subscribers and devices.

Mobile search requests include information about the device, operator
and subscriber. Mobile search responses include answers, not links.
Mobile search results are federated from numerous content sources and
presented in categories.

*Example of a search result that includes mobile elements:*

` `<feed xmlns="<nowiki>http://www.w3.org/2005/Atom</nowiki>" 
        xmlns:opensearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
        xmlns:advertisement="<nowiki>http://a9.com/-/opensearch/extensions/advertisement/1.0/</nowiki>">  
`   <!-- ... -->`  
`   `<entry>  
`     <!-- ... -->`  
`   `</entry>  
`   <!-- ... -->`  
`   `<m:device m:make="Motorola" m:model="V3r" m:id="mot_v3r_ver1">`MOT-V3r`</m:device>  
`   `<m:subscriber>`2065551212`</m:subscriber>  
` `</feed>

## Namespace

The XML namespace of the OpenSearch Mobile Extension is:

  -   
    `http://a9.com/-/opensearch/extensions/mobile/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch response.

## Parameters

The OpenSearch Mobile extension introduces the following parameters.

### The "userAgent" parameter

Replaced with a string describing the User-Agent of the mobile device
for which to target search results. This string is parsed and managed by
the search service.

If the search request includes the User-Agent as a header, then this
parameter should not be included in the URL. If the User-Agent header is
not provided, or is the value of a proxy or other intermediate server,
then this parameter must be included.

When the User-Agent parameter is provided, the search engine may filter
or format search results to target the specified mobile device.

An identifying substring of the User-Agent may be submitted only when
the entire User-Agent is not available.

*Example URL
template:*

` http://example.com/?q={searchTerms}&pw={startPage?}&userAgent={m:userAgent?}&format=atom`

*Example
request:*

` http://example.com/?q=pizza&userAgent=MOT-V3r%2F08.BD.20I%20MIB%2F2.2.1%20Profile%2FMIDP-2.0%20Configuration%2FCLDC-1.1&format=atom`

### The "subId" parameter

Replaced with the unique identifier of the subscriber or handset.

*Example URL
template:*

` http://example.com/?q={searchTerms}&pw={startPage?}&subId={m:subId?}&format=atom`

*Example
request:*

` http://example.com/?q=pizza&userAgent=MOT-V3r&subId=A12C92JXV558&format=atom`

### The "mcc" and "mnc" parameters

The mcc parameter specifies the [Mobile Country Code
(MCC)](http://en.wikipedia.org/wiki/Mobile_Country_Code) of the country,
and the mnc parameter specifies the [Mobile Network Code
(MNC)](http://en.wikipedia.org/wiki/Mobile_network_code)of the operator
network of the handset where the search request originated.

The MCC and MNC are used in combination to uniquely identify a mobile
phone operator within the GSM, CDMA, iDEN and UMTS mobile networks and
some satellite mobile networks.

*Example URL
template:*

` http://example.com/?q={searchTerms}&pw={startPage?}&mcc={m:mcc?}&mnc={m:mnc?}&format=atom`

*Example request from a Verizon Wireless handset in the United
States:*

` http://example.com/?q=pizza&userAgent=MOT-V3r&mcc=310&mnc=012&format=atom`

### Optional Parameters

The search server should use the "?" flag in the URL template when
requesting the source parameter to indicate that this parameter is
optional and that a search can still be performed even if the client
does not recognize the
extension.

*Example:*

` http://example.com/?q={searchTerms}&pw={startPage?}&userAgent={m:userAgent?}&subId={m:subId?}&mnc={m:mnc?}&mcc={m:mcc?}&format=atom`

## Atom Extensions

### New Relation Values for Atom Link Elements

To capture link relationships for mobile search results, this extension
introduces the following new values of the *rel* attribute of the [Atom
Link
element](http://www.atompub.org/2005/07/11/draft-ietf-atompub-format-10.html#rfc.section.4.2.7).

<table border="1">

<tr>

<td>

<b>rel Attribute Value</b>

</td>

<td>

<b>Description</b>

</td>

</tr>

<tr>

<td>

next-page

</td>

<td>

The value of the href attribute identifies the next full page of search
results.

</td>

</tr>

<tr>

<td>

page-\#

</td>

<td>

The value of the href attribute identifies a target page of search
results. (i.e. page-2, page-3, etc.)

</td>

</tr>

<tr>

<td>

section

</td>

<td>

The value of the href attribute identifies a section of search results.
(See below for the definition of "section".)

</td>

</tr>

<tr>

<tr>

<td>

detail

</td>

<td>

The value of the href attribute identifies a page containing details for
a single search result.

</td>

</tr>

<tr>

<td>

spelling

</td>

<td>

The value of the href attribute identifies the first full page of search
results for a spell-corrected search query.

</td>

</tr>

</table>

## Elements

The OpenSearch Mobile extension introduces the following elements.

### The "device" element

The `device` element is used to describe the mobile device targeted by
the search results.

  -   
    Restrictions: The element value is a String that is the User-Agent
    provided in the search request, either as a parameter or in the
    request headers.
    Requirements: This element may appear zero or one time.

<table>

<tr>

<td>

<b>Attribute Name</b>

</td>

<td>

<b>Attribute Value</b>

</td>

</tr>

<tr>

<td>

make

</td>

<td>

The device make or manufacturer.

</td>

</tr>

<tr>

<td>

model

</td>

<td>

The model name of the device.

</td>

</tr>

<tr>

<td>

id

</td>

<td>

The search service's unique identifier for the device.

</td>

</tr>

</table>

*Examples of `device`
elements:*

` `<m:device m:make="Motorola" m:model="V3r" m:id="mot_v3r_ver1">`MOT-V3r`</m:device>

` `<m:device m:make="Nokia" m:model="N73" m:id="nokia_n73_ver1">`NokiaN73`</m:device>

### The "subscriber" element

The `subscriber` element is used to identify the mobile subscriber
targeted by the search results.

  -   
    Restrictions: The element value is a String that is the unique
    identifier of the subscriber. The alphanumeric format of the
    identifier varies from operator to operator and is out of scope of
    this specification.
    Requirements: This element may appear zero or one time.

*Examples of `subscriber` elements:*

` `<m:subscriber>`2065551212`</m:subscriber>

` `<m:subscriber>`1a854e9c02fd2520`</m:subscriber>

## Nesting Search Results into Sections using Atom Entries

Mobile search is not desktop web search. Mobile search results are
presented in a federated format with search results categorized into
sections. A section generally corresponds to a.

In OpenSearch Mobile, the relationship between sections and search
results is expressed in the following way:

  - All immediate [Atom Entry
    element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry)
    children of the [Atom Feed
    element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#feed.entry)
    represent sections of mobile search results.
  - An [Atom Entry
    element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry)
    that represents a section of mobile search results contains zero or
    more immediate child [Atom Entry
    elements](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry),
    each representing an individual browsable or consumable mobile
    search result related to the section.
  - An [Atom Entry
    element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry)
    representing an individual mobile search result contains no child
    [Atom Entry
    elements](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry).
  - All [Atom Category
    elements](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.category)
    elements defined in an [Atom Entry
    element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry)
    representing a section of mobile search results are inherited by the
    immediate child [Atom Entry
    elements](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry),
    which represent individual search results related to the section.

### Suggested Extensions to an Atom Entry Element for Sections

Here is a list of suggested extension elements for an [Atom Entry
element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.entry)
that represents a section of mobile search results.

<table border="1">

<tr>

<td>

<b>Suggested Element</b>

</td>

<td>

<b>Source</b>

</td>

<td>

<b>Description</b>

</td>

</tr>

<tr>

<td>

totalResults

</td>

<td>

OpenSearch

</td>

<td>

The total number of mobile search results in this section.

</td>

</tr>

<tr>

<td>

entry

</td>

<td>

Atom

</td>

<td>

A mobile search result item related to the section. (One atom:entry
element per mobile search result.)

</td>

</tr>

</table>

### An Example Atom Entry Element for a Section of Search Results

Here is an example of a section of mobile search
results.

` `<atom:entry xs:type="m:sectionEntry" xmlns:xs="<nowiki>http://www.w3.org/2001/XMLSchema-instance</nowiki>">  
`   `<atom:category term="local-directory" label="LOCAL_DIRECTORY"/>  
`   `<atom:title atom:type="TEXT">`Local Business`</atom:title>  
`   `<atom:link title="9 Results" rel="self" href="<nowiki><http://example.com/opensearch?q=>`...`</nowiki>`"/>`  
`   `<opensearch:totalResults>`9`</opensearch:totalResults>  
`   `<atom:entry>  
`     `<atom:title atom:type="TEXT">`Cafe 5ive`</atom:title>  
`     `<atom:link rel="self" href="<nowiki><http://example.com/opensearch?q=>`...`</nowiki>`"/>`  
`   `</atom:entry>  
`   `<atom:entry>  
`     `<atom:title atom:type="TEXT">`M & M Associates`</atom:title>  
`     `<atom:link rel="self" href="<nowiki><http://example.com/opensearch?q=>`...`</nowiki>`"/>`  
`   `</atom:entry>  
`   `<atom:entry>  
`     `<atom:title atom:type="TEXT">`Simons Espresso Cafe`</atom:title>  
`     `<atom:link rel="self" href="<nowiki><http://example.com/opensearch?q=>`...`</nowiki>`"/>`  
`   `</atom:entry>  
` `</atom:entry>

## Suggested Extensions to an Atom Feed Element for Mobile Search

Here is a list of suggested extension elements for an [Atom Feed
element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#feed.entry)
that represents a feed of mobile search results.

<table border="1">

<tr>

<td>

<b>Suggested Element</b>

</td>

<td>

<b>OpenSearch
Extension</b>

</td>

<td>

<b>Description</b>

</td>

</tr>

<tr>

<td>

device

</td>

<td>

[Mobile](http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/Mobile/1.0/Draft_1)

</td>

<td>

The device targeted for search
results.

</td>

</tr>

<tr>

<td>

subscriber

</td>

<td>

[Mobile](http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/Mobile/1.0/Draft_1)

</td>

<td>

The subscriber targeted for search
results.

</td>

</tr>

<tr>

<td>

advertisement

</td>

<td>

[Advertisement](http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/Advertisement/1.0/Draft_1)

</td>

<td>

An advertisement to display with mobile search results. (Multiple
instances allowed.)

</td>

</tr>

</table>

## Related Extensions

Designers of OpenSearch-compliant mobile search systems should consider
supporting these additional
    extensions:

  - [Advertisement](http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/Advertisement/1.0/Draft_1)
  - [Commerce](http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/Commerce/1.0/Draft_1)
  - [Geo](http://www.opensearch.org/Specifications/OpenSearch/Extensions/Geo/1.0/Draft_1)
  - [Spelling](http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/Spelling/1.0/Draft_1)
  - [Relevance](http://www.opensearch.org/Specifications/OpenSearch/Extensions/Relevance/1.0)
  - [Suggestions](http://www.opensearch.org/Specifications/OpenSearch/Extensions/Suggestions/1.0)
    (possibly with alternative output formats)

## Authors

Gail Rahn Frederick, Damon Lanphear and Michael "Luni" Libes
\<opensearch@medio.com\> (Medio Systems)

## License

This document is made available by [Medio Systems](http://medio.com)
subject to the terms of the [Creative Commons Attribution-ShareAlike 3.0
License](http://creativecommons.org/licenses/by-sa/3.0/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
