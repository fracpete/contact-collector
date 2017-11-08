from django.http import HttpResponse
from django.template import loader
import logging
import django_excel as excel
from collect.models import Survey, Employer, Employee, Job

logger = logging.getLogger(__name__)


def index(request):
    template = loader.get_template('export/index.html')
    context = {
        'title': 'Export'
    }
    return HttpResponse(template.render(context, request))


def download(request):

    # read data
    header = [
        'survey_name',
        'survey_notes',
        'employer_name',
        'employer_address',
        'employer_notes',
        'employee_first',
        'employee_middle',
        'employee_last',
        'employee_email',
        'employee_notes',
        'job_title',
        'job_tech_skills',
        'job_deliverables',
        'job_description',
        'job_fulltime',
        'job_categories',
    ]
    body = []

    rs_s = Survey.objects.all()
    for r_s in rs_s:
        row = []
        body.append(row)
        rs_er = Employer.objects.all().filter(survey=r_s.id)
        for r_er in rs_er:
            rs_em = Employee.objects.all().filter(employer=r_er.id)
            for r_em in rs_em:
                row.append(r_s.name)
                row.append(r_s.notes)
                row.append(r_er.name)
                row.append(r_er.address)
                row.append(r_er.notes)
                row.append(r_em.first_name)
                row.append(r_em.middle_name)
                row.append(r_em.last_name)
                row.append(r_em.email)
                row.append(r_em.notes)

    # generate output
    book = excel.pe.Book({'Contacts': [header] + body})
    response = excel.make_response(book, "xls", file_name="contactcollector.xls")
    return response

