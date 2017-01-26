#
import webapp2
import cgi
import caesar
import helpers

def write_content(rotare, encrypted_message): #creates the html for the home page
    
    header = "Enter some text to ROT-N"
    submit = "<input type='submit'/>"
    textlabel= "<label>Text to rotate:</label>"
    textarea = "<textarea name='message'>" + encrypted_message + "</textarea>"
    rotate_label = "<label>Rotate by:</label>"
    rotare = "<textarea name='rot'>" + str(rotare) + "</textarea>"
    content = "<body>"+"<h1>" + header + "</h1>"  +"<p>"+ rotate_label + str(rotare) +"</p>"+ "<br>" +"<p>"+ textlabel + textarea  +"</p>"+ "<br>" + submit +"</body>"
    return content
    
class MainHandler(webapp2.RequestHandler): 
    def get(self): #contains the initial state of the homepage
        rotation_amount = 13
        encrypted_message = ""
        
        form =  "<form method='post'>"  + write_content(rotation_amount, encrypted_message) + "</form>"
        self.response.write(form)
        
    def post(self): #gathers user input and passes it to write_content
        rotate_recieved = self.request.get("rot")
        if rotate_recieved == 3.14 or str(rotate_recieved) == "pi":
            pass
        try:
            rotate_recieved = int(rotate_recieved)
            message_recieved = self.request.get("message")
            encrypted_message = caesar.encrypt(message_recieved, int(rotate_recieved))
            safe_message = cgi.escape(encrypted_message)
        
            form = "<form method='post'>"  + write_content(rotate_recieved, safe_message) + "</form>"
            self.response.write(form)
        except:
            rotate_recieved= 0
            message_recieved = self.request.get("message")
            encrypted_message = caesar.encrypt(message_recieved, int(rotate_recieved))
            safe_message = cgi.escape(encrypted_message)
        
            form = "<form method='post'>"  + write_content(rotate_recieved, safe_message) + "</form>"+"<p style='color:red;'>" + "Rotation amount must be an integer!" +"</p>"
            self.response.write(form)
'''        
class PiHandler(webapp2.RequestHandler):
    def get(self):
        form = "<p>" + "3.1415926535897932384626433832795028841971693993751058209749445923 0781640628620899862803482534211706798214808651328230664709384460 9550582231725359408128481117450284102701938521105559644622948954 9303819644288109756659334461284756482337867831652712019091456485 6692346034861045432664821339360726024914127372458700660631558817 4881520920962829254091715364367892590360011330530548820466521384 1469519415116094330572703657595919530921861173819326117931051185 4807446237996274956735188575272489122793818301194912983367336244 0656643086021394946395224737190702179860943702770539217176293176 7523846748184676694051320005681271452635608277857713427577896091 7363717872146844090122495343014654958537105079227968925892354201 9956112129021960864034418159813629774771309960518707211349999998 3729780499510597317328160963185950244594553469083026425223082533 4468503526193118817101000313783875288658753320838142061717766914 7303598253490428755468731159562863882353787593751957781857780532 171226806613001927876611195909216420198" + "</p>" + 
        self.response.write(form)

'''        
app = webapp2.WSGIApplication([
    ('/', MainHandler), #only Caesar page for now
    #('/pi', PiHandler), #surprise page
], debug=True)
