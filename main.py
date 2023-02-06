from types import NoneType
from typing import Any

from config import *


def in_range(value: int | float, dict_of_range: dict) -> str:
    """Метод проверяет нахождение значения в заданном диапазоне. Возвращет ключ из словаря RATIO_DISTANCE"""

    for name_distance in dict_of_range:
        if dict_of_range.get(name_distance)[0] <= value <= dict_of_range.get(name_distance)[1]:
            return name_distance


def control_type(user_object: Any, expected_types: list) -> None:
    """Метод проверяет, что аргумент на входе необходимого типа"""

    result = []
    for one_type in expected_types:
        if type(user_object) == one_type:
            result.append(True)
    if True not in result:
        raise Exception(ERROR_WRONG_TYPE.format(str(expected_types), type(user_object)))


def get_distance(price: int, distance: int | float) -> int:
    """Метод подсчитывает стоимость доставки с учетом дистанции. Возвращает стоимость доставки"""

    control_type(price, [int]), control_type(distance, [int, float])
    if distance <= 0:
        raise Exception(ERROR_METHOD.format(DISTANCE, distance))
    name_distance = in_range(distance, RATIO_DISTANCE)
    if name_distance in PRICE_DISTANCE.keys():
        price += PRICE_DISTANCE.get(name_distance)
    if name_distance is None:
        raise Exception(ERROR_METHOD.format(DISTANCE, distance))
    return price


def get_dimensions(price: int, dimensions: str) -> int:
    """Метод подсчитывает стоимость доставки с учетом габаритов. Возвращает стоимость доставки"""

    control_type(price, [int]), control_type(dimensions, [str])
    if dimensions in PRICE_DIMENSIONS.keys():
        price += PRICE_DIMENSIONS.get(dimensions)
    elif dimensions not in PRICE_DIMENSIONS.keys():
        raise Exception(ERROR_METHOD.format(DIMENSIONS, dimensions))
    return price


def get_fragility(price: int, fragility: bool, distance: int | float) -> int:
    """Метод подсчитывает стоимость доставки с учетом хрупкости. Возвращает стоимость доставки"""

    control_type(price, [int]), control_type(fragility, [bool]), control_type(distance, [int, float])
    if fragility.__eq__(True) and distance <= DISTANCE_FOR_FRAGILITY:
        price += PRICE_FRAGILITY.get(str(fragility))
    elif fragility.__eq__(True) and distance > DISTANCE_FOR_FRAGILITY:
        raise Exception(ERROR_DISTANCE_FRAGILITY)
    return price


def get_workload(price: int, workload: str | None) -> int | float:
    """Метод подсчитывает стоимость доставки с учетом загруженности службы доставки. Возвращает стоимость доставки"""

    control_type(price, [int]), control_type(workload, [str, NoneType])
    if workload in RATIO_WORKLOAD.keys():
        price *= RATIO_WORKLOAD.get(workload)
    return round(price, 2)


def min_price_delivery(price: int | float) -> int | float:
    """Метод сравнивает стоимость доставки с минимальной стоимостью. Возвращает стоимость доставки"""

    control_type(price, [int, float])
    if price <= MIN_DELIVERY_PRICE:
        price = MIN_DELIVERY_PRICE
    return price


def get_price_delivery(distance: int | float, dimensions: str, fragility: bool, workload: str | None) -> int | float:
    """Метод подсчитывает стоимость доставки с учетом дистанции, габаритов, хрупкости и загруженности службы доставки
    . Возвращает стоимость доставки"""

    price_delivery = START_DELIVERY_PRICE
    price_delivery = get_distance(price_delivery, distance)
    price_delivery = get_dimensions(price_delivery, dimensions)
    price_delivery = get_fragility(price_delivery, fragility, distance)
    price_delivery = get_workload(price_delivery, workload)
    price_delivery = min_price_delivery(price_delivery)
    return price_delivery
