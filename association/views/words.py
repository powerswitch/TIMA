from app.functions.piwik import track
from association.models import Language, Word
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.shortcuts import get_object_or_404, render

def words(request):
    o = request.GET.get('o') if 'o' in request.GET else 'name'
    l = request.GET.get('l')

    word_list = Word.objects.all().annotate(c=Count('word')).order_by(o)
    if l:
        lang = get_object_or_404(Language, code=l)
        word_list = word_list.filter(languages=lang)

    paginator = Paginator(word_list, 50)
    page = request.GET.get('page')
    try:
        words = paginator.page(page)
    except PageNotAnInteger:
        words = paginator.page(1)
    except EmptyPage:
        words = paginator.page(paginator.num_pages)

    track(request, 'Words | TIMA')
    return render(request, 'tima/words/words.html', locals())

def word(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    track(request, '%s | TIMA' % word)
    return render(request, 'tima/words/word.html', locals())