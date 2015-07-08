/*This is the javascript file for my memory games of stage 5 */


// initializing my variables
var CARDS = document.getElementsByClassName("card"); //all playable cards

var counter = 1; // clicks in a round, 

var card; // the card that has been clicked in this round

var card1 = ""; //card from 1st round
var card2 = ""; //card from 2st round
var pair1 = ""; //name of first card's pair
var pair2 = ""; //name of second card's pair

var score = 0;
var round = 0;

// main gameplay function - shows/hides the elements, and finds pairs
function isPair(cardNumber) { 
    if (!isWin()) {
        card = CARDS[cardNumber];
        if (counter == 1) { 
            closeCards()
            card.classList.add("show");
      	    card1 = card;
      	    pair1 = card1.id;
            counter +=1;
        } else if (counter == 2) {
            if (card == card1) {
                closeCards();
                round += 0.5;
            } else if (card != card1) {
                card.classList.add("show");
                card2 = card;
                pair2 = card2.id;
                if (pair1 == pair2) { 
                    card1.classList.remove("play"); 
                    card1.classList.add("win"); 
                    card2.classList.remove("play"); 
                    card2.classList.add("win");
                    closeCards();
                    score += 1;
                    if (!isWin()) { 
                        round += 1;
                        showMessage("happy")   
                    }          
                } else { 
                  showMessage("sad") 
                  round += 1;
                }
                counter = 1
            } 
        } 
    }
    console.log(score, round)
    document.getElementById("score").innerHTML = "Score: "+ score;
    document.getElementById("round").innerHTML = "Round: "+ round;
}


//function that closes all unpaired cards 
function closeCards() {
    if (card1) {
        card1.classList.remove("show");
        card1 = "";
    }
    if (card2) {
        card2.classList.remove("show");
        card2 = "";
    }
    counter = 1;

}

//function that checks if the player won
function isWin() {
    var winLength = document.getElementsByClassName("win").length;
    if (CARDS.length == winLength) {
        document.getElementsByClassName("congratulations")[0].classList.remove("hide");
        return true;
    }
    else {
      return false;
    }
}

// depending if the pair was found or not it displays a message for a few moments
function showMessage(message) {
    var timeDelay; //time duration of message depending on message to be displayed
    if (message == "happy") {
        timeDelay = 600;
    } else if (message == "sad"){
        timeDelay = 300;
    }
    messageBox = document.getElementsByClassName(message)[0]
    messageBox.classList.remove("hide");
    window.setTimeout("messageBox.classList.add('hide')", timeDelay ); 
}




 