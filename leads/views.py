from rest_framework import generics, status
from rest_framework.response import Response

from django.http import FileResponse, Http404

from .models import ResumeLead, ResumeDownloadToken, Contact
from .serializers import ResumeLeadSerializer, ContactSerializer
from .tasks import send_resume_email


class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ResumeLeadCreateView(generics.CreateAPIView):
    serializer_class = ResumeLeadSerializer
    queryset = ResumeLead.objects.all()

    def perform_create(self, serializer):

        request = self.request

        lead = serializer.save(
            ip_address=self.get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", "")
        )

        # create secure token
        token_obj = ResumeDownloadToken.objects.create(
            email=lead.email
        )

        # send email asynchronously
        send_resume_email.delay(
            lead.email,
            str(token_obj.token)
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")



class ResumeDownloadView(generics.GenericAPIView):

    def get(self, request, token):

        try:
            token_obj = ResumeDownloadToken.objects.get(
                token=token,
                is_used=False
            )
        except ResumeDownloadToken.DoesNotExist:
            raise Http404("Invalid or expired link")

        token_obj.is_used = True
        token_obj.save()

        file_path = "media/resume/my_resume.pdf"

        return FileResponse(
            open(file_path, "rb"),
            content_type="application/pdf"
        )