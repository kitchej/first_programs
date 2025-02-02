using System;

namespace Practice
{

    class Human{
        public string name;
        public double age;
        public char gender;

        public Human(string aName, double aAge, char aGender){
            name = aName;
            age = aAge;
            gender = aGender;
        }

        public void show_attributes(){
            Console.WriteLine($"Name: {name}\nAge: {age}\nGender: {gender}\n");
        }

        public void get_birthday(double current_year){
            Console.WriteLine(current_year - age);
        }
    }

    class SuperHuman : Human
    {
        public string SuperPower;

        public SuperHuman(string aName, double aAge, char aGender, string aSuperPower) : base(aName, aAge, aGender){
            SuperPower = aSuperPower;
        }

        public new void show_attributes(){ // use the 'new' keword to hide (overide) inherited methods
            Console.WriteLine($"Name: {name}\nAge: {age}\nGender: {gender}\nSuper Power: {SuperPower}\n");
        }

    }




    class Book
    {
        public string title;
        public string author;
        private double pages;

        public Book(string b_title, string b_author, double b_pages){
            title = b_title;
            author = b_author;
            Pages = b_pages;
        }
        
        // Getters and Setters
        // Allow us to control how attributes are shown and modified
        // 1.) Set attribute you want to control to 'private'
        // 2.) Create a new method that is the same name as your attribute but with the fist letter capitalized
        // 3.) Set its return type to whatever type your attribute is
        // 4.) Define a get{} and a set{} function
        //     a.) get - this is what will be displayed when code requests the value of a class attribute. Use 'return' + whatever you want to have show
        //     b.) set - this is what will happen when code requests to change the value of a class attribute
        // 5.) In the constructor function, capitalize the attribute name to ensure the get/set function applies when object is constructed too
        public double Pages{
            get {return pages;}
            set {
                if (value >= 1){
                    pages = value;
                }
                else{
                    pages = 1;
                }
            }
        }

        public void show_attributes(){
            Console.WriteLine($"Title: {title}\nAuthor: {author}\nPages: {pages}\n");
        }
    }
}