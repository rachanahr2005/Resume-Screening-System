from django.shortcuts import render, redirect
from .models import Candidate
from .utils import extract_text_from_pdf, get_skills, calculate_similarity, predict_candidate

def index(request):
    if request.method == "POST":
        job_description = request.POST.get('job_description')
        files = request.FILES.getlist('resumes')

        for f in files:
            text = extract_text_from_pdf(f)
            score = calculate_similarity(text, job_description)
            skills = get_skills(text)
            prediction, prob = predict_candidate(text,score)

            Candidate.objects.create(
                name=f.name,
                skills=skills,
                score=score,
                prediction=prediction,
                probability=prob
            )

        return redirect('dashboard')

    return render(request, 'scanner/index.html')

def dashboard(request):
    candidates = Candidate.objects.all()
    return render(request, 'scanner/dashboard.html', {'candidates': candidates})

def clear_data(request):
    Candidate.objects.all().delete()
    return redirect('index')