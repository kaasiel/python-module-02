#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: belaindr <belaindr@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/20 04:08:27 by belaindr            #+#    #+#            #
#   Updated: 2026/05/20 04:17:53 by belaindr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp > 40):
        raise ValueError(f"{temp} °C is too hot for plants max (max 40°C)")
    if (temp < 0):
        raise ValueError(f"{temp} °C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    for temp in ["25", "abc", "100", "-50"]:
        print(f"\nInput data is '{temp}'")
        try:
            result = input_temperature(temp)
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
