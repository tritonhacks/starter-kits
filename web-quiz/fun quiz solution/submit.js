/** Contains functions that handle quiz submission and displays results */


/* -------------------------------------------------------------
Handles the submission process
------------------------------------------------------------- */
function submit(){
  // Collect left and right values
  let leftValues = document.getElementsByClassName("left");
  let rightValues = document.getElementsByClassName("right");
  
  // Get the number of times left and right choices were selected
  let leftCount = 0, rightCount = 0;
  for(let i = 0; i < leftValues.length; i++){leftCount += leftValues[i].checked;}
  for(let i= 0; i < rightValues.length; i++){rightCount += rightValues[i].checked;}
  
  let result = leftCount - rightCount;
  
  // Display the results
  display(result);
}


/* -------------------------------------------------------------
Displays results
------------------------------------------------------------- */
function display(result){
  // Set the quiz result
  if( result > 0 ) result = 'left';
  else if( result < 0 ) result = 'right';
  else result = 'middle';
  
  // Get results containers
  let resultID = document.getElementById("result");
  let output = document.getElementById("output");

  // Update the output's text
  output.innerText = result;
  
  // Unhide the results by removing hide class
  resultID.className = "";
}