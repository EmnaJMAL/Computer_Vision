import pybullet as p
sim_sleep_time = 1./240 #By default the simulation step of pyBullet is 1./240
simulation_steps = 480 #Corresponds to 2 seconds
def sleepNSeconds(n=1.0):
    simulation_steps = int(n / sim_sleep_time);
    # print(seconds);
    for i in range(simulation_steps):
        time.sleep(sim_sleep_time)
        p.stepSimulation()
        
def spawnObject(
        objectPath, 
        objectPosition=[0,0,0], 
        objectOrientation=p.getQuaternionFromEuler([0.0, 0.0, 0.0]), 
        scaling=1.0):
    # try:
    print("Trying to spawn at {} with orientation {}".format(objectPosition, objectOrientation));
    print("Loading the URDF file...");
    # Load (spawn) the object into the scene
    objectIdSpawned = p.loadURDF(fileName=objectPath,
                        basePosition=objectPosition,
                        baseOrientation=objectOrientation,
                        useMaximalCoordinates=False, # bug: https://github.com/bulletphysics/bullet3/issues/4128
                        useFixedBase=0,
                        # flags=p.URDF_USE_SELF_COLLISION | p.URDF_USE_INERTIA_FROM_FILE,
                        # flags=p.URDF_USE_INERTIA_FROM_FILE,
                        globalScaling = scaling,
                        );
    print("Object created with id: {}".format(objectIdSpawned));
    return objectIdSpawned;
