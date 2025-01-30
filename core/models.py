from django.db import models

class Post(models.Model):
    TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('podcast', 'Podcast'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    media_url = models.URLField(blank=True, null=True)  # URL for media like images, videos, podcasts
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
