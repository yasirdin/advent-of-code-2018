import itertools
import logging

from typing import List

logging.basicConfig(level=logging.INFO)

# PART 1


def parse_text_file(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        list_of_freq_change_strings = f.read().split('\n')
        list_of_freq_change_ints = [
            int(freq) for freq in list_of_freq_change_strings
        ]
    return list_of_freq_change_ints


def calculate_resulting_frequency(list_of_frequency_changes: List[int]) -> int:
    return sum(list_of_frequency_changes)


list_of_frequency_changes = parse_text_file('day-1.txt')
resulting_frequency = calculate_resulting_frequency(list_of_frequency_changes)
logging.info(f'Part 1 resulting frequency: {resulting_frequency}.')


# PART 2


def find_first_repeat_resulting_frequency(
    list_of_frequency_changes: List[int],
) -> int:
    starting_frequency = 0
    resultant_frequencies = [starting_frequency]
    counter = 0

    for frequency_change in itertools.cycle(list_of_frequency_changes):
        if counter == 0:
            resultant_frequency = starting_frequency + frequency_change
            resultant_frequencies.append(resultant_frequency)
        else:
            resultant_frequency += frequency_change
            if resultant_frequency in resultant_frequencies:
                return resultant_frequency
            else:
                resultant_frequencies.append(resultant_frequency)
        counter += 1


logging.info(
    f'First resultant frequency reached twice: '
    f'{find_first_repeat_resulting_frequency(list_of_frequency_changes)}.'
)
