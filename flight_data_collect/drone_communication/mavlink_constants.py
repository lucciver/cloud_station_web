ORIENTATION_MESSAGE_NAME = 'ATTITUDE'
POWER_STATUS = 'POWER_STATUS'
GLOBAL_POSITION_INT = 'GLOBAL_POSITION_INT'
GPS_RAW_INT = 'GPS_RAW_INT'
GPS_RAW = 'GPS_RAW'
GPS_FIX_TYPE = {
    1 : "GPS_NO_FIX",
    2 : "GPS_2D_FIX",
    3 : "GPS_3D_FIX"
}
MAV_MODE = "MAV_MODE"
MAV_MODE = {
    0 : "PREFLIGHT",
    80 : "STABILIZE_DISARMED",
    208 : "STABILIZE_ARMED",
    64 : "MANUAL_DISARMED",
    192 : "MANUAL_ARMED",
    88 : "GUIDED_DISARMED", 
    216 : "GUIDED_ARMED",
    92 : "DISARMED",
    220 : "AUTO_ARMED",
    66 : "TEST_DISARMED",
    194 : "TEST_ARMED",
}
HEARTBEAT = "HEARTBEAT"

USEFUL_MESSAGES = [
    HEARTBEAT,
    ORIENTATION_MESSAGE_NAME,
    POWER_STATUS,
    GPS_RAW_INT,
    MAV_MODE
]