import cadquery as cq
import math


def model_kf_wingnut_port(name,coordinates = [0,0,0],rotation = [[0,0,0],[0,0,1],0],surface_thickness = 0):
    
    #COMMON PARAMETERS (ALL FLANGES)
    rim_thickness = 3
    angle = 15
    angle = math.radians(angle)
    groove_thickness = 2.5
    
    if name == "kf10":
        #ARBITRARY PARAMETERS:
        a = 5 #tube od
        b = 4 #tube id
        l = 20 #tube length
        #FIXED PARAMETERS (DEPENDS ON FLANGE):
        rim_od = 30
        rim_id = 12
    
    if name == "kf16":
        #ARBITRARY PARAMETERS:
        a = 8 #tube od
        b = 6 #tube id
        l = 20 #tube length
        #FIXED PARAMETERS (DEPENDS ON FLANGE):
        rim_od = 30
        rim_id = 17

    elif name == "kf25":
        a = 13
        b = 11
        l = 20
        rim_od = 40
        rim_id = 26
    
    elif name == "kf40":
        a = 20
        b = 18
        l = 20
        rim_od = 55
        rim_id = 41

    elif name == "kf50":
        a = 24
        b = 22
        l = 20
        rim_od = 75
        rim_id = 52

    
    wing_sketch = (
        cq.Workplane("XZ")
        .moveTo(a, 0)  
        .lineTo(a, l)  
        .lineTo(rim_od/2, l+((rim_od/2)-a)*math.tan(angle))
        .lineTo(rim_od/2, l+((rim_od/2)-a)*math.tan(angle) + rim_thickness)
        .lineTo(rim_id/2, l+((rim_od/2)-a)*math.tan(angle) + rim_thickness)
        .lineTo(rim_id/2, l+((rim_od/2)-a)*math.tan(angle) + rim_thickness- groove_thickness)
        .lineTo(b, l+((rim_od/2)-a)*math.tan(angle) + rim_thickness- groove_thickness)
        .lineTo(b, 0)
        .lineTo(a,0)
        .close()
    )
    
    wingnut_port = wing_sketch.revolve(angleDegrees=360, axisStart=(0, 0, 0), axisEnd=(0, 1, 0))
    wingnut_port = wingnut_port.rotate(rotation[0],rotation[1],rotation[2])
    wingnut_port = wingnut_port.translate((coordinates[0],coordinates[1],coordinates[2]))
    show_object(wingnut_port)

model_kf_wingnut_port("kf10",[0,0,0])
model_kf_wingnut_port("kf16",[0,0,100])
model_kf_wingnut_port("kf25",[0,0,200])
model_kf_wingnut_port("kf40",[0,0,300])
model_kf_wingnut_port("kf50",[0,0,400])

