from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import CustomUserManager
from django.http import JsonResponse

idnum=1#학번 나중에 받아서 대입
instance = CustomUserManager.objects.get(pk=idnum)
returndate=""#반납일자
thingtype=""#빌린 물건 이름 대입
borrownum=1#빌린갯수대입
themessageA=""
themessageB=""

borrowerid=0

def com(request):
    themessageB=instance.username+"\n"+instance.student_id+"\n"+thingtype+borrownum+"개"
    themessageA="팜시스템\n중앙동아리\n반납기한: "+returndate+"\n"+thingtype+borrownum+"개"
    return HttpResponse(themessageA+"\n"+themessageB)
# Create your views here.

def check_admin(request):
    if instance.is_staff:  # 관리자 여부 확인
        return JsonResponse({"status": "ok", "message": "관리자입니다."})
    else:
        return JsonResponse({"status": "no", "message": "관리자가 아닙니다."})
    
def accept(request):
        theid=request.POST.get("student_id")
        if request.method=="POST":
             req=CustomUserManager.get(student_id=theid)
             req.user_permissions=True
             req.save()
        return JsonResponse({"status": "ok", "message": "처리완료"})



'''HTML 스크립트

관리자 허용/거부 창 띄우기
var borrowerid=0;
document.getElementById("버튼 태그 이름").addEventListener("click", function() {
    fetch("/check-admin/")
    borrowerid=theid;
    .then(response => response.json())
    .then(data => {
        if (data.status === "ok") {
            alert("관리자 허용/거부 창 띄우기");
        } else {
            alert("대여 신청 완료 창 띄우기");
        }
    });
}); 

허용/거부 눌렀을 때

function approve(studentId) {
    fetch("/approve-request/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: new URLSearchParams({ theid: studentId })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

'''
