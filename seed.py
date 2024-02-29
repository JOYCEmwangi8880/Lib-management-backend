from app import app, db 
from models import Book, Member, Transaction
import datetime


def seed_data():
    with app.app_context():
        db.session.query(Book).delete()
        db.session.query(Member).delete()
        db.session.query(Transaction).delete()
        db.session.commit()


        books = [
                Book(title="The Great Gatsby", author="F. Scott Fitzgerald", stock=5, description="A novel depicting the lavish and decadent lifestyle of the wealthy during the Jazz Age."),
                Book(title="To Kill a Mockingbird", author="Harper Lee", stock=3, description="A powerful story addressing racial injustice and moral growth in the American South."),
                Book(title="1984", author="George Orwell", stock=1, description="A dystopian novel exploring themes of totalitarianism, surveillance, and propaganda."),
                Book(title="The Catcher in the Rye", author="J.D. Salinger", stock=4, description="A coming-of-age novel following the disillusioned teenager Holden Caulfield."),
                Book(title="The Odyssey", author="Homer", stock=2, description="An epic poem chronicling the adventures of the Greek hero Odysseus."),
                Book(title="Pride and Prejudice", author="Jane Austen", stock=6, description="A romantic novel set in early 19th-century England, focusing on the dynamics of class and marriage."),
                Book(title="The Hobbit", author="J.R.R. Tolkien", stock=7, description="A fantasy adventure novel featuring the hobbit Bilbo Baggins and his quest to reclaim a treasure guarded by a dragon."),
                Book(title="The Lord of the Rings", author="J.R.R. Tolkien", stock=8, description="An epic fantasy trilogy chronicling the journey to destroy the One Ring and defeat the Dark Lord Sauron."),
                Book(title="The Little Prince", author="Antoine de Saint-Exupéry", stock=9, description="A philosophical children's book about a young prince who travels to different planets."),
                Book(title="The Alchemist", author="Paulo Coelho", stock=10, description="A novel about a young shepherd named Santiago who embarks on a journey to find his personal legend."),
                Book(title="Moby Dick", author="Herman Melville", stock=5, description="A tale of obsession and revenge as Captain Ahab pursues the white whale, Moby Dick."),
                Book(title="War and Peace", author="Leo Tolstoy", stock=3, description="An epic novel set against the backdrop of Napoleon's invasion of Russia, exploring themes of love, war, and society."),
                Book(title="The Brothers Karamazov", author="Fyodor Dostoevsky", stock=1, description="A philosophical novel examining faith, morality, and the existence of God through the lives of the Karamazov brothers."),
                Book(title="One Hundred Years of Solitude", author="Gabriel García Márquez", stock=4, description="A magical realist novel chronicling the Buendía family across seven generations in the fictional town of Macondo."),
                Book(title="The Picture of Dorian Gray", author="Oscar Wilde", stock=2, description="A philosophical novel exploring the nature of beauty, morality, and the pursuit of pleasure."),
                Book(title="Brave New World", author="Aldous Huxley", stock=6, description="A dystopian novel set in a futuristic society where humans are engineered and conditioned for a predetermined social order."),
                Book(title="The Grapes of Wrath", author="John Steinbeck", stock=7, description="A novel depicting the hardships of Dust Bowl-era farmers as they migrate to California in search of a better life."),
                Book(title="Crime and Punishment", author="Fyodor Dostoevsky", stock=8, description="A psychological thriller following the moral and mental struggles of the impoverished student Raskolnikov."),
                Book(title="Frankenstein", author="Mary Shelley", stock=9, description="A gothic novel exploring themes of creation, ambition, and the consequences of playing god."),
                Book(title="The Canterbury Tales", author="Geoffrey Chaucer", stock=10, description="A collection of stories told by a group of pilgrims traveling to Canterbury Cathedral, offering a snapshot of medieval English society.")
]



        members = [
                Member(username="Alice Smith", email="alice.smith@example.com", debt=0.0),
                Member(username="Bob Johnson", email="bob.johnson@example.com", debt=0.0),
                Member(username="Charlie Brown", email="charlie.brown@example.com", debt=0.0),
                Member(username="Diana Prince", email="diana.prince@example.com", debt=0.0),
                Member(username="Eve Adams", email="eve.adams@example.com", debt=0.0),
                Member(username="Frank Miller", email="frank.miller@example.com", debt=0.0),
                Member(username="Grace Hopper", email="grace.hopper@example.com", debt=0.0),
                Member(username="Henry Ford", email="henry.ford@example.com", debt=0.0),
                Member(username="Isaac Newton", email="isaac.newton@example.com", debt=0.0),
                Member(username="Jackie Chan", email="jackie.chan@example.com", debt=0.0),
                Member(username="Luna Lovegood", email="luna.lovegood@example.com", debt=0.0),
                Member(username="Neville Longbottom", email="neville.longbottom@example.com", debt=0.0),
                Member(username="Hermione Granger", email="hermione.granger@example.com", debt=0.0),
                Member(username="Ron Weasley", email="ron.weasley@example.com", debt=0.0),
                Member(username="Severus Snape", email="severus.snape@example.com", debt=0.0),
                Member(username="Albus Dumbledore", email="albus.dumbledore@example.com", debt=0.0),
                Member(username="Sirius Black", email="sirius.black@example.com", debt=0.0),
                Member(username="Remus Lupin", email="remus.lupin@example.com", debt=0.0),
                Member(username="Rubeus Hagrid", email="rubeus.hagrid@example.com", debt=0.0),
                Member(username="Minerva McGonagall", email="minerva.mcgonagall@example.com", debt=0.0)
]

        for member in members:
                db.session.add(member)
        db.session.commit()


        for book in books:
                db.session.add(book)
        db.session.commit()

        transactions = [
                Transaction(member_id=members[0].id, book_id=books[0].id, date_issued=datetime.datetime(2024, 4, 1), rentfee=5.0, date_returned=datetime.datetime(2024, 2, 13)),
                Transaction(member_id=members[1].id, book_id=books[1].id, date_issued=datetime.datetime(2024, 6, 12), rentfee=3.0, date_returned=datetime.datetime(2024, 4, 10)),
                Transaction(member_id=members[2].id, book_id=books[2].id, date_issued=datetime.datetime(2024, 7, 13), rentfee=1.0, date_returned=datetime.datetime(2024, 5, 23)),
                Transaction(member_id=members[3].id, book_id=books[3].id, date_issued=datetime.datetime(2024, 1, 24), rentfee=4.0, date_returned=datetime.datetime(2024, 7, 16)),
                Transaction(member_id=members[4].id, book_id=books[4].id, date_issued=datetime.datetime(2024, 1, 15), rentfee=2.0, date_returned=datetime.datetime(2024, 8, 19)),
                Transaction(member_id=members[5].id, book_id=books[5].id, date_issued=datetime.datetime(2024, 2, 16), rentfee=6.0, date_returned=datetime.datetime(2024, 5, 13)),
                Transaction(member_id=members[6].id, book_id=books[6].id, date_issued=datetime.datetime(2024, 9, 27), rentfee=7.0, date_returned=datetime.datetime(2024, 1, 18)),
                Transaction(member_id=members[7].id, book_id=books[7].id, date_issued=datetime.datetime(2024, 1, 28), rentfee=8.0, date_returned=datetime.datetime(2024, 2, 12)),
                Transaction(member_id=members[8].id, book_id=books[8].id, date_issued=datetime.datetime(2024, 6, 19), rentfee=9.0, date_returned=datetime.datetime(2024, 6, 11)),
                Transaction(member_id=members[9].id, book_id=books[9].id, date_issued=datetime.datetime(2024, 2, 10), rentfee=10.0, date_returned=datetime.datetime(2023, 3, 16)),
                Transaction(member_id=members[10].id, book_id=books[10].id, date_issued=datetime.datetime(2024, 3, 21), rentfee=5.0, date_returned=datetime.datetime(2024, 1, 9)),
                Transaction(member_id=members[11].id, book_id=books[11].id, date_issued=datetime.datetime(2024, 4, 15), rentfee=3.0, date_returned=datetime.datetime(2024, 2, 20)),
                Transaction(member_id=members[12].id, book_id=books[12].id, date_issued=datetime.datetime(2024, 5, 11), rentfee=1.0, date_returned=datetime.datetime(2024, 3, 28)),
                Transaction(member_id=members[13].id, book_id=books[13].id, date_issued=datetime.datetime(2024, 6, 8), rentfee=4.0, date_returned=datetime.datetime(2024, 4, 15)),
                Transaction(member_id=members[14].id, book_id=books[14].id, date_issued=datetime.datetime(2024, 7, 4), rentfee=2.0, date_returned=datetime.datetime(2024, 5, 12)),
                Transaction(member_id=members[15].id, book_id=books[15].id, date_issued=datetime.datetime(2024, 8, 1), rentfee=6.0, date_returned=datetime.datetime(2024, 6, 8)),
                Transaction(member_id=members[16].id, book_id=books[16].id, date_issued=datetime.datetime(2024, 9, 3), rentfee=7.0, date_returned=datetime.datetime(2024, 7, 18)),
                Transaction(member_id=members[17].id, book_id=books[17].id, date_issued=datetime.datetime(2024, 10, 2), rentfee=8.0, date_returned=datetime.datetime(2024, 8, 20)),
                Transaction(member_id=members[18].id, book_id=books[18].id, date_issued=datetime.datetime(2024, 11, 15), rentfee=9.0, date_returned=datetime.datetime(2024, 9, 30)),
                Transaction(member_id=members[19].id, book_id=books[19].id, date_issued=datetime.datetime(2024, 12, 20), rentfee=10.0, date_returned=datetime.datetime(2024, 10, 10))
]


       
        
        
        for transaction in transactions:
            db.session.add(transaction)

        db.session.commit()
if __name__ == "__main__":
    seed_data()      