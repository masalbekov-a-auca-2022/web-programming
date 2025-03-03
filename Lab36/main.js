function sum(a,b){
  return a+b;
}

//function square(a){
    //return a*a;
//}

const square = (a) => a*a;

function max(a,b){
    return (a > b) ? a:b;
}

let globalVar = "Hello from Global!"

function displayGlobal(){
    console.log(globalVar);
}

function poorLocalVar(){
    let localVar = " i am local ";
    console.log(localVar);
}

if(true){
    var x = 1;
}
console.log(x)

if(true){
    let y = 1;
}
console.log(y) //error

if(true){
    const z = 1;
}
console.log(z) //error

function counter(){
    let count = 0;

    return function (){
        count++;
        console.log(count)
    }
}

const counter1 = counter();
const counter2 = counter();

counter1();
counter1();
counter1();

counter2();
counter2();
counter2();




