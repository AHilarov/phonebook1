# взаимодействие между processor и view

import processor
import view

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pass
            case 2:
                pass
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
    return