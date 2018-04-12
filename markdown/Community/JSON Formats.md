A list of existing JSON serializations of search results.

## Google Ajax Search API

Reference
<http://code.google.com/apis/ajaxsearch/documentation/#API_Overview>

Query:

` `<http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=Paris%20Hilton>

Response:

    <nowiki>{
     "responseData": {
      "cursor": {
       "currentPageIndex": 0, 
       "moreResultsUrl": "http:\/\/www.google.com\/search?oe=utf8&ie=utf8&source=uds&start=0&hl=en&q=Paris+Hilton", 
       "pages": [
        {
         "start": "0", 
         "label": 1
        }, 
        {
         "start": "4", 
         "label": 2
        }, 
        {
         "start": "8", 
         "label": 3
        }, 
        {
         "start": "12", 
         "label": 4
        }, 
        {
         "start": "16", 
         "label": 5
        }, 
        {
         "start": "20", 
         "label": 6
        }, 
        {
         "start": "24", 
         "label": 7
        }, 
        {
         "start": "28", 
         "label": 8
        }
       ], 
       "estimatedResultCount": "86700000"
      }, 
      "results": [
       {
        "GsearchResultClass": "GwebSearch", 
        "visibleUrl": "www.parishilton.com", 
        "titleNoFormatting": "Paris Hilton | The Official Website", 
        "title": "<b>Paris Hilton<\/b> | The Official Website", 
        "url": "http:\/\/www.parishilton.com\/", 
        "cacheUrl": "http:\/\/www.google.com\/search?q=cache:EgDCCgd54xQJ:www.parishilton.com", 
        "unescapedUrl": "http:\/\/www.parishilton.com\/", 
        "content": "<b>ParisHilton<\/b>.com <b>Paris Hilton<\/b>, Nicky <b>Hilton<\/b> Fashion, Pictures, Apparel, Jewellery  , Film, and Fun."
       }, 
       {
        "GsearchResultClass": "GwebSearch", 
        "visibleUrl": "en.wikipedia.org", 
        "titleNoFormatting": "Paris Hilton - Wikipedia, the free encyclopedia", 
        "title": "<b>Paris Hilton<\/b> - Wikipedia, the free encyclopedia", 
        "url": "http:\/\/en.wikipedia.org\/wiki\/Paris_Hilton", 
        "cacheUrl": "http:\/\/www.google.com\/search?q=cache:TwrPfhd22hYJ:en.wikipedia.org", 
        "unescapedUrl": "http:\/\/en.wikipedia.org\/wiki\/Paris_Hilton", 
        "content": "<b>Paris<\/b> Whitney <b>Hilton<\/b> (born February 17, 1981) is an American celebutante,   television personality, actress, singer and model. <b>...<\/b>"
       }, 
       {
        "GsearchResultClass": "GwebSearch", 
        "visibleUrl": "www.imdb.com", 
        "titleNoFormatting": "Paris Hilton", 
        "title": "<b>Paris Hilton<\/b>", 
        "url": "http:\/\/www.imdb.com\/name\/nm0385296\/", 
        "cacheUrl": "http:\/\/www.google.com\/search?q=cache:1i34KkqnsooJ:www.imdb.com", 
        "unescapedUrl": "http:\/\/www.imdb.com\/name\/nm0385296\/", 
        "content": "Socialite <b>Paris Hilton<\/b> was born on February 17, 1981 in New York City... Visit   IMDb for Photos, Filmography, Discussions, Bio, News, Awards, Agent, <b>...<\/b>"
       }, 
       {
        "GsearchResultClass": "GwebSearch", 
        "visibleUrl": "www.myspace.com", 
        "titleNoFormatting": "MySpace.com - Paris Hilton - 27 - Female - California - www ...", 
        "title": "MySpace.com - <b>Paris Hilton<\/b> - 27 - Female - California - www <b>...<\/b>", 
        "url": "http:\/\/www.myspace.com\/parishilton", 
        "cacheUrl": "http:\/\/www.google.com\/search?q=cache:DTzCq3_Z7C0J:www.myspace.com", 
        "unescapedUrl": "http:\/\/www.myspace.com\/parishilton", 
        "content": "<b>Paris Hilton&#39;s<\/b> Latest Blog Entry [Subscribe to this Blog] <b>....<\/b> Guess what <b>Paris<\/b>   <b>Hilton<\/b>? I&#39;ve read and bought that, Weekly In Touch Magazine, yesterday! <b>...<\/b>"
       }
      ]
     }, 
     "responseDetails": null, 
     "responseStatus": 200
    }</nowiki>

## Microsoft Live Search API 2.0

Reference <http://msdn.microsoft.com/en-us/library/dd250846.aspx>

    <nowiki>{
       "SearchResponse":{
          "Version":"2.0",
          "Query":{
             "SearchTerms":"testign"
          },
          "Spell":{
             "Total":1,
             "Results":[
                {
                   "Value":"testing"
                }
             ]
          },
          "Web":{
             "Total":5100,
             "Offset":0,
             "Results":[
                {
                   "Title":"Testign part 2 - Tiernan OTooles Programming Blog",
                   "Description":"If this works, it means nothing really, but i have managed to build a .TEXT blog posting app. could be handy if i move my main blog to .TEXT, which i am thinking about..",
                   "Url":"http:\/\/weblogs.asp.net\/tiernanotoole\/archive\/2004\/09\/24\/233830.aspx",
                   "DisplayUrl":"http:\/\/weblogs.asp.net\/tiernanotoole\/archive\/2004\/09\/24\/233830.aspx",
                   "DateTime":"2008-10-21T05:08:05Z",
                   "Rank":-1.835920
                }
             ]
          }
       }
    }</nowiki>

## Yahoo Web Search

Reference
<http://developer.yahoo.com/search/web/V1/webSearch.html>

Query:

` `<http://search.yahooapis.com/WebSearchService/V1/webSearch?appid=YahooDemo&query=madonna&results=2&output=json>

Response:

    <nowiki>{
     "ResultSet": {
      "Result": [
       {
        "MimeType": "text\/html", 
        "Cache": {
         "Url": "http:\/\/uk.wrs.yahoo.com\/_ylt=A0Je5VNQTSxJVhUAHg7dmMwF;_ylu=X3oDMTBwOHA5a2tvBGNvbG8DdwRwb3MDMQRzZWMDc3IEdnRpZAM-\/SIG=1602559ol\/EXP=1227726544\/**http%3A\/\/66.218.69.11\/search\/cache%3Fei=UTF-8%26appid=YahooDemo%26query=madonna%26results=2%26output=json%26u=www.madonna.com\/%26w=madonna%26d=A_opCkfiR2xZ%26icp=1%26.intl=us", 
         "Size": "141748"
        }, 
        "Title": "Madonna", 
        "Url": "http:\/\/www.madonna.com\/", 
        "ClickUrl": "http:\/\/uk.wrs.yahoo.com\/_ylt=A0Je5VNQTSxJVhUAHQ7dmMwF;_ylu=X3oDMTB2cXVjNTM5BGNvbG8DdwRsA1dTMQRwb3MDMQRzZWMDc3IEdnRpZAM-\/SIG=11blgi5po\/EXP=1227726544\/**http%3A\/\/www.madonna.com\/", 
        "DisplayUrl": "www.madonna.com\/", 
        "ModificationDate": 1227427200, 
        "Summary": "Official site of pop diva Madonna, with news, music, media, and fan club."
       }, 
       {
        "MimeType": "text\/html", 
        "Cache": {
         "Url": "http:\/\/uk.wrs.yahoo.com\/_ylt=A0Je5VNQTSxJVhUAIQ7dmMwF;_ylu=X3oDMTBwZG5hOWwzBGNvbG8DdwRwb3MDMgRzZWMDc3IEdnRpZAM-\/SIG=173hm0meq\/EXP=1227726544\/**http%3A\/\/66.218.69.11\/search\/cache%3Fei=UTF-8%26appid=YahooDemo%26query=madonna%26results=2%26output=json%26u=en.wikipedia.org\/wiki\/Madonna_%2528entertainer%2529%26w=madonna%26d=Hl5LlEfiR2ww%26icp=1%26.intl=us", 
         "Size": "332370"
        }, 
        "Title": "Madonna (Entertainer) - Wikipedia", 
        "Url": "http:\/\/en.wikipedia.org\/wiki\/Madonna_(entertainer)", 
        "ClickUrl": "http:\/\/uk.wrs.yahoo.com\/_ylt=A0Je5VNQTSxJVhUAIA7dmMwF;_ylu=X3oDMTB2ZjQ4dDExBGNvbG8DdwRsA1dTMQRwb3MDMgRzZWMDc3IEdnRpZAM-\/SIG=126n039ja\/EXP=1227726544\/**http%3A\/\/en.wikipedia.org\/wiki\/Madonna_(entertainer)", 
        "DisplayUrl": "en.wikipedia.org\/wiki\/Madonna_(entertainer)", 
        "ModificationDate": 1226995200, 
        "Summary": "Exhaustive bio and discography of Madonna's early life, career, \"Sex\" controversy, electronic club mix phase, and more."
       }
      ], 
      "totalResultsReturned": 2, 
      "totalResultsAvailable": 340000000, 
      "moreSearch": "\/WebSearchService\/V1\/webSearch?query=madonna&amp;appid=YahooDemo&amp;region=us", 
      "type": "web", 
      "firstResultPosition": 1
     }
    }</nowiki>

## eBay Shopping API Search

Reference
<http://developer.ebay.com/devzone/shopping/docs/howto/js_shopping/js_searchgs_nv_json/js_searchgs_nv_json.html>

Query:

` `<http://open.api.ebay.com/shopping?appid=MyAppID&version=517&siteid=0&callname=FindItems&QueryKeywords=ipod&responseencoding=JSON&callback=true>

Response:

    <nowiki>{
      "Ack": "Failure", 
      "Build": "e591_core_Bundled_7560815_R1", 
      "Errors": [
        {
          "ErrorClassification": "RequestError", 
          "ErrorCode": "1.20", 
          "LongMessage": "Application ID invalid.", 
          "SeverityCode": "Error", 
          "ShortMessage": "Application ID invalid."
        }
      ], 
      "Timestamp": "2008-11-25T19:44:28.387Z", 
      "Version": "591"
    }</nowiki>

*\[That looks like an error response. Was it supposed to be a list of
search results?\]*

## VoteReport API Search

Reference:
<http://highearthorbit.com/votereport-mapping-and-data-feeds/>

Query:

` `<http://votereport.us/reports.json?q=good&count=2>

Response:

    <nowiki>[
     {
      "report": {
       "display_text": "Talking about #votereport on android at #mobilecampnyc3 at 11:30. Just enjoyed good session with nathan from mobilecommons.", 
       "rating": null, 
       "name": "Nathan Freitas", 
       "zip": null, 
       "reporter": {
        "twitter_reporter": {
         "name": "Nathan Freitas", 
         "icon": "http:\/\/s3.amazonaws.com\/twitter_production\/profile_images\/61379092\/nfavatar_normal.jpg"
        }
       }, 
       "text": "Talking about #votereport on android at #mobilecampnyc3 at 11:30. Just enjoyed good session with nathan from mobilecommons.", 
       "created_at": "2008-11-15T16:19:07Z", 
       "audio_link": null, 
       "updated_at": "2008-11-15T16:19:16Z", 
       "display_html": "<div class=\"balloon\"><a href=\"http:\/\/twitter.com\/natdefreitas\"><img src=http:\/\/s3.amazonaws.com\/twitter_production\/profile_images\/61379092\/nfavatar_normal.jpg class=\"profile\" target=\"_new\"\/><\/a><img class=\"rating_icon\" style=\"clear:left;\" src=\"\/images\/rating_none.png\" \/><div class=\"balloon_body\"><span class=\"author\" id=\"screen_name\">Nathan Freitas<\/span>: <span class=\"entry-title\">Talking about #votereport on android at #mobilecampnyc3 at 11:30. Just enjoyed good session with nathan from mobilecommons.<\/span><br \/><br \/><div class='whenwhere'>reported <a href=\"http:\/\/twitter.com\/natdefreitas\/statuses\/1007133626\">10 days ago<\/a> <br \/>from Brooklyn, NY<br \/>via Twitter<\/div><\/div><\/div>", 
       "wait_time": null, 
       "source": "TWT", 
       "score": 0, 
       "location": {
        "location": {
         "administrative_area": "NY", 
         "geo_source_id": 1, 
         "thoroughfare": null, 
         "point": {
          "type": "Point", 
          "coordinates": [
           -73.971043, 
           40.675234
          ]
         }, 
         "created_at": "2008-10-30T02:43:27Z", 
         "locality": "Brooklyn", 
         "updated_at": "2008-10-30T02:43:27Z", 
         "filter_list": null, 
         "sub_administrative_area": null, 
         "postal_code": null, 
         "country_code": "US", 
         "address": "Brooklyn, NY, USA", 
         "id": 404
        }
       }, 
       "polling_place": null, 
       "id": 12605, 
       "icon": "http:\/\/s3.amazonaws.com\/twitter_production\/profile_images\/61379092\/nfavatar_normal.jpg"
      }
     }, 
     {
      "report": {
       "display_text": "Telephone report to 208-272-9024 #good", 
       "rating": 100, 
       "name": "Telephone User", 
       "zip": "84105", 
       "reporter": {
        "phone_reporter": {
         "name": "Telephone User", 
         "icon": "\/images\/phone_icon.jpg"
        }
       }, 
       "text": "Telephone report to 208-272-9024 #good", 
       "created_at": "2008-11-15T05:12:44Z", 
       "audio_link": "http:\/\/calls.votereport.us\/1226725807.587.gsm", 
       "updated_at": "2008-11-15T05:12:44Z", 
       "display_html": "<div class=\"balloon\"><br \/><img src=\"\/images\/phone_icon.jpg\" class=\"profile\" \/><img class=\"rating_icon\" style=\"clear:left;\" src=\"\/images\/rating_good.png\" \/><div class=\"balloon_body\"><span class=\"author\" id=\"screen_name\">Telephone User<\/span>: <span class=\"entry-title\">Telephone report to 208-272-9024 #good<\/span><br \/>0 minute wait time<br \/>Rating: 100<br \/><div class='whenwhere'>reported 10 days ago<br \/>from Salt Lake City, UT 84105<br \/>via Telephone<\/div><\/div><\/div>", 
       "wait_time": 0, 
       "source": "TEL", 
       "score": null, 
       "location": {
        "location": {
         "administrative_area": "UT", 
         "geo_source_id": 1, 
         "thoroughfare": null, 
         "point": {
          "type": "Point", 
          "coordinates": [
           -111.8628205, 
           40.7345053
          ]
         }, 
         "created_at": "2008-11-15T05:12:44Z", 
         "locality": "Salt Lake City", 
         "updated_at": "2008-11-15T05:12:44Z", 
         "filter_list": null, 
         "sub_administrative_area": null, 
         "postal_code": "84105", 
         "country_code": "US", 
         "address": "Salt Lake City, UT 84105, USA", 
         "id": 5986
        }
       }, 
       "polling_place": null, 
       "id": 12599, 
       "icon": "http:\/\/votereport.us\/images\/phone_icon.jpg"
      }
     }
    ]</nowiki>

## Twitter Search

Reference: <http://apiwiki.twitter.com/Search+API+Documentation>

Query:

` `<http://search.twitter.com/search.json?q=twitter&rpp=2>

Response:

    <nowiki>{
      "completed_in": 0.021294, 
      "max_id": 1083593812, 
      "next_page": "?page=2&max_id=1083593812&rpp=2&q=twitter", 
      "page": 1, 
      "query": "twitter", 
      "refresh_url": "?since_id=1083593812&q=twitter", 
      "results": [
        {
          "created_at": "Mon, 29 Dec 2008 07:31:23 +0000", 
          "from_user": "camerontoews", 
          "from_user_id": 2809592, 
          "id": 1083593812, 
          "iso_language_code": "en", 
          "profile_image_url": "http://s3.amazonaws.com/twitter_production/profile_images/68670172/camheadSM_normal.jpg", 
          "text": "Just got back from fry night at the barnes'. I hope nobody ever follows jeremy on twitter! Jeeeeez!", 
          "to_user_id": null
        }, 
        {
          "created_at": "Mon, 29 Dec 2008 07:31:15 +0000", 
          "from_user": "erillanos", 
          "from_user_id": 320492, 
          "id": 1083593677, 
          "iso_language_code": "en", 
          "profile_image_url": "http://s3.amazonaws.com/twitter_production/profile_images/66271606/DSCN0703_normal.JPG", 
          "text": "@kiffar dont go doing that now. i know i am super depressed right now to but thats to far. i just drink and sleep and twitter to distract me", 
          "to_user": "kiffar", 
          "to_user_id": 444259
        }
      ], 
      "results_per_page": 2, 
      "since_id": 0
    }</nowiki>

## The New York Times Article Search API

Reference:
<http://developer.nytimes.com/docs/article_search_api/>

Query:

` `<http://api.nytimes.com/svc/search/v1/article?query=(field>`:)keywords (facet:[value])(&params)&api-key=your-API-key`

Response:

    <nowiki>
    { "facets" : { "classifiers_facet" : [ { "count" : 83,
                "term" : "Top/News"
              },
              { "count" : 74,
                "term" : "Top/Classifieds/Automobiles/Topics/Wheel Spin"
              },
              { "count" : 69,
                "term" : "Top/News/Sports"
              },
              { "count" : 18,
                "term" : "Top/Features/Travel/Guides/Destinations/North America"
              },
              { "count" : 18,
                "term" : "Top/Features/Travel/Guides/Destinations/North America/United States"
              },
              { "count" : 15,
                "term" : "Top/Features/Travel/Guides/Destinations/Europe"
              },
              { "count" : 10,
                "term" : "Top/Classifieds/Automobiles"
              },
              { "count" : 10,
                "term" : "Top/News/Business"
              },
              { "count" : 6,
                "term" : "Top/Features/Magazine"
              },
              { "count" : 6,
                "term" : "Top/Features/Travel/Escapes"
              },
              { "count" : 6,
                "term" : "Top/Features/Travel/Guides/Destinations/Central and South America"
              },
              { "count" : 6,
                "term" : "Top/News/World/Europe"
              },
              { "count" : 5,
                "term" : "Top/Classifieds/Job Market/Job Categories/Fashion, Beauty and Fitness"
              },
              { "count" : 5,
                "term" : "Top/Classifieds/Job Market/Job Categories/Media, Entertainment and Publishing"
              },
              { "count" : 5,
                "term" : "Top/News/Obituaries"
              }
            ],
          "des_facet" : [ { "count" : 126,
                "term" : "AUTOMOBILE RACING"
              },
              { "count" : 22,
                "term" : "AUTOMOBILES"
              },
              { "count" : 15,
                "term" : "BIOGRAPHICAL INFORMATION"
              },
              { "count" : 8,
                "term" : "INDIANAPOLIS 500 (AUTO RACE)"
              },
              { "count" : 8,
                "term" : "PROFESSIONAL ATHLETICS"
              },
              { "count" : 5,
                "term" : "ACCIDENTS AND SAFETY"
              },
              { "count" : 4,
                "term" : "DEATHS (OBITUARIES)"
              },
              { "count" : 4,
                "term" : "FORMULA ONE GRAND PRIX (AUTO RACE)"
              },
              { "count" : 4,
                "term" : "MERGERS, ACQUISITIONS AND DIVESTITURES"
              },
              { "count" : 4,
                "term" : "TELEVISION"
              },
              { "count" : 4,
                "term" : "TRAVEL AND VACATIONS"
              },
              { "count" : 3,
                "term" : "APPAREL"
              },
              { "count" : 3,
                "term" : "FINANCES"
              },
              { "count" : 2,
                "term" : "ADVERTISING"
              },
              { "count" : 2,
                "term" : "ADVERTISING AND MARKETING"
              }
            ],
          "geo_facet" : [ { "count" : 5,
                "term" : "UNITED STATES"
              },
              { "count" : 4,
                "term" : "BRAZIL"
              },
              { "count" : 4,
                "term" : "EUROPE"
              },
              { "count" : 4,
                "term" : "NEW YORK CITY"
              },
              { "count" : 3,
                "term" : "MONACO"
              },
              { "count" : 2,
                "term" : "AMERICA"
              },
              { "count" : 2,
                "term" : "FRANCE"
              },
              { "count" : 2,
                "term" : "GREAT BRITAIN"
              },
              { "count" : 2,
                "term" : "INDIANAPOLIS (IND)"
              },
              { "count" : 2,
                "term" : "INDIANAPOLIS (INDIANA)"
              },
              { "count" : 2,
                "term" : "JAPAN"
              },
              { "count" : 2,
                "term" : "LONG ISLAND (NY)"
              },
              { "count" : 2,
                "term" : "SAHARA DESERT"
              },
              { "count" : 1,
                "term" : "AFRICA"
              },
              { "count" : 1,
                "term" : "ALABAMA"
              }
            ],
          "org_facet" : [ { "count" : 12,
                "term" : "FORMULA ONE"
              },
              { "count" : 5,
                "term" : "NATIONAL ASSN OF STOCK CAR AUTO RACING"
              },
              { "count" : 4,
                "term" : "FORD MOTOR CO"
              },
              { "count" : 4,
                "term" : "INDIANAPOLIS MOTOR SPEEDWAY"
              },
              { "count" : 2,
                "term" : "CHAMPIONSHIP AUTO RACING TEAMS"
              },
              { "count" : 2,
                "term" : "ESPN"
              },
              { "count" : 2,
                "term" : "HONDA MOTOR CO"
              },
              { "count" : 2,
                "term" : "JAGUAR CARS LTD"
              },
              { "count" : 2,
                "term" : "JAGUAR PLC"
              },
              { "count" : 2,
                "term" : "MASERATI SPA"
              },
              { "count" : 2,
                "term" : "MITSUBISHI MOTORS CORP"
              },
              { "count" : 2,
                "term" : "PHILIP MORRIS COMPANIES INC"
              },
              { "count" : 2,
                "term" : "PORSCHE AG"
              },
              { "count" : 1,
                "term" : "AL QAEDA"
              },
              { "count" : 1,
                "term" : "ALFA ROMEO OF ITALY"
              }
            ],
          "per_facet" : [ { "count" : 3,
                "term" : "ANDRETTI, MICHAEL"
              },
              { "count" : 3,
                "term" : "FITTIPALDI, EMERSON"
              },
              { "count" : 3,
                "term" : "MANSELL, NIGEL"
              },
              { "count" : 3,
                "term" : "SENNA, AYRTON"
              },
              { "count" : 2,
                "term" : "ANDRETTI, MARIO"
              },
              { "count" : 2,
                "term" : "FABI, TEO"
              },
              { "count" : 2,
                "term" : "FRANCE, BILL JR"
              },
              { "count" : 2,
                "term" : "LUYENDYK, ARIE"
              },
              { "count" : 2,
                "term" : "ZANARDI, ALEX"
              },
              { "count" : 1,
                "term" : "ALLEN, WOODY"
              },
              { "count" : 1,
                "term" : "BARBER, GEORGE"
              },
              { "count" : 1,
                "term" : "BOURDAIS, SEBASTIEN"
              },
              { "count" : 1,
                "term" : "BRACK, KENNY"
              },
              { "count" : 1,
                "term" : "CASTRONEVES, HELIO"
              },
              { "count" : 1,
                "term" : "CONNER, DENNIS"
              }
            ]
        },
      "offset" : "0",
      "results" : [ { "body" : "Phil Hill, one of the greatest of American auto racers, an introspective and cerebral champion whose celebrated driving career began when he took a neighbor's new Oldsmobile for a spin as a 9-year-old, died Thursday in Monterey, Calif. He was 81 and lived in Santa Monica, Calif., in the same house in which he grew up. His death was confirmed by his",
            "byline" : "By BRUCE WEBER",
            "classifiers_facet" : [ "Top/News/Sports",
                "Top/News/Obituaries",
                "Top/Classifieds/Automobiles/Topics/Wheel Spin"
              ],
            "date" : "20080829",
            "day_of_week_facet" : "Friday",
            "des_facet" : [ "AUTOMOBILE RACING",
                "DEATHS (OBITUARIES)"
              ],
            "desk_facet" : "Sports Desk",
            "fee" : "N",
            "large_image" : "Y",
            "large_image_height" : "450",
            "large_image_url" : "",
            "large_image_width" : "363",
            "lead_paragraph" : "",
            "material_type_facet" : [ "Obituary",
                "Biography"
              ],
            "nytd_des_facet" : [ "Automobile Racing",
                "Deaths (Obituaries)"
              ],
            "nytd_lead_paragraph" : "Mr. Hill was one of the greatest of American auto racers, an introspective and cerebral champion who led a celebrated driving career.",
            "nytd_org_facet" : [ "Formula One" ],
            "nytd_per_facet" : [ "Hill, Phil" ],
            "nytd_section_facet" : [ "Obituaries",
                "Sports"
              ],
            "nytd_title" : "Phil Hill, a Racing Legend at Odds With the Sport at Times, Is Dead at 81",
            "org_facet" : [ "FORMULA ONE" ],
            "page_facet" : "8",
            "per_facet" : [ "HILL, PHIL" ],
            "publication_day" : "29",
            "publication_month" : "08",
            "publication_year" : "2008",
            "small_image" : "Y",
            "small_image_height" : "75",
            "small_image_url" : "http://graphics8.nytimes.com/images/2008/08/29/sports/hill_75757.jpg",
            "source_facet" : "The New York Times",
            "title" : "Phil Hill, a Racing Legend at Odds With the Sport at Times, Is Dead at 81",
            "url" : "http://www.nytimes.com/2008/08/29/sports/othersports/29hill.html",
            "word_count" : "1159"
          },
          { "author" : "Cathy Horyn is the fashion critic for The New York Times",
            "body" : "ISTANBUL PARK is not really a park but a three-mile-long race-car track situated in a forlorn area of scrubland and solitary, flag-draped Shell gas stations about 40 miles east of Istanbul, off the main highway to Ankara. A development of pink-stucco villas was encroaching on some old farms. It was a Friday morning in early May, two days before the",
            "byline" : "By CATHY HORYN",
            "classifiers_facet" : [ "Top/News/World/Countries and Territories/Turkey",
                "Top/Features/Travel/Guides/Destinations/Europe/Turkey/Istanbul",
                "Top/Features/Magazine",
                "Top/News",
                "Top/Features/Travel/Guides/Destinations/Europe",
                "Top/Features/Travel/Guides/Destinations/Europe/Turkey",
                "Top/News/World/Middle East"
              ],
            "date" : "20080727",
            "day_of_week_facet" : "Sunday",
            "des_facet" : [ "AUTOMOBILES",
                "AUTOMOBILE RACING"
              ],
            "desk_facet" : "Magazine Desk",
            "fee" : "N",
            "geo_facet" : [ "ISTANBUL (TURKEY)" ],
            "large_image" : "Y",
            "large_image_height" : "396",
            "large_image_url" : "",
            "large_image_width" : "600",
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "nytd_des_facet" : [ "Automobiles",
                "Automobile Racing"
              ],
            "nytd_geo_facet" : [ "Istanbul (Turkey)" ],
            "nytd_lead_paragraph" : "He’s the next big thing in Formula One auto racing. But can he hang on to his innocence in the revved-up whirl of Grand Prix?",
            "nytd_org_facet" : [ "Formula One",
                "Bayerische Motorenwerke AG",
                "Renault SA",
                "Daimler AG"
              ],
            "nytd_per_facet" : [ "Hamilton, Lewis" ],
            "nytd_section_facet" : [ "Magazine" ],
            "nytd_title" : "Lewis Hamilton Just Wants to Go Fast",
            "org_facet" : [ "FORMULA ONE",
                "BAYERISCHE MOTORENWERKE AG",
                "RENAULT SA",
                "DAIMLER AG"
              ],
            "page_facet" : "30",
            "per_facet" : [ "HAMILTON, LEWIS" ],
            "publication_day" : "27",
            "publication_month" : "07",
            "publication_year" : "2008",
            "small_image" : "Y",
            "small_image_height" : "75",
            "small_image_url" : "http://graphics8.nytimes.com/images/2008/07/27/magazine/27hamilton-75.jpg",
            "source_facet" : "The New York Times",
            "title" : "HE'S THE NEXT BIG THING IN FORMULA ONE AUTO RACING. BUT CAN HE HANG ON TO HIS INNOCENCE IN THE REVVED-UP WHIRL OF GRAND PRIX?",
            "url" : "http://www.nytimes.com/2008/07/27/magazine/27Hamilton-t.html",
            "word_count" : "5228"
          },
          { "abstract" : "Danica Patrick becomes first woman to win Indy car race; defeats two-time Indy 500 winner Helio Castroneves by nearly six seconds in Indy Japan 300; achieved celebrity three years ago when she became first woman to lead Indianapolis 500; finished fourth in that race but became phenomenon; companies embraced her willingness to market her good looks, but celebrity brought question of when or if she could win; naysayers chorus had grown increasingly loud as her winless streak wore on; in 2007, she switched to team co-owned by Michael Andretti, former racer who is son of Mario Andretti; photos (M)",
            "body" : "When a 23-year-old rookie named Danica Patrick became the first woman to lead the Indianapolis 500 three years ago, she raised the tantalizing possibility that in a male-dominated American sport, a woman might for the first time stand in victory lane. Patrick eventually finished fourth in that race, but she quickly became a phenomenon. Companies",
            "byline" : "By DAVE CALDWELL",
            "classifiers_facet" : [ "Top/News",
                "Top/News/Sports",
                "Top/Classifieds/Job Market/Job Categories/Marketing, Advertising and PR",
                "Top/News/Front Page",
                "Top/Classifieds/Automobiles/Topics/Wheel Spin"
              ],
            "date" : "20080421",
            "day_of_week_facet" : "Monday",
            "des_facet" : [ "INDY JAPAN 300",
                "INDIANAPOLIS 500 (AUTO RACE)",
                "AUTOMOBILE RACING",
                "RECORDS AND ACHIEVEMENTS",
                "ADVERTISING AND MARKETING",
                "WOMEN"
              ],
            "desk_facet" : "Sports Desk",
            "fee" : "N",
            "large_image" : "Y",
            "large_image_height" : "450",
            "large_image_url" : "",
            "large_image_width" : "622",
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "nytd_des_facet" : [ "Automobile Racing" ],
            "nytd_lead_paragraph" : "Danica Patrick became the first woman to win an Indy car race, using successful fuel strategy to capture an IndyCar Series event in Motegi, Japan.",
            "nytd_per_facet" : [ "Patrick, Danica" ],
            "nytd_section_facet" : [ "Front Page",
                "Sports"
              ],
            "nytd_title" : "Racing to Victory, and Leaving the Men and the Doubters Behind",
            "page_facet" : "1",
            "per_facet" : [ "ANDRETTI, MARIO",
                "ANDRETTI, MICHAEL",
                "CASTRONEVES, HELIO",
                "PATRICK, DANICA"
              ],
            "publication_day" : "21",
            "publication_month" : "04",
            "publication_year" : "2008",
            "small_image" : "Y",
            "small_image_height" : "75",
            "small_image_url" : "http://graphics8.nytimes.com/images/2008/04/20/sports/20patrick_75.jpg",
            "source_facet" : "The New York Times",
            "title" : "Racing to Victory, and Leaving the Men and the Doubters Behind",
            "url" : "http://www.nytimes.com/2008/04/21/sports/othersports/21patrick.html",
            "word_count" : "1086"
          },
          { "body" : "Few scandals in recent years have provoked as much anger and dismay across Europe as the saga of Max Mosley, the overseer of grand prix motor racing who made tabloid news last weekend in a front-page exposé and accompanying Web video showing him in a sadomasochistic orgy with five supposed prostitutes in a London sex ''dungeon.'' But beyond the",
            "byline" : "By JOHN F. BURNS",
            "classifiers_facet" : [ "Top/News",
                "Top/News/World"
              ],
            "date" : "20080407",
            "day_of_week_facet" : "Monday",
            "des_facet" : [ "NAZI POLICIES TOWARD JEWS AND MINORITIES",
                "AUTOMOBILE RACING",
                "RECORDINGS AND DOWNLOADS (VIDEO)",
                "PROSTITUTION",
                "SEX"
              ],
            "desk_facet" : "Foreign Desk",
            "fee" : "N",
            "large_image" : "Y",
            "large_image_height" : "450",
            "large_image_url" : "",
            "large_image_width" : "650",
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "nytd_des_facet" : [ "Nazi Policies Toward Jews and Minorities",
                "Automobile Racing",
                "Recordings and Downloads (Video)",
                "Prostitution",
                "Sex"
              ],
            "nytd_lead_paragraph" : "A London tabloid’s claim that Max Mosley was involved in a sex orgy with Nazi undertones has prompted calls for his resignation. He has refused and is suing the tabloid.",
            "nytd_org_facet" : [ "Formula One",
                "Sunday Times",
                "Times of London"
              ],
            "nytd_section_facet" : [ "World" ],
            "nytd_title" : "Possible Nazi Theme of Grand Prix Boss’s Orgy Draws Calls to Quit",
            "org_facet" : [ "FORMULA ONE",
                "SUNDAY TIMES",
                "TIMES OF LONDON"
              ],
            "page_facet" : "6",
            "publication_day" : "07",
            "publication_month" : "04",
            "publication_year" : "2008",
            "small_image" : "Y",
            "small_image_height" : "75",
            "small_image_url" : "http://graphics8.nytimes.com/images/2008/04/07/world/07formula.75.jpg",
            "source_facet" : "The New York Times",
            "title" : "Possible Nazi Theme of Grand Prix Boss's Orgy Draws Calls to Quit",
            "url" : "http://www.nytimes.com/2008/04/07/world/europe/07formula.html",
            "word_count" : "1628"
          },
          { "body" : "HOWARD KROPLICK's fascination for local history has led him into lots of musty library archives, looking for the Long Island that predated suburbia. ''I was especially interested in areas where I lived,'' said Mr. Kroplick, 58, who grew up in East Meadow and now lives with his wife and two daughters in East Hills. ''I loved looking at the pictures",
            "byline" : "By KARIN LIPSON",
            "classifiers_facet" : [ "Top/News/New York and Region",
                "Top/Features/Travel/Guides/Destinations/North America/United States/New York/Long Island",
                "Top/News/U.S./U.S. States, Territories and Possessions/New York",
                "Top/Features/Travel/Guides/Destinations/North America",
                "Top/News/New York and Region/Long Island",
                "Top/Features/Travel/Guides/Destinations/North America/United States/New York",
                "Top/Features/Travel/Guides/Destinations/North America/United States"
              ],
            "date" : "20080316",
            "day_of_week_facet" : "Sunday",
            "des_facet" : [ "AUTOMOBILES",
                "AUTOMOBILE RACING"
              ],
            "desk_facet" : "Long Island Weekly Desk",
            "fee" : "N",
            "geo_facet" : [ "LONG ISLAND (NY)" ],
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "nytd_des_facet" : [ "Automobiles",
                "Automobile Racing"
              ],
            "nytd_geo_facet" : [ "Long Island (NY)" ],
            "nytd_lead_paragraph" : "The Vanderbilt Cup Races, automobile rallies held on Long Island from 1904 to 1910, were celebrated sporting events of their day.",
            "nytd_section_facet" : [ "New York and Region" ],
            "nytd_title" : "Long Before Nascar, Dirt-Road Daredevils",
            "page_facet" : "9",
            "publication_day" : "16",
            "publication_month" : "03",
            "publication_year" : "2008",
            "source_facet" : "The New York Times",
            "title" : "Long Before Nascar, Dirt-Road Daredevils",
            "url" : "http://www.nytimes.com/2008/03/16/nyregion/nyregionspecial2/16bookli.html",
            "word_count" : "588"
          },
          { "body" : "THE telephone call that would change George Schuster's life and, perhaps, the course of the automobile industry didn't give him much time to prepare. He had barely 12 hours to catch an overnight train from New England so he would be in New York City the next morning, Feb. 12, 1908, for the start of the longest auto race in history: around the",
            "byline" : "By JERRY GARRETT",
            "classifiers_facet" : [ "Top/Classifieds/Automobiles" ],
            "date" : "20080210",
            "day_of_week_facet" : "Sunday",
            "des_facet" : [ "AUTOMOBILES",
                "AUTOMOBILE RACING"
              ],
            "desk_facet" : "Automobiles",
            "fee" : "N",
            "large_image" : "Y",
            "large_image_height" : "432",
            "large_image_url" : "",
            "large_image_width" : "600",
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "medium_image" : "Y",
            "medium_image_height" : "240",
            "medium_image_url" : "",
            "medium_image_width" : "337",
            "multimedia" : [ { "headline" : "No Shoulder Next 22,000 Miles",
                  "summary" : "The 1908 New York to Paris race was one of the earliest international automobile races. The interactive map shows the route taken by the American team as well as the planned route for a commemorative race set to begin in May.",
                  "type" : "Other",
                  "url" : "http://www.nytimes.com/interactive/2008/02/10/automobiles/20080210_GREATRACE_MAP.html"
                },
                { "headline" : "Great Race of 1908: Competitors",
                  "height" : "700",
                  "summary" : "Six cars competed in the first around-the-world race from New York to Paris. Only three made it all the way.",
                  "type" : "Slideshow",
                  "url" : "http://www.nytimes.com/slideshow/2008/02/10/automobiles/0210-RACE-CARS_index.html",
                  "width" : "750"
                }
              ],
            "nytd_des_facet" : [ "Automobiles",
                "Automobile Racing"
              ],
            "nytd_lead_paragraph" : "Competitors in the first around-the-world race traveled by land and by sea, crossing continents with few good roads and making repairs on the fly.",
            "nytd_section_facet" : [ "Automobiles" ],
            "nytd_title" : "New York to Paris the Hard Way, 100 Years Ago",
            "page_facet" : "1",
            "publication_day" : "10",
            "publication_month" : "02",
            "publication_year" : "2008",
            "related_multimedia" : "Y",
            "small_image" : "Y",
            "small_image_height" : "75",
            "small_image_url" : "http://graphics8.nytimes.com/images/2008/02/10/automobiles/75-race-01.jpg",
            "source_facet" : "The New York Times",
            "title" : "New York to Paris the Hard Way, 100 Years Ago",
            "url" : "http://www.nytimes.com/2008/02/10/automobiles/10RACE.html",
            "word_count" : "1485"
          },
          { "abstract" : "Dakar Rally is canceled because of terrorist threats (S)",
            "body" : "The Dakar Rally, the motorcycle, car and truck race across the Sahara, was canceled Friday by organizers citing ''direct'' threats of terrorism from a militant group linked to Al Qaeda. The 16-day, 5,760-mile race, called off for the first time in its 30-year history, was to start Saturday in Lisbon, with about 550 competitors. The race route winds",
            "classifiers_facet" : [ "Top/News/Sports",
                "Top/Features/Travel/Guides/Destinations/Africa/Senegal/Dakar",
                "Top/News/World/Countries and Territories/Senegal",
                "Top/Classifieds/Automobiles/Topics/Wheel Spin",
                "Top/News/World/Africa",
                "Top/News",
                "Top/Features/Travel/Guides/Destinations/Africa/Senegal",
                "Top/Features/Travel/Guides/Destinations/Africa"
              ],
            "date" : "20080105",
            "day_of_week_facet" : "Saturday",
            "des_facet" : [ "AUTOMOBILE RACING",
                "TERRORISM",
                "DAKAR RALLY"
              ],
            "desk_facet" : "Sports Desk",
            "fee" : "N",
            "geo_facet" : [ "DAKAR (SENEGAL)",
                "SAHARA DESERT"
              ],
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "nytd_des_facet" : [ "Terrorism",
                "Dakar Rally"
              ],
            "nytd_geo_facet" : [ "Dakar (Senegal)",
                "Sahara Desert"
              ],
            "nytd_lead_paragraph" : "The Dakar Rally, the motorcycle, car and truck race across the Sahara, was canceled Friday by organizers citing “direct” threats of terrorism from a militant group linked to Al Qaeda.",
            "nytd_org_facet" : [ "Al Qaeda" ],
            "nytd_section_facet" : [ "Sports" ],
            "nytd_title" : "Rally Canceled After Terror Threats",
            "org_facet" : [ "AL QAEDA" ],
            "page_facet" : "6",
            "publication_day" : "05",
            "publication_month" : "01",
            "publication_year" : "2008",
            "source_facet" : "The New York Times",
            "title" : "Rally Canceled After Terror Threats",
            "url" : "http://www.nytimes.com/2008/01/05/sports/othersports/05autos.html",
            "word_count" : "196"
          },
          { "abstract" : "Alexander Roy's new book The Driver: My Dangerous Pursuit of Speed and Truth in the Outlaw Racing World describes life as illegal endurance-driver; Roy drove from New York to Los Angeles (Calif) in 31 hours in 2006, largely by evading police and avoiding speed traps; photos (M)",
            "body" : "The message came across the police scanner in October 2006 as Alexander Roy was driving his 2000 BMW M5 west on Interstate 44 in Oklahoma: ''I have a report of a blue BMW speeding, weaving in and out of traffic and driving recklessly. Be advised.'' Roy said he heard it shortly after he and his co-driver, David Maher, had been exceeding 150 miles an",
            "byline" : "By DAVID SHAFTEL; Happy Blitt contributed reporting.",
            "classifiers_facet" : [ "Top/Features/Books",
                "Top/News/Sports",
                "Top/Features/Travel/Guides/Destinations/North America/United States/California",
                "Top/News/U.S./Mid-Atlantic",
                "Top/Classifieds/Automobiles/Topics/Wheel Spin",
                "Top/Classifieds/Job Market/Job Categories/Media, Entertainment and Publishing",
                "Top/News/U.S./West",
                "Top/Features/Travel/Guides/Destinations/North America/United States/California/Los Angeles",
                "Top/News/U.S./U.S. States, Territories and Possessions/New York",
                "Top/News",
                "Top/News/U.S./U.S. States, Territories and Possessions/California",
                "Top/Features/Travel/Guides/Destinations/North America",
                "Top/Features/Travel/Guides/Destinations/North America/United States/New York/New York City",
                "Top/Features/Travel/Guides/Destinations/North America/United States"
              ],
            "date" : "20071017",
            "day_of_week_facet" : "Wednesday",
            "des_facet" : [ "SPEED LIMITS AND SPEEDING",
                "AUTOMOBILES",
                "BOOKS AND LITERATURE",
                "ROADS AND TRAFFIC",
                "AUTOMOBILE RACING"
              ],
            "desk_facet" : "Sports Desk",
            "fee" : "N",
            "geo_facet" : [ "LOS ANGELES (CALIF)",
                "NEW YORK CITY"
              ],
            "large_image" : "Y",
            "large_image_height" : "352",
            "large_image_url" : "",
            "large_image_width" : "600",
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "medium_image" : "Y",
            "medium_image_height" : "240",
            "medium_image_url" : "",
            "medium_image_width" : "337",
            "nytd_des_facet" : [ "Automobiles",
                "Roads and Traffic"
              ],
            "nytd_lead_paragraph" : "Alexander Roy’s memoir, released on Tuesday, describes a subculture of illegal endurance racing and efforts to break transcontinental records set in the 1970s and 80s.",
            "nytd_org_facet" : [ "HarperCollins Publishers" ],
            "nytd_section_facet" : [ "Books",
                "Sports"
              ],
            "nytd_title" : "Tale of Outlaw Racing, With the U.S. as a Course",
            "org_facet" : [ "HARPERCOLLINS PUBLISHERS" ],
            "page_facet" : "1",
            "per_facet" : [ "ROY, ALEXANDER" ],
            "publication_day" : "17",
            "publication_month" : "10",
            "publication_year" : "2007",
            "small_image" : "Y",
            "small_image_height" : "75",
            "small_image_url" : "http://graphics8.nytimes.com/images/2007/10/17/sports/17speed.1.75.jpg",
            "source_facet" : "The New York Times",
            "title" : "Tale of Outlaw Racing, With the U.S. as a Course",
            "url" : "http://www.nytimes.com/2007/10/17/sports/othersports/17speed.html",
            "word_count" : "1234",
            "works_mentioned_facet" : [ "DRIVER, THE: MY DANGEROUS PURSUIT OF SPEED AND TRUTH (BOOK)" ]
          },
          { "abstract" : "Hans Ruesch, successful Swiss racecar driver in days of European Grand Prix racing and well-received adventure novelist, dies at age 94 (M)",
            "body" : "Hans Ruesch, a successful Swiss racecar driver in the years before World War II who later became a writer of well-received novels of adventure, two of which became Hollywood films, died on Monday at his home in Lugano, Switzerland. He was 94. The cause was cancer, his daughter, Vivian Ruesch Mellon, said. Mr. Ruesch was believed to have been one of",
            "byline" : "By MARGALIT FOX",
            "classifiers_facet" : [ "Top/Features/Books",
                "Top/News/Sports",
                "Top/News/Obituaries",
                "Top/Classifieds/Automobiles/Topics/Wheel Spin"
              ],
            "date" : "20070903",
            "day_of_week_facet" : "Monday",
            "des_facet" : [ "DEATHS (OBITUARIES)",
                "BOOKS AND LITERATURE",
                "AUTOMOBILE RACING",
                "BIOGRAPHICAL INFORMATION"
              ],
            "desk_facet" : "Sports Desk",
            "fee" : "N",
            "lead_paragraph" : "",
            "material_type_facet" : [ "Obituary" ],
            "nytd_des_facet" : [ "Books and Literature",
                "Deaths (Obituaries)",
                "Automobile Racing"
              ],
            "nytd_lead_paragraph" : "Mr. Ruesch was a successful Swiss racecar driver in the years before World War II who later became a writer of well-received novels of adventure, two of which became Hollywood films.",
            "nytd_section_facet" : [ "Obituaries",
                "Books",
                "Sports"
              ],
            "nytd_title" : "Hans Ruesch, Writer and Grand Prix Winner, Dies at 94",
            "page_facet" : "5",
            "per_facet" : [ "RUESCH, HANS" ],
            "publication_day" : "03",
            "publication_month" : "09",
            "publication_year" : "2007",
            "source_facet" : "The New York Times",
            "title" : "Hans Ruesch, 94, Writer And Grand Prix Winner",
            "url" : "http://www.nytimes.com/2007/09/03/sports/03ruesch.html",
            "word_count" : "432"
          },
          { "abstract" : "Jimmie Johnson wins Sharp Aquos 500 (S)",
            "body" : "Jimmie Johnson grabbed a victory last night at California Speedway, clinching a spot in Nascar's Chase for the Nextel Cup championship and guaranteeing he will be no worse than tied for the top seed in the 10-race playoff. Johnson dominated the second half of the Sharp Aquos 500, a race that began in bright sunshine with temperatures of more than",
            "byline" : "By THE ASSOCIATED PRESS",
            "classifiers_facet" : [ "Top/News",
                "Top/News/Sports",
                "Top/Classifieds/Automobiles/Topics/Wheel Spin"
              ],
            "column_facet" : "AUTO RACING ROUNDUP",
            "date" : "20070903",
            "day_of_week_facet" : "Monday",
            "des_facet" : [ "AUTOMOBILE RACING",
                "SHARP AQUOS 500"
              ],
            "desk_facet" : "Sports Desk",
            "fee" : "N",
            "lead_paragraph" : "",
            "material_type_facet" : [ "News" ],
            "nytd_des_facet" : [ "Automobile Racing" ],
            "nytd_lead_paragraph" : "The driver won a shortened race in Detroit on Sunday, his series-best fifth victory this season and the 12th of his career.",
            "nytd_section_facet" : [ "Sports" ],
            "nytd_title" : "Johnson Cruises in California for Fifth Win of Season",
            "page_facet" : "4",
            "per_facet" : [ "JOHNSON, JIMMIE" ],
            "publication_day" : "03",
            "publication_month" : "09",
            "publication_year" : "2007",
            "source_facet" : "The New York Times",
            "title" : "AUTO RACING ROUNDUP; Johnson Cruises in California for Fifth Win of Season",
            "url" : "http://www.nytimes.com/2007/09/03/sports/othersports/03autos.html",
            "word_count" : "721"
          }
        ],
      "tokens" : [ "des_facet:[AUTOMOBILE RACING]",
          "europe"
        ],
      "total" : 126
    }
    </nowiki>

## Tony Hammond draft at CrossTech

Reference
<http://www.crossref.org/CrossTech/2009/07/opensearch_formats_for_review.html>
and <http://nurture.nature.com/opensearch/solar2-json.txt>

Response:

    <nowiki>{
    
        "feed": {
            "title": "cql.keywords adj \"solar eclipse\"",
            "link": [
                {
                    "rel": "self",
                    "href": "...?version=1.1&operation=searchRetrieve&query=cql.keywords%20adj%20%22solar%20eclipse%22&httpAccept=application/json&maximumRecords=2&startIndex=12"
                },
                {
                    "rel": "first",
                    "href": "...?version=1.1&operation=searchRetrieve&query=cql.keywords%20adj%20%22solar%20eclipse%22&httpAccept=application/json&maximumRecords=2&startIndex=1"
                },
                {
                    "rel": "previous",
                    "href": "...?version=1.1&operation=searchRetrieve&query=cql.keywords%20adj%20%22solar%20eclipse%22&httpAccept=application/json&maximumRecords=2&startIndex=11"
                },
                {
                    "rel": "next",
                    "href": "...?version=1.1&operation=searchRetrieve&query=cql.keywords%20adj%20%22solar%20eclipse%22&httpAccept=application/json&maximumRecords=2&startIndex=13"
                },
                
                {
                    "rel": "last",
                    "href": "...?version=1.1&operation=searchRetrieve&query=cql.keywords%20adj%20%22solar%20eclipse%22&httpAccept=application/json&maximumRecords=2&startIndex=1509"
                }
            ],
            "id": "urn:uuid:a6852153-dc12-4cd9-b3e0-f9ff2ed7f0b3",
            "author": {
                "name": "Nature Publishing Group",
                "uri": "http://www.nature.com",
                "email": "interfaces@nature.com"
            },
            "updated": "2009-07-23T11:38:08+00:00",
            "rights": "© 2009 Nature Publication Group",
            "icon": "http:...",
            "opensearch:totalResults": 1509,
            "opensearch:startIndex": 12,
            "opensearch:itemsPerPage": 2,
            "opensearch:Query": {
                "opensearch:role": "request",
                "opensearch:searchTerms": "cql.keywords adj \"solar eclipse\""
            },
            "sru:numberOfRecords": 1509,
            "sru:resultSetId": "a6852153-dc12-4cd9-b3e0-f9ff2ed7f0b3",
            "dc:publisher": "Nature Publishing Group",
            "dc:language": "en",
            "dc:rights": "© 2009 Nature Publication Group",
            "prism:copyright": "© 2009 Nature Publication Group",
            "prism:rightsAgent": "permissions@nature.com",
            "entry": [
                {
                    "title": "Chronometry: Effect of the 1999 solar eclipse on atomic clocks",
                    "link": "http://dx.doi.org/10.1038/45442",
                    "id": "doi:10.1038/45442",
                    "updated": "2009-07-23T11:38:08+00:00",
                    "sru:recordSchema": "info:srw/schema/11/pam-v2.1",
                    "sru:recordPacking": "xml",
                    "sru:recordData": {
                        "pam:message": {
                            "pam:article": {
                                "xhtml:head": {
                                    "dc:identifier": "doi:10.1038/45442",
                                    "dc:title": "Chronometry: Effect of the 1999 solar eclipse on atomic clocks",
                                    "dc:creator": [
                                        "Thomas Udem",
                                        "Jörg Reichert",
                                        "Ronald Holzwarth",
                                        "Theodor Hänsch",
                                        "Rainer Krämer",
                                        "Jörg Hahn",
                                        "Jens Hammesfahr"
                                    ],
                                    "prism:publicationName": "Nature",
                                    "prism:issn": "0028-0836",
                                    "prism:eIssn": null,
                                    "prism:doi": "10.1038/45442",
                                    "dc:publisher": null,
                                    "prism:publicationDate": "1999-12-16",
                                    "prism:volume": "402",
                                    "prism:number": "6763",
                                    "prism:startingPage": "749",
                                    "prism:url": "http://dx.doi.org/10.1038/45442",
                                    "prism:copyright": null,
                                    "prism:alternateTitle": "nature"
                                }
                            }
                        }
                    },
                    "sru:recordPosition": 12
                },
                {
                    "title": "The earliest known solar eclipse record redated",
                    "link": "http://dx.doi.org/10.1038/338238a0",
                    "id": "doi:10.1038/338238a0",
                    "updated": "2009-07-23T11:38:08+00:00",
                    "sru:recordSchema": "info:srw/schema/11/pam-v2.1",
                    "sru:recordPacking": "xml",
                    "sru:recordData": {
                        "pam:message": {
                            "pam:article": {
                                "xhtml:head": {
                                    "dc:identifier": "doi:10.1038/338238a0",
                                    "dc:title": "The earliest known solar eclipse record redated",
                                    "dc:creator": [
                                        "T. de Jong",
                                        "W. H. van Soldt"
                                    ],
                                    "prism:publicationName": "Nature",
                                    "prism:issn": "0028-0836",
                                    "prism:eIssn": null,
                                    "prism:doi": "10.1038/338238a0",
                                    "dc:publisher": null,
                                    "prism:publicationDate": "1989-03-16",
                                    "prism:volume": "338",
                                    "prism:number": "6212",
                                    "prism:startingPage": "238",
                                    "prism:url": "http://dx.doi.org/10.1038/338238a0",
                                    "prism:copyright": null,
                                    "prism:alternateTitle": "nature"
                                }
                            }
                        }
                    },
                    "sru:recordPosition": 13
                }
            ]
        }
    }</nowiki>
