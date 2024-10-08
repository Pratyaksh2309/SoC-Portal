# Generated by Django 4.2.6 on 2024-04-20 08:49

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('profile_picture', models.ImageField(blank=True, default='', upload_to=accounts.models.upload_to_location)),
                ('phone_number', models.CharField(max_length=15)),
                ('roll_number', models.CharField(error_messages={'unique': 'A user with that roll number already exists.'}, help_text='Required. 20 characters or fewer.', max_length=20, unique=True, verbose_name='roll number')),
                ('year', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year'), ('M.Tech', 'M.Tech'), ('Ph.D.', 'Ph.D.')], max_length=100)),
                ('department', models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Electrical Engineering', 'Electrical Engineering'), ('Energy Science and Engineering', 'Energy Science and Engineering'), ('Engineering Physics', 'Engineering Physics'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Industrial Design Centre', 'Industrial Design Centre'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering and Materials Science', 'Metallurgical Engineering and Materials Science'), ('Physics', 'Physics')], max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('verification_token', models.CharField(blank=True, default='', max_length=32)),
            ],
        ),
    ]
