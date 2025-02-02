/* 
* Display (C++ version)
* Written by Joshua Kitchen 3/27/2021
*
* Error codes:
* 1 = out of bounds
* 2 = bad argument
*/
#include <iostream>
#include <cstdlib>
#include <vector>
#include <chrono>
#include <thread>

class Pixel{
    public:
        int x;
        int y;
        char value;

        Pixel(int pixel_x, int pixel_y, char pixel_value){
            x = pixel_x;
            y = pixel_y;
            value = pixel_value;
        }
};


class Sprite{
    public:
    std::vector<Pixel> pixels;
    int length;
    int height;

        Sprite(std::vector<Pixel> sprite_pixels){
            pixels = sprite_pixels;
            int largest_x = pixels[0].x;
            int largest_y = pixels[0].y;

            int smallest_x = pixels[0].x;
            int smallest_y = pixels[0].y;

            for(Pixel p:pixels){
                if(p.x > largest_x){
                    largest_x = p.x;
                }
                if(p.x < smallest_x){
                    smallest_x = p.x;
                }

                if(p.y > largest_y){
                    largest_y = p.y;
                }
                if(p.y < smallest_y){
                    smallest_y = p.y;
                }
            }

            length = (largest_x - smallest_x) + 1;
            height = (largest_y - smallest_y) + 1;
        }

        void show_coords(){
            for(Pixel p:pixels){
                std::cout << p.value << ": (" << p.x << ", " << p.y << ")\n"; 
            }
        }

        // direction: left, right, up, down
        // length: how far to move the sprite
        int move(std::string direction, int distance){
            for(int i=0;i<=pixels.size() - 1;i++){
                if(direction ==  "left"){
                    pixels[i].x = pixels[i].x - distance;
                }
                else if(direction == "right"){
                    pixels[i].x = pixels[i].x + distance;
                }
                else if(direction == "up"){
                    pixels[i].y = pixels[i].y - distance;
                }
                else if(direction == "down"){
                    pixels[i].y = pixels[i].y + distance;
                }
                else{
                    return 2;
                }
            }
            return 0;
        }

        // direction: right, left, up, down
        int flip(std::string direction, bool in_place=false){
            if(direction == "right"){
                int temp = (length * 2) - 1;
                for(int i=0;i<=pixels.size();i++){
                    pixels[i].x = pixels[i].x + temp;
                    temp = temp - 2;
                }
                if(in_place == true){
                    move("left", length);
                }
            }
            else if(direction == "left"){
                int temp = (length * 2) - 1;
                for(int i=0;i<=pixels.size();i++){
                    pixels[i].x = pixels[i].x - temp;
                    temp = temp + 2;
                }
                if(in_place == true){
                    move("right", length);
                }
            }
            else if(direction == "down"){
                int temp = (height * 2) - 1;
                for(int i=0;i<=pixels.size();i++){
                    pixels[i].y = pixels[i].y - temp;
                    temp = temp - 2;
                }
                if(in_place == true){
                    move("up", height);
                }
            }
            else if(direction == "up"){
                int temp = (height * 2) - 1;
                for(int i=0;i<=pixels.size();i++){
                    pixels[i].y = pixels[i].y + temp;
                    temp = temp + 2;
                }
                if(in_place == true){
                    move("down", height);
                }
            }
            else{
                return 2;
            }
            return 0;
        }

        //direction: clockwise, counterclock
        //length: how many pixels to rotate the sprite
        void rotate(std::string direction, int length){

        }

        
};


class Display{

    int rows;
    int columns;
    char bg;
    std::vector<std::vector<char>> screen;

    public:
        Display(int display_rows, int display_columns, char display_bg){
            rows = display_rows;
            columns = display_columns;
            bg = display_bg;
            std::vector<char> temp;
            for(int r=0; r<=rows-1; r++){
                temp.clear();
                for(int c=0;c<=columns-1;c++){
                    temp.push_back(bg);
                }
                screen.push_back(temp);
            }
        }

        void clear_terminal(){
            std::system("clear");
        }

        void clear_display(){
            for(int r=0; r<=rows-1; r++){
                for(int c=0; c<=columns-1;c++){
                    screen[r][c] = bg;
                }
            }
        }

        int length(){
            return columns;
        }

        int height(){
            return rows;
        }

        void change_bg(char new_bg){
            for(int r=0; r<=rows-1; r++){
                for(int c=0; c<=columns-1;c++){
                    char value = screen[r][c];
                    if(value == bg){
                        screen[r][c] = new_bg;
                    }
                }
            }
            bg = new_bg;
        }

        int draw_char(int x_pos, int y_pos, char character){
            if(x_pos > columns - 1 or x_pos < 0){
                return 1;
            }

            if(y_pos > rows - 1 or y_pos < 0){
                return 1;
            }

            screen[y_pos][x_pos] = character;
            return 0;
        }

        std::vector<int> draw_sprite(Sprite sprite){
            std::vector<int> errorCodes;
            for(Pixel p:sprite.pixels){
                int exit_code = draw_char(p.x, p.y, p.value);
                errorCodes.push_back(exit_code);
            }
            return errorCodes;
        }

        void show(){
            for(int r=0; r<=rows-1; r++){
                for(int c=0; c<=columns-1;c++){
                    std::cout << screen[r][c];
                }
                std::cout << "\n";
            }
        }
};


void scrolling_text(Display display_obj, std::string text, int speed=100, int stop=-1, std::string direction="rightToLeft"){

    int y = display_obj.height() / 2;
    std::vector<int> char_coords;
    std::vector<char> char_vector;
    for(char s:text){
        if(direction == "leftToRight"){
            char_coords.push_back(-1);
        }
        else if(direction == "rightToLeft"){
            char_coords.push_back(display_obj.length());
        }
        else{
            std::cout << "Bad argument " << "\"" << direction << "\"" << " for direction" << "\n";
            return;
        }
        
        char_vector.push_back(s);
    }

    if(direction == "leftToRight"){
        if(stop < 0){
        stop = display_obj.length() - 1;
        }

        int offset = char_vector.size() + 1;
        while(char_coords[0] <= stop){
            std::this_thread::sleep_for(std::chrono::milliseconds(speed));
            display_obj.clear_display();
            display_obj.clear_terminal();

            for(int i=char_vector.size() - 1;i>=0;i--){
                if(i >= offset){
                    char_coords[i] ++;
                    if(char_coords[i] > display_obj.length() - 1){} // ignore if char is out of view
                    else{
                        display_obj.draw_char(char_coords[i], y, char_vector[i]);
                    }
                }
            }
            offset --;
            display_obj.show();
        }
    }
    else if (direction == "rightToLeft"){
        int offset = -1;
        while(char_coords.back() >= stop){
            std::this_thread::sleep_for(std::chrono::milliseconds(speed));
            display_obj.clear_display();
            display_obj.clear_terminal();

            for(int i=0;i<=char_vector.size() - 1;i++){
                if(i <= offset){
                    char_coords[i] --;
                    if(char_coords[i] < 0){} // ignore if char is out of view
                    else{
                        display_obj.draw_char(char_coords[i], y, char_vector[i]);
                    }
                }
            }
            offset ++;
            display_obj.show();
        }
    }
}


int main(int argc, char *argv[]){
    // std::vector<Pixel> pix = {Pixel(25, 12, 'O'), Pixel(24, 13, '-'), Pixel(25, 13, '|'), Pixel(26, 13, '-'), Pixel(25, 14, '|'), Pixel(24, 15, '/'), Pixel(26, 15, '\\')};
    std::vector<Pixel> pix = {Pixel(1, 12, '-'), Pixel(2, 12, '-'), Pixel(3, 12, '-'), Pixel(4, 12, '+')};
    Sprite mySprite = Sprite(pix);
    Display screen = Display(25, 51, ' ');
    screen.draw_sprite(mySprite);
    mySprite.flip("right");
    screen.draw_sprite(mySprite);
    mySprite.flip("up");
    screen.draw_sprite(mySprite);
    mySprite.flip("down");
    screen.draw_sprite(mySprite);
    screen.show();
}