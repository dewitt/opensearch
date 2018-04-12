## Notice

## Introduction

The OpenSearch Commerce Extension allows search engines to include
information about previewing and purchasing digital commerce items in
search results.

*Example of a search result that includes commerce elements:*

` `<feed xmlns="<nowiki>http://www.w3.org/2005/Atom</nowiki>" 
        xmlns:opensearch="<nowiki>http://a9.com/-/spec/opensearch/1.1/</nowiki>"
        xmlns:advertisement="<nowiki>http://a9.com/-/opensearch/extensions/advertisement/1.0/</nowiki>">  
`   <!-- ... -->`  
`   `<entry>  
`     <!-- ... -->`  
`     `<com:adultContent>`false`<com:adultContent>  
`     `<com:partnerId>`1234567`</com:partnerId>  
`     `<com:rating>`5.0`</com:rating>  
`     `<com:price value="2" unit="GBP" terms="unlimited"/>  
`     `<com:attribution>  
`       `<com:label atom:type="TEXT">`By Example.com`</com:label>  
`       `<atom:link href="<nowiki><http://example.com></nowiki>`"/>`  
`     `</com:attribution>  
`   `</entry>  
`   <!-- ... -->`  
` `</feed>

## Namespace

The XML namespace of the OpenSearch Commmerce Extension is:

  -   
    `http://a9.com/-/opensearch/extensions/commerce/1.0/`

This namespace and a corresponding namespace prefix must be included
when the extension is used in an OpenSearch response.

## Elements

The OpenSearch Advertisement extension introduces the following
elements.

### The "adultContent" element

The `adultContent` element specifies whether the item contains
age-restricted content. The definition of "age-restricted content" is
defined within locales and out of scope of this document.

  -   
    Restrictions: The element value is boolean (true or false). A true
    value indicates that the item contains age-restricted content.
    Requirements: This element may appear zero or one time.

*Examples of `adultContent` elements:*

` `<com:adultContent>`false`<com:adultContent>

` `<com:adultContent>`true`<com:adultContent>

### The "attribution" element

The `attribution` element specifies a contractually-obligated
attribution to be displayed with the digital commerce item.

  -   
    Requirements: This element may appear zero or one time.

<table border="1">

<tr>

<td>

<b>Sub-element Name</b>

</td>

<td>

<b>Required?</b>

</td>

<td>

<b>Sub-element Value</b>

</td>

</tr>

<tr>

<td>

label

</td>

<td>

Yes

</td>

<td>

An [atom:text
construct](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#text.constructs)
that specifies the label to display alongsite the digital commerce item.

</td>

</tr>

<tr>

<td>

link

</td>

<td>

Yes

</td>

<td>

An [Atom Link
element](http://www.atomenabled.org/developers/syndication/atom-format-spec.php#element.link)
that is the link target of the attribution label.

</td>

</tr>

</table>

*Examples of `attribution` elements:*

` `<com:attribution>  
`   `<com:label atom:type="TEXT">`By Example.com`</com:label>  
`   `<atom:link href="<nowiki><http://example.com></nowiki>`"/>`  
` `</com:attribution>

` `<com:attribution>  
`  `<com:label atom:type="TEXT">`Movies by Example.com`</com:label>  
`  `<atom:link href="<nowiki><http://example.com></nowiki>`"/>`  
` `</com:attribution>

### The "partnerId" element

The `partnerId` element is used to specify a unique identifier of a
browsable or consumable digital commerce item in a partner content
catalog.

  -   
    Restrictions: The element value is a String identifier of the item
    in a partner content catalog.
    Requirements: This element may appear zero or one time.

*Examples of `partnerId` elements:*

` `<com:partnerId>`1234567`</com:partnerId>

### The "price" element

The `price` element specifies the purchase terms, price and currency for
a consumable digital commerce item.

  -   
    Restrictions: The element value is undefined.
    Requirements: This element may appear zero or more times.

<table border="1">

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

value

</td>

<td>

A float indicating the value of the consumable item.

</td>

</tr>

<tr>

<td>

unit

</td>

<td>

The currency unit of the price.

</td>

</tr>

<tr>

<td>

terms

</td>

<td>

The terms of use for purchasing the product at this price.

</td>

</tr>

<tr>

<td>

expiration

</td>

<td>

Expiration information for the purchase.

</td>

</tr>

</table>

*Examples of `price`
elements:*

` `<com:price value="1.99" unit="USD" terms="Trial" expiration="10 days"/>

` `<com:price value="2" unit="GBP" terms="unlimited"/>

### The "rating" element

The `rating` element specifies a numeric rating for a content item.
Rating semantics for digital commerce items are out of scope for this
specification.

  -   
    Restrictions: The element value is a float rating value between 0.0
    and 5.0, inclusive.
    Requirements: This element may appear zero or one time.

*Examples of `rating` elements:*

` `<com:rating>`1.5`</com:rating>

` `<com:rating>`5.0`</com:rating>

## Authors

Gail Rahn Frederick, Damon Lanphear and Michael "Luni" Libes
\<opensearch@medio.com\> (Medio Systems)

## License

This document is made available by [Medio Systems](http://medio.com)
subject to the terms of the [Creative Commons Attribution-ShareAlike 3.0
License](http://creativecommons.org/licenses/by-sa/3.0/).

[Category:Specification](Category:Specification "wikilink")
[Category:Extension](Category:Extension "wikilink")
