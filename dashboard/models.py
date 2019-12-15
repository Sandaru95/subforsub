from django.db import models

class Comment(models.Model):
    owner_user_profile = models.ForeignKey('accounts.Signal_User_Profile', on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=5000)

    def __str__(self):
        return str(self.comment_text[:50])