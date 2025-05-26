from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self._is_on = False  
        
    @abstractmethod
    def operate(self):
        pass
    
    def show_status(self):
        status = "ON" if self._is_on else "OFF"
        print(f"{self.name} is currently {status}")
    
    def turn_on(self):
        self._is_on = True
        print(f"{self.name} has been turned ON")
    
    def turn_off(self):
        self._is_on = False
        print(f"{self.name} has been turned OFF")
    
    @property
    def is_on(self):
        return self._is_on


class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self._brightness = 70
    
    def operate(self):
        if self._is_on:
            print(f"{self.name} is illuminating the room at {self._brightness}% brightness")
        else:
            print(f"{self.name} is off. No illumination.")
    
    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Brightness must be a number")
        if 0 <= value <= 100:
            self._brightness = value
            print(f"{self.name} brightness set to {value}%")
        else:
            raise ValueError("Brightness must be between 0 and 100")


class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self._speed = "medium"
    
    def operate(self):
        if self._is_on:
            print(f"{self.name} is rotating at {self._speed} speed")
        else:
            print(f"{self.name} is off. No air circulation.")
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        valid_speeds = ["low", "medium", "high"]
        if value.lower() in valid_speeds:
            self._speed = value.lower()
            print(f"{self.name} speed set to {value}")
        else:
            raise ValueError(f"Speed must be one of {valid_speeds}")


class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self._temperature = 24
    
    def operate(self):
        if self._is_on:
            print(f"{self.name} is cooling the room to {self._temperature}°C")
        else:
            print(f"{self.name} is off. No cooling.")
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature must be a number")
        if 16 <= value <= 30:
            self._temperature = value
            print(f"{self.name} temperature set to {value}°C")
        else:
            raise ValueError("Temperature must be between 16°C and 30°C")

def main():
    light = SmartLight("Living Room Light")
    fan = SmartFan("Bedroom Fan")
    ac = SmartAC("Kitchen AC")
    
    print("\n--- Initial Status ---")
    light.show_status()
    fan.show_status()
    ac.show_status()
    
    print("\n--- Turning Devices On ---")
    light.turn_on()
    fan.turn_on()
    ac.turn_on()
    
    print("\n--- Updated Status ---")
    light.show_status()
    fan.show_status()
    ac.show_status()
    
    print("\n--- Operating Devices ---")
    light.operate()
    fan.operate()
    ac.operate()
    
    print("\n--- Attempting to Access Private Attributes ---")
    try:
        print(light._is_on)
        print("Direct access worked, but this violates encapsulation!")
    except AttributeError:
        print("Cannot access private attribute directly")
    
    print("\n--- Using Getters/Setters ---")
    print(f"Light is on: {light.is_on}")
    print(f"Current brightness: {light.brightness}%")
    light.brightness = 90
    print(f"Updated brightness: {light.brightness}%")
    
    print(f"Fan is on: {fan.is_on}")
    print(f"Current speed: {fan.speed}")
    fan.speed = "high"
    print(f"Updated speed: {fan.speed}")
    
    print(f"AC is on: {ac.is_on}")
    print(f"Current temperature: {ac.temperature}°C")
    ac.temperature = 22
    print(f"Updated temperature: {ac.temperature}°C")
    
    print("\n--- Testing Validation ---")
    try:
        light.brightness = 150  
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        fan.speed = "super"  
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        ac.temperature = 10  
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n--- Turning Devices Off ---")
    light.turn_off()
    fan.turn_off()
    ac.turn_off()
    
    print("\n--- Operating After Turning Off ---")
    light.operate()
    fan.operate()
    ac.operate()

if __name__ == "__main__":
    main()