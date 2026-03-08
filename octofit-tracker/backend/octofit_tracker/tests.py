from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel', superpower='Flight')
        self.assertEqual(user.email, 'test@hero.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', members=['Iron Man', 'Spider-Man'])
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', activity_type='Running', duration=30, date='2026-03-08')
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(leaderboard.team, 'Marvel')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
