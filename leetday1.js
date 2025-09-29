console.log("hi");
// o(n!) that we add for loop for every element
const strings=['a','b','c','d']
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
    console.log("hello");
}