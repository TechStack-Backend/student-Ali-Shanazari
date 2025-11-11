from django.shortcuts import render
from django.http import Http404



DEVELOPERS  = [
{
"username": "hassan",
"first_name": "Hassan",
"last_name": "Kabirian",
"skills": ["Python", "Django", "Vue.js"],
},
{
"username": "sara",
"first_name": "Sara",
"last_name": "Ahmadi",
"skills": ["JavaScript", "React", "CSS"],
},
{
"username": "ali",
"first_name": "Ali",
"last_name": "Rezayi",
"skills": ["Java", "Spring Boot", "SQL"],
}]

def developers_list_view(request):
    context = {"developers": DEVELOPERS }
    return render(request, "../templates/developers_list.html", context)

def developers_cv_view(request, username):
    dev = next((d for d in DEVELOPERS if d["username"] == username), None)
    if not dev:
        raise Http404("developer not found")
    return render(request, "../templates/developer_cv.html", {"dev": dev})
