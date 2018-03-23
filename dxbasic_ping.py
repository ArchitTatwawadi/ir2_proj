from pyax12.connection import Connection

# Connect to the serial port
serial_connection = Connection(port="COM5", baudrate=1000000)

for dynamixel_id in range(1, 11) :

	# Ping the third dynamixel unit
	is_available = serial_connection.ping(dynamixel_id)

	print(is_available)

# Close the serial connection
serial_connection.close()
