from services.library_service import LibraryService
from services.report import (report_available, report_borrowed,
    report_user_history)
from utils.display import print_header, print_book_list, print_user_info
from utils.error_handler import safe_int