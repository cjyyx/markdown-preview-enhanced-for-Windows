#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <windows.h>
#include <shellapi.h>

void system_hide(char *cmd){
 SHELLEXECUTEINFO sei;

    ZeroMemory(&sei, sizeof(sei));
    sei.cbSize = sizeof(sei);
    sei.fMask = SEE_MASK_NOCLOSEPROCESS;
    sei.lpVerb = "open";
    sei.lpFile = "cmd.exe";
    sei.lpParameters = cmd;
    sei.nShow = SW_HIDE;

    // 执行命令并隐藏窗口
    ShellExecuteEx(&sei);

    // 等待进程结束
    WaitForSingleObject(sei.hProcess, INFINITE);

    // 关闭进程句柄
    CloseHandle(sei.hProcess);
}

int main(int argc, char const *argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("argv %d: %s\n", i, argv[i]);
    }
    printf("\n");

    char exe_path[1024];
    strcpy(exe_path, argv[0]);
    for (int i = 0; exe_path[i]; i++)
    {
        if (exe_path[i] == '\\')
        {
            exe_path[i] = '/';
        }
    }
    printf("exe_path: %s\n", exe_path);

    char exe_dir[1024];

    char *last_slash = strrchr(exe_path, '/');
    if (last_slash != NULL)
    {
        size_t len = last_slash - exe_path;
        strncpy(exe_dir, exe_path, len);
        exe_dir[len] = '\0';
    }
    else
    {
        exe_dir[0] = '\0';
    }

    printf("exe_dir: %s\n", exe_dir);

    char *temp = "/crossnote-js/crossnote.js";
    char js_path[1024];
    strcpy(js_path, exe_dir);
    strcat(js_path, temp);
    printf("js_path: %s\n", js_path);

    char const *md_path = argv[1];
    printf("md_path: %s\n", md_path);

    char cmd[1024];
    strcpy(cmd, "/c node ");
    strcat(cmd, js_path);
    strcat(cmd, " ");
    strcat(cmd, md_path);

    printf("cmd: %s\n\n\n", cmd);

    // system(cmd);
    system_hide(cmd);

    printf("\n\n\nWaiting for 10 seconds, then exit...\n");
    sleep(10);

    // printf("Press Enter to continue...");
    // getchar();

    return 0;
}
