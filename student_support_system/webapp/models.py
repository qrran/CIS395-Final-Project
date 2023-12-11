from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    # add some attributes or fields

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    student_id = models.IntegerField()

    student_email = models.CharField(max_length=200)

    phone_number = models.CharField(max_length=100)

    major = models.CharField(max_length=100)

    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=4.0)

    # Community Engagement
    # community_engagement = models.ForeignKey('CommunityEngagement', on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return self.first_name + "   " + self.last_name
