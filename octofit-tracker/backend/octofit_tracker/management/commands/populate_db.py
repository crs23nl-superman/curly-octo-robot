from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Marvel team
        marvel_members = [
            {'email': 'ironman@marvel.com', 'name': 'Iron Man', 'team': 'Marvel', 'superpower': 'Powered Armor'},
            {'email': 'spiderman@marvel.com', 'name': 'Spider-Man', 'team': 'Marvel', 'superpower': 'Spider Sense'},
            {'email': 'captain@marvel.com', 'name': 'Captain America', 'team': 'Marvel', 'superpower': 'Super Soldier'},
        ]
        for member in marvel_members:
            User.objects.create(**member)
        Team.objects.create(name='Marvel', members=[m['name'] for m in marvel_members])

        # DC team
        dc_members = [
            {'email': 'batman@dc.com', 'name': 'Batman', 'team': 'DC', 'superpower': 'Detective'},
            {'email': 'superman@dc.com', 'name': 'Superman', 'team': 'DC', 'superpower': 'Super Strength'},
            {'email': 'wonderwoman@dc.com', 'name': 'Wonder Woman', 'team': 'DC', 'superpower': 'Amazonian'},
        ]
        for member in dc_members:
            User.objects.create(**member)
        Team.objects.create(name='DC', members=[m['name'] for m in dc_members])

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30, date='2026-03-08')
        Activity.objects.create(user='Batman', activity_type='Cycling', duration=45, date='2026-03-08')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Run 100m sprints', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with superhero test data'))
