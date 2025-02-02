#include <iostream>
#include <filesystem>
#include <vector>
#include <bits/stdc++.h>

namespace fs = std::filesystem;

std::vector<std::string> stringSplitter(std::string str, char delimeter){
    std::vector<std::string> items;
    std::string token;
    std::stringstream splitter(str);

        while(std::getline(splitter, token, delimeter)){
            items.push_back(token);
        }
    
    return items;
}

int clear(){
    std::system("clear");
    return 0;
}

int ch_dir(std::string path){
    if (!fs::exists(path)){
        std::cout << path << " does not exist" << std::endl;
        return 1;
    }

    try{
        fs::current_path(path);
    }

    catch(fs::filesystem_error& e){
        return 1;
    }

    return 0;
}


int show_dir_contents(){
    
    for (auto& p: fs::directory_iterator(fs::current_path())){
        std::vector<std::string> splitPath;
        try{
            std::string fileName = p.path().string();
            splitPath = stringSplitter(fileName, '/');
            if (splitPath.back()[0] == '.'){
                continue;
            } 
            std::cout << splitPath.back() << "  " << fs::file_size(p) << std::endl;
        }
        catch(fs::filesystem_error& e){
            std::cout << "" << std::endl;
        }
    }
    return 0;
}






int main()
{   
    std::string commands[] = {"cd", "ls", "clear"};

    int (*show_dir_contents_pointer)();
    int (*clear_pointer)();
    int (*ch_dir_pointer)(std::string);  

    show_dir_contents_pointer = &show_dir_contents;
    clear_pointer = &clear;
    ch_dir_pointer = &ch_dir;

    std::map<std::string, int(*)()> no_arg_funcs;
    std::map<std::string, int(*)(std::string)> one_arg_funcs;

    no_arg_funcs.insert(std::pair<std::string, int(*)()>("ls", show_dir_contents_pointer));
    no_arg_funcs.insert(std::pair<std::string, int(*)()>("clear", clear_pointer));

    one_arg_funcs.insert(std::pair<std::string, int(*)(std::string)>("cd", ch_dir_pointer));

    while(true){
        std::string command;
        std::vector<std::string> splitCommand;
        int error_code;

        std::cout << fs::current_path().string() << " $: ";
        std::getline(std::cin, command);

        if(command == "exit"){
            break;
        }

        splitCommand = stringSplitter(command, ' ');

        bool in_array = false;
        for (std::string i: commands){
            if(splitCommand[0] == i){
                in_array = true;
            }
        }

        if(in_array != true){
            std::cout << "Invalid command: \"" << command << "\"" << std::endl;
            continue;
        }

        if (splitCommand.size() == 1){
            error_code = no_arg_funcs[splitCommand[0]]();
            if (error_code == 1){
                continue;
            }
        }
        else if (splitCommand.size() == 2){
            error_code = one_arg_funcs[splitCommand[0]](splitCommand[1]);
            if (error_code == 1){
                continue;
            }
        }
        else{
            std::cout << "Invalid command: \"" << command << "\"" << std::endl;
        }

        
        
    }
}