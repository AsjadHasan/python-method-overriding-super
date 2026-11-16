
"""
Project: Override Parent Method Using super()
Description: Demonstrates method overriding and inheritance
             using super() in Python.
"""


class Vehicle:
    """Parent class representing a vehicle."""

    def __init__(self, name: str, max_speed: int):
        """Initialize vehicle name and maximum speed."""
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity: int):
        """Return the vehicle's seating capacity."""
        return f"{self.name} seating capacity is: {capacity}"


class Bus(Vehicle):
    """Child class representing a bus."""

    def seating_capacity(self, capacity: int = 50):
        """Override seating capacity with a default of 50."""
        return super().seating_capacity(capacity)


def main():
    """Create a Bus object and display its seating capacity."""
    bus = Bus("School Bus", 120)
    print(bus.seating_capacity())


if __name__ == "__main__":
    main()
