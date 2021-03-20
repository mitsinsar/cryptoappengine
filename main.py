import webapp2
import urllib3
class UpdateCachedData(webapp2.RequestHandler):
    def get(self):
        # request = urllib2.Request('<GCF URL>', headers={"cronrequest" : "true"})
        # contents = urllib2.urlopen(request).read()
        print("working every 30 secs")
app = webapp2.WSGIApplication([
    ('/update', UpdateCachedData),
    ], debug=True)
