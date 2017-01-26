#
import webapp2
import caesar
import helpers




class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hellooooo world!"
        encrypted_message = caesar.encrypt(message, 13)
        
        textarea = "<textarea>" + encrypted_message + "</textarea>"
        submit = "<input type='submit'/>"
        form = "<form>" + textarea + "</form>" + "<br>" + submit
        
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
