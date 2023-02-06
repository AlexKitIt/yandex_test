import pytest

from config import *
from main import (
    get_distance,
    get_dimensions,
    get_fragility,
    get_workload,
    min_price_delivery,
    get_price_delivery
)


class TestPriceDelivery:

    def setup(self):
        self.price = 2
        self.price_450 = 450

        self.very_low_distance = 2, "very_low_distance"
        self.low_distance = 10, "low_distance"
        self.medium_distance = 30, "medium_distance"
        self.high_distance = 100, "high_distance"
        self.zero_distance = 0
        self.negative_distance = -2
        self.over_distance = 9999999999

        self.dimensions_big = "big"
        self.dimensions_small = "small"
        self.dimensions_false = "very small"

        self.fragility = True
        self.not_fragility = False

        self.vh_workload = "very high"
        self.h_workload = "high"
        self.heightened_workload = "heightened"
        self.workload_false = "not"
        self.no_workload = None

    def test_get_distance(self):
        message = ERROR_MESSAGE_TEST.format("дистанции")
        assert get_distance(self.price, self.very_low_distance[0]) \
               == PRICE_DISTANCE.get(self.very_low_distance[1]) + self.price, message
        assert get_distance(self.price, self.low_distance[0]) \
               == PRICE_DISTANCE.get(self.low_distance[1]) + self.price, message
        assert get_distance(self.price, self.medium_distance[0]) \
               == PRICE_DISTANCE.get(self.medium_distance[1]) + self.price, message
        assert get_distance(self.price, self.high_distance[0]) \
               == PRICE_DISTANCE.get(self.high_distance[1]) + self.price, message
        assert get_distance(self.price, self.high_distance[0]) \
               == PRICE_DISTANCE.get(self.high_distance[1]) + self.price, message
        with pytest.raises(Exception):
            get_distance(self.price, self.zero_distance)
        with pytest.raises(Exception):
            get_distance(self.price, self.negative_distance)
        with pytest.raises(Exception):
            get_distance(self.price, self.over_distance)

    def test_get_dimensions(self):
        message = ERROR_MESSAGE_TEST.format("габаритов")
        assert get_dimensions(self.price, self.dimensions_big) \
               == PRICE_DIMENSIONS.get(self.dimensions_big) + self.price, message
        assert get_dimensions(self.price, self.dimensions_small) \
               == PRICE_DIMENSIONS.get(self.dimensions_small) + self.price, message
        with pytest.raises(Exception):
            get_dimensions(self.price, self.dimensions_false)

    def test_get_fragility(self):
        message = ERROR_MESSAGE_TEST.format("хрупкости")
        assert get_fragility(self.price, self.fragility, self.medium_distance[0]) \
               == PRICE_FRAGILITY.get(str(self.fragility)) + self.price, message
        assert get_fragility(self.price, self.not_fragility, self.low_distance[0]) \
               == self.price, message
        with pytest.raises(Exception):
            get_fragility(self.price, self.fragility, self.high_distance[0])

    def test_get_workload(self):
        message = ERROR_MESSAGE_TEST.format("коэффициента загруженности")
        assert get_workload(self.price, self.vh_workload) \
               == round(RATIO_WORKLOAD.get(self.vh_workload) * self.price, 2), message
        assert get_workload(self.price, self.h_workload) \
               == round(RATIO_WORKLOAD.get(self.h_workload) * self.price, 2), message
        assert get_workload(self.price, self.heightened_workload) \
               == round(RATIO_WORKLOAD.get(self.heightened_workload) * self.price, 2), message
        assert get_workload(self.price, self.no_workload) == self.price, message
        assert get_workload(self.price, self.workload_false) == self.price, message

    def test_min_price_delivery(self):
        message = ERROR_MESSAGE_TEST.format("минимальной цены")
        assert min_price_delivery(self.price) == MIN_DELIVERY_PRICE, message
        assert min_price_delivery(self.price_450) == self.price_450, message

    def test_get_price_delivery(self):
        message = ERROR_MESSAGE_TEST.format("всех параметров")
        assert get_price_delivery(
            self.low_distance[0], self.dimensions_big, self.fragility, self.vh_workload).__eq__(
            min_price_delivery(
                (PRICE_DISTANCE.get(self.low_distance[1]) + PRICE_DIMENSIONS.get(self.dimensions_big)
                 + PRICE_FRAGILITY.get(str(self.fragility))) * RATIO_WORKLOAD.get(self.vh_workload))), message
        assert get_price_delivery(
            self.very_low_distance[0], self.dimensions_small,
            self.not_fragility, self.no_workload).__eq__(
            min_price_delivery(
                (PRICE_DISTANCE.get(self.very_low_distance[1]) + PRICE_DIMENSIONS.get(
                    self.dimensions_small)))), message


if __name__ == '__main__':
    pytest.main()
