This document describes the process used to extract the contents of
opensearch.org, import them into a version controlled repository,
convert to clean HTML5, and republish.

Initial Export
--------------

1) An unformatted copy of every page was retrieved and stored:

  $ curl http://www.opensearch.org/Special:Allpages |\
      grep -o '<a href="/[A-Z]\([^:"]*\)"' |\
      sed -n 's/^.*\"\/\([^"]*\)\".*$/\1/p' |\
      sort |\
      uniq |\
      sed 's|^\(Specifications\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/1.1\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Parameter\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Parameter/1.0\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Referrer\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Referrer/1.0\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Relevance/1.0\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Suggestions\)$|&/index\.html|g' |\
      sed 's|^\(Specifications/OpenSearch/Extensions/Suggestions/1.1\)$|&/index\.html|g' |\
      awk '/(.*)/ { printf "url = \"http://www.opensearch.org/%s?action=render\"\noutput = \"site/%s\"\n\n", $0, $0 }' |\
      curl --create-dirs --config - 

