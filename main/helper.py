#Gets the voltage from an analog input pin
def get_voltage(pin):
    return (pin.value*3.3)/65536