# взаимодействие между processor и view

import processor
import view


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                processor.open_file()
            case 2:
                processor.save_file()
            case 3:
                
                view.show_contacts(processor.get_contacts())
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
                break

    