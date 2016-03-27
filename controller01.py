import vex

#region config
RightDrive = vex.Motor(1)
spinner1   = vex.Motor(2)
spinner2   = vex.Motor(3, True)
spinner3   = vex.Motor(4)
spinner4   = vex.Motor(5, True)
ballfeeder = vex.Motor(6)
intake     = vex.Motor(7)
motor_8    = vex.Motor(8)
motor_9    = vex.Motor(9, True)
LeftDrive  = vex.Motor(10, True)
joystick   = vex.Joystick()
#endregion config

def autonomous():
  pass
vex.run_autonomous(autonomous)

def driver():
  # You will usually have a while forever loop
  while True:
    # Driver control code here, setting motors based on joystick movements
    joystick.set_deadband(20)
    RightDrive.run(joystick.axis2())
    LeftDrive.run(joystick.axis3())
    if joystick.b5up():
      spinner1.run(100)
    else:
      spinner1.off()
    if joystick.b5up():
      spinner2.run(100)
    else:
      spinner2.off()
    if joystick.b5up():
      spinner3.run(100)
    else:
      spinner3.off()
    if joystick.b5up():
      spinner4.run(100)
    else:
      spinner4.off()
    if joystick.b8up():
      ballfeeder.run(100)
    else:
      ballfeeder.off()
    if joystick.b7up():
      intake.run(100)
    else:
      intake.off()
    if joystick.b7left():
      motor_8.run(100)
    else:
      motor_8.off()
    if joystick.b8left():
      motor_9.run(100)
    else:
      motor_9.off()
    if joystick.b5down():
      spinner1.run(75)
    else:
      spinner1.off()
    if joystick.b5down():
      spinner2.run(75)
    else:
      spinner2.off()
    if joystick.b5down():
      spinner3.run(75)
    else:
      spinner3.off()
    if joystick.b5down():
      spinner4.run(75)
    else:
      spinner4.off()
    if joystick.b8down():
      ballfeeder.run(-(100))
    else:
      ballfeeder.off()
    if joystick.b7down():
      intake.run(-(100))
    else:
      intake.off()
    if joystick.b7right():
      motor_8.run(-(100))
    else:
      motor_8.off()
    if joystick.b8right():
      motor_9.run(-(100))
    else:
      motor_9.off()
vex.run_driver(driver)


# main thread
# Code which will run in both autonomous and driver modes
# (e.g. object avoidance logic)
pass

