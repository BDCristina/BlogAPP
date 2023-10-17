class Pagination:
    
    def __init__(self, page_number, last_page):
        self.limit = 5
        self.first_page = page_number
        self.last_page = last_page
