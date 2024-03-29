# Generated by Django 3.0.3 on 2020-05-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_number', models.CharField(max_length=16)),
                ('admin_passwd', models.CharField(max_length=16)),
                ('admin_pic_path', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_token', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'info_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_id', models.CharField(blank=True, max_length=16, null=True)),
                ('te_co_id', models.CharField(blank=True, max_length=16, null=True)),
                ('what_week', models.CharField(blank=True, max_length=16, null=True)),
                ('what_day', models.CharField(blank=True, max_length=16, null=True)),
                ('which_lesson', models.CharField(blank=True, max_length=16, null=True)),
                ('state', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'info_check',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoChoose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_id', models.CharField(blank=True, max_length=16, null=True)),
                ('te_co_id', models.CharField(blank=True, max_length=16, null=True)),
                ('truant_number', models.IntegerField(blank=True, null=True)),
                ('belate_number', models.IntegerField(blank=True, null=True)),
                ('leave_number', models.IntegerField(blank=True, null=True)),
                ('all_number', models.IntegerField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_choose',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_id', models.CharField(blank=True, max_length=16, null=True)),
                ('cl_grade', models.CharField(blank=True, max_length=16, null=True)),
                ('cl_number', models.CharField(blank=True, max_length=16, null=True)),
                ('cl_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sp_id', models.CharField(blank=True, max_length=16, null=True)),
                ('te_id', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'info_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoCollege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_id', models.CharField(max_length=16)),
                ('co_name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'info_college',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cour_id', models.CharField(max_length=16)),
                ('cour_name', models.CharField(max_length=50)),
                ('cour_credit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoFacecode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_id', models.CharField(blank=True, max_length=16, null=True)),
                ('img_path', models.CharField(blank=True, max_length=255, null=True)),
                ('face_encoding', models.CharField(blank=True, max_length=2500, null=True)),
            ],
            options={
                'db_table': 'info_facecode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(blank=True, null=True)),
                ('suggest', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'info_feedback',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoLeaveTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_id', models.CharField(blank=True, max_length=16, null=True)),
                ('le_name', models.CharField(blank=True, max_length=16, null=True)),
                ('leave_start_time', models.TimeField(blank=True, null=True)),
                ('leave_stop_time', models.TimeField(blank=True, null=True)),
                ('leave_reson', models.CharField(blank=True, max_length=256, null=True)),
                ('leave_teacher_idea', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'info_leave_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_number', models.CharField(blank=True, max_length=16, null=True)),
                ('attendance', models.IntegerField(blank=True, null=True)),
                ('absent', models.IntegerField(blank=True, null=True)),
                ('late', models.IntegerField(blank=True, null=True)),
                ('leave', models.IntegerField(blank=True, null=True)),
                ('absent_number', models.IntegerField(blank=True, null=True)),
                ('late_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_rule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoSpecialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_id', models.CharField(blank=True, max_length=16, null=True)),
                ('sp_name', models.CharField(blank=True, max_length=50, null=True)),
                ('co_id', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'info_specialty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_id', models.CharField(blank=True, max_length=16, null=True)),
                ('st_name', models.CharField(blank=True, max_length=50, null=True)),
                ('st_age', models.IntegerField(blank=True, null=True)),
                ('st_sex', models.CharField(blank=True, max_length=2, null=True)),
                ('st_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('st_email', models.CharField(blank=True, max_length=50, null=True)),
                ('st_pic_path', models.CharField(blank=True, max_length=255, null=True)),
                ('st_login_id', models.CharField(max_length=16)),
                ('st_passwd', models.CharField(max_length=16)),
                ('st_token', models.CharField(blank=True, max_length=60, null=True)),
                ('cl_id', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'info_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('te_id', models.CharField(blank=True, max_length=16, null=True)),
                ('te_name', models.CharField(blank=True, max_length=50, null=True)),
                ('te_age', models.IntegerField(blank=True, null=True)),
                ('te_sex', models.CharField(blank=True, max_length=2, null=True)),
                ('te_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('te_email', models.CharField(blank=True, max_length=50, null=True)),
                ('te_pic_path', models.CharField(blank=True, max_length=255, null=True)),
                ('te_login_id', models.CharField(max_length=16)),
                ('te_passwd', models.CharField(max_length=16)),
                ('te_token', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'info_teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoTeCour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('te_co_id', models.CharField(blank=True, max_length=16, null=True)),
                ('te_id', models.CharField(blank=True, max_length=16, null=True)),
                ('cour_id', models.CharField(blank=True, max_length=16, null=True)),
                ('begin_time', models.CharField(blank=True, max_length=16, null=True)),
                ('end_time', models.CharField(blank=True, max_length=16, null=True)),
                ('specific', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'info_te_cour',
                'managed': False,
            },
        ),
    ]
