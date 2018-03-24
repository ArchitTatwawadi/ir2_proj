import ir2_base as ir
import time

def Archit_motion():
  ir.initall()
  #move neck from 90 to 135
  ir.nk(100)
  ir.nk(135)
  ir.leu(135)
  ir.reu(45)

  for x in range(0, 3):  
    ir.hd(40)
    #time.sleep(1)
    ir.hd(150)
    
  ir.initall()
    
def Mohak_motion():
  ir.initall()
  
  ir.rsu(45) #up
  ir.lsu(135) #up
  
  for x in range(0, 3):
    ir.rss(75) #inward
    ir.lss(115)
    time.sleep(0.5)
    ir.rss(90) #outward
    ir.lss(90)
    
  ir.initall()
    
def shashwath_motion():
  ir.initall()
  
  for x in range(0,3):
    ir.rsu(135) #down
    ir.lsu(125) #up
    ir.leu(45) #inward
    time.sleep(0.5)
    ir.leu(135) #outward
    
    ir.leu(90) #reset
    ir.lsu(45) #down
    ir.rsu(65) #up
    ir.reu(125) #inward
    time.sleep(0.5)
    ir.reu(45) #outward
    
    ir.reu(90)
  ir.initall()
    
def sandeeep_motion():
  ir.initall()
  
  ir.lsu(45) #down
  ir.rsu(45) #up
  ir.reu(45) #inward
  time.sleep(1)
  ir.reu(90)
  ir.rsu(135) #down
  ir.initall()
  
  
def surya_motion():
  ir.initall()
  
  for x in range(0,3):
    ir.hd(75) #down
    ir.leu(135) #inward
    ir.reu(45) #inward
  
    time.sleep(0.5)
  
    ir.reu(90)
    ir.leu(90)
    ir.hd(90) 
  ir.initall()
    

def unknown_person_motion():
  ir.initall()
  
  ir.rsu(135) #down
  ir.lsu(45) #down
  
  ir.rer(135) #inward
  ir.ler(45) #inward
  
  for x in range(0,3):
    ir.nk(135)
    ir.nk(45)
  ir.initall()

  
  
