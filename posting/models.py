from django.db import models

# Create your models here.
class Post(models.Model):
    original_post = models.URLField(blank=True, null=True, max_length=500)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True, max_length=500)
    tags = models.CharField(max_length=200, blank=True, null=True, default="#Ucpc")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # These fields determine how each post should be displayed on the page.
    hot = models.BooleanField(default=False, verbose_name="Display at the Hot posts Panel?")
    most = models.BooleanField(default=False, verbose_name="Display at the Most picked Panel?")
    popular = models.BooleanField(default=False, verbose_name="Display at the Polular Panel?")

    def __str__(self):
        return self.title