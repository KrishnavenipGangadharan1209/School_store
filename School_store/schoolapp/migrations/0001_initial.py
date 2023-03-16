# Generated by Django 4.1.4 on 2023-03-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('department', models.CharField(choices=[('data_science', 'Data Science'), ('artificial_intelligence', 'Artificial Intelligence'), ('machine_learning', 'Machine Learning'), ('BSc_Physics', 'BSc Physics'), ('BSc_Chemistry', 'BSc Chemistry'), ('BSc_Biology', 'BSc Biology'), ('BBA', 'BBA'), ('MBA', 'MBA'), ('BCom', 'BCom'), ('MCom', 'MCom'), ('Statitics', 'Statitics'), ('History', 'History'), ('Economics', 'Economics'), ('Political_Science', 'Political Science')], max_length=50)),
                ('item', models.CharField(choices=[('notebook', 'Notebook'), ('pen', 'Pen'), ('epaper', 'Exam Paper'), ('inst_box', 'Instrument Box'), ('calculator', 'Calculator')], max_length=50)),
                ('purpose', models.CharField(choices=[('order', 'Place Order'), ('return', 'Return Item')], max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
    ]