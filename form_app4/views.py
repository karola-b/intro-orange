from django.shortcuts import render, redirect


def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'form_app4/task_form.html',
        )
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            with open('tasks.txt', 'a+') as f:
                f.write(task + "\n")

        return redirect("form_app4:task_list_view")


def task_list_view(request):
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    return render(
        request,
        'form_app4/task_list.html',
        context={
            'tasks': tasks,
        }
    )
