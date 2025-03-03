for (let i =0; i <= 10; i++){
  console.log(i)
}

n =10

while(n > 0){
  console.log(n);
  n--;
}

let userInput;

do{
  userInput = parseInt(prompt("Enter num greater than 10:"), 10)

} while (userInput <= 10);

console.log("Valid input recieved: ", userInput);

let fruits = ['Banana', 'Apple', 'Mango', 'Atai', 'Amantai'];
for(let i = 0; i < fruits.length; i++){
  console.log(fruits[i])
}

let fruits = ['Banana', 'Apple', 'Mango', 'Atai', 'Amantai'];

let i = 0;
while(i<fruits.length){
  console.log(fruits[i]);
  i++;
}

let nums = [3, 7, 12, 5, 9]
for(let i =0; i< nums.length; i++){
  if (nums[i] === 12){
    console.log("Success!")
    break
  }
  console.log(nums[i])
}

let nums = [3, 7, 12, 5, 9]
for(let i =0; i< nums.length; i++){
  if (nums[i] === 5){

    continue
  }
  console.log(nums[i])
}