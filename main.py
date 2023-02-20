from views.menuView import menu_principal
from controllers.matchController import matchController

def main():
    #menu_principal()
    m = matchController()
    print(m.match_winner("tournoi","Round 1","AA0001","AA0002","AA0001"))

if __name__ == "__main__":
    main()
