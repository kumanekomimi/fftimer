import sys, time, re, os
import art


def fftimer(input_time):
  
  ## タイマーが5分以上のときのやつ
  fmin_flag = False
  if input_time > 300:
    fmin_flag = True
  
  remine_time = input_time
  while remine_time > 0:

    print("残り時間\n")

    s = str(art.text2art(format(remine_time, "04x")))
    print(s)

    if fmin_flag ==True and remine_time <= 300:
      print("\n残り５分ですが進捗いかがです?")

    remine_time -= 1
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

  print("")
  if fmin_flag == True:
    print("タイマーストップ 進捗はどうなりました?")
  else:
    print("タイマーストップ")


def start_ff():
  # pomodolll = [25*60, 10*60]
  flag = False

  while flag == False:
    print("カウントしたい時間を16進数4桁で入力してね")
    input_time = input()

    if len(str(input_time)) > 4:
      print("桁数が大きいよ")
    elif re.fullmatch('^[0-9a-fA-F]+$',input_time) == None:
      print("16進数じゃないよ")
    else:
      print("タイマースタート!!")
      flag = True

  fftimer(int(input_time,16))


def main():
  con_flag = False

  while con_flag == False:
    start_ff()
    
    print("\n\nコンティニューしますか? y: する, それ以外:終了")
    con = input()
    print("")
    if con == 'y':
      pass
    else:
      print("お疲れ様でした!!")
      con_flag == True


if __name__ == '__main__':
  main()
