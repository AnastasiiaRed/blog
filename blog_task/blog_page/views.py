from django.http.response  import HttpResponseRedirect,Http404
from django.shortcuts import redirect,render
from blog_page.models import Comments
from blog_page.forms import CommentForm
from django.views.decorators.csrf import csrf_protect

	
@csrf_protect	
def addcomment(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_text = form.cleaned_data['comments_text']
            saving_all = Comments.objects.create(comments_text=form_text)
            return redirect(addcomment)
    else:
        form = CommentForm()
    comments=Comments.objects.all()
    return render(request, 'blog.html', {'comments':comments,'form': form})
1
    
	
