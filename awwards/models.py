from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('images')
    bio = models.TextField(max_length=500, blank=True)
    contact = models.CharField(max_length=30, blank=True)
    # email_confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Project.objects.get(user_id=id)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    image = CloudinaryField('images')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_project(self):
        return self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def project_by_id(cls, id):
        project = Project.objects.filter(id=id)
        return project

    @classmethod
    def search_project(cls, name):
        return cls.objects.filter(title__icontains=name).all()


class Rates(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    creativity = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    usability = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    content = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    average = models.DecimalField(default=1, blank=False, decimal_places=2, max_digits=40)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title