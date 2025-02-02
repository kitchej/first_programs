#ifndef __EXAMPLES_H_INCLUDED__  
#define __EXAMPLES_H_INCLUDED__ 
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h> 
#include "calculator.h"


std::string readFile(std::string path){
    std::fstream file;
    file.open(path, std::ios::in);
    std::string line;
    std::string text;
    while(std::getline(file, line)){
        text = text + line;
    }
    file.close();
    return text;
}

void writeFile(std::string path, std::string text, bool append = false){
    std::fstream file;
    if(append == true){
         file.open(path, std::ios::app);
    }
    else{
        file.open(path, std::ios::out);
    }
    
    file << text;
    file.close();
}

void vectorExample(){
    std::vector<std::string> names = {"Josh", "Alex", "Mark", "Adam"};
    
    for(std::string name:names){
        std::cout << name <<std::endl;
    }
    
    std::cout << "\n" << std::endl;
    
    names.insert(names.begin() + 1, 1, "Corey");
    
    names.push_back("Zach");
    
    for(std::string name:names){
        std::cout << name << std::endl;
    }
    
    std::cout << "\n" << std::endl;
    std::cout << "Item at vector postion 4: " << names[4] << std::endl;
}

void mapExample(){
    std::map<std::string, int> nameAge;
    
    nameAge.insert(std::pair<std::string, int>("Jacob", 16));
    nameAge.insert(std::pair<std::string, int>("Jared", 20));
    nameAge.insert(std::pair<std::string, int>("Jon", 29));
    nameAge.insert(std::pair<std::string, int>("Josh", 24));
    nameAge.insert(std::pair<std::string, int>("Jennifer", 27));
    
    std::cout << nameAge["Jon"] << std::endl;
}

void pointersExample(int num){
    int var = num;
    int *location = &var;
    
    std::cout << "printing out 'location': " << location << std::endl;
    std::cout << "printng out '*location': " << *location << std::endl;

    *location = 10;

    std::cout << "Changed varible pointed to with '*location = 10': " << *location << std::endl;
    
}

void declaringPointerToFunc(){
    void (*pointersExamplePoint)(int); // create pointer variable - [return type] (*functionName)(argTypes);

    pointersExamplePoint = &pointersExample; // assign value of memory address to pointer variable

    pointersExamplePoint(30); // call func with pointer variable name and then args [pointerVariable](args);
}

void mapOfFuncPointers(){
    void (*pointersExamplePoint)(int); // create the function pointer

    pointersExamplePoint = &pointersExample; // assign value of memory address to pointer variable

    // mapping must be EXACTLY the same as decleration of pointer variable
    // Example:
    // int (*funcName)(char);
    // MUST BE std::map<std::string, int(*)(char)> funcs;

    std::map<std::string, void(*)(int)> funcs; 
    funcs.insert(std::pair<std::string, void(*)(int)>("pointers", pointersExamplePoint));
    funcs["pointers"](25);

}

void calc(){
    std::map<std::string, int(*)(int, int)> funcs;
    funcs["add"] = add;
    funcs["subtract"] = subtract;
    funcs["multiply"] = multiply;
    funcs["divide"] = divide;
    
    
    while(true){
        int n1;
        int n2;
        std::string op;
        
        std::cout << "Enter a number: ";
        std::cin >> n1;
        std::cout << "Enter another number: ";
        std::cin >> n2;
        std::cout << "Enter Operator: ";
        std::cin >> op;
        std::cout << funcs[op](n1, n2) << std::endl;;
    }
}

void structs(){
    struct person{
        std::string name = "Jim";
        int age = 25;
        std::string phone = "801-668-2340";
        char sex = 'M';
    };

    person jim;
    person* jimPoint = &jim;

    std::cout << jim.phone << std::endl; // accesses struct itself
    std::cout << jimPoint->phone << std::endl; // accesses struct through pointer
}

void simpleLinkedList(){
    struct node{
        int value;
        node* next;
    };    

    node h;
    node b;
    node t;

    node* head = &h;
    node* body = &b;
    node* tail = &t;

    head->value = 0;
    head->next = body;

    body->value = 1;
    body->next = tail;

    tail->value = 2;
    tail->next = NULL;

    node* temp = head;
    while(temp != NULL){
        std::cout << temp->value << std::endl;
        temp = temp->next;
    }
}

void advCalculator(){
    int num1;
    int num2;
    std::vector<std::string> items;
    std::string op;
    std::string expresion = "";
    std::string token;

    while(true){
        std::cout << "Enter expression: ";
        std::getline(std::cin, expresion);

        if(expresion == "exit"){
            break;
        }

        std::stringstream splitter(expresion);

        while(std::getline(splitter, token, ' ')){
            items.push_back(token);
        }
        
        try{
            num1 = std::stoi(items[0]);
            op = items[1];
            num2 = std::stoi(items[2]);
        }

        catch(std::invalid_argument){
            std::cout << "Invalid Argument" << std::endl;
            items.clear();
            continue;
        }

        items.clear();

        if(op == "+"){
            std::cout << add(num1, num2) << std::endl;
        }

        else if(op == "-"){
            std::cout << subtract(num1, num2) << std::endl;
        }

        else if(op == "*"){
            std::cout << multiply(num1, num2) << std::endl;
        }

        else if(op == "/"){
            std::cout << divide(num1, num2) << std::endl;
        }

        else if(op == "%"){
            std::cout << modulo(num1, num2) << std::endl;
        }

        else{
            std::cout << "Operator \"" << op << "\" not supported" << std::endl;
        }


    }

}

std::vector<std::string> stringSplitter(std::string str, char delimeter){
    std::vector<std::string> items;
    std::string token;
    std::stringstream splitter(str);
    
        while(std::getline(splitter, token, delimeter)){
            items.push_back(token);
        }
    
    return items;
}

#endif