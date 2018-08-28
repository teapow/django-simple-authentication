"""Tests for simple_authentication.models.user."""

from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    """Shared TestCase base class."""

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="password",
            first_name="Thomas",
            last_name="Power",
        )


class StrTestCase(UserTestCase):
    """Tests for User.__str__()."""

    def test_str_returns_str_instance(self):
        # __str__() returns a string instance.
        self.assertIsInstance(self.user.__str__(), str)

    def test_str_returns_joined_name(self):
        # __str__() returns a string consisting of the first_name joined
        # with the last_name if both values are set.
        self.assertEqual(self.user.__str__(), "Thomas Power")

    def test_str_returns_email_if_first_name_and_last_name_are_none(self):
        # __str__() returns the email address of the User if both first_name
        # and last_name are set to None.
        self.user.first_name = None
        self.user.last_name = None

        self.assertEqual(self.user.__str__(), "test@example.com")

    def test_str_returns_email_if_first_name_and_last_name_are_blank(self):
        # __str__() returns the email address of the User if both first_name
        # and last_name are set to empty strings.
        self.user.first_name = ""
        self.user.last_name = ""

        self.assertEqual(self.user.__str__(), "test@example.com")

    def test_str_returns_first_name_only_if_last_name_is_none(self):
        # __str__() returns only the first_name of the User if the last_name
        # is set to None.
        self.user.last_name = None

        self.assertEqual(self.user.__str__(), "Thomas")

    def test_str_returns_first_name_only_if_last_name_is_blank(self):
        # __str__() returns only the first_name of the User if the last_name
        # is set to an empty string.
        self.user.last_name = ""

        self.assertEqual(self.user.__str__(), "Thomas")

    def test_str_returns_last_name_only_if_first_name_is_none(self):
        # __str__() returns only the last_name of the User if the first_name
        # is set to None.
        self.user.first_name = None

        self.assertEqual(self.user.__str__(), "Power")

    def test_str_returns_last_name_only_if_first_name_is_blank(self):
        # __str__() returns only the last_name of the User if the first_name
        # is set to an empty string.
        self.user.first_name = ""

        self.assertEqual(self.user.__str__(), "Power")


class UsernameTestCase(UserTestCase):
    """Tests for User.username (property)."""

    def test_username_property_returns_email(self):
        # username property returns the object email address.
        self.assertEqual(self.user.username, "test@example.com")


class NameTestCase(UserTestCase):
    """Tests for User.name (property)."""

    def test_name_property_returns_full_name(self):
        # name property returns the full name of the user (via the __str__
        # method).
        self.assertEqual(self.user.name, "Thomas Power")

    def test_name_property_handles_deactivated_user_account(self):
        # name property returns a special string when is_active is False.
        self.user.is_active = False
        self.assertEqual(self.user.name, "Deactivated user")


class GetFullNameTestCase(UserTestCase):
    """Tests for User.get_full_name()."""

    def test_get_full_name_returns_full_name(self):
        # get_full_name() returns the full name of the user.
        self.assertEqual(self.user.get_full_name(), "Thomas Power")

    def test_get_full_name_handles_deactivated_user_account(self):
        # get_full_name() returns a special string when is_active is False.
        self.user.is_active = False
        self.assertEqual(self.user.get_full_name(), "Deactivated user")


class GetShortNameTestCase(UserTestCase):
    """Tests for User.get_short_name()."""

    def test_get_short_name_returns_first_name_if_set(self):
        # get_short_name() returns the user's first_name.
        self.assertEqual(self.user.get_short_name(), "Thomas")

    def test_get_short_name_returns_email_if_first_name_not_set(self):
        # get_short_name() returns the user's email if first_name is not set.
        self.user.first_name = None
        self.assertEqual(self.user.get_short_name(), "test@example.com")


class GetLongNameTestCase(UserTestCase):
    """Tests for User.get_long_name()."""

    def test_get_long_name_returns_joined_name(self):
        # get_long_name() returns first_name and last_name joined.
        self.assertEqual(self.user.get_long_name(), "Thomas Power")

    def test_get_long_name_returns_only_first_name_if_last_name_not_set(self):
        # get_long_name() will return only the first_name if the last_name is
        # not set.
        self.user.last_name = None
        self.assertEqual(self.user.get_long_name(), "Thomas")

    def test_get_long_name_returns_only_email_if_first_name_not_set(self):
        # get_long_name() will return only the user's email address if the
        # first_name is not set (and will disregard the last_name).
        self.user.first_name = None
        self.assertEqual(self.user.get_long_name(), "test@example.com")


class SaveTestCase(UserTestCase):
    """Tests for User.save()."""

    def test_save_forces_email_to_lowercase(self):
        # save() will force email to be lowercase when saved.
        self.user.email = "TEST@EXAMPLE.COM"
        self.user.save()

        self.assertEqual(self.user.email, "test@example.com")


class SetPasswordTestCase(UserTestCase):
    """Tests for User.set_password()."""

    def test_set_password_sets_force_password_change_to_false(self):
        # set_password() will set the force_password_change flag to False.
        self.user.force_password_change = True
        self.user.set_password("password")

        self.assertFalse(self.user.force_password_change)
