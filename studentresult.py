
import sys

def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    percentage = (total / 300) * 100

    return total, average, percentage


if __name__ == "__main__":
    m1 = int(sys.argv[1])
    m2 = int(sys.argv[2])
    m3 = int(sys.argv[3])

    total, average, percentage = calculate_result(m1, m2, m3)

    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Percentage:", percentage, "%")

