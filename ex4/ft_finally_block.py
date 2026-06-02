#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: belaindr <belaindr@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 11:20:45 by belaindr            #+#    #+#            #
#   Updated: 2026/05/28 13:48:48 by belaindr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not (plant_name == plant_name.capitalize()):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        for plant in ("Tomato", "Lettuce", "Carrote"):
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")

    try:
        for plant in ("Tomato", "lettuce"):
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
