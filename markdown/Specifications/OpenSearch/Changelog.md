## Version 1.1, Draft 3, Release Candidate

  - Merged core specification into single document.
  - Moved the `<Param/>` element and the `<Url/>` element's '`method`'
    attribute to the OpenSearch parameter extension.
  - Added the '`indexOffset`' and '`pageOffset`' to the `<Url/>`
    element.
  - Replaced the OpenSearch `<link/>` element with the standard Atom
    `<link/>` element.

## Version 1.1, Draft 2 (December 6 2005)

  - Unified XML namespace across core specifications.
  - Added section on autodiscovery.
  - Modified `<Tags/>` value to allow up to 256 characters.
  - Modified `<Contact/>` and `<Tags/>` elements to make them optional.
  - Modified `<atom:link rel="..."/>` values to match Atom
    specification.
  - Added `<Query/>` element.
  - Replaced `<SampleSearch/>` element in description with `<Query
    role="example"/>`.
  - Replaced `<searchTerms/>` element in response with `<Query
    role="request"/>`.

## Version 1.1, Draft 1 (September 9 2005)

  - Updated XML namespaces to reflect the new version.
  - Moved information regarding host restrictions to query syntax
    specification.
  - Modified `<Image/>` element to allow multiple occurrences.
  - Added '`width`', '`height`', and '`type`' attributes to `<Image/>`
    element.
  - Added `<Language/>`, `<OutputEncoding/>`, and `<InputEncoding/>`
    elements to description.
  - Added '`language`', '`outputEncoding`', and '`inputEncoding`' as
    core search parameters.
  - Specified MIME type for description documents.
  - Specified extensibility mechanism for custom search parameters.
  - Added '`?`' modifier for search parameters.
  - Specified extensibility mechanism for description documents.
  - Specified use of `<atom:link/>` elements in response.
  - Added `<searchTerms/>` element to response.
  - Added '`template`', '`type`', and '`method`' attributes to `<Url/>`
    element.
  - Added '`<Param/>` element to `<Url/>` element to support POST
    requests.
  - Modified `<Url/>` elements to allow multiple occurrences.
  - Removed <code>\<Format/\>/code\> element from description.
  - Renamed OpenSearch RSS to OpenSearch Response.
  - Added support for Atom, HTML, and other response formats.

## Version 1.0 (March 15 2005)

  - Released OpenSearch Description, OpenSearch Query Syntax, and
    OpenSearch RSS core specifications.
