import win32gui
import win32api
import win32con
import time

3672 3328 

3672 2448
titlename = "文化海康"
hwnd = win32gui.FindWindow(None, titlename)

win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
win32gui.SetForegroundWindow(hwnd)
#left, top, right, bottom
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left)
# sub_handles = []
# win32gui.EnumChildWindows(hwnd, None, sub_handles)
# print(sub_handles)

exit()

while True:

    try:
        pdhk = win32gui.GetWindowRect(hwnd)
        win32api.SetCursorPos([pdhk[0] + 53, pdhk[1] + 680])
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        time.sleep(1)

        win32api.SetCursorPos([pdhk[0]+367 , pdhk[1] + 680])
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        time.sleep(1)

    except Exception as e:
        print(str(e))
