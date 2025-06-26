from django.db import models

class Announcement(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement @ {self.created_at.strftime('%Y-%m-%d %H:%M')}"
