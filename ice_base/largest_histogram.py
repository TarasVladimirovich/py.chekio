
def largest_histogram(histogram):
    area = 0
    for i in range(len(histogram)):
        for j in range(i + 1, len(histogram) + 1):
            base = len(histogram[i:j])
            height = min(histogram[i:j])
            area = max(area, base * height)
    return area


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")