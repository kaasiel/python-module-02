#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: belaindr <belaindr@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 23:13:59 by belaindr            #+#    #+#            #
#   Updated: 2026/06/02 12:00:03 by belaindr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        res = input_temperature('25')
        print("Input data is '25'")
        print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        res = input_temperature('abc')
        print(f"Temperature is now {res}°C")
        print()
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
