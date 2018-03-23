
def Archit_motion()
  go_to_intial_pose()
  #move neck from 90 to 135
  move_neck(100)
  move_neck(135)
  move_lf_elbow(135)
  move_rt_elbow(45)
  for x in range(0, 3):  
    Move_head("up")
    Move_head("down")

  
  
