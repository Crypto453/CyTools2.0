import time
import colorama
banner_a = ("                            ,-.")
banner_b = ("       ___,---.__          /'|`|          __,---,___")
banner_c = ("    ,-'    |`    `-.____,-'  |  `-.____,-'    //    `-.")
banner_d = ("  ,'        |           ~'|     /`~           |        `.")
banner_e = ("     ___//              `. ,'          ,  , |___      |")
banner_f = ("|    ,-'   `-.__   _         |        ,    __,-'   `-.    |")
banner_g = ("|   /          /|_  `   .    |    ,      _/|          |   |")
banner_h = ("|  |           | |`-.___ |   |   / ___,-'/ /           |  /")
banner_i = (" |  |           | `._   `||  |  //'   _,' |           /  /")
banner_j = ("  `-.|         /'  _ `---'' , . ``---' _  `|         /,-'")
banner_k = ("     ``       /     |    ,='/ |`=.    /     |       ''")
banner_l = ("             |__   /||_,--.,-.--,--._/||   __|")
banner_m = ("             /  `./  ||`| |  |  | /,//' |,'  |")
banner_n = ("            /   /     ||--+--|--+-/-|     |   |")
banner_o = ("           |   |     /'|_|_| | /_/_/`|     |   |")
banner_p = ("            |   |__, |_     `~'     _/ .__/   /")
banner_q = ("             `-._,-'   `-._______,-'   `-._,-'CyTools 2.0")
banner_banner = [banner_a, banner_b, banner_c, banner_d, banner_e, banner_f, banner_g, banner_h, banner_i, banner_j, banner_k, banner_l, banner_m, banner_n, banner_o, banner_p, banner_q]
for banner_x in banner_banner:
    print(chr(27)+"[1;33m"+banner_x)
    time.sleep(0.1) 
