from django.shortcuts import render, get_object_or_404
from .models import Room, Comment

from datetime import datetime

# Create your views here.
def main(request):
    rooms = Room.objects

    return render(request, 'main.html', {'info':rooms})

def create(request):
    return 

# room = 방확인하기
def roomdetail(request, abc):
    room_detail = get_object_or_404(Room, pk=abc)
    return render(request, 'roomdetail.html', {'a': room_detail} )

def comment(request):
    comment = Comment()
    comment.content = request.GET['content']
    comment.write_date = datetime.now()
    comment.userid = request.user
    comment.save()

    return render(request,'roomdetail.html',{'detail':comment})

