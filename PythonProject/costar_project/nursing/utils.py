from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5


def generate_ticket_pdf(ticket):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A5)

    # Заголовок
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 750, "КИНОТЕАТР 'CINEMA'")

    # Данные билета
    p.setFont("Helvetica", 12)
    p.drawString(50, 700, f"Билет №: {ticket.id}")
    p.drawString(50, 680, f"Фильм: {ticket.session.title}")
    p.drawString(50, 660, f"Дата: {ticket.session.start_time.strftime('%d.%m.%Y %H:%M')}")
    p.drawString(50, 640, f"Место: {ticket.seat.number}")
    p.drawString(50, 620, f"Покупатель: {ticket.customer.last_name} {ticket.customer.first_name}")

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer