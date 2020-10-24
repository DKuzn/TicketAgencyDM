import sys
from PyQt5 import QtWidgets
from sql_utils import *
import mainwindow


class TicketAgencyApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyApp, self).__init__()
        self.setupUi(self)
        self.payButton.clicked.connect(self.pay_button_clicked)
        self.addToOrderButton.clicked.connect(self.add_to_order_button_clicked)
        self.formTicketsButton.clicked.connect(self.form_ticket_button_clicked)
        self.eventSiteChoice.addItems(event_sites_list())
        self.eventSiteChoice.activated.connect(self.event_site_choose)

    def pay_button_clicked(self):
        pass

    def add_to_order_button_clicked(self):
        pass

    def form_ticket_button_clicked(self):
        pass

    def event_site_choose(self):
        self.eventChoice.clear()
        self.eventChoice.addItems(events_list(self.eventSiteChoice.currentText()))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TicketAgencyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
