import unittest
import os
import json
from datetime import datetime
from crypto_wallet.utils import get_formatted_datetime, save_to_json_file


class TestUtils(unittest.TestCase):

    def test_get_formatted_datetime(self):
        # Test that the function returns the current date and time in the correct format
        formatted_datetime = get_formatted_datetime()
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.assertEqual(formatted_datetime, now)

    def test_save_to_json_file(self):
        # Prepare test data
        test_data = {
            "mnemonic": "earn pen input pencil pigeon minimum gospel kingdom security asset hawk math",
            "address": "0x064f2E08695f9DD09E14a1CB73841D1F0aF012A6",
            "private_key": "0xce9e4e475e60c0b895265f1448962daecd0ac3a7fc1ffe66a8185c8fdb630a4f"
        }
        prefix = 'test_wallet'

        # Generate the expected filename format
        timestamp = get_formatted_datetime()
        expected_filename = f"{prefix}_{timestamp}.json"

        # Call the function to save data
        save_to_json_file(test_data, prefix)

        # Check if the file exists
        self.assertTrue(os.path.exists(expected_filename))

        # Read the file and check its content
        with open(expected_filename, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, test_data)

        # Clean up by removing the file
        os.remove(expected_filename)


if __name__ == '__main__':
    unittest.main()
