import unittest
from unittest.mock import MagicMock, patch

import src.database.db_manager as dbm

class TestDBManager(unittest.TestCase):

    # Test connection
    # def test_insert_into_table(self):
    #     mock_connection = MagicMock()

    #     # Your test data
    #     test_table_name = 'test_table'
    #     test_data = [
    #         {'id': 1, 'name': 'Alice'},
    #         {'id': 2, 'name': 'Bob'},
    #         {'id': 3, 'name': 'Charlie'}
    #     ]

    #     with patch('mysql.connector.connect') as mock_connect:
    #         mock_connect.return_value = mock_connection

    #         dbm.insert_into_table(test_table_name, test_data)

    #     mock_connection.cursor.assert_called_once() 

    def test_generate_insert_query_normal(self):
        test_table_name = 'test_table'
        test_data = [
            {'id': 1, 'name': 'Alpha'},
            {'id': 2, 'name': 'Bravo'},
            {'id': 3, 'name': 'Charlie'}
        ]

        expected_query = "INSERT INTO test_table (id, name) VALUES (%(id)s, %(name)s)"
        generated_query = dbm.generate_insert_query(test_data,test_table_name)
        self.assertEqual(expected_query,generated_query)

    def test_generate_insert_query_empty_list(self):
        test_table_name = 'test_table'
        test_data = []

        with self.assertRaises(ValueError):
            dbm.generate_insert_query(test_data,test_table_name)

    def test_generate_insert_query_with_bad_data_input(self):
        test_table_name = 'test_table'
        test_data = 'test_data'

        with self.assertRaises(TypeError):
            dbm.generate_insert_query(test_data, test_table_name)

    def test_generate_insert_query_with_bad_table_name_input(self):
        test_table_name = 123
        test_data = [
            {'id': 1, 'name': 'Alpha'},
            {'id': 2, 'name': 'Bravo'},
            {'id': 3, 'name': 'Charlie'}
        ]

        with self.assertRaises(TypeError):
            dbm.generate_insert_query(test_data, test_table_name)

    def test_generate_insert_query_with_mixed_types_input(self):
        test_table_name = 'test_table'
        test_data = [
            {'id': 1, 'name': 'Alpha'},
            '11',
            {'id': 3, 'name': 'Charlie'}
        ]

        with self.assertRaises(ValueError):
            dbm.generate_insert_query(test_data, test_table_name)

    def test_generate_insert_query_edge_case_one_element(self):
        test_table_name = 'test_table'
        test_data = [{'id': 3, 'name': 'Charlie'}]

        expected_query = "INSERT INTO test_table (id, name) VALUES (%(id)s, %(name)s)"
        generated_query = dbm.generate_insert_query(test_data,test_table_name)
        self.assertEqual(expected_query,generated_query)

    def test_generate_insert_query_nonequal_number_of_keys(self):
        test_table_name = 'test_table'
        test_data = [
            {'id': 1, 'name': 'Alpha'},
            {'id': 2, 'name': 'Bravo', 'additionalkey':1},
            {'id': 3, 'name': 'Charlie'}
        ]

        with self.assertRaises(ValueError):
            dbm.generate_insert_query(test_data,test_table_name)

    def test_generate_insert_query_mixed_keys(self):
        test_table_name = 'test_table'
        test_data = [
            {'id': 1, 'name': 'Alpha'},
            {'ids': 2, 'names': 'Bravo'},
            {'id': 3, 'name': 'Charlie'}
        ]

        with self.assertRaises(ValueError):
            dbm.generate_insert_query(test_data,test_table_name)

if __name__ == '__main__':
    unittest.main()


