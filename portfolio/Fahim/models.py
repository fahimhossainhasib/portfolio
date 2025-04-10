from django.db import models    
from django.utils.text import slugify

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)  # or use ManyToMany if you want tags
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    published_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    images = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True)
    
    def clean_content(self, content):
        content = content.replace('\n', '</p><p>')
        return f'<p>{content}</p>'

    def save(self, *args, **kwargs):
        if self.content:
            self.content = self.clean_content(self.content)
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
