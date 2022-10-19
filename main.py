# Your python program will go here.

# // Numbers
# let someInteger = 1;
# let someFloat = 1 / 2;

# // Strings
# let someString = "This is a normal string.";
# let someOtherString = 'This string uses single quotes.';
# let someStringLiteral = `String literals are special.
# They support break returns, and they allow you to do string formatting:
# For example, 1/2 is equal to ${1 / 2}.`;

# // console.log("Is the string '1' equal to the number 1?", "1" == 1);
# // console.log("Is the string '1' strictly equal to the number 1?", "1" === 1);

# // Booleans
# let someTrueValue = true;
# let someFalseValue = false;

# // console.log(someInteger === 1);
# // console.log(someInteger === 0);

# // Arrays
# const books = [
#   {
#     title: "Neuromancer",
#     author: "William Gibson",
#     year_published: 1984,
#     isbn: "",
#     rating: 100
#   },
#   {
#     title: "Snow Crash",
#     author: "Neal Stephenson",
#     year_published: 1992,
#     isbn: "978-01336162-0",
#     rating: 100
#   },
#   {
#     title: "Altered Carbon",
#     author: "Richard K. Morgan",
#     year_published: 2002,
#     isbn: "",
#     rating: 100
#   },
#   {
#     title: "Cryptonomicon",
#     author: "Neal Stephenson",
#     year_published: 2000,
#     isbn: "978-0-380-78862-0",
#     rating: 95
#   }
# ];

# // for (let i = 0; i < books.length; i++) {
# //   console.log(books[i].title);
# //   console.log(books[i].author);
# //   console.log(books[i].year_published);
# //   console.log(books[i].isbn);
# //   console.log(books[i].rating);
# //   console.log('-----');
# // }

# // console.log(books);
# // console.log(books[0]);

# // Objects
# let snowCrash = {
#   title: "Snow Crash",
#   author: "Neal Stephenson",
#   year_published: 1992,
#   isbn: "978-01336162-0",
#   rating: 100
# }

# // console.log(snowCrash.title);
# // console.log(snowCrash.author);
# // console.log(snowCrash.year_published);
# // console.log(snowCrash.isbn);
# // console.log(snowCrash.rating);

# // Null/Undefined
# let someNull = null;
# let someUndefined = undefined;

# const crypto = {
#   title: "Cryptonomicon",
#   author: "Neal Stephenson",
#   year_published: 2000,
#   isbn: "978-0-380-78862-0",
#   rating: 95
# }

# // console.log(crypto.ibsn);

# //Functions
# const someFunction = (someArgument) => {
#   // This is the body of the function.
#   return someArgument;
# }

# const sum = (arrayOfNumbers) => {
#   let result = 0;
#   for (let i = 0; i < arrayOfNumbers.length; i++) {
#     result += arrayOfNumbers[i];
#   }
#   return result
# }

# const numberArray = [
#   1,
#   2,
#   3,
#   4,
#   5,
#   6,
#   7,
#   8,
#   9,
#   10,
#   11,
#   12,
#   13,
#   14,
#   15,
#   16,
#   17,
#   18,
#   19,
#   20
# ]

# // console.log(numberArray[0] + numberArray[1] + numberArray[2] +
# //   numberArray[3] + numberArray[4] + numberArray[5] +
# //   numberArray[6] + numberArray[7] + numberArray[8] +
# //   numberArray[9]);

# // console.log(sum(numberArray));

# function someFunc() {
#   console.log("This function is not a const.");
# }

# function someFunc() {
#   console.log("That previous function will never run!");
# }

# someFunc();

# // Looping

# let pets = [
#   {
#     name: "Sombra",
#     age: 0.5,
#     color: "black",
#     is_awake: false,
#     is_affectionate: true,
#   }, {
#     name: "Grizelle",
#     age: 5,
#     color: "brown",
#     is_awake: true,
#     is_affectionate: true,
#   }, {
#     name: "Maxi",
#     age: 4,
#     color: "brown ombre",
#     is_awake: true,
#     is_affectionate: true,
#   }, {
#     name: "Dexter",
#     age: 7,
#     color: "black",
#     is_awake: false,
#     is_affectionate: true,
#   },
#   {
#     name: "Bazel",
#     age: 2.5,
#     color: "light brown",
#     is_awake: true,
#     is_affectionate: true,
#   }
# ]
# // A "Traditional" for loop
# //  | start          | condition             | how to update your "pointer"
# for (let iterator = 0; iterator < pets.length; iterator++) {
#   if (!pets[iterator].is_awake) {
#     console.log(pets[iterator]);
#   }
# }
# // console.log("Length of pets array:", pets.length);
# // console.log("Item from the pets array at pets.length:", pets[pets.length]);
# // console.log("Item before that previous item:", pets[pets.length - 1]);
# // for (let i = pets.length - 1; i >= 0; i-- /* i = i - 1 */) {
# //   console.log(pets[i]);
# // }

# // For Of loop
# for (let pet of pets) {
#   console.log(pet);
# }

# // For In loop
# for (let petIndex in pets) {
#   console.log(petIndex);
# }

# const someFunc = (elem) => {
#   console.log(elem);
# };

# // ForEach loop
# pets.forEach((elem) => {
#   console.log(elem);
# });

# // While
# //    | conditional
# // while (true) {
# //   console.log("This will never end.");
# // }

# // Functions
# function sum(a, b) {
#   return a + b;
# }

# // function sum(a, b) {
# //   console.log("This function will be used instead of the real one...");
# // }

# // console.log(sum(0.1, 0.2));

# const sumFunc = (a, b) => {
#   return a + b
# }

# // If/else if/else
# for (let i = 0; i < 10; i++) {
#   if (i < 5) {
#     console.log("i is less than 5!", i);
#   } else if (i < 9) {
#     console.log("i is still less than 9.", i);
#   } else {
#     console.log("i is equal to 9!", i);
#   }
# }

# let pet = {
#   name: "Sombra",
#   age: 0.5,
#   color: "black",
#   is_awake: false,
#   is_affectionate: true,
# }

# //Ternary operator
# // condition ? value if true : value if false
# let someHTML = `<h2>${pet.name ? pet.name : "No pet selected."}</h2>`
