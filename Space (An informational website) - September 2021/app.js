function populate() {
    if(quiz.isEnded()) {
        showScores();
    }
    else {
        // show question
        var element = document.getElementById("question");
        element.innerHTML = quiz.getQuestionIndex().text;

        // show options
        var choices = quiz.getQuestionIndex().choices;
        for(var i = 0; i < choices.length; i++) {
            var element = document.getElementById("choice" + i);
            element.innerHTML = choices[i];
            guess("bt" + i, choices[i]);
        }

        showProgress();
    }
};

function guess(id, guess) {
    var button = document.getElementById(id);
    button.onclick = function() {
        quiz.guess(guess);
        populate();
    }
};


function showProgress() {
    var currentQuestionNumber = quiz.questionIndex + 1;
    var element = document.getElementById("progress");
    element.innerHTML = "Question " + currentQuestionNumber + " of " + quiz.questions.length;
};

function showScores() {
    var gameOverHTML = "<h1>Result</h1>";
    gameOverHTML += "<h2 id='score'> Your scores: " + quiz.score + "</h2>";
    var element = document.getElementById("quiz");
    element.innerHTML = gameOverHTML;
};

// create questions
var questions = [
      new Question("How many planets are there in our solar system?", ["7", "8","9", "10"], "8"),
	  new Question(" How old is the solar system", ["5000 years", " 5 million years","5 billion years", "500 billion years"], "5 billion years"),
    

    new Question("Which of these planets is the smallest?", ["Jupiter", "Saturn","Mercury", "Uranus"], "Mercury"),
        
	new Question("What is the sun mainly made up of?", ["Lava", "Rock","Gas", "Molten Iron"], "Gas"),
	
	new Question("Saturn is a planet known for the large rings that surround it. What are these rings made of?", ["Ice and rock", "Gases and radiation","Asteroids of all sizes", "Space junk"], "Ice and rock"),
	
	new Question(" Which of the following is the largest planet of the Solar System according to size?", ["Uranus", "Neptune","Jupiter", "Saturn"], "Jupiter"),
	
	new Question("Which of the following planets in the Solar System takes the shortest revolution?", ["Mercury", "Neptune","Mars", "Venus"], "Mercury"),
	
	new Question("Which planet is reffered to as the 'Red Planet'?", ["Mercury", "Earth","Mars", "Uranus"], "Mercury"),
	
	new Question("Which planet is the hottest planet of the solar system?", ["Mercury", "Neptune","Uranus", "Venus"], "Venus"),
	new Question("Which statement describes the atmosphere of the planet correctly?", ["Venus is mostly carbon dioxide", "Mercury is mostly nitrogen","Earth is mostly oxygen", "Saturn is mostly helium"], "Venus is mostly carbon dioxide"),
];


var quiz = new Quiz(questions);


populate();

