#!/usr/bin/env python2

import signal
import webbrowser
from stat_checker import StatChecker
from state import State

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from gi.repository import GObject as gobject

SERVER_ADDRESS = "http://buildbot.buildbot.net"
BUILDERS = ["py26-tw0900", "py26-tw1020", "py26-tw1110"]
BRANCH = "master"
NOTIFY_ON_STATUS_CHANGE = True
CHECK_INTERVAL_S = 60


APPINDICATOR_ID = 'buildbot-indicator'


def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID,
                                           gtk.STOCK_YES,
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()


def build_menu():
    menu = gtk.Menu()
    item_branch_name = gtk.MenuItem(BRANCH)
    item_branch_name.set_sensitive(False)
    menu.append(item_branch_name)
    menu.append(gtk.SeparatorMenuItem())
    item_open_buildbot = gtk.MenuItem('open buildbot')
    item_open_buildbot.connect('activate', open_buildbot)
    menu.append(item_open_buildbot)
    item_quit = gtk.MenuItem('quit')
    item_quit.connect('activate', terminate)
    menu.append(item_quit)
    menu.show_all()
    return menu


def open_buildbot(_):
    webbrowser.open_new(SERVER_ADDRESS)


def terminate(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    notify.init(APPINDICATOR_ID)
    checker = StatChecker(SERVER_ADDRESS, BUILDERS, BRANCH)
    state = State(checker)
    gobject.timeout_add(1000*CHECK_INTERVAL_S, notify.Notification.new("notif", "notif").show)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()