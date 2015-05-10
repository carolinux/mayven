import requests
import sys
import json

MAX_RESULTS = 5 
URL = "http://search.maven.org/solrsearch/select?q={}&rows={}&wt=json"


def process(maven_thing):
    gid = maven_thing['g']
    artifact = maven_thing['a']
    version = maven_thing['latestVersion']
    return gid, artifact , version


class SbtTransformer(object):

    @staticmethod
    def transform(g,a,v):
        return '"{}" % "{}" % "{}"'.format(g,a,v)

if __name__ == '__main__':
   search = sys.argv[1]
   fmt = "sbt"
   maxr = MAX_RESULTS
   res = json.loads(requests.get(URL.format(search, maxr)).content)
   sources = res["response"]["docs"]
   gav = map(process, sources)
   for g,a,v in gav:
       print SbtTransformer.transform(g,a,v)
