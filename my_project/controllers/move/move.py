from controller import Robot, Motor, DistanceSensor


TIME_STEP = 64
MAX_SPEED = 6.28


robot = Robot()


#left and right sensors to detect obstacles
Lsensor = robot.getDevice("ls")
Rsensor = robot.getDevice("rs")


#enabling them
Lsensor.enable(TIME_STEP)
Rsensor.enable(TIME_STEP)


#create robot objects for my 4 wheels engines
frstM = robot.getDevice('1')
scndM = robot.getDevice('2')
thrdM = robot.getDevice('3')
frthM = robot.getDevice('4')


frstM.setPosition(float('inf'))
scndM.setPosition(float('inf'))
thrdM.setPosition(float('inf'))
frthM.setPosition(float('inf'))


#initializing their velocity at first by zero
frstM.setVelocity(0.0)
scndM.setVelocity(0.0)
thrdM.setVelocity(0.0)
frthM.setVelocity(0.0)


while robot.step(TIME_STEP) != -1:

    #set their velocity to start moving
    frstSpeed = 0.5 * MAX_SPEED
    scndSpeed = 0.5 * MAX_SPEED
    thrdSpeed = 0.5 * MAX_SPEED
    frthSpeed = 0.5 * MAX_SPEED
    

    #read from sensors if their is any obstacles
    right_obstacle = Rsensor.getValue() < 1000
    left_obstacle = Lsensor.getValue() < 1000


    #if then move to the right by making the up left and back left wheels move back(make their speed negative) and athores move forward
    if right_obstacle or left_obstacle: 
        frstSpeed = -0.5 * MAX_SPEED
        thrdSpeed = -0.5 * MAX_SPEED
        scndSpeed = 0.5 * MAX_SPEED
        frthSpeed = 0.5 * MAX_SPEED
    
   
    frstM.setVelocity(frstSpeed)
    scndM.setVelocity(scndSpeed)
    thrdM.setVelocity(thrdSpeed)
    frthM.setVelocity(frthSpeed)
