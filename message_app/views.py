from django.shortcuts import render, redirect

from message_app.models import Message
from message_app.forms import MessageForm


def contact1(request):
    if request.method == "POST":
        data = request.POST
        print(data)

        email = data.get('email')
        category = data.get('category')
        subject = data.get('subject')
        body = data.get('body')
        fav_date = data.get('fav_date')
        fav_time = data.get('fav_time')

        Message.objects.create(
            email=email,
            category=category,
            subject=subject,
            body=body,
            fav_date=fav_date,
            fav_time=fav_time
        )

        return redirect('message_app:contact1')
    return render(
        request,
        'message_app/contact1.html'
    )


def contact2(request):
    if request.method == "POST":
        form = MessageForm(request.POST) # querydict, bound form (postać związana)

        if form.is_valid():
            data = form.cleaned_data
            email = data.get('email')
            category = data.get('category')
            subject = data.get('subject')
            body = data.get('body')
            fav_date = data.get('fav_date')
            fav_time = data.get('fav_time')

            Message.objects.create(
                email=email,
                category=category,
                subject=subject,
                body=body,
                fav_date=fav_date,
                fav_time=fav_time
            )

            return redirect('message_app:contact2')

        else:
            return render(
                request,
                'message_app/contact2.html',
                context={
                    'form': form,
                }
            )

    elif request.method == "GET":
        form = MessageForm() # unbound form (postać niezwiązana)

        return render(
            request,
            'message_app/contact2.html',
            context={
                'form': form,
            }
        )
