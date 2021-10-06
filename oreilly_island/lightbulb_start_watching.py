from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    start_index = 0
    if start_watching:
        if start_watching not in els:
            els.append(start_watching)
        els.sort()
        start_index = els.index(start_watching)
        if start_index + 1 == len(els):
            return 0
    return sum((els[i+1] - els[i]).total_seconds() for i in range(start_index, len(els), 2))


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )

    assert (
            sum_light(
                els=[
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                start_watching=datetime(2015, 1, 12, 10, 0, 5),
            )
            == 5
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                datetime(2015, 1, 12, 10, 0, 0),
            )
            == 10
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 11, 0, 0),
            )
            == 610
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 11, 0, 10),
            )
            == 600
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 10, 10, 0),
            )
            == 620
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                    datetime(2015, 1, 12, 11, 10, 11),
                    datetime(2015, 1, 12, 12, 10, 11),
                ],
                datetime(2015, 1, 12, 12, 10, 11),
            )
            == 0
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                    datetime(2015, 1, 12, 11, 10, 11),
                    datetime(2015, 1, 12, 12, 10, 11),
                ],
                datetime(2015, 1, 12, 12, 9, 11),
            )
            == 60
    )

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")
