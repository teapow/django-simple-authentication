from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta

User = get_user_model()


class CreateUserTestCase(TestCase):
    """ Tests for UserManager.create_user. """

    def test_create_user_creates_regular_user(self):
        # create_user() will create a new User object using the input
        # arguments.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("password"))

    def test_create_user_saves_to_database(self):
        # create_user() will create a new User object to the database.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
        )

        user_queryset = User.objects.all()
        self.assertEqual(user_queryset.count(), 1)
        self.assertEqual(user, user_queryset.get())

    def test_create_user_raises_value_error_with_invalid_email(self):
        # create_user() will raise a ValueError if a the input email is
        # falsy.
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=None,
                password="password",
            )

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="",
                password="password",
            )

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=0,
                password="password",
            )

    def test_create_user_accepts_extra_kwargs(self):
        # create_user() allows extra model values to be set via kwargs.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
            first_name="Thomas",
            last_name="Power",
        )

        self.assertEqual(user.first_name, "Thomas")
        self.assertEqual(user.last_name, "Power")

    def test_create_user_sets_date_joined(self):
        # create_user() will set the date_joined value correctly.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
        )

        threshold = timedelta(seconds=1)
        self.assertAlmostEqual(user.date_joined, now(), delta=threshold)

    def test_create_user_raises_type_error_for_unknown_extra_kwargs(self):
        # create_user() raises a TypeError when passed extra kwargs that
        # don't map to a User model field.
        with self.assertRaises(TypeError):
            User.objects.create_user(
                email="test@example.com",
                password="password",
                test="value",
            )

    def test_create_user_protects_fields(self):
        # create_user() does not allow protected fields to be overridden
        # using extra kwargs.
        protected_field_map = {
            "date_joined": now(),
            "last_login": now(),
            "is_active": False,
            "is_staff": True,
            "is_superuser": True,
        }

        for field, value in protected_field_map.items():
            with self.assertRaises(TypeError):
                User.objects.create_user(
                    email="test@example.com",
                    password="password",
                    **{field: value}
                )

    def test_create_user_sets_is_superuser_to_false(self):
        # create_user() sets the is_superuser flag to False by default.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
        )

        self.assertFalse(user.is_superuser)

    def test_create_user_sets_is_staff_to_false(self):
        # create_user() sets the is_staff flag to False by default.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
        )

        self.assertFalse(user.is_staff)

    def test_create_user_sets_is_active_to_true(self):
        # create_user() sets the is_active flag to True by default.
        user = User.objects.create_user(
            email="test@example.com",
            password="password",
        )

        self.assertTrue(user.is_active)


class CreateSuperUserTestCase(TestCase):
    """ Tests for UserManager.create_superuser. """

    def test_create_superuser_creates_regular_user(self):
        # create_superuser() will create a new User object using the input
        # arguments.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("password"))

    def test_create_superuser_saves_to_database(self):
        # create_superuser() will create a new User object to the database.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
        )

        user_queryset = User.objects.all()
        self.assertEqual(user_queryset.count(), 1)
        self.assertEqual(user, user_queryset.get())

    def test_create_superuser_raises_value_error_with_invalid_email(self):
        # create_superuser() will raise a ValueError if a the input email is
        # falsy.
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email=None,
                password="password",
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="",
                password="password",
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email=0,
                password="password",
            )

    def test_create_superuser_accepts_extra_kwargs(self):
        # create_superuser() allows extra model values to be set via kwargs.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
            first_name="Thomas",
            last_name="Power",
        )

        self.assertEqual(user.first_name, "Thomas")
        self.assertEqual(user.last_name, "Power")

    def test_create_superuser_sets_date_joined(self):
        # create_superuser() will set the date_joined value correctly.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
        )

        threshold = timedelta(seconds=1)
        self.assertAlmostEqual(user.date_joined, now(), delta=threshold)

    def test_create_superuser_raises_type_error_for_unknown_extra_kwargs(self):
        # create_superuser() raises a TypeError when passed extra kwargs that
        # don't map to a User model field.
        with self.assertRaises(TypeError):
            User.objects.create_superuser(
                email="test@example.com",
                password="password",
                test="value",
            )

    def test_create_superuser_protects_fields(self):
        # create_superuser() does not allow protected fields to be overridden
        # using extra kwargs.
        protected_field_map = {
            "date_joined": now(),
            "last_login": now(),
            "is_active": False,
            "is_staff": False,
            "is_superuser": False,
        }

        for field, value in protected_field_map.items():
            with self.assertRaises(TypeError):
                User.objects.create_superuser(
                    email="test@example.com",
                    password="password",
                    **{field: value}
                )

    def test_create_superuser_sets_is_superuser_to_false(self):
        # create_superuser() sets the is_superuser flag to True by default.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
        )

        self.assertTrue(user.is_superuser)

    def test_create_superuser_sets_is_staff_to_false(self):
        # create_superuser() sets the is_staff flag to True by default.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
        )

        self.assertTrue(user.is_staff)

    def test_create_superuser_sets_is_active_to_true(self):
        # create_superuser() sets the is_active flag to True by default.
        user = User.objects.create_superuser(
            email="test@example.com",
            password="password",
        )

        self.assertTrue(user.is_active)
