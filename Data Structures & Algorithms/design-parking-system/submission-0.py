class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.max_capacity = [-1, big, medium, small]
        self.current_capacity = [0] * 4

    def addCar(self, carType: int) -> bool:
        if self.current_capacity[carType] >= self.max_capacity[carType]:
            return False
        self.current_capacity[carType] += 1
        return True
