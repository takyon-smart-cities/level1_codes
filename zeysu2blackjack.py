import random
class players:
    def __init__(self,bet=50.00):
        self.hand=[]
        self.bet=bet
    def hit(self):
        indx=random.randrange(0,len(deck))
        self.hand.append(deck[indx])
        del deck[indx]
class dealers:
    def __init__(self):
        self.hand=[]
    def hit(self):
        indx=random.randrange(0,len(deck))
        self.hand.append(deck[indx])
        del deck[indx]
        
class cards:
    def __init__(self,value,name):
        self.value=value
        self.name=name
    def __repr__(self):
        return "{}".format(self.name)
ace=cards(0,"ace")
two=cards(2,"two")
three=cards(3,"three")
four=cards(4,"four")
five=cards(5,"five")
six=cards(6,"six")
seven=cards(7,"seven")
eight=cards(8,"eight")
nine=cards(9,"nine")
ten=cards(10,"ten")
vale=cards(10,"jack")
queen=cards(10,"queen")
king=cards(10,"king")
deck=[ace,two,three,four,five,six,seven,eight,nine,ten,vale,queen,king]*4
def main():
    bet=float(input("Place your bet: "))
    player=players(bet)
    dealer=dealers()
    player.hit()
    player.hit()
    dealer.hit()
    dealer.hit()
    print("Your initial cards: {}".format(player.hand))
    print("Dealer's face-up card: [{}]".format(dealer.hand[0]))
    if ace in dealer.hand:
        summd=sum(card.value for card in dealer.hand)
        if summd+11<=21:
            finalsumd=summd+11
        else:
            finalsumd=summd+1
    if ace not in dealer.hand:
        finalsumd=sum(card.value for card in dealer.hand)
    if ace in player.hand:
        summp=sum(card.value for card in player.hand)
        if summp+11<=21:
            finalsump=summp+11
        else:
            finalsump=summp+1
    if ace not in player.hand:
        finalsump=sum(card.value for card in player.hand)
    if finalsump==21:
        if finalsumd==21:
            print("Push!")
            print("Your initial bet: €{}".format(player.bet))
            print("Your final money: €{}".format(player.bet))
        else:
            money=2.5*player.bet
            print("Blackjack!")
            print("Your initial bet: €{}".format(player.bet))
            print("Your final money: €{}".format(money))
    if finalsump>21:
        print("Busted! You lose!")
        print("Your initial bet: €{}".format(player.bet))
        print("Your final money: €0.00")
    if finalsump<21:
        if finalsumd>21:
            money=2*player.bet
            print("You win!")
            print("Your initial bet: €{}".format(player.bet))
            print("Your final money: €{}".format(money))
        if finalsumd==21:
            print("Dealer got blackjack! You lose!")
            print("Your initial bet: €{}".format(player.bet))
            print("Your final money: €0.00")
        if finalsumd<21:
                  while finalsumd<17:
                      dealer.hit()
                      if ace in dealer.hand:
                          summd=sum(card.value for card in dealer.hand)
                          if summd+11<=21:
                              finalsumd=summd+11
                          else:
                              finalsumd=summd+1
                      if ace not in dealer.hand:
                          finalsumd=sum(card.value for card in dealer.hand)
                      if finalsumd>=17:
                          break
                  while finalsump<21:
                      answer=input("Hit or Stand? ")
                      if answer=="Hit":
                          player.hit()
                      if answer=="Stand":
                          break
                      print("Your current cards: {}".format(player.hand))
                      if ace in player.hand:
                          summp=sum(card.value for card in player.hand)
                          if summp+11<=21:
                              finalsump=summp+11
                          else:
                              finalsump=summp+1
                      if ace not in player.hand:
                          finalsump=sum(card.value for card in player.hand)
                  if finalsump>21:
                      print("Busted! You lose!")
                      print("Your initial bet: €{}".format(player.bet))
                      print("Your final money: €0.00")
                  if finalsump==21:
                      if finalsumd!=21:
                          money=2*player.bet
                          print("You win!")
                          print("Your initial bet: €{}".format(player.bet))
                          print("Your final money: €{}".format(money))
                      if finalsumd==21:
                          print("Tie!")
                          print("Your initial bet: €{}".format(player.bet))
                          print("Your final money: €{}".format(player.bet))
                  if finalsump<21:
                      if finalsump>finalsumd:
                          money=2*player.bet
                          print("You win!")
                          print("Your initial bet: €{}".format(player.bet))
                          print("Your final money: €{}".format(money))
                      if finalsump==finalsumd:
                          print("Tie!")
                          print("Your initial bet: €{}".format(player.bet))
                          print("Your final money: €{}".format(player.bet))
                      if finalsump<finalsumd:
                          if finalsumd>21:
                              money=2*player.bet
                              print("You win!")
                              print("Your initial bet: €{}".format(player.bet))
                              print("Your final money: €{}".format(money))
                          if finalsumd<=21:
                              print("You lose!")
                              print("Your initial bet: €{}".format(player.bet))
                              print("Your final money: €0.00")
    
        
        
    
            
    
        
if __name__=="__main__":
    main()
    
    



