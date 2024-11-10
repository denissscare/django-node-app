from django.db import models


class Photo(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to='photos/')
  my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
  
  def __str__(self):
    return self.title
  
  class Meta:
        ordering = ['my_order']