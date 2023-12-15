"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests for models"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        # get_user_model() is a helper function that Django provides
        # for retrieving the user model that is active in this project.
        # It's the recommended way of retrieving the user model
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
