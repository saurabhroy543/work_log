from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@login_required
def blog(request):
    if request.method == "GET":
        all_blog_type = Blog_Type.objects.filter(
            is_approve=True
        ).all()
        all_author = Author.objects.all()
        context = {
            'all_blog_type': all_blog_type,
            'all_author': all_author
        }
        return render(request, "main_admin/blog.html", context)


@login_required
def add_blog(request):
    """
    param request: data
    :return: None
    function : Create blog
    """

    if request.method == "POST":
        try:
            qry_admin_user = AdminUser.objects.get(admin_user_id=request.session['user_id'])
        except:
            qry_admin_user = None

        Blog.objects.create(
            name=request.POST['add_blogname'],
            description=request.POST['add_blogdesc'],
            blog_type=Blog_Type.objects.get(id=request.POST['add_blogtype']),
            author=Author.objects.get(id=request.POST['add_blogauthor']),
            banner_image=request.FILES.get('add_bannerimage', None),
            description_image=request.FILES.get('add_decriptionimage', None),
            admin_user_id=qry_admin_user,
        )
        messages.success(request, "Data added successfully!")

    return redirect("/blog")


@login_required
def get_blog_datatable(request):
    """
    :param request:
    :return: JsonResponse of all blog
    """
    start = request.GET['start']
    length = request.GET['length']
    end = int(start) + int(length)
    search_value = request.GET['search[value]']
    order_column_number = request.GET['order[0][column]']
    order_column_name = request.GET['columns[' + order_column_number + '][data]']
    order_value = request.GET['order[0][dir]']
    order_sign = '-' + order_column_name

    if order_value == 'asc':
        order_sign = order_column_name

    if search_value == '':
        qry_blog = Blog.objects.all().order_by(
            order_sign
        ).values(
            'id', 'blog_type__name', 'author__name', 'name', 'description', 'banner_image', 'description_image',
            'admin_user_id__username', 'create_dt', 'is_approve'
        )
    else:
        qry_blog = Blog.objects.filter(
            Q(name__icontains=search_value) |
            Q(blog_type__name__icontains=search_value) |
            Q(author__name__icontains=search_value) |
            Q(admin_user_id__username__icontains=search_value) |
            Q(create_dt__icontains=search_value)
        ).order_by(
            order_sign
        ).values(
            'id', 'blog_type__name', 'author__name', 'name', 'description', 'banner_image', 'description_image',
            'admin_user_id__username', 'create_dt', 'is_approve'
        )

    context = {
        'data': list(qry_blog[int(start):end]),
        'recordsTotal': len(qry_blog),
        'recordsFiltered': len(qry_blog)
    }

    return JsonResponse(context)


@csrf_exempt
@login_required
def get_blog_ajax(request):
    """
    :param request: id
    :return: specific blog details
    """
    if request.method == 'POST':
        blog_id = request.POST['id']
        qry_blog = Blog.objects.filter(
            id=blog_id
        ).first()
        data = {
            'id': qry_blog.id,
            'name': qry_blog.name,
            'description': qry_blog.description,
            'blog_type': qry_blog.blog_type.id,
            'author': qry_blog.author.id,
        }

    return JsonResponse(data, safe=False)


@csrf_exempt
@login_required
def approve_disapprove_blog(request):
    """
    :param request: approve_disapprove_id,
                           approve_disapprove_tag
    :return: JsonResponse
    :function: Approve & disapprove blog
    """
    if request.method == 'POST':
        approve_disapprove_id = request.POST['approve_disapprove_id']
        approve_disapprove_tag = request.POST['approve_disapprove_tag']

        try:
            qry_admin_user = AdminUser.objects.get(admin_user_id=request.session['user_id'])
        except:
            qry_admin_user = None

        Blog.objects.filter(
            id=approve_disapprove_id
        ).update(
            is_approve=approve_disapprove_tag,
            admin_user_id=qry_admin_user
        )

        context = {
            'status': True,
            'message': 'Status is update!'
        }
    else:
        context = {
            'status': False,
            'message': 'Get method not allow!'
        }
    return JsonResponse(context)


@login_required
def edit_blog(request):
    """
    :param request: id
    :return: None
    :function: edit blog
    """
    if request.method == "POST":
        qry_blog = Blog.objects.filter(id=request.POST['edit_id']).first()
        qry_blog.name = request.POST['edit_blogname']
        qry_blog.description = request.POST['edit_blogdesc']
        qry_blog.author = Author.objects.get(id=request.POST['edit_blogauthor'])
        qry_blog.blog_type = Blog_Type.objects.get(id=request.POST['edit_blogtype'])
        qry_blog.banner_image = request.FILES.get('edit_bannerimage', qry_blog.banner_image)
        qry_blog.description_image = request.FILES.get('edit_decriptionimage', qry_blog.description_image)
        qry_blog.save()

        messages.success(request, "Data updated successfully!")

    return redirect("/blog")


@login_required
def delete_blog(request):
    """
    :param request: id
    :return: None
    :function: delete blog
    """
    if request.method == "POST":
        Blog.objects.filter(id=request.POST['delete_id']).delete()
        messages.success(request, "Data deleted successfully!")

    return redirect("/blog")
