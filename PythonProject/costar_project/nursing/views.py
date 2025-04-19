from django.shortcuts import render, redirect
from .models import Customer, MovieSession, Seat, Ticket
from .utils import generate_ticket_pdf
from django.http import HttpResponse


def buy_ticket_view(request):
    if request.method == 'POST':
        # Создание клиента
        customer = Customer.objects.create(
            last_name=request.POST['last_name'],
            first_name=request.POST['first_name'],
            phone=request.POST.get('phone', ''),
            birth_date=request.POST.get('birth_date', '2000-01-01')
        )

        # Создание билета (первое свободное место)
        seat = Seat.objects.filter(ticket__isnull=True).first()
        ticket = Ticket.objects.create(
            customer=customer,
            session_id=request.POST['session_id'],
            seat=seat
        )
        return redirect('ticket-pdf', ticket_id=ticket.id)

    # GET-запрос: отображение формы
    sessions = MovieSession.objects.all()
    return render(request, 'nursing/buy_ticket.html', {'sessions': sessions})


def ticket_pdf(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    pdf = generate_ticket_pdf(ticket)
    return HttpResponse(pdf, content_type='application/pdf')