class Appliance:
    def status(self):
        print("This is a generic appliance. Status is unknown.")

class Fan(Appliance):
    def status(self):
        print("The fan is running at medium speed.")
        
class Light(Appliance):
    def status(self):
        print("The light is turned on with 75% brightness.")

class AC(Appliance):
    def status(self):
        print("The AC is set to 24 degrees Celsius in cooling mode.")

if __name__ == "__main__":
    appliances = [Fan(), Light(), AC()]
    
    for appliance in appliances:
        appliance.status()