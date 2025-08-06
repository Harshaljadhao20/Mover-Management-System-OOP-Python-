from abc import ABC, abstractmethod

# Abstract class for common structure
class MoveRequest(ABC):
    def __init__(self, customer_name, distance_km):
        self.customer_name = customer_name
        self._distance_km = distance_km
        self.__status = "Pending"  # Private

    def update_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class HomeMove(MoveRequest):
    def __init__(self, customer_name, distance_km, num_rooms):
        super().__init__(customer_name, distance_km)
        self.num_rooms = num_rooms

    def calculate_cost(self):
        return 500 * self.num_rooms + 20 * self._distance_km

    def display_info(self):
        print(f"[Home Move] Customer: {self.customer_name}, Rooms: {self.num_rooms}, Distance: {self._distance_km} km")
        print(f"Status: {self.get_status()}, Estimated Cost: ₹{self.calculate_cost()}")


class OfficeMove(MoveRequest):
    def __init__(self, customer_name, distance_km, num_desks):
        super().__init__(customer_name, distance_km)
        self.num_desks = num_desks

    def calculate_cost(self):
        return 300 * self.num_desks + 25 * self._distance_km

    def display_info(self):
        print(f"[Office Move] Customer: {self.customer_name}, Desks: {self.num_desks}, Distance: {self._distance_km} km")
        print(f"Status: {self.get_status()}, Estimated Cost: ₹{self.calculate_cost()}")


# Demo usage
if __name__ == "__main__":
    move1 = HomeMove("Harshal", 10, 3)
    move2 = OfficeMove("TechCorp Ltd", 25, 10)

    move1.display_info()
    move1.update_status("Confirmed")
    print()

    move2.display_info()
    move2.update_status("In Progress")
    print()

    # Final status check
    print(f"{move1.customer_name}'s move status: {move1.get_status()}")
    print(f"{move2.customer_name}'s move status: {move2.get_status()}")
