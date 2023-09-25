# Constant

uint8 GEAR_P = 0
uint8 GEAR_R = 1
uint8 GEAR_N = 2
uint8 GEAR_D = 3

uint8 ESTOP_NONE = 0
uint8 ESTOP_HARD_OPERATOR   = 1
uint8 ESTOP_HARD_SOFTWARE   = 2
uint8 ESTOP_SOFT_OPERATOR = 4
uint8 ESTOP_SOFT_PASSENGER = 8

uint8 STATUS_MANUAL = 0
uint8 STATUS_AUTO = 1
uint8 STATUS_ERROR = 2

# Message

Header  header

uint8   estop                  # [ESTOP_NONE, ESTOP_HARD_OPERATOR, ESTOP_HARD_SOFTWARE, ESTOP_SOFT_OPERATOR, ESTOP_SOFT_PASSENGER]

uint8   gear                   # [GEAR_P, GEAR_R, GEAR_N, GEAR_D]
float32 speed_kmh              # 0.0 ~ 511.75 km/h (front wheel speed)
float32 wheel_angle_deg        # -30.0(CW) ~ +30.0(CCW) deg

uint8   target_gear            # [GEAR_P, GEAR_R, GEAR_N, GEAR_D]
float32 target_speed_kmh       # 0.0 ~ 511.75 km/h
float32 target_speed_limit_kmh # 0.0 ~ 511.75 km/h
float32 target_wheel_angle_deg # -30(CW) ~ +30(CCW) deg

uint8 auto_status              # [STATUS_MANUAL, STATUS_AUTO, STATUS_ERROR]
uint8 steer_status             # [STATUS_MANUAL, STATUS_AUTO, STATUS_ERROR]
uint8 speed_status             # [STATUS_MANUAL, STATUS_AUTO, STATUS_ERROR]

bool start_stop                # true: started, false: stopped
bool request_turn_left         # true: requested
bool request_turn_right        # true: requested
