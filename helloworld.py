"""A simple webapp2 server."""

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!\n')
        # Random message, used to sanity check the app was updated.
        self.response.write('logical-waters-676 deployment again.')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
