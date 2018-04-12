## Why Should I Upgrade?

OpenSearch 1.0 was a first attempt at syndicating search results in an
open format. OpenSearch 1.1 is a more mature format, including many
changes that came about from comments on the first version. OpenSearch
1.1 is more powerful, flexible, and extensible.

Additionally, most software that produces and consumes OpenSearch will
make use of the new format, so it is a good idea to stay up to date.

**But I don’t want to\!**

This upgrade is actually very simple. Every effort was made to keep
OpenSearch 1.1 back-compatible with OpenSearch 1.0, though there are a
small number of changes that needed to be made.

Bear in mind that ; there are many new features that you can now use to
enhance your syndicated search results.

## What changed?

This document covers only the small handful of steps that are required
to upgrade. Be sure to read [the full changelog between OpenSearch 1.0
and OpenSearch 1.1](Specifications/OpenSearch/Changelog "wikilink").

## Upgrade steps

To upgrade, you will need to:

1.  [Update your OpenSearch description
    documents](#Update_your_OpenSearch_description_documents "wikilink")
2.  [Update your OpenSearch response
    feeds](#Update_your_OpenSearch_response_feeds "wikilink")

### Change the XML namespace

With OpenSearch 1.1, all parts of the OpenSearch specification were
moved under a single namespace:

  -   
    `http://a9.com/-/spec/opensearch/1.1/`

You will need to change to this namespace in both your OpenSearch
description documents and in your OpenSearch response feeds (formerly
called OpenSearch RSS).

### Update your OpenSearch description documents

To upgrade an OpenSearch description document from OpenSearch 1.0 to
OpenSearch 1.1 you will need to:

1.  [Change the XML namespace](#Change_the_XML_namespace "wikilink")
2.  [Modify the "Url" element](#Modify_the_"Url"_element "wikilink")
3.  [Replace the "SampleSearch"
    element](#Replace_the_"SampleSearch"_element "wikilink")
4.  [Remove the "Format"
    element](#Remove_the_"Format"_element "wikilink")

#### Modify the "Url" element

This is the most important change. You will need to:

1.  Move the template URL from a child text node into the new
    "`template`" attribute.
2.  Add a "`type`" attribute.

*Example of the old 1.0 Url element:*

`  `<Url>`http://example.com/?q={searchTerms}`</Url>

*Example of the new 1.1 Url element:*

` `<Url type="application/rss+xml"
       template="<nowiki>[`http://example.com/?q={searchTerms}`](http://example.com/?q=%7BsearchTerms%7D)</nowiki>`" />`

#### Replace the "SampleSearch" element

The old "SampleSearch" element has been replaced by the more powerful
"Query" element.

To convert to OpenSearch 1.1, replace your SampleSearch element with a
Query element of type="example".

*Example of the old 1.0 SampleSearch element:*

`  `<SampleSearch>`cat`</SampleSearch>

*Example of the new 1.1 Query element:*

` `<Query role="example" searchTerms="cat" />

#### Remove the "Format" element

The "Format" element has been removed from OpenSearch 1.1. Remove it
from your OpenSearch description document.

### Update your OpenSearch response feeds

To upgrade an OpenSearch response feed (formerly called OpenSearch RSS)
from OpenSearch 1.0 to OpenSearch 1.1 you will simply need to:

1.  [Change the XML namespace](#Change_the_XML_namespace "wikilink")

Of course, you will likely want to explore other types of result formats
(such as Atom 1.0) and the [wealth of powerful
functionality](Specifications/OpenSearch/1.1#OpenSearch_response_elements "wikilink")
available in OpenSearch 1.1.
