from django.shortcuts import render
from .models import Ingestion
import os 
from django.core.files.storage import default_storage
from PyPDF3 import PdfFileWriter, PdfFileReader
from django.conf import settings
from pdf2image import convert_from_path
from PIL import Image
import PIL.Image

# Create your views here.
def extract_pdf_2_image(request, *args, **kwargs):
    pdf_id = kwargs['id']
    pdf_path = Ingestion.objects.filter(id=pdf_id).values_list('page_img_path', flat=True)[0]
    doc_path = str(pdf_path).split('/')[0]
    # print(pdf_path)
    f = default_storage.open(pdf_path, 'r')
    # print(f'this is the media path: {settings.MEDIA_ROOT}')       
    pdf_filename = os.path.join(settings.MEDIA_ROOT, pdf_path)
    doc_path_name = os.path.join(settings.MEDIA_ROOT, doc_path)
    img_path = os.path.join(doc_path_name, 'pdf_img')

    inputpdf = PdfFileReader(open(pdf_filename, "rb"))
    maxPages = inputpdf.numPages
    i=1
    if not os.path.exists(img_path):
        # print(f'\n\nthis is the new path: {doc_path_name}\n\n')
        os.makedirs(img_path)

        for page in range(1, maxPages, 10):
            pil_images = convert_from_path(pdf_filename, dpi=200, first_page=page, last_page=min(page + 10 - 1, maxPages), fmt= 'jpg', thread_count=1, userpw=None, use_cropbox=False, strict=False)
            for img in pil_images:
                img.save(img_path +'/page_' + str(i) + '.jpg', 'JPEG')
                i+=1

    
    exam_paper = Ingestion.objects.filter(status=0)

    context = {
        'exam_paper' : exam_paper,
        'img_path' : os.path.join(settings.MEDIA_URL, doc_path)
    }
    return render (request, 'ingest_question_to_sys.html', context)

def list_all_exam_papers(request, *args, **kwargs):
    exam_paper = Ingestion.objects.filter(status=0)
    context = {
        'exam_paper' : exam_paper        
    }
    return render (request, 'ingest_question_to_sys.html', context)
