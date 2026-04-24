# styles.py
import ctypes
from PyQt5.QtWidgets import QMessageBox

def get_dark_stylesheet():
    return """
        QMainWindow, QWidget {
            background-color: #121212;
            color: #FFFFFF;
            font-family: 'Segoe UI', sans-serif;
        }
        QLabel {
            color: #FFFFFF;
        }
        QTableWidget {
            background-color: #1E1E1E;
            color: #FFFFFF;
            gridline-color: #333333;
            border: 1px solid #333333;
        }
        QHeaderView::section {
            background-color: #333333;
            color: #FFFFFF;
            padding: 5px;
            border: 1px solid #121212;
        }
        QPushButton {
            background-color: #333333;
            color: white;
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #444444;
        }
        QPushButton:hover {
            background-color: #444444;
        }
        QPushButton#RegisterBtn {
            background-color: #2c3e50;
            font-weight: bold;
        }
        QPushButton#RefreshBtn {
            background-color: #2c3e50;
            font-weight: bold;
        }
    """

def apply_dark_titlebar(window):
    try:
        window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        hwnd = window.winId().__int__()
        rendering_policy = ctypes.c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, 
            ctypes.byref(rendering_policy), 
            ctypes.sizeof(rendering_policy)
        )
    except Exception as e:
        print(f"Dark titlebar error: {e}")


def show_styled_msg(parent, title, text, icon=QMessageBox.Information):
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(icon)
    
    msg.setStyleSheet(get_dark_stylesheet() + """
        QMessageBox { 
            background-color: #121212; 
        }
        QLabel { 
            color: white; 
            font-size: 14px; 
            min-width: 400px;  
            qproperty-wordWrap: True; 
        }
        QPushButton { 
            min-width: 100px; 
            background-color: #333; 
            color: white; 
            border-radius: 5px; 
            padding: 5px; 
        }
    """)
    
    try:
        import ctypes
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        hwnd = msg.winId().__int__()
        rendering_policy = ctypes.c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, 
            ctypes.byref(rendering_policy), 
            ctypes.sizeof(rendering_policy)
        )
    except:
        pass

    return msg.exec_()