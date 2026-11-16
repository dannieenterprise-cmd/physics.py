def calculate_area_of_a_circle(radius):
    area = 3.14 * radius * radius
    print("Area of circle is:", area)

def calculate_velocity(distance, time):
    velocity = distance / time
    print("Velocity is:", velocity)

choice = input("Enter 'velocity' or 'area': ").lower()

if choice == "velocity":
    distance = float(input("Distance: "))
    time = float(input("Time: "))
    calculate_velocity(distance, time)
elif choice == "area":
    radius = float(input("Radius: "))
    calculate_area_of_a_circle(radius)
else:
    print("Invalid choice.")