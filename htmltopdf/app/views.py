from django.shortcuts import render
from weasyprint import HTML
from django.http import HttpResponse
from .models import ConvertedUrls

def html_to_pdf(request):
    url = request.POST.get('url')
    pdf = HTML(url).write_pdf(optimize_size=('fonts', 'images'))
    allurls = ConvertedUrls.objects.create(url=url)
    allurls.save()
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response

def home(request):
    return render(request, 'html-to-pdf.html')