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
from sql_utils import get_ticket_info
from PIL import Image


def get_qrcode(text: str):
    img = qrcode.make(text)
    img = img.get_image()
    img = img.resize((800, 800))
    return img


def form_ticket_info(ticket: int):
    info = get_ticket_info(ticket)
    header = 'Тип: Название: Площадка: Дата: Время: Ряд: Место: Цена:'.split(' ')
    to_info = ['Билетное агенство "Кузница"\n', 'Номер билета: ' + str(ticket) + '\n']
    for i, inf in enumerate(info):
        row = [header[i], ' ', str(inf), '\n']
        to_info += row
    formed_info = ''.join(to_info)
    return formed_info


def get_a4(tickets: list):
    qr_codes = []
    for i in tickets:
        img = get_qrcode(form_ticket_info(int(i)))
        qr_codes.append(img)
    background = Image.new('L', (2480, 3508), color=255)
    qr = 0
    for y in range(0, background.size[1] - 800, 800):
        for x in range(0, background.size[0] - 800, 800):
            if qr < len(qr_codes):
                background.paste(qr_codes[qr], (x, y))
                qr += 1

    return background


if __name__ == '__main__':
    back = get_a4(['10010001', '10010002', '10010003', '10010004'])
    back.show()
