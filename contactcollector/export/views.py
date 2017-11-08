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
    header_cont = [
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
    ]
    body_cont = []
    header_job = [
        'survey_name',
        'survey_notes',
        'employer_name',
        'employer_address',
        'employer_notes',
        'job_title',
        'job_description',
        'job_fulltime',
        'job_tech_skills',
        'job_responsibilities',
        'job_deliverables',
        'job_categories',
    ]
    body_job = []

    rs_s = Survey.objects.all()
    for r_s in rs_s:
        rs_er = Employer.objects.all().filter(survey=r_s.id)
        for r_er in rs_er:
            rs_em = Employee.objects.all().filter(employer=r_er.id)
            for r_em in rs_em:
                row = []
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
                body_cont.append(row)

            rs_j = Job.objects.all().filter(employer=r_er.id)
            for r_j in rs_j:
                row = []
                row.append(r_s.name)
                row.append(r_s.notes)
                row.append(r_er.name)
                row.append(r_er.address)
                row.append(r_er.notes)
                row.append(r_j.title)
                row.append(r_j.description)
                row.append(r_j.full_time)
                row.append(r_j.technical_skills)
                row.append(r_j.responsibilities)
                row.append(r_j.deliverables)
                row.append(r_j.categories)
                body_job.append(row)

    # generate output
    book = excel.pe.Book({
        'Contacts': [header_cont] + body_cont,
        'Jobs': [header_job] + body_job,
    })
    response = excel.make_response(book, "xls", file_name="contactcollector.xls")
    return response

