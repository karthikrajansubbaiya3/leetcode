
console.log("hi");
// o(n!) that we add for loop for every element
const strings = ['a', 'b', 'c', 'd']



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

strings.splice(2, 0, 'alien');
// go tho second index second parameter in case if we want to delete add the element so we do the half of operations so it would be o(n/2) remove the constants 



//refrence type
var object1 = { value: 1 }
var object2 = object1;
var object3 = { value: 1 }
if (object1 === object3) {

}
else {
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
const object4 = {
    a: function () {
        console.log(this)
    }
}
//instatiation
//instatiation when you make copy of an object and reuse it
class Player {
    constructor(name, type) {
        //properties
        console.log(this);
        this.name = name;
        this.type = type;
    }
    introduce() {
        console.log(`hi am ${this.name}, i'm a${this.type}`);
    }
}
class Wizard extends Player {
    constructor(name, type) {
        super(name, type)
    } l
    play() {
        console.log(`weeee i'm a ${this.type}`);
    }
}
const wizard1 = new Wizard('shelly', 'healer');
wizard1.introduce()
//implementing array
class newarray {
    constructor() {
        this.length = 0;
        this.data = {};

    }
    get(index) {
        return this.data[index];
    }
    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }
    delete(index) {
        const item = this.data[index];
        this.shiftitems(index);

        return item;
    }
    pop() {
        delete this.data[this.length - 1];
        this.length--;
    }
    shiftitems(index) {
        for (let i = index; i < this.length; i++) {
            this.data[i] = this.data[i + 1];
        }
        delete this.data[this.length - 1];
        this.length--;
    }
}
const newArray = new newarray
newArray.push('hi');
newArray.push('hello');
newArray.push('are you');
//newArray.shiftitems(1)
newArray.delete(0)
console.log(newArray);

//treat any string question into array
const backwards = [];
function reverse(str) {

    if (str.length < 2 || typeof str != 'string' || !str)
        return str
    for (let i = str.length - 1; i >= 0; i--) {

        backwards.push(str[i]);
    }
    return backwards.join('')

}
console.log(backwards)
function reverse2(str) {
    return str.split('').reverse().join('')
}
const reverse3 = str => [...str].reverse().join('')
reverse('Timbits Hi')
console.log(backwards)
reverse2('Timbits Hi')
reverse3('Timbits Hi')

function mergesortedarrays(array1, array2) {
    let array1item = array1[0];
    let array2item = array2[0];
    const mergesortedarray = [];
    let i = 1;
    let j = 1;
    if (array1.length === 0) {
        return array1;
    }
    if (array2.length === 0) {
        return array2;
    }
    while (array1item || array2item) {
        if (array2item === undefined || array1item < array2item) { //array1item < array2item
            mergesortedarray.push(array1item)
            array1item = array1[i];
            i++;
        }
        else {
            mergesortedarray.push(array2item)
            array2item = array2[j];
            j++;
        }

    }
    return mergesortedarray;
}
console.log(mergesortedarrays([0, 4, 31], [1, 3, 5]));
//twosum array
function Twosumarray(array1, array2, target) {
    array1.forEach(function (numbers, index) {
        array1.forEach(function (secondNumber, index2) {
            let sum = 0
            sum = numbers + secondNumber
            if (sum === target) {
                //console.log(indexof(numbers),indexof(secondNumber))
                console.log(index, index2)

            }
        })
    })

}
const number = [1, 2, 3, 4]
const number2 = [2, 5, 7, 9]
const target = 5
//Twosumarray(number,number2,target)
function twosumarray2(number3, target2) {
    for (let i = 0; i < number3.length; i++) {
        for (let j = 0; j < number3.length; j++) {
            if (i == j) {
                continue //same item of two array can be add up test case failed add these line
            }
            else {
                let sum = 0
                sum = number3[i] + number3[j]
                if (sum === target2) {

                    return [number3[i], number3[j]]
                }
            }
        }
    }
}
const number3 = [1, 2, 3, 4, 6]
const target2 = 5
const number4 = twosumarray2(number3, target2)
console.log(number4)
//hash tables in javascript objects in python dictionary java has maps ruby has hashes
// we have to set key value pair
// it is done through hash function
// hash function is a simple function that generates values of fixed lenght for each input that it gets
//that function given an input always output the same output
//big o(1)
//hash collision happens it allocates random memory space it allocates same memory to two because of this we can have o(n/k)
//k is number of elements in hash tabels
//map and set are prebuilt datastructure
// map have any of type should be as key
//set only stores key

class hashtable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash
    }
    set(key, value) {
        const address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, value]);
        return this.data;
    }
    // this.data[address].push([key,value]);
    // return this.data;

 keys() {
    if (!this.data.length) {
      return undefined
    }
    let result = []
    // loop through all the elements
    for (let i = 0; i < this.data.length; i++) {
        // if it's not an empty memory cell
        if (this.data[i] && this.data[i].length) {
          // but also loop through all the potential collisions
          if (this.data.length > 1) {
            for (let j = 0; j < this.data[i].length; j++) {
              result.push(this.data[i][j][0])
            }
          } else {
            result.push(this.data[i][0])
          } 
        }
    }
    return result; 
  }


    get(key) {
        const address = this._hash(key);
        const currentbucket = this.data[address]
        if (currentbucket) {
            for (let i = 0; i < currentbucket.length; i++) {
                if (currentbucket[i][0] === key) {
                    return currentbucket[i][1];
                }

            }
        }
    }
    keys() {
        const array = []
        for (let i = 0; i < this.data.length; i++) {
            if (this.data[i]) {
                array.push(this.data[i][0])
            }
        }
        return array;
    }
}

const myhashtable = new hashtable(50)
myhashtable.set('grapes', 10000);
const hash = myhashtable.get('grapes');
const hash2 = myhashtable.keys()
console.log(hash2)
//uderscore befor method is telling tat is private property
//charcode returns an integer 
//most recurring caharacter
// in this approach o(n^2) time complexity is higher and two same behind comes it will fails for that we need hash]
// this is naive approach (things comes to mind first)
function mostrecurringcaharcter(input){

    for (let i=0;i<input.length;i++){
        for(let j=i+1;j<input.length;j++){
            if(input[i]===input[j]){
                return input[i];
            }


        }
    }
}

// const mstr=mostrecurringcaharcter([1,2,3,2,5,6,6])
// console.log(mstr)
//hash
function mostrecuuringchar(input){
    let map={};
    for(let i=0;i<input.length;i++){
        if(map[input[i]]!==undefined){
            return input[i]

        }
        else{
            map[input[i]]=i
        }
        
    }
    return undefined
}
const mstr2=mostrecuuringchar([2,5,1,2,3,5,1,2,4])
console.log(mstr2)

//charcode returns an integer

//we put items in shelves retrive them in unordered

function twoSum(nums, target) {
    for(let i=0;i<nums.length;i++){
    for(let j=i+1;i<nums.length;j++){
   let sum=0
   sum=nums[i]+nums[j]
   if(sum===target){
    return[i,j];
   }
    }
    }
}

console.log(twoSum([2,7,11,15], 9))