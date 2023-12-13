"""
Test Custom Django management command.
"""
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Custom Django management command."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available."""
        patched_check.return_value = True
        # when we call check() it will return True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])
        # check() should be called once

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OpeationError."""
        patched_check.side_effect = [Psycopg2OperationalError] * 2 + \
            [OperationalError] * 3 + [True]
        # first 2 times we call check() it will return Psycopg2OperationalError
        # The way you make it raise an exception instead of
        # actually pretend to value is to use side_effect

        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
