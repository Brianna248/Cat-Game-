class animal:
    def __init__(self, given_name, given_colour):
        self.name= given_name
        self.colour= given_colour

    def make_noise(self):
        print("Animal made a noise!")

class orca_wale(animal):
    pass

class device:
    def __init__(self, height, width,name)
        self.height= height
        self.width= width
        self.name= name
    def power_on(self):
        power=input("would you like to power on the computer?(Please input Yes or No)")
        if power=="Yes":
            print("device has been powered on")
        else:
            print("Your device has not been powered on")


class computer(device):
    ef power_on(self):
        power=input("would you like to power on the computer?(Please input 1 for yes or 2 for no)")
        if power=="1":
            print("device has been powered on")
        elif power=="2":
            print("Your device has not been powered on")
        else:
            print("Your device has not been powered on (you have given an inadequate input)")

