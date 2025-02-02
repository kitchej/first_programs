#ifndef __CALCULATOR_H_INCLUDED__  
#define __CALCULATOR_H_INCLUDED__  

int add(int num1, int num2){
    return num1 + num2;
}

int subtract(int num1, int num2){
    return num1 - num2;
}

int multiply(int num1, int num2){
    return num1 * num2;
}

int divide(int num1, int num2){
    if(num2 == 0){
        std::cout << "Zero Division Error" << std::endl;
        return 0;
    }
    else{
        return num1 / num2;
    }
    
}

int modulo(int num1, int num2){
    if(num2 == 0){
        std::cout << "Zero Division Error" << std::endl;
        return 0;
    }
    else{
        return num1 % num2;
    }
}

#endif