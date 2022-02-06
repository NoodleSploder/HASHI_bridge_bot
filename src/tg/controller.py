import src.tg.texts as texts
from src.tg import utilities
import src.db.crud as crud
from src.tg.keyboards import create_user_notices_keyboard


class Controller:
    def __init__(self, gp_data, eth_price):
        self.gp_data = gp_data
        self.eth_price = eth_price

    def eth(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.eth.format(eth_price.data, gp['fast'], round(((gp['fast'] * 26058)/1000000000)*eth_price.data, 1), round(((gp['fast'] * 98345)/1000000000)*eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 26058)/1000000000)*eth_price.data, 1), round(((gp['average'] * 98345)/1000000000)*eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 26058)/1000000000)*eth_price.data, 1),  round(((gp['slow'] * 98345)/1000000000)*eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def dai(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.dai.format(eth_price.data, gp['fast'], round(((gp['fast'] * 54852) / 1000000000) * eth_price.data, 1), round(((gp['fast'] * 119542) / 1000000000) * eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 54852) / 1000000000) * eth_price.data, 1), round(((gp['average'] * 119542) / 1000000000) * eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 54852) / 1000000000) * eth_price.data, 1), round(((gp['slow'] * 119542) / 1000000000) * eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def xor(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.xor.format(eth_price.data, gp['fast'], round(((gp['fast'] * 52229) / 1000000000) * eth_price.data, 1), round(((gp['fast'] * 108806 ) / 1000000000) * eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 52229) / 1000000000) * eth_price.data, 1), round(((gp['average'] * 108806 ) / 1000000000) * eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 52229) / 1000000000) * eth_price.data, 1), round(((gp['slow'] * 108806 ) / 1000000000) * eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def val(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.val.format(eth_price.data, gp['fast'], round(((gp['fast'] * 50093) / 1000000000) * eth_price.data, 1), round(((gp['fast'] * 125070) / 1000000000) * eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 50093) / 1000000000) * eth_price.data, 1), round(((gp['average'] * 125070) / 1000000000) * eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 50093) / 1000000000) * eth_price.data, 1), round(((gp['slow'] * 125070) / 1000000000) * eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def ceres(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.ceres.format(eth_price.data, gp['fast'], round(((gp['fast'] * 48227) / 1000000000) * eth_price.data, 1), round(((gp['fast'] * 122819) / 1000000000) * eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 48227) / 1000000000) * eth_price.data, 1), round(((gp['average'] * 122819) / 1000000000) * eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 48227) / 1000000000) * eth_price.data, 1), round(((gp['slow'] * 122819) / 1000000000) * eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def pswap(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.pswap.format(eth_price.data, gp['fast'], round(((gp['fast'] * 48239) / 1000000000) * eth_price.data, 1), round(((gp['fast'] * 122521) / 1000000000) * eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 48239) / 1000000000) * eth_price.data, 1), round(((gp['average'] * 122521) / 1000000000) * eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 48239) / 1000000000) * eth_price.data, 1), round(((gp['slow'] * 122521) / 1000000000) * eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def usdc(self, update):
        gp = self.gp_data
        eth_price = self.eth_price
        text = texts.usdc.format(eth_price.data, gp['fast'], round(((gp['fast'] * 68239) / 1000000000) * eth_price.data, 1), round(((gp['fast'] * 130568) / 1000000000) * eth_price.data, 1),
                               gp['average'], round(((gp['average'] * 68239) / 1000000000) * eth_price.data, 1), round(((gp['average'] * 130568) / 1000000000) * eth_price.data, 1),
                               gp['slow'], round(((gp['slow'] * 68239) / 1000000000) * eth_price.data, 1), round(((gp['slow'] * 130568) / 1000000000) * eth_price.data, 1))

        tg_id = update.effective_chat.id
        if not crud.is_user_exists(tg_id):
            crud.create_user(tg_id)
        crud.create_interaction(tg_id)
        return text

    def create_notice(self, tg_id, gp, gp_type):
        if utilities.is_float(gp):
            gp = float(gp)
            gp_now = self.gp_data[gp_type]
            if not crud.is_user_exists(tg_id):
                crud.create_user(tg_id)
            if gp + 4.9 >= gp_now:
                return False, 'Notice price is either above or too close to current gas price.'
            elif crud.is_user_has_close_notices(tg_id, gp, gp_type):
                return False, 'You already have a similar notice.'
            else:
                crud.create_notice(tg_id, gp, gp_type)
                return True, 'Success.'
        else:
            return False, f'Error. Type the gwei amount after the tx speed to create a notice. \nExample: "/{gp_type} 50".'

    def create_notice_by_command(self, update, gp_type: str):
        try:
            tg_id, gp = update.effective_chat.id, update.message.text.split(' ')[1]
            is_created, text = self.create_notice(tg_id, gp, gp_type)
            return text
        except:
            return f'Error. Type the gwei amount after the tx speed to create a notice. \nExample: "/{gp_type} 50".'

    def create_notice_by_keyboard(self, update, gp_type: str):
        tg_id, gp = update.effective_chat.id, update.message.text
        is_created, text = self.create_notice(tg_id, gp, gp_type)
        if is_created:
            return is_created, text
        else:
            text += '\nEnter desired gas price:'
            return is_created, text

    def get_notices(self, update):
        tg_id = update.effective_chat.id
        notices = crud.get_user_notices(tg_id)
        keyboard = create_user_notices_keyboard(notices)
        return 'Your notices:', keyboard

    def update_notices_list(self, update):
        tg_id, notice_to_delite = update.effective_chat.id, update.callback_query.data
        crud.delete_notice(notice_to_delite)
        notices = crud.get_user_notices(tg_id)
        keyboard = create_user_notices_keyboard(notices)
        return 'Notice deleted', keyboard
