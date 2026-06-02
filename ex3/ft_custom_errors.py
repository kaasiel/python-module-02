#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: belaindr <belaindr@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/21 12:55:24 by belaindr            #+#    #+#            #
#   Updated: 2026/06/02 12:00:33 by belaindr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water error") -> None:
        super().__init__(message)


def check_plant_error(name: str, stats: int, water: int) -> None:
    if (stats):
        raise PlantError(f"the {name} plant is wilting!")
    if (water):
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant_error("tomato", 1 > 0, 0)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_plant_error("tomato", 1 < 0, 1)
    except WaterError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting catching all garden errors...")
    for stats, water in [(1, 0), (0, 1)]:
        try:
            check_plant_error("Tomato", stats, water)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
