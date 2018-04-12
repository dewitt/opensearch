## Notice

## Introduction

Geospatial data is becoming increasingly available as the tools for
specifying and sharing location are more ubiquitous and easy to use. The
purpose of the OpenSearch-Geo extensions is to provide a standard
mechanism to query a resource based on geographic extents, or location
name.

The geospatial results are based on the GeoRSS standard. Therefore,
latitude/longitude order, bounding box parameters are using that
standard.

### Namespace

Updated July 27, 2007: the OpenSearch Geo extension namespace was
shortened to just "geo" instead of "opensearchgeo". This was to make the
namespace more succinct.

## Example

Example of a detailed OpenSearch description document that describes a
search engine that accept geospatial search
parameters.

<?xml version="1.0" encoding="UTF-8"?>

` `<OpenSearchDescription xmlns="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
                         xmlns:geo="<nowiki>http://a9.com/-/opensearch/extensions/geo/1.0/</nowiki>">  
`   `<ShortName>`Web Search`</ShortName>  
`   `<Description>`Use Example.com to search the Web.`</Description>  
`   `<Tags>`example web`</Tags>  
`   `<Contact>`admin@example.com`</Contact>  
`   `<Url type="application/vnd.google-earth.kml+xml"
        template="<nowiki>[`http://example.com/?q={searchTerms}&pw={startPage`](http://example.com/?q=%7BsearchTerms%7D&pw=%7BstartPage)`?}&bbox={`<geo:box>`?}&format=kml`</nowiki>`"/>`  
`   `<Url type="application/atom+xml"
        template="<nowiki>[`http://example.com/?q={searchTerms}&pw={startPage`](http://example.com/?q=%7BsearchTerms%7D&pw=%7BstartPage)`?}&bbox={`<geo:box>`?}&format=atom`</nowiki>`"/>`  
`   `<Url type="application/rss+xml"
        template="<nowiki>[`http://example.com/?q={searchTerms}&pw={startPage`](http://example.com/?q=%7BsearchTerms%7D&pw=%7BstartPage)`?}&bbox={`<geo:box>`?}&format=rss`</nowiki>`"/>`  
`   `<Url type="text/html"
        template="<nowiki>[`http://example.com/?q={searchTerms}&bbox={geo:box`](http://example.com/?q=%7BsearchTerms%7D&bbox=%7Bgeo:box)`?}&pw={startPage?}`</nowiki>`"/>`  
`   `<LongName>`Example.com Web Search`</LongName>  
`   `<Image height="64" width="64" type="image/png"><http://example.com/websearch.png></Image>  
`   `<Image height="16" width="16" type="image/vnd.microsoft.icon">`http://example.com/websearch.ico`</Image>  
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

The XML namespace of the OpenSearch Geo Extension is:

  -   
    `http://a9.com/-/opensearch/extensions/geo/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch Description document.

## Parameters

### The "name" parameter

Replaced with a string describing the location (place name) to perform
the search. This location string will be parsed and geocoded by the
search service.

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&pw={startPage?}&l={geo:name?}&format=rss`

</code>

Example request:

<code>

` http://example.com/?q=pizza&l=boston&format=rss`

</code>

#### The "locationString" parameter (deprecated)

Use the "name" parameter instead.

### The "lat" and "lon" parameters

Replaced with the "latitude, longitude", respectively, in decimal
degrees in [EPSG:4326](http://nsidc.org/data/atlas/epsg_4326.html)
(typical WGS84 coordinates as returned by a GPS receiver). This
parameter should also include a "radius" parameter that specifies the
search radius, in meters. If no radius is supplied, then the search
service is free to use a default radius but should specify this radius
in the returned result.

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&pw={startPage?}&lat={geo:lat?}&lon={geo:lon?}&r={geo:radius?}&format=rss`

</code>

Example request:

<code>

` http://example.com/?q=pizza&lat=43.25&lon=-123.45&format=rss`

</code>

### The "radius" parameters

The radius parameter, used with the lat and lon parameters, specifies
the search distance from this point. The distance is in meters along the
Earth's
surface.

Example:

` http://example.com/?q=pizza&lat=43.25&lon=-123.45&radius=10000&format=rss`

### The "box" parameter

Replaced with the bounding box to search for geospatial results within.
The box is defined by "west, south, east, north" coordinates of
longitude, latitude, in a
[EPSG:4326](http://nsidc.org/data/atlas/epsg_4326.html) decimal degrees.
This is also commonly referred to by minX, minY, maxX, maxY (where
longitude is the X-axis, and latitude is the Y-axis), or also SouthWest
corner and NorthEast corner.

` `<geo:box>` ~ west, south, east, north`

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&pw={startPage?}&bbox={geo:box?}&format=rss`

</code>

Example
request:

<code>

` http://example.com/?q=pizza&b=-111.032,42.943,-119.856,43.039&format=rss`

</code>

### The "geometry" parameter

Replaced with a geometry defined using the Well Known Text (WKT)
standard. The following 2D geometric objects can be described:

  - POINT
  - LINESTRING
  - POLYGON
  - MULTIPOINT
  - MULTILINESTRING
  - MULTIPOLYGON

Note that the WKT coordinate pairs are in lon, lat order; opposit to
GeoRSS.

Polygons are a collection of linearrings. The outer ring is expressed in
counter-clockwise order. Internal rings have the opposite orientation,
appearing as clockwise (see 6.1.11.1 in OGC Simple Features
Specification v. 1.2.0).

Spaces must be URL encoded ('%20' or '+') in the request.

Example
geometries:

<code>

` POINT(6 10)`  
` LINESTRING(3 4,10 50,20 25)`  
` POLYGON((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2))`  
` MULTIPOINT(3.5 5.6, 4.8 10.5)`  
` MULTILINESTRING((3 4,10 50,20 25),(-5 -8,-10 -8,-15 -4))`  
` MULTIPOLYGON(((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2)),((6 3,9 2,9 4,6 3)))`

</code>

Example URL
template:

<code>

` http://example.com/?q={searchTerms}&pw={startPage?}&g={geo:geometry?}&format=rss`

</code>

Example
request:

<code>

` http://example.com/?q=pizza&g=POLYGON((0.582%2040.496%2C%200.231%2040.737%2C%200.736%2042.869%2C%203.351%2042.386%2C%203.263%2041.814%2C%202.164%2041.265%2C%200.978%20%20%2040.957%2C%200.802%2040.781%2C%200.978%2040.649%2C%200.582%2040.496))&format=rss`

</code>

References:

  - Wikipedia:
    <http://en.wikipedia.org/wiki/Well-known_text#Geometric_objects>
  - OGC Simple Features Specification:
    <http://portal.opengeospatial.org/files/?artifact_id=18241>

#### The "polygon" parameter (deprecated)

Use the "geometry" parameter instead.

### The "relation" parameter

Replace by the spatial relation of the search. By default the geo
searches return the records that intersect the query. The possible
values are:

  - intersects (default)
  - contains
  - disjoint

### The "uid" parameter

Replace by the identifier of the resource within the search engine
context (local reference). This parameter is used to query resources by
their fragment identifier, unique within the search scope only. It can
be used to query local identifiers that are not URI including the
support of GML identifiers

## Optional Parameters

The search server should use the "?" flag in the URL template when
requesting the source parameter to indicate that this parameter is
optional and that a search can still be performed even if the client
does not recognize the extension.

Therefore, if a service provides multiple optional geographic search
parameters, these can be combined into a single definition of optional
parameters:

Example:

` http://example.com/?q={searchTerms}&pw={startPage?}&p={geo:polygon?}&lat={geo:lat?}&lon={geo:lon?}&d={geo:radius?}&bbox={geo:box?}&format=kml`

## Geo response elements

The OpenSearch-Geo response elements can be used by search engines to
augment existing XML formats with search-related metadata. See the
[OpenSearch
response](http://www.opensearch.org/Specifications/OpenSearch/1.1#OpenSearch_response_elements)
definition for a general overview of the response options.

The following examples illustrate Geo-specific responses. For RSS and
Atom responses, it is suggested to use the GeoRSS channel elements in
addition to the OpenSearch-Geo elements.

### Atom Response

Example
request:

<code>

` http://example.com/New+York+History?pw=3&format=atom&bbox=-74.0667,40.69418,-73.9116,40.7722"`

</code>

Example response:

<?xml version="1.0" encoding="UTF-8"?>

`    `<feed xmlns="<nowiki>http://www.w3.org/2005/Atom</nowiki>" 
           xmlns:opensearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
           xmlns:georss="<nowiki>http://www.georss.org/georss</nowiki>">  
`      `

<title>

Example.com Search: New York
history

</title>

`      `<link href="<nowiki><http://example.com/New+York+history></nowiki>`"/>`  
`      `<updated>`2003-12-13T18:30:02Z`</updated>  
`      `<author>` `  
`        `<name>`Example.com, Inc.`</name>  
`      `</author>` `  
`      `<id><urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6></id>  
`      `<opensearch:totalResults>`4230000`</opensearch:totalResults>  
`      `<opensearch:startIndex>`21`</opensearch:startIndex>  
`      `<opensearch:itemsPerPage>`10`</opensearch:itemsPerPage>  
`      `<opensearch:Query role="request" searchTerms="New York History" startPage="3" geo:box="-74.0667,40.69418,-73.9116,40.7722"/>  
`      `<link rel="alternate" href="<nowiki><http://example.com/New+York+History?pw=3&bbox=-74.0667,40.69418,-73.9116,40.7722>`" type="text/html"/>`  
`      `<link rel="search" type="application/opensearchdescription+xml" href="<nowiki><http://example.com/opensearchdescription.xml></nowiki>`"/>`  
`      `<georss:box>`40.69418 -74.0667 40.7722 -73.9116`</georss:box>  
`      `<entry>  
`        `

<title>

New York
History

</title>

`        `<link href="<nowiki><http://www.columbia.edu/cu/lweb/eguids/amerihist/nyc.html></nowiki>`"/>`  
`        `<id><urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a></id>  
`        `<updated>`2003-12-13T18:30:02Z`</updated>  
`        `<georss:line>`40.73763 -73.9972 40.73519 -73.99167 40.737015 -73.99035 40.73643 -73.98914 40.734640 -73.990431 40.731617 -73.991504`</georss:line>  
`        `<content type="text">  
`          ... Union Square.NYC - A virtual tour and information on `  
`          businesses ...  with historic photos of Columbia's own New York `  
`          neighborhood ... Internet Resources for the City's History. ...`  
`        `</content>  
`      `</entry>  
`    `</feed>

### KML Response

KML is an acceptable and recommended response option for geospatial
searches. KML allows for styling and complex responses, similar to HTML
response for non-spatial queries.

Example
request:

<code>

` http://example.com/New+York+History?pw=3&format=kml&bbox=-74.0667,40.69418,-73.9116,40.7722"`

</code>

Example response:

<code>

<?xml version="1.0" encoding="UTF-8"?>

`   `<kml xmlns="<nowiki>http://earth.google.com/kml/2.2</nowiki>"
      xmlns:atom="<nowiki>http://www.w3.org/2005/Atom</nowiki>"
      xmlns:opensearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
      xmlns:opensearchgeo="<nowiki>http://a9.com/-/opensearch/extensions/geo/1.0/</nowiki>">  
`      `<opensearch:totalResults>`4230000`</opensearch:totalResults>  
`      `<opensearch:startIndex>`21`</opensearch:startIndex>  
`      `<opensearch:itemsPerPage>`10`</opensearch:itemsPerPage>  
`      `<opensearch:Query role="request" searchTerms="New York History" startPage="3" geo:box="-74.0667,40.69418,-73.9116,40.7722"/>  
`      `<atom:link rel="alternate" href="<nowiki><http://example.com/New+York+History?pw=3&bbox=-74.0667,40.69418,-73.9116,40.7722></nowiki>`" type="text/html"/>`  
`      `<atom:link rel="alternate" href="<nowiki><http://example.com/New+York+History?pw=3&bbox=-74.0667,40.69418,-73.9116,40.7722&format=atom></nowiki>`" type="application/atom+xml"/>       `  
`   `<Document>  
`     `<name>`NYCHistory.kml`</name>  
`     `<open>`1`</open>  
`     `<Placemark>  
`       `<name>`New York History`</name>  
`       `<atom:link>`http://www.columbia.edu/cu/lweb/eguids/amerihist/nyc.html`</atom:link>  
`       `<LineString>  
`         `<coordinates>  
`           -73.9972,40.73763,0 -73.99167,40.73519,0 -73.99035,40.737015,0 `  
`           -73.98914,40.73643,0 -73.990431,40.734640,0 -73.991504,40.731617,0`  
`         `</coordinates>  
`       `</LineString>  
`     `</Placemark>  
`   `</Document>  
`   `</kml>

</code>

## Author

Andrew Turner \<ajturner@highearthorbit.com\>

## Contributors

DeWitt Clinton \<dewitt@opensearch.org\>

Andrew Turner

Jo Walsh

Oscar Fonts

Pedro Goncalves

## License

This document is made available subject to the terms of the [Creative
Commons Attribution-ShareAlike 2.5
License](http://creativecommons.org/licenses/by-sa/2.5/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
