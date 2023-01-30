menu_options = {
    1: 'Gestion des tournois',
    2: 'Gestion des tours',
    3: 'Gestion des joueurs',
    4: 'Gestion des matchs',
    5: 'Quitter'
}

class Menu:
    def __init__(self,menu):
        """Init the menu"""
        self.menu = menu

    def print_menu(self):
        for key in menu_options.keys():
            print(key, '--', menu_options[key])

    def gestion_tournois(self):
         print('Handle option \'Gestion des tournois\'')

    def gestion_tours(self):
         print('Handle option \'Gestion des tours\'')

    def gestion_joueurs(self):
         print('Handle option \'Gestion des joueurs\'')

    def gestion_match(self):
        print('Handle option \'Gestion des matchs\'')

    if __name__=='__main__':
        while(True):
            print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            #Check what choice was entered and act accordingly
            if option == 1:
               gestion_tournois()
            elif option == 2:
                gestion_tours()
            elif option == 3:
                gestion_joueurs()
            elif option == 4:
                gestion_match()
            elif option == 5:
                print('Thanks message before exiting')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 5.')

