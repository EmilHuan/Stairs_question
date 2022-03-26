# 匯入 Stairs_question.py
from Stairs_question import stairs_cal

# 主程式用 while True 包覆，出現例外 (Exception) 時可重新讓使用者輸入
while True:
    # 例外處理
    try:
        # 樓梯總階數
        stairs = eval(input("輸入樓梯總階數："))

    # SyntaxError 例外，輸入值出現特殊字元時回傳錯誤訊息
    except SyntaxError:
        print("錯誤！輸入值不能有特殊字元，請重新輸入")
        print()

    # NameError 例外，輸入值出現文字時回傳錯誤訊息
    except NameError:
        print("錯誤！輸入值不能有文字，請重新輸入")
        print()

    # 如例外檢查通過，執行 Date_function.py 檔案裡的函數 print_date
    else:
        ways = stairs_cal()
        answer = ways.ways_cal(stairs)
        print("共 {} 種不同的上樓方式".format(answer))

        # 詢問使用者是否要繼續計算其它階梯數
        next_print = input("要計算其它階梯數嗎？(繼續計算請輸入 y，結束計算請按任意鍵)：")
        if next_print.lower().strip() == "y":
            print()
            pass
        else:
            print("感謝您的使用！")
            # 終止 while True (結束列計算)
            break
