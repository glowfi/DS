# Fixed sliding window Format


def fixed(arr, k):

    i, j = 0, 0

    while j < len(arr):

        # Do some work

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            # Print Ans

            # Remove Calculations for i

            # Slide Window
            i += 1
            j += 1


# Variable sliding window Format


def fixed(arr, k):

    i, j = 0, 0
    contd = None

    while j < len(arr):

        # Do some work

        if contd < k:
            j += 1

        elif contd == k:
            # Print Ans
            pass

        elif contd > k:
            while contd > k:
                # Remove Calculations for i

                # Slide Window
                i += 1
            j += 1
