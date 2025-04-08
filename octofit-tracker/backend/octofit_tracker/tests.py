# tests.py
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.test import APIClient
from rest_framework import status

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.age, 25)

class TeamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)
    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertIn(self.user, self.team.members.all())

class ActivityModelTest(TestCase):
     def setUp(self):
         self.user = User.objects.create(email="test@example.com", name="Test User", age=25)
         self.activity = Activity.objects.create(user=self.user, type="Running", duration=60)

     def test_activity_creation(self):
         self.assertEqual(self.activity.type, "Running")
         self.assertEqual(self.activity.duration, 60)
         self.assertEqual(self.activity.user, self.user)

class LeaderboardModelTest(TestCase):
     def setUp(self):
         self.team = Team.objects.create(name="Test Team")
         self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

     def test_leaderboard_creation(self):
         self.assertEqual(self.leaderboard.team, self.team)
         self.assertEqual(self.leaderboard.points, 100)

class WorkoutModelTest(TestCase):
     def setUp(self):
         self.workout = Workout.objects.create(name="Test Workout", description="Test Description")

     def test_workout_creation(self):
         self.assertEqual(self.workout.name, "Test Workout")
         self.assertEqual(self.workout.description, "Test Description")

class UserSerializerTest(TestCase):
     def setUp(self):
         self.user_data = {"email": "test@example.com", "name": "Test User", "age": 25}
         self.serializer = UserSerializer(data=self.user_data)

     def test_serializer_valid(self):
         self.assertTrue(self.serializer.is_valid())

class UserViewSetTest(TestCase):
     def setUp(self):
         self.client = APIClient()
         self.user_data = {"email": "test@example.com", "name": "Test User", "age": 25}
         self.user = User.objects.create(**self.user_data)

     def test_get_users(self):
         response = self.client.get("/users/")
         self.assertEqual(response.status_code, status.HTTP_200_OK)

     def test_create_user(self):
         response = self.client.post("/users/", self.user_data, format="json")
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
