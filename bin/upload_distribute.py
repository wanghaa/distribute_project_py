from bin.project_upload import *

if __name__ == '__main__':
    try:
        # 设置日志文件
        time_str = str(time.time())
        log_file = '../log/upload_distribution_' + time_str + '.log'
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            filename=log_file,
                            filemode='w',
                            datefmt='%Y-%m-%d %X')

        # 定义配置文件路径
        conf_file_name = '../conf/upload_distribute.conf'
        # 选择配置文件section
        conf, section = select_section(conf_file_name)
        # 检测配置文件正确性
        check_config(conf, section)
        # 执行停止命令
        # stop_cmd_file = conf.get(section, 'stop_cmd_file')
        # exec_file_cmd(conf, section, stop_cmd_file)
        # 备份原文件
        backup_ori(conf, section)
        # 上传文件
        upload(conf, section)
        # 备份新上传的文件
        backup_new(conf, section)
        # 执行启动命令
        # start_cmd_file = conf.get(section, 'start_cmd_file')
        # exec_file_cmd(conf, section, start_cmd_file)

        # 监听服务是否启动成功

        # 实行完毕暂停
        os.system('pause')
    except Exception as e:
        print(traceback.format_exc())
        project_upload.__err_exit_show_msg(str(e))
