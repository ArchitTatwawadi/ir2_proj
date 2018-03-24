import ir2_base as ir
import Motions as mo

ir.open_port()
ir.set_speed(300)
ir.set_sleep(0.5)

#ir.nk(90)
#ir.nk(40)
#ir.nk(90)
#ir.nk(130)
#ir.nk(90)

#ir.initall()

mo.Archit_motion()
#mo.Mohak_motion()

ir.close_port()
