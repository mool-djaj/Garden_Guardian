class PlantError(Exception):
    """Custom exception raised for errors in the plant's name."""
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Opening watering system")

    try:
        print("Testing valid plants...")
        for plant in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(plant)

        print("Testing invalid plants...")
        for plant in ["Tomato", "lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    test_watering_system()

    print("Cleanup always happens, even with errors!")
