
console.log("hi");
// o(n!) that we add for loop for every element
const strings=['a','b','c','d']



// scalable 
const array1 = ['nemo']
const large = new Array(100).fill("nemo")
function findnemo(Array) {
    let t0 = performance.now();
    for (let i = 0; i < array1.length; i++) {

        if (array1[i] = "nemo") {
            if (array1[i] == "nemo") {
                console.log("found");
                break; //using this we can make code eeficient by not running rest of this afer finding
            }
        }

    }
    let t1 = performance.now(); //seconds to measure the code runs 
    console.log("call took to find nemo " + (t0 - t1) + 'milliseconds');
}
findnemo(large) //o(n) -->linear time

const boxses = [1, 2, 3, 4, 5]
function findboxes(Array) {
    console.log(boxses[0])

}
findboxes(boxses) //o(1) constant time no matter how many inputs increase same number of operation
//funchallenge(input)
function funchallenge(input) {
    let a = 10 //o(1)
    a = 50 + 3 //o(1)
    for (let i = 0; i < input.length; i++) { // for loops have linear time o(n)
        anotherfunction() //o(n)
        let stranger = true //o(n)
        a++; //o(n)
    }
    return a; //o(1)

}
//big(o)=1+1+1+n+n+n+n =3+4n=o(3+4n)=0(n) constancts will be negligible
//the best rule of big o is we always care about wrost case scenario

//rule:2;remove the consttants

//rule3:different terms of input
function compresseoftwoboxes(boxes, boxses2) {
    boxes.foreach(function (boxes) {
        console.log("hi")
    })

    boxses2.foreach(function (boxses2) {
        console.log("hello")
    })

}
//o(a+b)
// two function near by tat means they donot have same number of items instead of o(n) it should be o(a+b)

//log all pairs of array arra=[1,2,3,4,5] 
function logallpair(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            console.log(array[i] + "," + array[j]);
        }
    }
}
const array = [1, 2, 3, 4, 5]
logallpair(array) // when loops become nested we can use o(n*n)


// drop non dominants
//print all numbers and allpairsums
const numbers = [1, 2, 3, 4, 5]

function printAllNumbersThenAllPairSums(numbers) {
    console.log('these are the numbers');
    numbers.forEach(function (number) {
        console.log(number);
    });

    numbers.forEach(function (firstNumber) {
        numbers.forEach(function (secondNumber) {
            console.log(firstNumber + secondNumber);
        });
    });
}
printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])
//o(n+n*n) we care about most important one (dominant one) here n*2 is the dominant one we can ignore n so that could be o(n^2)
console.log("hi");
// o(n!) that we add for loop for every element
const strings1 = ['a', 'b', 'c', 'd']

strings.push('e')// it will push element at end of array it can directly to go o(1)
//pop
strings.pop() //it will pop last element of the array
//unshift it will insert elemwnt at first by shifiting indexses so the it will need to acess all the elemewnt so o(n)
// so the number of element increase so array size also increase
// splice it will add elemnt atmiddle of thwe array

strings.splice(2,0,'alien');
// go tho second index second parameter in case if we want to delete add the element so we do the half of operations so it would be o(n/2) remove the constants 



//refrence type
var object1={value:1}
var object2=object1;
var object3={value:1}
if (object1===object3){

}
else{
}

strings.splice(2, 0, 'alien');
// go tho second index second parameter in case if we want to delete add the element so we do the half of operations so it would be o(n/2) remove the constants 

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])
//o(n+n*n) we care about most important one (dominant one) here n*2 is the dominant one we can ignore n so that could be o(n^2)
//data structure + algorithm=program

//refrence type
var object1 = { value: 1 }
var object2 = object1;
var object3 = { value: 1 }
if (object1 === object3) {

}
else {

    console.log("hello");
}
//context type
// context tells you where we are in the object
// what is the object environment that were in right now 
//this refers to what object its inside of
const object4={
    a:function(){
        console.log(this)
    }
}
//instatiation
//instatiation when you make copy of an object and reuse it
class Player{
    constructor(name,type){
        //properties
        console.log(this);
        this.name=name;
        this.type=type;
    }
    introduce() {
        console.log(`hi am ${this.name}, i'm a${this.type}`);
    }
}
class Wizard extends Player{
    constructor(name,type){
        super(name,type)
    }
    play() {
        console.log(`weeee i'm a ${this.type}`);
    }
}
const wizard1=new Wizard('shelly','healer');
wizard1.introduce()