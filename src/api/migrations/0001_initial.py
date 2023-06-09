# Generated by Django 4.0.4 on 2023-06-26 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=10)),
                ('date_of_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=2)),
                ('date_of_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('date_of_created', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Organization Name')),
                ('description', models.TextField(verbose_name='Organization Description')),
                ('date_of_created', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.ImageField(upload_to='organization', verbose_name='Organization Logo Image URL')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
                'db_table': 'organization',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('date_of_created', models.DateTimeField(auto_now_add=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.region')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state'),
        ),
    ]
