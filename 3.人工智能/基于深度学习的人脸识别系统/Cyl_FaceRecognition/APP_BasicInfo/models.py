from django.db import models


class InfoAdmin(models.Model):
    admin_number = models.CharField(max_length=16)
    admin_passwd = models.CharField(max_length=16)
    admin_pic_path = models.CharField(max_length=255, blank=True, null=True)
    admin_token = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_admin'


class InfoCheck(models.Model):
    st_id = models.CharField(max_length=16, blank=True, null=True)
    te_co_id = models.CharField(max_length=16, blank=True, null=True)
    what_week = models.CharField(max_length=16, blank=True, null=True)
    what_day = models.CharField(max_length=16, blank=True, null=True)
    which_lesson = models.CharField(max_length=16, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_check'


class InfoChoose(models.Model):
    st_id = models.CharField(max_length=16, blank=True, null=True)
    te_co_id = models.CharField(max_length=16, blank=True, null=True)
    truant_number = models.IntegerField(blank=True, null=True)
    belate_number = models.IntegerField(blank=True, null=True)
    leave_number = models.IntegerField(blank=True, null=True)
    all_number = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_choose'



class InfoClass(models.Model):
    cl_id = models.CharField(max_length=16, blank=True, null=True)
    cl_grade = models.CharField(max_length=16, blank=True, null=True)
    cl_number = models.CharField(max_length=16, blank=True, null=True)
    cl_name = models.CharField(max_length=50, blank=True, null=True)
    sp_id = models.CharField(max_length=16, blank=True, null=True)
    te_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_class'


class InfoCollege(models.Model):
    co_id = models.CharField(max_length=16)
    co_name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'info_college'


class InfoCourse(models.Model):
    cour_id = models.CharField(max_length=16)
    cour_name = models.CharField(max_length=50)
    cour_credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_course'


class InfoFacecode(models.Model):
    st_id = models.CharField(max_length=16, blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    face_encoding = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_facecode'


class InfoFeedback(models.Model):
    start = models.IntegerField(blank=True, null=True)
    suggest = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_feedback'



class InfoLeaveTable(models.Model):
    st_id = models.CharField(max_length=16, blank=True, null=True)
    le_name = models.CharField(max_length=16, blank=True, null=True)
    leave_start_time = models.TimeField(blank=True, null=True)
    leave_stop_time = models.TimeField(blank=True, null=True)
    leave_reson = models.CharField(max_length=256, blank=True, null=True)
    leave_teacher_idea = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_leave_table'


class InfoRule(models.Model):
    admin_number = models.CharField(max_length=16, blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    absent = models.IntegerField(blank=True, null=True)
    late = models.IntegerField(blank=True, null=True)
    leave = models.IntegerField(blank=True, null=True)
    absent_number = models.IntegerField(blank=True, null=True)
    late_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_rule'



class InfoSpecialty(models.Model):
    sp_id = models.CharField(max_length=16, blank=True, null=True)
    sp_name = models.CharField(max_length=50, blank=True, null=True)
    co_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_specialty'


class InfoStudent(models.Model):
    st_id = models.CharField(max_length=16, blank=True, null=True)
    st_name = models.CharField(max_length=50, blank=True, null=True)
    st_age = models.IntegerField(blank=True, null=True)
    st_sex = models.CharField(max_length=2, blank=True, null=True)
    st_phone = models.CharField(max_length=16, blank=True, null=True)
    st_email = models.CharField(max_length=50, blank=True, null=True)
    st_pic_path = models.CharField(max_length=255, blank=True, null=True)
    st_login_id = models.CharField(max_length=16)
    st_passwd = models.CharField(max_length=16)
    st_token = models.CharField(max_length=60, blank=True, null=True)
    cl_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_student'


class InfoTeCour(models.Model):
    te_co_id = models.CharField(max_length=16, blank=True, null=True)
    te_id = models.CharField(max_length=16, blank=True, null=True)
    cour_id = models.CharField(max_length=16, blank=True, null=True)
    begin_time = models.CharField(max_length=16, blank=True, null=True)
    end_time = models.CharField(max_length=16, blank=True, null=True)
    specific = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_te_cour'


class InfoTeacher(models.Model):
    te_id = models.CharField(max_length=16, blank=True, null=True)
    te_name = models.CharField(max_length=50, blank=True, null=True)
    te_age = models.IntegerField(blank=True, null=True)
    te_sex = models.CharField(max_length=2, blank=True, null=True)
    te_phone = models.CharField(max_length=16, blank=True, null=True)
    te_email = models.CharField(max_length=50, blank=True, null=True)
    te_pic_path = models.CharField(max_length=255, blank=True, null=True)
    te_login_id = models.CharField(max_length=16)
    te_passwd = models.CharField(max_length=16)
    te_token = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_teacher'
