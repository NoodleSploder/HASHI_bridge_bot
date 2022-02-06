from tg.notice_sender import send_message
from db.crud import session
from db.db_connect import User
import telegram


if __name__ == '__main__':
    users = session.query(User).filter(User.id > 393).all()
    sended = 0
    deleted = 0
    for user in users:
        try:
            send_message(user.tg_id, text)
            sended += 1
        except (Exception, telegram.error.Unauthorized, telegram.error.BadRequest):
            session.delete(user)
            session.commit()
            deleted += 1
        print(f'sended: {sended}, deleted: {deleted}, last: {user.id}')