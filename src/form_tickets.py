# form_tickets.py
#
# Copyright 2020 Дмитрий Кузнецов
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import qrcode
import textwrap
from sql_utils import get_ticket_info_form
from PIL import Image, ImageDraw, ImageFont


def get_qrcode(text: str):
    img = qrcode.make(text)
    img = img.get_image()
    img = img.resize((600, 600))
    return img


def form_ticket_info(ticket: int):
    info = get_ticket_info_form(ticket)
    header = 'Тип: Название: Площадка: Дата: Время: Ряд: Место: Цена: Клиент:'.split(' ')
    to_info = ['\n'.join(('Билетное агентство "Кузница"', 'Номер билета: ' + str(ticket)))]
    for i, inf in enumerate(info):
        row = ''.join((header[i], ' ', str(inf)))
        row = textwrap.wrap(row, width=26)
        to_info += row
    formed_info = '\n'.join(to_info)
    return formed_info


def get_a4(tickets: list):
    template = Image.open('../resources/ticket_template.png').convert('RGB')
    images = []
    backs = []
    font = ImageFont.truetype('../resources/Montserrat-SemiBold.ttf', size=36)
    for i in tickets:
        info = form_ticket_info(int(i))
        qr_code = get_qrcode(info)
        img = Image.new('RGB', (1600, 800), color=(255, 255, 255))
        img.paste(template, (0, 0))
        img.paste(qr_code, (900, 100))
        draw = ImageDraw.Draw(img)
        draw.text((200, 150), text=info, font=font, fill=(0, 0, 0))
        images.append(img)
    background1 = Image.new('RGB', (3508, 2480), color=(255, 255, 255))
    backs.append(background1)
    background2 = Image.new('RGB', (3508, 2480), color=(255, 255, 255))
    backs.append(background2)
    qr = 0
    for i in range(2):
        for y in range(20, background1.size[1] - 800, 820):
            for x in range(20, background1.size[0] - 800, 1620):
                if qr < len(images) and qr < 6:
                    backs[0].paste(images[qr], (x, y))
                    qr += 1
                elif qr < len(images):
                    backs[1].paste(images[qr], (x, y))
                    qr += 1
    return backs


if __name__ == '__main__':
    back = get_a4(['97', '98', '99'])
    back[0].show()
