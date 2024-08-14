from django.db import models


# Create your models here.
class Participants(models.Model):
    ParticipateID = models.IntegerField(primary_key=True)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)


class Subjects(models.Model):
    ParticipateID = models.ForeignKey(Participants, on_delete=models.CASCADE)
    SubjectCode = models.IntegerField(primary_key=True)
    SubjectName = models.CharField(max_length=20)


class Teachers(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    ParticipateID = models.ForeignKey(Participants, on_delete=models.CASCADE)
    SubjectCode = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)


class ProgessRecordBook(models.Model):
    ParticipateID = models.ForeignKey(Participants, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    SubjectCode = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = (('ParticipateID', 'TeacherID', 'SubjectCode'),)


class Feedbacks(models.Model):
    FeedbackID = models.AutoField(primary_key=True)
    ParticipateID = models.ForeignKey(Participants, on_delete=models.CASCADE)
    Feedback = models.TextField()
