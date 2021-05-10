# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    if m >= d:
        num_refills = 0
    else:
        prev_distance = 0
        mileage_remaining = m
        stops.append(d)
        idx = 0
        num_refills = 0
        while idx < len(stops):
            if stops[idx] - prev_distance > m:
                num_refills = - 1
                break
            else:
                temp_distance = prev_distance + mileage_remaining
                if temp_distance == stops[idx]:
                    if stops[idx] != d:
                        num_refills = num_refills + 1
                        mileage_remaining = m

                if temp_distance < stops[idx]:
                    num_refills = num_refills + 1
                    mileage_remaining = m - (stops[idx] - prev_distance)

                if temp_distance > stops[idx]:
                    mileage_remaining = mileage_remaining - (stops[idx] - prev_distance)

                prev_distance = stops[idx]
                idx = idx + 1

    return num_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
