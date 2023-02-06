
DISTANCE = "дистанции"
RATIO_DISTANCE = {"very_low_distance": [0, 2],
                  "low_distance": [2, 10],
                  "medium_distance": [10, 30],
                  "high_distance": [31, 999999999]}
PRICE_DISTANCE = {"very_low_distance": 50,
                  "low_distance": 100,
                  "medium_distance": 200,
                  "high_distance": 300}

DIMENSIONS = "габаритов"
PRICE_DIMENSIONS = {"big": 200,
                    "small": 100}

FRAGILITY = "хрупкости"
DISTANCE_FOR_FRAGILITY = 30
PRICE_FRAGILITY = {"True": 300}

WORKLOAD = "загруженности службы доставки"
RATIO_WORKLOAD = {"very high": 1.6,
                  "high": 1.4,
                  "heightened": 1.2}

START_DELIVERY_PRICE = 0
MIN_DELIVERY_PRICE = 400

ERROR_WRONG_TYPE = "Передан неверный тип аргумента. Ожидался '{}', передан '{}'"
ERROR_METHOD = "Значение {} указано некорректно и составляет '{}'"
ERROR_DISTANCE_FRAGILITY = "Возить хрупкие грузы на расстояние более 30 км запрещено"
ERROR_MESSAGE_TEST = "Рассчет стоимости доставки с учетом {} выполнен неверно"
