from django.db import models


class Blog_Entry(models.Model):
    title = models.CharField(max_length=100, verbose_name="Blog entry title", help_text="title of the post")
    content = models.TextField(
        verbose_name="blog post text",
        help_text="write your text here",
        blank=True,
        null=True, )
    preview = models.ImageField(
        upload_to="blog/preview",
        blank=True,
        null=True,
        verbose_name="blog post preview",
        help_text="Upload preview photo", )
    creation_date = models.DateTimeField(
        blank=True, null=True, verbose_name="creation date", help_text="date of post creation"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="visits counter",
        help_text="Number of views",
        default=0
    )
    is_published = models.BooleanField(default=True, verbose_name="published")

    def __str__(self):
        return f"{self.title} {self.creation_date}"

    class Meta:
        verbose_name = "blog_entry"
        verbose_name_plural = "blog_entries"
        ordering = ("creation_date",)
