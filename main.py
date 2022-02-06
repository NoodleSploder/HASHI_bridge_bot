import multiprocessing
from src.gasprice.gasPrice import gp_updater
import time
from src.tg.interface import interface
from src.tg.notice_sender import notice_sender
from src.db.db_connect import Base, engine

def main():
    with multiprocessing.Manager() as manager:
        gp_data = manager.dict()
        eth_price = manager.Namespace()
        eth_price.data = 0

        gp_updater_process = multiprocessing.Process(target=gp_updater, args=(gp_data, eth_price))
        interface_process = multiprocessing.Process(target=interface, args=(gp_data, eth_price))
        notice_sender_process = multiprocessing.Process(target=notice_sender, args=(gp_data,))

        print('Creating Database...')
        Base.metadata.create_all(engine)

        gp_updater_process.start()
        print('gp updater started')

        interface_process.start()
        print('interface started')

        while not gp_data:
            print('wait for first gp update...')
            time.sleep(5)

        notice_sender_process.start()
        print('notice sender started')

        gp_updater_process.join()
        interface_process.join()
        notice_sender_process.join()
        print('done')
if __name__ == '__main__':
    main()