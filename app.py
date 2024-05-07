import os 
from flask import Flask, jsonify, request
from models import db, Book, Member, Transaction
from datetime import datetime
from flask_migrate import Migrate
from flask_cors import CORS



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# getting all books

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books])

#getting each book by id

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        # Return a  404 error if the book is not found
        return jsonify({'error': 'Book not found'}),  404
    else:
        # Return the book details if the book is found
        return jsonify(book.serialize())
    

#gettting a book by  its title
@app.route('/books/title', methods=['GET'])
def get_book_by_title():
    title = request.args.get('title')
    if not title:
        return jsonify({'error': 'Book title is required'}),   400
    
    book = Book.query.filter_by(title=title).first()
    
    if not book:
        return jsonify({'error': 'Book not found'}),   404
    else:
        return jsonify(book.serialize())



    
#getting a book by author 
@app.route('/books/author', methods=['GET'])
def get_books_by_author():
    author = request.args.get('author')
    if not author:
        return jsonify({'error': 'Author name is required'}),   400
    
    books = Book.query.filter_by(author=author).all()
    
    if not books:
        return jsonify({'error': 'No books found by the given author'}),   404
    else:
        return jsonify([book.serialize() for book in books])


#adding new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    
    # Create a new book object
    new_book = Book(title=data['title'], author=data['author'], stock=data['stock'])
    
    # Add the new book to the database
    db.session.add(new_book)
    db.session.commit()
    
    # Return a response indicating the book was added successfully
    return jsonify({'message': 'New book added successfully'}),  201

#making partial updates to  a book
@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}),  404
    data = request.get_json()
    for key, value in data.items():
        setattr(book, key, value)
    db.session.commit()
    return jsonify(book.to_dict())

#upadting a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def updating_a_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}),  404
    
    data = request.get_json()
    # Assuming the data includes all necessary fields for a book
    book.title = data['title']
    book.author = data['author']
    book.stock = data['stock']
    
    db.session.commit()
    return jsonify(book.to_dict()),  200


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}),  404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'result': 'Book deleted successfully!'})

#issuing a book
@app.route('/issue_book', methods=['POST'])
def issue_book():
    member_id = request.form.get('member_id')
    book_id = request.form.get('book_id')
    
    if not member_id or not book_id:
        return jsonify({"error": "Missing member_id or book_id"}),  400
    
    # Check if the book is available
    book = Book.query.get(book_id)
    if book and book.stock >  0:
        # Issue the book
        book.stock -=  1
        transaction = Transaction(member_id=member_id, book_id=book_id, date_issued=datetime.datetime.now())
        db.session.add(transaction)
        db.session.commit()
        return jsonify({"message": "Book issued successfully"}),  201
    else:
        return jsonify({"error": "Book not available"}),  400

#returning a book
@app.route('/return_book', methods=['PUT'])
def return_book():
    data = request.json
    transaction_id = data.get('transaction_id')
    
    # Find the transaction
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        # Update the transaction
        transaction.date_returned = datetime.datetime.now()
        db.session.commit()
        return jsonify({"message": "Book returned successfully"}),  200
    else:
        return jsonify({"error": "Transaction not found"}),  404
    
    
# getting all members
@app.route('/members', methods = ['GET'])
def get_memebers():
   members= Member.query.all()
   return jsonify([member.to_dict() for member in members])


# Getting a member by ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({'error': 'Member not found'}),   404
    
    return jsonify(member.to_dict()),   200
    


# adding new member
@app.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    new_member = Member(username=data['username'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify(new_member.to_dict()),   201


#  making partial updates to a member
@app.route('/members/<int:member_id>', methods=['PATCH'])
def update_member(member_id):
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({'error!': 'Member not found!!!!'}),  404
    data = request.get_json()
    for key, value in data.items():
        setattr(member, key, value)
    db.session.commit()
    return jsonify (member . to_dict())


#updating a member 
@app.route('/members/<int:member_id>', methods=['PUT'])
def updating_a_member(member_id):
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({'error': 'Member not found'}),  404
    
    data = request.get_json()
    # Assuming the data includes all necessary fields for a member
    member.name = data['name']
    member.email = data['email']
    member.username = data['username']
    # Add other fields as necessary
    
    db.session.commit()
    return jsonify(member.to_dict()),  200


# deleting a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({'error': 'Member not found'}),  404
    db.session.delete(member)
    db.session.commit()
    return jsonify({'result': 'Member deleted successfully!!'})

#getting transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions])


# getting transactions ofa member
@app.route('/transactions/<int:member_id>', methods=['GET'])
def get_transactions_by_member(member_id):
    transactions = Transaction.query.filter_by(member_id=member_id).all()
    return jsonify([transaction.to_dict() for transaction in transactions])

#creating new transactions
@app.route('/transactions', methods=['POST'])
def create_transaction():
    member_id = request.json.get('member_id')
    book_id = request.json.get('book_id')
    date_issued = datetime.now()  
    rentfee = request.json.get('rentfee')

    new_transaction = Transaction(member_id=member_id, book_id=book_id, date_issued=date_issued, rentfee=rentfee)
    db.session.add(new_transaction)
    db.session.commit()

    return jsonify(new_transaction.to_dict()),   201


#updating transaction on return date of a abook
@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction_return_date(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        transaction.date_returned = datetime.now()  # Corrected usage
        db.session.commit()
        return jsonify(transaction.to_dict()),   200
    else:
        return jsonify({"error": "Transaction not found"}),   404

    
#calculating total debt of a member
@app.route('/members/<int:member_id>/debt', methods=['GET'])
def get_member_debt(member_id):
    total_debt = db.session.query(db.func.sum(Transaction.rentfee)).filter(Transaction.member_id == member_id, Transaction.date_returned.isnot(None)).scalar()
    if total_debt is None:
        total_debt =  0.0
    return jsonify({"total_debt": total_debt})


#getting total fee of all transactions
@app.route('/total_fee', methods=['GET'])
def get_total_fee():
    total_fee = db.session.query(db.func.sum(Transaction.rentfee)).scalar()
    if total_fee is None:
        total_fee =  0.0
    return jsonify({"total_fee": total_fee})    

if __name__ == '__main__':
  app.run(port= 5000, debug=True)