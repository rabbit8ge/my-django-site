from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import RequestContext
from models import Blogs, Categories, Project, Organization
from django.http import Http404
from django.contrib.sitemaps import Sitemap
import datetime
from django.http.response import HttpResponse

# Import PROJECT_ROOT to read local files.
import os
from myblog.settings import PROJECT_ROOT
import json
# Create your views here.

def generate_projects():
    '''
    @deprecated: we should store the information in db.
    '''
    projects = []
    proj0 = Project()
    proj0.name = 'CT Simulation Platform'
    proj0.url = 'blogs/ct-simulation-platform'
    proj0.image = '/media/images/projects/ct_simulation_platform.jpg'
    proj0.desc = 'C/C++, CUDA, boost'
    #proj0.content =
    proj0.start_date = '2011'
    proj0.end_date = '2013'
    projects.append(proj0)
    proj1 = Project()
    proj1.name = 'CT Reconstruction Platform'
    proj1.url = 'blogs/ct-reconstruction-platform'
    proj1.image = '/media/images/projects/ct_reconstruction_platform.gif'
    proj1.desc = 'Matlab, C/C++, CUDA, boost'
    proj1.start_date = '2013'
    proj1.end_date = '2015'
    projects.append(proj1)
    
    return projects

def generate_organizations():
    organizations = []
    org0 = Organization()
    org0.name = 'Shanghai Jiao Tong University'
    org0.role = 'Electronic Engineering'
    org0.image = 'media/images/grad-cap_ypanfy.png'
    org0.url = 'http://www.seiee.sjtu.edu.cn/'
    org0.start_date = '2005'
    org0.end_date = '2009'
    organizations.append(org0)
    org1 = Organization()
    org1.name = 'Shanghai Jiao Tong University'
    org1.role = 'Biomedical Engineering'
    org1.image = 'media/images/grad-cap_ypanfy.png'
    org1.url = 'http://med-x.sjtu.edu.cn/index.asp'
    org1.start_date = '2009'
    org1.end_date = '2012'
    organizations.append(org1)
    org2 = Organization()
    org2.name = 'United Imaging Healthcare Ltd.'
    org2.role = 'Algorithm & Software Engineer'
    org2.image = 'media/images/orgs/uih.png'
    org2.url = 'http://www.united-imaging.com/'
    org2.start_date = '2011'
    org2.end_date = '2015'
    organizations.append(org2)
    org3 = Organization()
    org3.name = 'Autodesk Software (China) Ltd.'
    org3.role = 'Software Development Engineer'
    org3.image = 'media/images/orgs/autodesk.png'
    org3.url = 'http://www.autodesk.com/'
    org3.start_date = '2012'
    org3.end_date = 'now'
    organizations.append(org3)
    
    return organizations

def generate_travels():
    '''
    '''
    travels = []
    filePath = os.path.join(PROJECT_ROOT, 'media/json/TravelPositions.json')
    f = file(filePath)
    travels = json.load(f)
    
    return travels

def index(request):
    print('debug: start index method.')
    blogs = Blogs.objects.all().filter(publish=True)[:3]
    categories = Categories.objects.all()
    projects = generate_projects()
    organizations = generate_organizations()
    travels = json.dumps(generate_travels())
    
    page_title = 'Home'
    meta_keywords = 'He Yiping, Yiping, Yiping He, hyp'
    meta_description = 'Welcome He Yiping'' personal website.'
    try:
        no = blogs.count()
    except:
        print('exception of blogs: ')

    try:
        ret = render_to_response('index.html', locals(), context_instance = RequestContext(request))
    except e:
        print('exception of render: ', e)
    print('debug: end index method.')
    return ret

def blogs(request):

    blogs = Blogs.objects.all().filter(publish=True)
    categories = Categories.objects.all()
    page_title = 'all blogs'
    title = 'blogs'
    recent_blogs = Blogs.objects.filter(publish=True)[:5]
    meta_keywords = 'Technical blogs,programming blogs, programming'
    meta_description = ''
    no = blogs.count()


    return render_to_response('allblogs.html', locals(), context_instance = RequestContext(request))


def category_view(request, slug):
    categories = Categories.objects.all()
    category = get_object_or_404(Categories, slug=slug)
    recent_blogs = Blogs.objects.filter(publish=True)[:5]
    page_title = 'category'+'-'+category.name
    title = category.name
    meta_keywords = category.name
    meta_description = 'Blogs related to '+category.name
    blogs = Blogs.objects.filter(category=category).filter(publish=True)
    no = blogs.count()

    return render_to_response('category.html', locals(), context_instance = RequestContext(request))

def blog_view(request, slug):
    categories = Categories.objects.all()
    recent_blogs = Blogs.objects.filter(publish=True)[:5]
    blog = get_object_or_404(Blogs, slug=slug)
    page_title = 'blog'+'|'+ ' '+ blog.title

    if blog.publish == True:
        pass
    else:
        raise Http404


    return render_to_response('blog.html', locals(), context_instance = RequestContext(request))

def handler404(request):

    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    page_title = 'Error - 500'
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
def contact(request):

    blogs = Blogs.objects.all().filter(publish=True)[:3]
    categories = Categories.objects.all()
    page_title = 'Contact'
    meta_keywords = 'Contact Kd johar'

    meta_description = 'Contact Kd Johar'
    no = blogs.count()
    return render_to_response('contact.html', locals(), context_instance = RequestContext(request))

class blog_sitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Blogs.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date
        