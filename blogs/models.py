# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from tagging.fields import TagField

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse ('category_view', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.name




class Blogs(models.Model):
    page_title = models.CharField(max_length=150, unique=True, verbose_name='Page Title', blank=True)
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    meta_description = models.CharField(max_length=500, verbose_name='Meta Description', blank=True)
    meta_keywords = models.CharField(max_length=250, verbose_name='Meta Keywords', blank=True)
    body = RichTextField()
    category = models.ForeignKey(Categories)
    publish = models.BooleanField(default=None)
    tags = TagField()

    class Meta:
        ordering = ['-date'] # Order as inverse-date.
        verbose_name_plural = "Blogs"


    def get_absolute_url(self):
        '''
        @todo: the url is incorrect used in index.html
        '''
        return reverse ('blog_view', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.title



class Project(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="URL")
    image = models.URLField(verbose_name="Image")
    desc = models.TextField(verbose_name="Description")
    content = RichTextField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = 'Projects'

    def get_absolute_url(self):
        return reverse ('project_view', kwargs={'slug': self.slug})
    
    def __unicode__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    role = models.CharField(max_length=150, unique=False, verbose_name="Role")
    image = models.URLField(verbose_name="Image")
    url = models.URLField(verbose_name="Link")
    desc = models.TextField(verbose_name="Description")
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Orgnaization"
        
    def get_absolute_url(self):
        return reverse ('org_view', kwargs={'name': self.name})
    
    def __unicode__(self):
        return self.name

