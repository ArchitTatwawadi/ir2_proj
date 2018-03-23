from pyax12.connection import Connection
import time


NK  = 1 # range -60 to 50
RSU = 2 # range -53 to 115
RSS = 3 # range -87 to 51
RER = 4 # range -114 to 100
REU = 5 # range -150 to 40
LSU = 6 # range -113 to 40
LSS = 7 # range -49 to 81
LER = 8 # range -90 to 98
LEU = 9 # range -133 to 86
HD  = 10 # range -39 to 36

speed = 100
sleep_time = 0.5
global serial_connection 

def open_port():
    global serial_connection 
    # Connect to the serial port
    serial_connection = Connection(port="/dev/ttyUSB0", baudrate=1000000)
    
def close_port():
    # Close the serial connection
    serial_connection.close()
    
def set_speed(val):
    speed = val

def set_sleep(val):
        sleep_time = val

def send_pos(mid, deg):
    global serial_connection 
    serial_connection.goto(mid, deg, speed, degrees=True)
    time.sleep(sleep_time)    #` Wait 1 second

def get_pos(mid):
    global serial_connection 
    return serial_connection.get_present_position(mid,True) 

def initall():
    global serial_connection 
    for dynamixel_id in range(1, 11) :
        serial_connection.goto(dynamixel_id, 0, speed, degrees=True)
        time.sleep(sleep_time)    # Wait 1 second

def nk(deg):
    send_pos(1,deg)
        
def rsu(deg):
    send_pos(2,deg)    

def rss(deg):
    send_pos(3,deg)    

def rer(deg):
    send_pos(4,deg)    

def reu(deg):
    send_pos(5,deg)    

def lsu(deg):
    send_pos(6,deg)    

def lss(deg):
    send_pos(7,deg)    

def ler(deg):
    send_pos(8,deg)    

def leu(deg):
    send_pos(9,deg)


def hd(deg):
    send_pos(10,deg)

def get_nk(deg):
    return get_pos(1)
        
def get_rsu():
    return get_pos(2)    

def get_rss():
    return get_pos(3)    

def get_rer():
    return get_pos(4)    

def get_reu():
    return get_pos(5)    

def get_lsu():
    return get_pos(6)    

def get_lss():
    return get_pos(7)    

def get_ler():
    return get_pos(8)    

def get_leu():
    return get_pos(9)


def get_hd():
    return get_pos(10)


###############################################################33
