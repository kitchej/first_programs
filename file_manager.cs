using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace fileManager
{
    public static class globals{
        public static string home_dir;
        public static List<string> dir_history = new List<string>();
    }

    class Program
    {
        static void clear(){
            if(Environment.OSVersion.Platform == PlatformID.Win32NT){
                System.Diagnostics.Process.Start("cmd.exe", "/C cls");
                
            }
            else{
                System.Diagnostics.Process.Start("/bin/bash", "-c clear");
            }
            
        }

        static void show_dir_conents(){
            DirectoryInfo dirInfo = new DirectoryInfo(Directory.GetCurrentDirectory());
            DirectoryInfo[] dirs = dirInfo.GetDirectories();
            FileInfo[] files = dirInfo.GetFiles();
            Console.WriteLine("Size        Mod Time         Name");
            foreach(DirectoryInfo dir in dirs){
                if(dir.Name[0] == '.'){
                    continue;
                }
                string info = $"------{dir.LastWriteTime}------{dir.Name}";
                Console.WriteLine(info);
            }
            foreach(FileInfo file in files){
                if(file.Name[0] == '.'){
                    continue;
                }
                string info = $"{file.Length}------{file.LastWriteTime}------{file.Name}";
                Console.WriteLine(info);
            }
        }

        static void ch_dir(string dir){
            if(dir == "-"){
                if(globals.dir_history.Count == 0){
                    return;
                }
                globals.dir_history.Remove(globals.dir_history.Last());
                
                if(globals.dir_history.Count != 0){
                    Directory.SetCurrentDirectory(globals.dir_history.Last());
                    return;
                }
                else{
                    return;
                }
                
            }

            if(!Directory.Exists(dir)){
                Console.WriteLine($"\"{dir}\" is not a valid directory");
                return;
            }
            globals.dir_history.Add(Path.Join(Directory.GetCurrentDirectory(), dir));
            Directory.SetCurrentDirectory(dir);
        }

        static void create_dir(string name){
            Directory.CreateDirectory(name);
        }

        static void delete_dir(string name){
            if(!Directory.Exists(name)){
                Console.WriteLine($"\"{name}\" is not a valid directory");
                return;
            }
            Directory.Delete(name);
        }

        static void delete_file(string name){
            if(!File.Exists(name)){
                Console.WriteLine($"\"{name}\" is not a valid directory");
                return;
            }
            File.Delete(name);
        }

        static void move_file(string name, string dest_path){
            if(!Directory.Exists(dest_path)){
                Console.WriteLine($"\"{dest_path}\" is not a valid directory");
                return;
            }
            if(!File.Exists(name)){
                Console.WriteLine($"\"{name}\" is not a valid filename");
                return;
            }
            Directory.Move(name, dest_path);
        }

        static void create_file(string name){
            Console.Write("Enter Text: ");
            string text = Console.ReadLine();
            using (StreamWriter sw = new StreamWriter(name)) {
                sw.Write(text);
            }
        }

        static void read_file(string name){
            string text;
            using (StreamReader sw = new StreamReader(name)) {
                text = sw.ReadToEnd();
            }
            Console.WriteLine(text);
            
        }

        static void home(){
            Directory.SetCurrentDirectory(globals.home_dir);
            globals.dir_history.Add(globals.home_dir);
        }

        // static void search(string where, string type, string parameters){

        //     static void search_dir(string type, string parameters){

        //     }

        //     static void search_full(string type, string parameters){

        //     }

            


        //     if(where == "here"){
        //         search_dir();
        //     }
        //     else if(where == "all"){
        //         search_full();
        //     }
        //     else{
        //         Console.WriteLine($"Invalid arg \"{where}\" for search location");
        //     }



        // }

        static void Main(string[] args)
        {
            Dictionary<string, Action> funcs_with_no_args = new Dictionary<string, Action>(){
                {"clear", clear},
                {"ls", show_dir_conents},
                {"home", home}
            };

            Dictionary<string, Delegate> funcs_with_arg = new Dictionary<string, Delegate>();
            funcs_with_arg["cd"] = new Action<string>(ch_dir);
            funcs_with_arg["mkdir"] = new Action<string>(create_dir);
            funcs_with_arg["rmdir"] = new Action<string>(delete_dir);
            funcs_with_arg["rmfile"] = new Action<string>(delete_file);
            funcs_with_arg["mkfile"] = new Action<string>(create_file);
            funcs_with_arg["rdfile"] = new Action<string>(read_file);
            
            if(Environment.OSVersion.Platform == PlatformID.Win32NT){
                globals.home_dir = Environment.GetEnvironmentVariable("HOMEPATH%");
            }

            else{
                globals.home_dir = Environment.GetEnvironmentVariable("HOME");
            }

            Directory.SetCurrentDirectory(globals.home_dir);
           globals.dir_history.Add(globals.home_dir);

            while(true){
                string command;
                string[] splitCommand;

                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"{Directory.GetCurrentDirectory()} $: ");
                Console.ForegroundColor = ConsoleColor.White;
                command = Console.ReadLine();

                if(command == "exit"){
                    break;
                }

                splitCommand = command.Split(' ');

                if(splitCommand.Length == 1){
                    try{
                        funcs_with_no_args[splitCommand[0]]();
                    }
                    catch(System.Collections.Generic.KeyNotFoundException){
                        Console.WriteLine($"Invalid command\"{splitCommand[0]}\"");
                    }
                }

                else if(splitCommand.Length == 2){
                    
                    try{
                        funcs_with_arg[splitCommand[0]].DynamicInvoke(splitCommand[1]);
                    }
                    catch(System.Collections.Generic.KeyNotFoundException){
                        Console.WriteLine($"Invalid command\"{splitCommand[0]}\"");
                    }
                }
            }           
        }
    }
}
