import bottle
import os

app = bottle.Bottle()

angle = 90
os.system("sudo python servo.py 90")

@app.route('/')
def root():
	"Root"
	return bottle.template('main.tpl',angle=angle)

@app.route('/turn/<newangle>')
def turn(newangle=80):
	"Turn the servo to the specified angle"
	global angle
	angle = newangle
	os.system("sudo python servo.py %i" % int(angle))
	return "Turned to %i" % int(angle)

@app.route('/drive')
def drive():
	"Turn camera and snap"
	global angle
	angle = int(bottle.request.query.angle)
	os.system("sudo python servo.py %i" % angle)
	os.system("raspistill -vf -hf -o static/snap.jpg")
	bottle.redirect('/')

@app.route('/snap')
def snap():
	"Snap a picture"
	os.system('raspistill -vf -hf -o static/snap.jpg')
	return bottle.static_file('snap.jpg',root='static')

@app.route('/static/<filename:path>')
def static(filename):
	"Return a static file"
	return bottle.static_file(filename,root='static')

if __name__ == "__main__":
	bottle.run(app,host='0.0.0.0')

