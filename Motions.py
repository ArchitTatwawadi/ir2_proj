
def Archit_motion()
  go_to_intial_pose()
  #move neck from 90 to 135
  move_neck(100)
  move_neck(135)
  move_lf_elbow_updown(135)
  move_rt_elbow_updown(45)
  
  for x in range(0, 3):  
    Move_head("up")
    sleep(for few ms)
    Move_head("down")
    
    
def Mohak_motion()
  go_to_intial_pose()
  
  move_rt_shoulder_updown(45) #up
  move_lf_shoulder_updown(135) #up
  
  for x in range(0, 3):
    move_rt_shoulder_side(75) #inward
    move_lf_shoulder_side(115)
    sleep(for few ms)
    move_rt_shoulder_side(90) #outward
    move_lf_shoulder_side(90)
    
    
def shashwath_motion()
  go_to_initial_pose()
  
  for x in range(0:3)
    move_rt_shoulder_updown(135) #down
    move_lf_shoulder_updown(125) #up
    move_lf_elbow_updown(45) #inward
    sleep(for very few ms)
    move_lf_elbow_updown(135) #outward
    
    move_lf_elbow_updown(90) #reset
    move_lf_shoulder_updown(45) #down
    move_rt_shoulder_updown(65) #up
    move_rt_elbow_updown(125) #inward
    sleep(for very few ms)
    move_rt_elbow_updown(45) #outward
    
    move_rt_elbow_updown(90)
    
def sandeeep_motion()
  go_to_initial_pose()
  
  move_lf_shoulder_updown(45) #down
  move_rt_shoulder_updown(45) #up
  move_rt_elbow_updown(45) #inward
  sleep(in sec)
  move_rt_elbow_updown(90)
  move_rt_shoulder_updown(135) #down
  
  
def surya_motion()
  go_to_initial_pose()
  
  for x in range(0,3)
    move_head(75) #down
    move_lt_elbow_updown(135) #inward
    move_rt_elbow_updown(45) #inward
  
    sleep(in ms)
  
    move_lf_elbow_updown(90)
    move_rt_elbow_updown(90)
    move_head(90) 
    

def unknown_person_motion()
  go_to_initial_pose()
  
  move_rt_shoulder_updown(135) #down
  move_lf_shoulder_updown(45) #down
  
  move_rt_elbow_rotate(135) #inward
  move_lf_elbow_rotate(45) #inward
  
  for x in range(0,3)
    move_neck(135)
    move_neck(45)

  
  
