#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: belaindr <belaindr@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/20 04:35:08 by belaindr            #+#    #+#            #
#   Updated: 2026/05/22 15:07:21 by belaindr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')

    elif operation_number == 1:
        x = 1 / 0 # noqa F841

    elif operation_number == 2:
        open("/non/existent/file")

    elif operation_number == 3:
        result = "temperature: " + 42 # type: ignore[operator] # noqa F841


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in (0, 1, 2, 3, 4):
        print(f"\nTesting operation {i}...")
        try:
            garden_operations(i)
            print("operation completed successfully")
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as e:
            print(f"caught {e.__class__.__name__}: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
