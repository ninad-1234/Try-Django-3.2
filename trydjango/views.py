from django.http import HttpResponse
import random 

from django.template.loader import render_to_string


from articles.models import Article


def home_view(request, *args, **kwargs):
    print(1000 * 100)
    print(request)
    name ="Justin"

    print(args, kwargs)


    random_id = random.randint(1, 2)

    article_obj = Article.objects.get(id=random_id)
    articles_queryset= Article.objects.all()
    context = {
        "object_list": articles_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING= render_to_string("home-view.html",
    context= context)
    #HTML_STRING = """
    #<h1>{title} (id: {id})! </h1>
    #<p>{content} ! </p>
    #""".format(**context)

    return HttpResponse(HTML_STRING)
    