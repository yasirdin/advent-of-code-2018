from collections import Counter
import logging

from typing import List, Tuple


logging.basicConfig(level=logging.INFO)

# PART 1


def parse_text_file_to_list(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        return f.read().split('\n')


list_of_ids = parse_text_file_to_list('day-2.txt')


def calculate_checksum(list_of_ids: List[str]) -> int:
    two_counter = 0
    three_counter = 0
    for id in list_of_ids:
        counts = list(Counter(id).values())
        if 2 in counts:
            two_counter += 1
        if 3 in counts:
            three_counter += 1
    return two_counter * three_counter


logging.info(f'Checksum: {calculate_checksum(list_of_ids)}')

# PART 2


def find_box_ids(list_of_ids: [List[str]]) -> Tuple[str, str]:
    for index, id in enumerate(list_of_ids, 0):
        other_ids = list_of_ids
        for other_id in other_ids:
            letter_diff_counter = 0
            for letter_in_id, letter_in_other_id in zip(id, other_id):
                if letter_in_id != letter_in_other_id:
                    letter_diff_counter += 1
            if letter_diff_counter == 1:
                return (id, other_id)


def get_common_letters_in_ids(ids: Tuple[str, str]) -> str:
    first_id, second_id = ids
    common_letters = []
    for letter_in_first_id, letter_in_second_id in zip(first_id, second_id):
        if letter_in_first_id == letter_in_second_id:
            common_letters.append(letter_in_first_id)
    return ''.join(common_letters)


logging.info(
    f'{get_common_letters_in_ids(find_box_ids(list_of_ids))}'
)
