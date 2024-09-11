
def clamp_mag(val: float, max_mag: float) -> float:
    """
    Clamps the value `val` between -max_mag and max_mag.

    Args:
        val (float): The value to be clamped.
        max_mag (float): The maximum magnitude allowed.

    Returns:
        float: The clamped value.

    """
    
    if val > max_mag:
        return max_mag

    if val < -max_mag:
        return -max_mag

    return val



def lerp(val: float, input_min: float, input_max: float, output_min: float, output_max: float) -> float:

    return output_min + ((val - input_min) / (input_max - input_min)) * (output_max - output_min)


def clamp(val: float, min_output: float, max_output: float) -> float:

    return min(max_output, max(min_output, val))



class PIDController:
    """
    Simple PID controller implementation.

    Includes derivative kickback, integral windup, and output protections.

    Attributes:
        kp (float): Proportional gain.
        ki (float): Integral gain.
        kd (float): Derivative gain.
        integral_limit (float): Integral windup limit.
        output_limit (float): Output limit.
        prev_error (float): Previous error value.
        prev_input (float): Previous input value.
        prev_time (float | None): Previous time value.
        integral (float): Integral term.

    Methods:
        update(target: float, input: float, time: float) -> float:
            Updates the PID controller with the given target, input, and time values.
    """
    
    def __init__(self, kp: float = 1, ki: float = 0, kd: float = 0,
                 integral_limit: float = 1_000, output_limit: float = 1_000) -> None:
        """
        Initializes a PIDController object.

        Args:
            kp (float): Proportional gain (default: 1).
            ki (float): Integral gain (default: 0).
            kd (float): Derivative gain (default: 0).
            integral_limit (float): Integral windup limit (default: 1000).
            output_limit (float): Output limit (default: 1000).

        Returns:
            None
        """

        # Tuning parameters
        self.kp: float = kp
        self.ki: float = ki
        self.kd: float = kd

        # Integral windup limit
        self.integral_limit: float = integral_limit

        # Output limit
        self.output_limit: float = output_limit

        # Previous values
        self.prev_error: float = 0.0
        self.prev_input: float = 0.0
        self.prev_time: float | None = None

        # Integral term
        self.integral: float = 0.0



    def update(self, target: float, input: float, time: float) -> float:
        """
        Updates the PID controller with the given target, input, and time values.

        Args:
            target (float): The desired target value.
            input (float): The current input value.
            time (float): The current time value.

        Returns:
            float: The calculated output value.

        """

        error = target - input

        # Don't return anything on first call
        if self.prev_time is None:
            self.prev_error = error
            self.prev_time = time
            self.prev_input = input
            return 0


        time_delta = time - self.prev_time
        

        # Integral windup prevention
        self.integral = clamp_mag(self.integral + (error * time_delta), self.integral_limit)

        # Derivative kickback prevention
        derivative = (error - self.prev_error) / time_delta

        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        # Store previous values
        self.prev_error = error
        self.prev_time = time
        self.prev_input = input

        return clamp_mag(output, self.output_limit)
