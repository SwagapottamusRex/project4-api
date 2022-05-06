from django.db import models
from jwt_auth.models import CustomUser



class Color(models.Model):
  color_name = models.CharField(max_length=30)
  def __str__(self):
    return f'Color: {self.color_name}'

class Pixel(models.Model):
  x_axis = models.IntegerField(default= None)
  y_axis = models.IntegerField(default=None)
  color = models.ForeignKey(Color, related_name= 'color', on_delete= models.PROTECT, null=False, default=2)
  current_owner = models.ForeignKey(CustomUser, related_name='pixel', on_delete=models.PROTECT, null=True)
  number_of_times_changed = models.IntegerField(default=None)
  def __str__(self):
    return f'X axis = {self.x_axis} Y axis = {self.y_axis} Color = {self.color}'


class Community(models.Model):
  creator = models.ForeignKey(CustomUser, related_name= 'community', on_delete=models.CASCADE, null=True)
  image = models.CharField(max_length=250)
  name = models.CharField(max_length=50, default=None)
  def __str__(self):
    return f'creator: {self.creator}...Community Name: {self.name}'

class Comment(models.Model):
  thread = models.ForeignKey('Thread', related_name='thread', on_delete=models.CASCADE, null=True, blank=True)
  text = models.CharField(max_length=250)
  creator_of_comment = models.ForeignKey(CustomUser, related_name='creator', on_delete=models.CASCADE, null=True)
  def __str__(self):
    return f'creator of comment: {self.creator_of_comment} Comment: {self.text}'

class Thread(models.Model):
  title = models.CharField(max_length=200)
  reply_thread = models.ForeignKey(Comment, related_name = 'comment', on_delete=models.CASCADE, null=True, blank=True)
  community = models.ForeignKey(Community, related_name='community', on_delete=models.CASCADE, null=True)
  def __str__(self):
    return f'Thread Title: {self.title} Community belonging: {self.community}'