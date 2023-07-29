from flask import Flask, render_template, request
import TurtleDebug
# from mobility import Motor
import threading

app = Flask(__name__)

debug = False

cmdVel = [0,0]

# MotorA = Motor(2,3)
# MotorB = Motor(17,27)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drive', methods=['POST'])
def drive():
    command = request.form['command']
    
    if command == 'forward':
        cmdVel[0] = 100
    elif command == 'backward':
        cmdVel[0] = -100
    elif command == 'left':
        cmdVel[1] = 50
    elif cmdVel == 'right':
        cmdVel[1] = -50
    
    return 'Command received: ' + command

def driveThread():
        while True:
            Motor.move(cmdVel[0], cmdVel[1])

if __name__ == '__main__':
    if debug:
        turtledb = TurtleDebug.DebugTurtle()
        # start turtle thread
        threading.Thread(target=turtledb.mainloop).start()
        
    # Start drive thread
    # threading.Thread(target=driveThread).start()
    app.run(debug=True, host='0.0.0.0')
