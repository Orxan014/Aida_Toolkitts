from django.db import models
from teams_app.models import Team
# Create your models here.

class Calendar(models.Model):
    # project_id = models.ForeignKey('teams_app.Team', on_delete=models.CASCADE)
    post = models.TextField()
    post_image = models.ImageField(upload_to='Post_images/', null=True, blank=True)
    set_date = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return f'{self.post}'
