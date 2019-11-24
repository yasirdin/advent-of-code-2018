from collections import Counter
from itertools import chain
import logging
import re

import numpy as np

from typing import Dict, List, Tuple

logging.basicConfig(level=logging.INFO)

# PART 1: How many square inches of fabric are within two or more claims?


def parse_text_file_to_list(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        return f.read().split('\n')


list_of_claims = parse_text_file_to_list('day-3.txt')


def parse_claim_string(claim: str) -> Tuple[str, str, str]:
    id = re.search('#(.*) @', claim).group(1)
    distance_from_left_and_top = re.search('@ (.*):', claim).group(1)
    dimensions = re.search(': (.*)', claim).group(1)
    return (id, distance_from_left_and_top, dimensions)


def get_coordinates_occupied_by_each_claim(
    list_of_claims: List[str],
) -> Dict[int, List[Tuple[int, int]]]:
    coordinates_occupied_by_each_claim = {}
    for claim in list_of_claims:
        id, distance_from_left_and_top, dimensions = parse_claim_string(claim)

        distance_from_left, distance_from_top = tuple(
            int(distance) for distance in distance_from_left_and_top.split(',')
        )

        dimensions = [int(dimension) for dimension in dimensions.split('x')]
        width = dimensions[0]
        height = dimensions[1]

        possible_x_coordinates = np.arange(
            distance_from_left + 1,
            (distance_from_left + width) + 1,
        )
        possible_y_coordinates = np.arange(
            distance_from_top + 1,
            (distance_from_top + height) + 1,
        )

        coordinates_occupied_by_claim = []
        for x in possible_x_coordinates:
            for y in possible_y_coordinates:
                coordinates_occupied_by_claim.append((x, y))

        coordinates_occupied_by_each_claim[id] = coordinates_occupied_by_claim

    return coordinates_occupied_by_each_claim


coordinates_occupied_by_each_claim = get_coordinates_occupied_by_each_claim(
    list_of_claims,
)
# An easy, but slow way, to flatten a nested list
all_coordinates = sum(list(coordinates_occupied_by_each_claim.values()), [])
inches_within_two_or_more_claims = sum(
    1 for count in Counter(all_coordinates).values() if count >= 2
)

logging.info(
    f'Number of inches in two or more claims: '
    f'{inches_within_two_or_more_claims}.'
)


# PART 2: What is the ID of the only claim that doesn't overlap?


def find_id_of_claim_with_unique_coordinates(
    coordinates_occupied_by_each_claim: Dict[int, List[Tuple[int, int]]],
) -> int:
    for id, coordinates in coordinates_occupied_by_each_claim.items():
        other_dict_without_current = {
            k: v for k, v in coordinates_occupied_by_each_claim.items() if k != id
        }
        other_coordinates = list(other_dict_without_current.values())
        other_coordinates = list(chain(*other_coordinates))  # Flatten
        if len(list(set(coordinates) & set(other_coordinates))) == 0:
            return id


logging.info(
    f"ID of the claim that doesn't overlap: "
    f'{find_id_of_claim_with_unique_coordinates(coordinates_occupied_by_each_claim)}'
)
