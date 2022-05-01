from src.books.models import Book
from src.books.schema import BookOut

from ninja import Router

router = Router()


@router.get("/", response=list[BookOut])
def get_books(request):
    return Book.objects.all()
