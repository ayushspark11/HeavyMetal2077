class Mech:
    walk = None
    run = None
    jump = None
    tonnage = None
    cost = None
    battleValue = None
    head = None
    centerTorso = None
    leftTorso = None
    rightTorso = None
    leftArm = None
    rightArm = None
    leftLeg = None
    rightLeg = None

    class Part:
        armor = None
        structure = None
        compartments = None
        components = None
    
    class Component:
        name = None
        type = None
        size = None
        isDestroyed = False
        range = None
        heat = None
        damage = None
        ammo = None
        pilotingModifier = None
        movementModifier = None
        gunneryModifier = None
        forceTest = None
        #TODO: determine where modifiers affect
        effectDistance = None