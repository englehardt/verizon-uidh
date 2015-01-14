from publicsuffix import PublicSuffixList
from urlparse import urlparse
import sqlite3

turn_cookies = [u'%2861545288920755498%', u'%8861973013353481274%', u'%4049160904546000383%', u'%8432793100254789139%', u'%2645485736339061857%', u'%3071864441180715499%', u'%3451938460152193492%', u'%4450345702584606554%', u'%2892601177349552337%', u'%8539579497380496210%', u'%2803939613498528605%', u'%8523136024635649394%']

psl = PublicSuffixList()

con = sqlite3.connect('verizon_1.sqlite')
cur = con.cursor()

#### IN URL

urls = set()
cur.execute(("SELECT url FROM http_requests WHERE "
            "{seq}".format(seq=" OR ".join(["url LIKE ?"]*len(turn_cookies)))),
            turn_cookies)
for url, in cur.fetchall():
    urls.add(psl.get_public_suffix(urlparse(url).hostname))

print "ID in URL:"
temp = list(urls)
temp.sort()
for item in temp: print item

#### IN REFERRER

urls = set()
cur.execute(("SELECT url FROM http_requests WHERE "
            "{seq}".format(seq=" OR ".join(["referrer LIKE ?"]*len(turn_cookies)))),
            turn_cookies)
for url, in cur.fetchall():
    urls.add(psl.get_public_suffix(urlparse(url).hostname))

print "\n\nID in referrer:"
temp = list(urls)
temp.sort()
for item in temp: print item

#### IN SET-COOKIE

urls = set()
#cur.execute(("SELECT r.url FROM http_responses r, http_cookies c WHERE "
#             "c.http_type = 'response' AND c.header_id = r.id AND "
#             "{seq}".format(seq=" OR ".join(["c.value LIKE ?"]*len(turn_cookies)))),
#            turn_cookies)
cur.execute(("SELECT url FROM http_responses WHERE id IN "
             "(SELECT header_id FROM http_cookies WHERE "
             "http_type = 'response' AND "
             "({seq}))".format(seq=" OR ".join(["value LIKE ?"]*len(turn_cookies)))),
            turn_cookies)

for url, in cur.fetchall():
    urls.add(psl.get_public_suffix(urlparse(url).hostname))

print "\n\nID in Set-Cookie:"
temp = list(urls)
temp.sort()
for item in temp: print item

con.close()
