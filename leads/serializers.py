from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Contact, ResumeLead, Resume

from .tasks import send_contact_email, send_confirmation_email


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
        ]

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Message must be at least 10 characters long."
            )
        return value

    def create(self, validated_data):
        send_contact_email.delay( validated_data.get("name"),
            validated_data.get("email"),
            validated_data.get("subject"),
            validated_data.get("message"))

        send_confirmation_email.delay(
            validated_data.get("name"),
            validated_data.get("email"))
        return super().create(validated_data)


class ResumeLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeLead
        fields = [
            "id",
            "email",
            "full_name",
            "role",
            "company",
            "reason",
        ]
