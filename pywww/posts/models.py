from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="posts"
    )
    # atrybuty
    title = models.CharField(max_length=255)  # pole tekstowe o określonej długości
    content = models.TextField()  # pole tekstowe o nieokreślonej długości
    published = models.BooleanField(default=False)  # flaga true/false
    sponsored = models.BooleanField(default=False)  # flaga true/false
    created = models.DateTimeField(auto_now_add=True)  # data utworzenia - tylko przy utworzeniu
    modified = models.DateTimeField(auto_now=True)  # data modyfikacji - zawsze gdy klikniemy save
    tags = models.ManyToManyField('tags.Tag', related_name="posts", blank=True)
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)



    def is_content_long(self, n_chars=200):
        return len(self.content) > n_chars

    def short_content(self, n=200):
        return self.content[:n]

    def __str__(self):
        s = '[X]' if self.published else '[ ]'
        return f'{self.title} by {self.author}'
