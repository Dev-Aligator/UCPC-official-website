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

    def save(self, *args, **kwargs):
        if self.image_url:
            if 'drive.google.com' in self.image_url:
                # extract the ID from the original URL
                id_index = self.image_url.find('/d/') + 3
                view_index = self.image_url.find('/view')
                file_id = self.image_url[id_index:view_index]

                # create the new URL with the ID
                new_url = 'https://drive.google.com/uc?export=view&id=' + file_id

                # set the image_url field to the new URL
                self.image_url = new_url

        super().save(*args, **kwargs)
    
    # These fields determine how each post should be displayed on the page.
    hot = models.BooleanField(default=False, verbose_name="Display at the Hot posts Panel?")
    most = models.BooleanField(default=False, verbose_name="Display at the Most picked Panel?")
    popular = models.BooleanField(default=False, verbose_name="Display at the Polular Panel?")

    def __str__(self):
        return self.title