### How to return OpenSearch results from your search engine

The exact details on what needs to be done for your site depend on your
particular technology.

To get you started, the [OpenSearch client libraries
page](Community/OpenSearch_client_libraries "wikilink") contains a list
of libraries that can produce OpenSearch results within popular software
packages and programming languages.

If those libraries don't meet your needs, there are three basic steps
for publishing your search results as OpenSearch:

1.  Modify your search engine to optionally return results in RSS or
    Atom format, augmented with [OpenSearch response
    elements](Specifications/OpenSearch/1.1#OpenSearch_response_elements "wikilink").
      - Check to see if there is [already
        software](Community/OpenSearch_client_libraries "wikilink") to
        do this for you.
      - If you can edit the source code of your search engine, do so to
        support RSS or Atom based search results.
      - If you can not edit the source code, then you may be able to
        write a wrapper around the existing search results to transform
        them into RSS or Atom. XSLT works well for transforming
        XML-based search results, and Perl and Python are good languages
        to scrape HTML based search results.
2.  Create a [OpenSearch description
    document](Specifications/OpenSearch/1.1#OpenSearch_description_document "wikilink")
    and publish it on the same host as the search engine.
3.  Lastly, you’ll probably want to submit your OpenSearch description
    document to the one of the [directories of search engines that
    support
    OpenSearch](Community/OpenSearch_search_engine_directories "wikilink").

### How to indicate errors

There is no hard rule about how the search server should communicate
error conditions to the search client.

However, the technique of returning a single result containing an error
message provides the end-user with an explanation as to what wrong.

For
example:

<?xml version="1.0" encoding="UTF-8"?>

` `<rss version="2.0" xmlns:openSearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>">  
`   `<channel>  
`     `

<title>

*title*

</title>

`     `<link>*`link`*</link>  
`     `<description>*`description`*</description>  
`     `<openSearch:totalResults>`1`</openSearch:totalResults>  
`     `<openSearch:startIndex>`1`</openSearch:startIndex>  
`     `<openSearch:itemsPerPage>`1`</openSearch:itemsPerPage>  
`     `<item>  
`       `

<title>

Error

</title>

`       `<description>*`error`` ``message`*</description>  
`     `</item>  
`   `</channel>  
` `</rss>

### How to read OpenSearch results

You can use a publicly available search aggregator or search client,
such as [those listed
here](Community/OpenSearch_search_clients "wikilink").

Or you can build your own search client, perhaps using one of the
exisiting [OpenSearch client
libraries](Community/OpenSearch_client_libraries "wikilink") to get you
started.

And if nothing meets your exact needs, you can always write something
from scratch by following the [OpenSearch
specification](Specifications/OpenSearch/1.1 "wikilink").

For generating parsing/validation/marshalling-code, an [XML Schema
Definition](http://lastfmapi.svn.sourceforge.net/viewvc/lastfmapi/lastfmlib/trunk/lastfmlib/src/jaxme/OpenSearch.xsd?view=markup)
describing OpenSearch might come in handy.

### How to find OpenSearch enabled search engines

To find search engines that support OpenSearch, view [this list of sites
that maintain directories of OpenSearch enabled search
engines](Community/OpenSearch_search_engine_directories "wikilink").

### How to embed rich content in OpenSearch results

One solution is to use a [microformats-based](http://microformats.org)
approach. Please see the article on [OpenSearch and
microformats](Documentation/Recommendations/OpenSearch_and_microformats "wikilink")
for more information about this technique.
