import json
from datetime import datetime


def get_formatted_datetime():
    """
    Get the current date and time formatted as yyyy-mm-dd_hh-mm-ss.
    :return: Formatted date and time string
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")


def save_to_json_file(data, prefix='data'):
    """
    Save data to a JSON file with a timestamped filename.

    :param data: Dictionary containing the data to save
    :param prefix: Prefix for the filename
    :raises IOError: If there is an issue with file writing
    :raises TypeError: If the data provided is not serializable to JSON
    """
    try:
        file_saved_time = get_formatted_datetime()
        filename = f"{prefix}_{file_saved_time}.json"
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except TypeError as e:
        print(f"Data provided is not serializable to JSON: {e}")
