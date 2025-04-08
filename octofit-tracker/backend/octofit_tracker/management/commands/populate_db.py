from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='user1@example.com', name='User One', age=25),
            User(_id=ObjectId(), email='user2@example.com', name='User Two', age=30),
            User(_id=ObjectId(), email='user3@example.com', name='User Three', age=35),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team(_id=ObjectId(), name='Team Alpha')
        team.save()
        team.members.set(users)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Running', duration=60),
            Activity(_id=ObjectId(), user=users[1], type='Cycling', duration=90),
            Activity(_id=ObjectId(), user=users[2], type='Swimming', duration=45),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team, points=100),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A refreshing morning run'),
            Workout(_id=ObjectId(), name='Evening Swim', description='Relaxing swim in the evening'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
