from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

engine = create_engine('sqlite:///todo.db?check_same_thread = False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='NULL')
    deadline = Column(Date, default=datetime.today())
    menu = ["1) Today's tasks", "2) Week's tasks", "3) All tasks", "4) Missed tasks", "5) Add task", "6) Delete task", "0) Exit"]

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user_input = None

while user_input != 0:
    today = datetime.today().date()
    for item in Table.menu:
        print(item)
    user_input = int(input())
    if user_input == 1:
        print(f'Today {today.day} {today.strftime("%b")}:')
        rows = session.query(Table).filter(Table.deadline == today).all()
        if not rows:
            print("Nothing to do!")
        else:
            for i, row in enumerate(rows):
                print(f'{i+1}. {row.task}')
        print()
    elif user_input == 2:
        for daydiff in range(7):
            queryday = today + timedelta(days=daydiff)
            print(f'{weekday[queryday.weekday()]} {queryday.day} {queryday.strftime("%b")}')
            rows = session.query(Table).filter(Table.deadline == queryday).all()
            if not rows:
                print("Nothing to do!")
            else:
                for i, row in enumerate(rows):
                    print(f'{i+1}. {row.task}. {row.deadline}')
            print()
        print()
    elif user_input == 3:
        print('All tasks:')
        rows = session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to do!")
        else:
            for i, row in enumerate(rows):
                print(f'{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime("%b")}')
        print()
    elif user_input == 4:
        print('Missed tasks:')
        rows = session.query(Table).filter(Table.deadline < today).order_by(Table.deadline).all()
        if not rows:
            print("Nothing is missed!")
        else:
            for i, row in enumerate(rows):
                print(f'{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime("%b")}')
        print()
    elif user_input == 5:
        task_name = input('Enter task\n')
        task_deadline = input('Enter deadline\n')
        new_row = Table(task=task_name, deadline=datetime.strptime(task_deadline, '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print('The task has been added!')
        print()
    elif user_input == 6:
        print('Chose the number of the task you want to delete:')
        rows = session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to delete!")
        else:
            for i, row in enumerate(rows):
                print(f'{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime("%b")}')
            rowid = int(input()) - 1
            specificrow = rows[rowid]
            session.delete(specificrow)
            session.commit()
            print('The task has been deleted!')
        print()
    elif user_input == 0:
        print('Bye!')
