from controller import Robot, Motor, DistanceSensor

TIME_STEP = 64
MAX_SPEED = 6.28


robot = Robot()

Lsensor = robot.getDevice("ls")
Rsensor = robot.getDevice("rs")

Lsensor.enable(TIME_STEP)
Rsensor.enable(TIME_STEP)

frstM = robot.getDevice('1')
scndM = robot.getDevice('2')
thrdM = robot.getDevice('3')
frthM = robot.getDevice('4')

frstM.setPosition(float('inf'))
scndM.setPosition(float('inf'))
thrdM.setPosition(float('inf'))
frthM.setPosition(float('inf'))

frstM.setVelocity(0.0)
scndM.setVelocity(0.0)
thrdM.setVelocity(0.0)
frthM.setVelocity(0.0)


while robot.step(TIME_STEP) != -1:
    
    frstSpeed = 0.5 * MAX_SPEED
    scndSpeed = 0.5 * MAX_SPEED
    thrdSpeed = 0.5 * MAX_SPEED
    frthSpeed = 0.5 * MAX_SPEED
    
    
    
    
    
    
    right_obstacle = Rsensor.getValue() < 1000
    left_obstacle = Lsensor.getValue() < 1000

    
    if right_obstacle or left_obstacle: 
        frstSpeed = -0.5 * MAX_SPEED
        thrdSpeed = -0.5 * MAX_SPEED
        scndSpeed = 0.5 * MAX_SPEED
        frthSpeed = 0.5 * MAX_SPEED
    
   
    frstM.setVelocity(frstSpeed)
    scndM.setVelocity(scndSpeed)
    thrdM.setVelocity(thrdSpeed)
    frthM.setVelocity(frthSpeed)