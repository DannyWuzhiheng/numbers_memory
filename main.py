import random  
import turtle as t
import time
t.bgpic(r"D:\Nubers_Memory\background.png")
t.colormode(255)
t.bgcolor(118,198,196)
t.color(255,0,0)
def generate_digit():  
    return random.randint(0, 9)  
  
def show_sequence(sequence): 
    v=''.join(map(str, sequence)) 
    t.write(f"初始数字是：{v}",font=("楷体",40,'normal'),align='center')  
  
def main_game():  
    sequence = [generate_digit() for _ in range(5)]  # 初始5位数字序列  
    max_length = 0 
    show_sequence(sequence)  

    while True:  
        time.sleep(1)
        t.clear()
        player_input = t.textinput("请输入你记住的数字序列：",'')  
        if player_input == ''.join(map(str, sequence)):  
            con=generate_digit()
            sequence.append(con)  # 添加一位新数字  
             
            if len(sequence) > max_length:  
                max_length = len(sequence)-1  
        
        else:  
            t.write(f"游戏结束。你最高记住的位数是：{max_length}",font=("楷体",30,'normal'),align='center')
            time.sleep(1)
            exit()
              
        t.write(f'追加的数字是：{con}',font=("楷体",50,'normal'),align='center')

if __name__ == "__main__":  
    main_game()
