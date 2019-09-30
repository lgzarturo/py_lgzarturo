from django.shortcuts import render, get_object_or_404

from projects.models import Project


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/index.html', context)


def show(request, slug):
    project = get_object_or_404(Project, slug=slug)
    absolute_url = request.build_absolute_uri("%s/%s" % ('projects', project.slug))
    context = {
        'project': project,
        'absolute_url': absolute_url,
    }
    return render(request, 'projects/show.html', context)
