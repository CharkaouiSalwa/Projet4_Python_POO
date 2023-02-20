from views.menuView import menu_principal
from controllers.matchController import matchController

def main():
    #menu_principal()
    m = matchController()
    print(m.creer_matchs("test","saad"))

if __name__ == "__main__":
    main()
