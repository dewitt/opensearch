## Notice

## Introduction

As the amount of historic data builds on the web, it is valuable to
provide a way for users and tools to easily query based on time and
timespans. The purpose of the OpenSearch-Time extensions is to provide a
standard mechanism to query a resource based on temporal extents.

The Temporal parameters are based on the
[iCalendar](http://en.wikipedia.org/wiki/ICalendar) and Microformat
standards.

### Namespace

Updated July 27, 2007: the OpenSearch Time extension namespace was
shortened to just "time" instead of "opensearchtime". This was to make
the namespace more succint.

## Example

Example of a detailed OpenSearch description document that describes a
search engine that accept temporal search
parameters.

<?xml version="1.0" encoding="UTF-8"?>

` `<OpenSearchDescription xmlns="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
                         xmlns:time="<nowiki>http://a9.com/-/opensearch/extensions/time/1.0/</nowiki>">  
`   `<ShortName>`Web Search`</ShortName>  
`   `<Description>`Use Example.com to search the Web.`</Description>  
`   `<Tags>`example web`</Tags>  
`   `<Contact>`admin@example.com`</Contact>  
`   `<Url type="application/atom+xml"
        template="<nowiki>[`http://example.com/?q={searchTerms}&dtstart={time:start`](http://example.com/?q=%7BsearchTerms%7D&dtstart=%7Btime:start)`?}&dtend={time:end?}&pw={startPage?}&format=atom`</nowiki>`"/>`  
`   `<Url type="text/html"
        template="<nowiki>[`http://example.com/?q={searchTerms}&dtstart={time:start`](http://example.com/?q=%7BsearchTerms%7D&dtstart=%7Btime:start)`?}&dtend={time:end?}&pw={startPage?}`</nowiki>`"/>`  
`   `<LongName>`Example.com Web Search`</LongName>  
`   `<Image height="64" width="64" type="image/png"><http://example.com/websearch.png></Image>  
`   `<Query role="example" searchTerms="cat" />  
`   `<Developer>`Example.com Development Team`</Developer>  
`   `<Attribution>  
`       Search data Copyright 2005, Example.com, Inc., All Rights Reserved`  
`   `</Attribution>  
`   `<SyndicationRight>`open`</SyndicationRight>  
`   `<AdultContent>`false`</AdultContent>  
`   `<Language>`en-us`</Language>  
`   `<OutputEncoding>`UTF-8`</OutputEncoding>  
`   `<InputEncoding>`UTF-8`</InputEncoding>  
` `</OpenSearchDescription>

## Namespace

The XML namespace of the OpenSearch Time Extension is:

` http://a9.com/-/opensearch/extensions/time/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch Description
document.

## Parameters

### The "start" and "end" parameters

` http://example.com/?q={searchTerms}&pw={startPage?}&dtstart={time:start}&dtend={time:end}&format=rss`

Replaced with a string of the beginning of the time slice of the search
query. This string should match the [RFC-3339 - Date and Time on the
Internet: Timestamps](http://www.ietf.org/rfc/rfc3339.txt), which is
also used by the [Atom syndication
format](http://www.ietf.org/rfc/rfc4287.txt).

It is of the format

` YYYY-MM-DDTHH:mm:ssZ`  
` 1996-12-19T16:39:57-08:00`

'Z' is the time-offset, where 'Z' signifies UTC or an actual offset can
be
used.

Example:

` http://example.com/?q=news&dtstart=2007-02-12T04:30:02Z&dtend=2007-03-11T02:28:00Z&format=rss`

## Author

Andrew Turner \<ajturner@highearthorbit.com\>

## Contributors

DeWitt Clinton \<dewitt@opensearch.org\>

## License

This document is made available subject to the terms of the [Creative
Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
