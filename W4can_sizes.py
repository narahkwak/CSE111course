from math import pi

def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    cost_per_can = 0.28
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficiency = calculate_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.1f}")

def calculate_volume(radius, height):
    volume = float(pi * (radius ** 2) * height)
    return volume

def calculate_surface_area(radius, height):
    surface_area = float(2 * pi * radius * (radius + height))
    return surface_area

def calculate_storage_efficiency(volume, surface_area):
    storage_efficiency = float(volume / surface_area)
    return storage_efficiency

main()