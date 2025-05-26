class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def display_device_info(self):
        print(f"Device ID: {self.device_id}")
        print(f"Model: {self.model}")

class Flyer:
    def fly(self):
        print("The Device is now flying.")

class Drone(Device, Flyer):
    def __init__(self, device_id, model, camera_resolution):
        Device.__init__(self, device_id, model)
        self.camera_resolution = camera_resolution

    def capture_image(self):
        print(f"Capturing image with resolution: {self.camera_resolution} MP")

    def display_drone_info(self):
        self.display_device_info()
        print(f"Camera Resolution: {self.camera_resolution} MP")

if __name__ == "__main__":
    drone = Drone("DRN123", "Phantom 4", 20)
    drone.display_drone_info()
    drone.fly()
    drone.capture_image()