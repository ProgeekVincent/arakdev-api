import uuid
from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"



class ResumeLead(models.Model):

    ROLE_CHOICES = [
        ("recruiter", "Recruiter"),
        ("founder", "Founder"),
        ("engineer", "Engineer"),
        ("student", "Student"),
        ("other", "Other"),
    ]

    REASON_CHOICES = [
        ("hiring", "Hiring"),
        ("collaboration", "Collaboration"),
        ("research", "Researching Candidate"),
        ("learning", "Learning"),
        ("other", "Other"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField()
    full_name = models.CharField(max_length=255, blank=True)

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True)
    company = models.CharField(max_length=255, blank=True)

    reason = models.CharField(max_length=50, choices=REASON_CHOICES, blank=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class ResumeDownloadToken(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)

    is_used = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.email)