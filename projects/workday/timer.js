var date = new Date();
var currentTime = 0;
var endTime = 0;
var timeLeft = 0;

var numberWords = {
	"1":"one",
	"2":"two",
	"3":"three",
	"4":"four",
	"5":"five",
	"6":"six",
	"7":"seven",
	"8":"eigtht",
	"9":"nine",
	"0":"zero"
};

function numberToDigits(n){
	var s = n.toString();
	var digitList = s.split('');
	while(digitList.length !== 5){
		digitList.splice(0, 0, '0');
	}
	let wordList = [];
	digitList.forEach(function(item, index){
		wordList.push(numberWords[item]);
	});
	return wordList;
}

function renderTime(){
	if((currentTime > 0) && (currentTime < endTime)){
		let wordList = numberToDigits(timeLeft);
		wordList.reverse();
		let n = 0;
		$(".number-outer-inner").each(function(){
			$(this).removeClass();
			$(this).addClass("number-outer-inner");
			$(this).addClass(wordList[n]);
			n++;
		});
		var percent = Math.floor((currentTime / endTime) * 100);
		$(".progress-bar-inner").css("width", percent + "%");
		$(".progress-bar-inner").css("animation", "none");
	}else{
		if(currentTime >= endTime){
			$(".number-outer-inner").each(function(){
				$(this).removeClass();
				$(this).addClass("number-outer-inner zero");
			});
			$(".progress-bar-inner").css("width", "100%");
			$(".progress-bar-inner").css("animation", "flash .5s infinite");
		}
	}
	currentTime++;
	timeLeft--;
}

function setWork(){
	currentTime = ((date.getHours() * 60 * 60) + (date.getMinutes() * 60) + (date.getSeconds())) - 28800;
	endTime = 32400;
	timeLeft = endTime - currentTime;
}

function setSchool(){
	currentTime = ((date.getHours() * 60 * 60) + (date.getMinutes() * 60) + (date.getSeconds())) - 29700;
	endTime = 25200;
	timeLeft = endTime - currentTime;
}

function setCustom(){
	if(/^\d+$/.test($("#seconds-input").val())){
		currentTime = 1;
		endTime = parseInt($("#seconds-input").val()) + 1;
		timeLeft = endTime - currentTime;
		$("#seconds-input").val("");
	}else{
		alert("Invalid Time");
	}
}

$(".tab").click(function(){
	$(".settings").toggleClass("visible");
	$(".tab").toggleClass("tab-on");
});
$(".submit").click(setCustom);
$(".set-work").click(setWork);
$(".set-school").click(setSchool);

setInterval(renderTime,1000);
