[
  {
    "name": "Test: Get all books",
    "request": {
      "url": "http://localhost:5000/books",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get book by ID (valid)",
    "request": {
      "url": "http://localhost:5000/books/1",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get book by ID (invalid)",
    "request": {
      "url": "http://localhost:5000/books/1000",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get book by title (valid)",
    "request": {
      "url": "http://localhost:5000/books/title?title=The+Great+Gatsby",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get book by title (invalid)",
    "request": {
      "url": "http://localhost:5000/books/title",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get books by author (valid)",
    "request": {
      "url": "http://localhost:5000/books/author?author=F.+Scott+Fitzgerald",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get books by author (invalid)",
    "request": {
      "url": "http://localhost:5000/books/author",
      "method": "GET"
    }
  },
  {
    "name": "Test: Create new book",
    "request": {
      "url": "http://localhost:5000/books",
      "method": "POST",
      "body": "{\"title\": \"To Kill a Mockingbird\", \"author\": \"Harper Lee\", \"stock\": 10}",
      "headers": {
        "Content-Type": "application/json"
      }
    }
  },
  {
    "name": "Test: Update book",
    "request": {
      "url": "http://localhost:5000/books/1",
      "method": "PUT",
      "body": "{\"title\": \"1984\", \"author\": \"George Orwell\", \"stock\": 20}",
      "headers": {
        "Content-Type": "application/json"
      }
    }
  },
  {
    "name": "Test: Partial update to a book",
    "request": {
      "url": "http://localhost:5000/books/1",
      "method": "PATCH",
      "body": "{\"stock\": 30}",
      "headers": {
        "Content-Type": "application/json"
      }
    }
  },
  {
    "name": "Test: Delete book",
    "request": {
      "url": "http://localhost:5000/books/1",
      "method": "DELETE"
    }
  },
  {
    "name": "Test: Issue book",
    "request": {
      "url": "http://localhost:5000/issue_book",
      "method": "POST",
      "body": {
        "member_id": 1,
        "book_id": 1
      }
    }
  },
  {
    "name": "Test: Return book",
    "request": {
      "url": "http://localhost:5000/return_book",
      "method": "PUT",
      "body": {
        "transaction_id": 1
      }
    }
  },
  {
    "name": "Test: Get all members",
    "request": {
      "url": "http://localhost:5000/members",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get member by ID (valid)",
    "request": {
      "url": "http://localhost:5000/members/1",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get member by ID (invalid)",
    "request": {
      "url": "http://localhost:5000/members/1000",
      "method": "GET"
    }
  },
  {
    "name": "Test: Create new member",
    "request": {
      "url": "http://localhost:5000/members",
      "method": "POST",
      "body": "{\"username\": \"JohnDoe\", \"email\": \"john@example.com\"}",
      "headers": {
        "Content-Type": "application/json"
      }
    }
  },
  {
    "name": "Test: Update member",
    "request": {
      "url": "http://localhost:5000/members/1",
      "method": "PUT",
      "body": "{\"username\": \"JaneDoe\", \"email\": \"jane@example.com\"}",
      "headers": {
        "Content-Type": "application/json"
      }
    }
  },
  {
    "name": "Test: Delete member",
    "request": {
      "url": "http://localhost:5000/members/1",
      "method": "DELETE"
    }
  },
  {
    "name": "Test: Get transactions",
    "request": {
      "url": "http://localhost:5000/transactions",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get transactions by member",
    "request": {
      "url": "http://localhost:5000/transactions/1",
      "method": "GET"
    }
  },
  {
    "name": "Test: Create new transaction",
    "request": {
      "url": "http://localhost:5000/transactions",
      "method": "POST",
      "body": {
        "member_id": 1,
        "book_id": 1,
        "rentfee": 10
      }
    }
  },
  {
    "name": "Test: Update transaction return date",
    "request": {
      "url": "http://localhost:5000/transactions/1",
      "method": "PUT",
      "body": {
        "date_returned": "2024-03-25T12:00:00Z"
      }
    }
  },
  {
    "name": "Test: Get member debt",
    "request": {
      "url": "http://localhost:5000/members/1/debt",
      "method": "GET"
    }
  },
  {
    "name": "Test: Get total fee",
    "request": {
      "url": "http://localhost:5000/total_fee",
      "method": "GET"
    }
  }
]
