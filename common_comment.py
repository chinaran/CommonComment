import datetime, getpass
import sublime, sublime_plugin
import datetime
import os

# 优化文件路径
# 包含 github.com 的文件路径从 github.com 开始，否则只保留名字
def handle_code_file_path(file_path):
    i = file_path.find("github.com")
    if i == -1:
        return os.path.basename(file_path)
    return file_path[i:]


# 添加文件开头注释
class AddFileCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        if file_path is None:
            print("Can not comment without file")
            return
        if file_path.endswith(".py"):
            self.view.run_command("insert_snippet",
                {
                    "contents": '"""' "\n"
                        "    Author:       alan (wangran@rxthinking.com)" "\n"
                        "    Created Time: " "%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                        "    File Name:    " "%s" %handle_code_file_path(file_path) + "\n"
                        "    Description:  " "\n"
                    '"""'
                }
            )
        else: # go c/c++
            self.view.run_command("insert_snippet",
                {
                    "contents": "/**""\n"
                    " * Author:       alan (wangran@rxthinking.com)" "\n"
                    " * Created Time: " "%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                    " * File Name:    " "%s" %handle_code_file_path(file_path) + "\n"
                    " * Description:  " "\n"
                    " */"
                }
            )

# 添加代码块注释
class AddCodeBlockCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        if file_path is None:
            print("Can not comment without file")
            return
        if file_path.endswith(".py"):
            self.view.run_command("insert_snippet",
                {
                    "contents": '"""' "\n"
                        "    Author:      alan (wangran@rxthinking.com)" "\n"
                        "    Code Time:   " "%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                        "    Description: " "\n"
                    '"""'
                }
            )
        else: # go c/c++
            self.view.run_command("insert_snippet",
                {
                    "contents": "/**""\n"
                    " * Author:      alan (wangran@rxthinking.com)" "\n"
                    " * Code Time:   " "%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                    " * Description: " "\n"
                    " */"
                }
            )

