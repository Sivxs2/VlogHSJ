from django.db import models
from django.utils.timezone import now

class Content(models.Model):
    """Abstract base class for shared content fields and behavior."""
    title = models.CharField(max_length=255, default="Untitled")
    description = models.TextField(default="No description provided")
    author = models.CharField(max_length=100, default="Anonymous")
    published_date = models.DateField(default=now)
    tags = models.CharField(max_length=200, blank=True, default=" ")  # Comma-separated tags

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def show_published_date(self):
        """Return the published date in a readable format."""
        return self.published_date.strftime('%d, %m, %Y')

    def show_tags(self):
        """Return tags as a list."""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def show_author(self):
        """Return the author's name."""
        return self.author

    def show_description(self):
        """Return the description."""
        return self.description

    def show_info(self):
        """Show basic information about the content."""
        info = f"""
        Title: {self.title}
        Description: {self.description}
        Author: {self.author}
        Published on: {self.show_published_date()}
        Tags: {', '.join(self.show_tags())}
        """
        return info.strip()


class VlogPost(Content):
    """Child class representing a vlog post."""
    video_url = models.URLField(max_length=500, default="No URL available")

    class Meta:
        ordering = ['-published_date']  # Default ordering by published date

    def show_info(self):
        """Override to include vlog-specific details."""
        info = f"""
        {super().show_info()}
        Video URL: {self.video_url}
        """
        return info.strip()

