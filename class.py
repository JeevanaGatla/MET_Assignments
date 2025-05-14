


class Laptop:
    def __init__ (self,color,brand):
        self.color = color
        self.brand = brand
        self.version = 3.10
        
    def start(self):
        print(f"{self.brand} laptop is started working")

    def screen_on(self):
        print(f"laptop screen is on ")

    def display(self):
        print(f"vedio is displaying on the screen")

    def low_battery(self):
        print(f"Battery low , Please connect the charger ")

    def power_off(self):
        print(f"power off due to low battery")

    def stop(self):
        print(f"laptop is stopped working")

laptop = Laptop("Black","Dell")

laptop.start()
laptop.screen_on()
laptop.low_battery()
laptop.power_off()
laptop.stop()


