from django.shortcuts import render, redirect
from .text_to_speech import generate_audio
from .models import AudioBlog

def audio_blog_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        tempo = request.POST.get('tempo')
        audio_file = generate_audio(text, tempo)
        
        # Save audio file to disk
        audio_blog = AudioBlog.objects.create(text=text, tempo=tempo)
        audio_blog.audio_file.save('audio_file.mp3', audio_file)
        
        # Redirect to success page
        return redirect('audio_blog_success')
    else:
        return render(request, 'audio_blog.html')
