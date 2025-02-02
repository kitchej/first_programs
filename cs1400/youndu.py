"""
Project Name: Project 1 - Crew Share Calculator
Author: Joshua Kitchen
Due Date: 9/19/2020
Course: CS1400-005

Note: When entering number of crew members, include BOTH Youndu AND Qill in the total crew.
"""


def main():
    try:
        reavers = input("Enter number of crew members: ")
        units = input("Enter number of units: ")
        reavers = int(reavers)
        units = int(units)
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    units = units - ((reavers - 2) * 3)

    # calculate Youndu's cut

    youndu_cut = units * 0.13

    youndu_cut = str(youndu_cut).split(".")

    youndu_cut = int(youndu_cut[0])  # drop the fractional part of the total to get a whole number

    units = units - youndu_cut

    # calculate Quill's cut

    quill_cut = units * 0.11

    quill_cut = str(quill_cut).split(".")

    quill_cut = int(quill_cut[0])

    units = units - quill_cut

    # calculate Crews cut

    crew_cut = units / reavers

    crew_cut = str(crew_cut).split(".")

    crew_cut = int(crew_cut[0])

    # calculate RBF fund

    rbf = units - (reavers * crew_cut)

    print(
        f"Youndu's share: {youndu_cut + crew_cut}\n"
        f"Quill's share: {quill_cut + crew_cut}\n"
        f"Crew share: {crew_cut}\n"
        f"RBF: {rbf}"
          )


if __name__ == "__main__":
    main()
